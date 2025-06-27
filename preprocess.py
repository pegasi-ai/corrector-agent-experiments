from docx import Document
import mammoth
import textwrap
from html import unescape
from typing import Dict, Tuple, List
import re


# load file
def docx_to_html(path: str) -> str:
    """Convert a .docx into HTML, preserving tables and links."""
    with open(path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        # result.value is the HTML string
        # result.messages contains any warnings
        return result.value
    
# split data
def split_html_into_paragraphs(html):
    # Use regex to find all <p>...</p> blocks
    paragraphs = re.findall(r'<p.*?>.*?</p>', html, re.DOTALL)
    return paragraphs

# parse file
def extract_text_and_citations_per_citation_href(html: str) -> Dict[str, str]:
    """
    Finds all <a href="...">...</a> links in the HTML string,
    and for each returns the text immediately before the link (stripped of any tags).
    """
    # Regex to find <a ... href="URL">label</a>
    link_re = re.compile(
        r'<a\s+[^>]*href="(?P<href>[^"]+)"[^>]*>.*?</a>',
        flags=re.IGNORECASE | re.DOTALL
    )
    
    results: Dict[str, str] = {}
    last_end = 0
    
    for m in link_re.finditer(html):
        url = m.group('href')
        # Segment from end of last link (or start) up to this link
        pre_segment = html[last_end : m.start()]
        # Remove any HTML tags from that segment and collapse whitespace
        text_before = re.sub(r'<[^>]+>', '', pre_segment).strip()
        results[text_before] = url
        last_end = m.end()
    
    return results

def extract_text_and_citations_per_section_href(text: str) -> dict:
    """
    Same functionality but returns a dictionary instead of tuple.
    Returns:
    dict: {"text": clean_text, "citations": citations}
    """
    # 1. Extract all citation URLs
    citations = re.findall(
        r'<a\s+[^>]*href="([^"]+)"',
        text,
        flags=re.IGNORECASE
    )
    # 2. Remove all <a>…</a> segments entirely (so link text doesn't remain)
    html_no_links = re.sub(
        r'<a\s+[^>]*>.*?</a>',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )
    # 3. Strip all remaining HTML tags
    text_only = re.sub(r'<[^>]+>', ' ', html_no_links)
    # 4. Decode HTML entities (e.g. &amp; → &)
    text_only = unescape(text_only)
    # 5. Collapse multiple whitespace into single spaces
    clean_text = re.sub(r'\s+', ' ', text_only).strip()
    
    return {
        "text": clean_text,
        "citations": citations
    }

def extract_text_and_citations_per_citation_source(html: str) -> Dict[str, str]:
    """
    From an HTML string with markdown-style [Source](URL) citations,
    return a dict mapping each citation context to its URL.
    Each context is the clean text chunk immediately preceding that citation.
    """
    # 1. Decode HTML entities
    decoded = unescape(html)

    # 2. Strip HTML tags
    text = re.sub(r'<[^>]+>', ' ', decoded)

    # 3. Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # 4. Find all [Source](URL)
    link_pattern = re.compile(r'\[Source\]\((https?://[^\)]+)\)', flags=re.IGNORECASE)

    results: Dict[str, str] = {}
    last_end = 0

    for m in link_pattern.finditer(text):
        url = m.group(1)
        # the text between the end of the previous link (or start) and this one
        context = text[last_end:m.start()].strip()
        results[context] = url
        last_end = m.end()

    return results

def run_href(text: str):
 
    # II. split file
    sections = split_html_into_paragraphs(text)

    # III. parse file
    text_links_per_citation = []
    text_links_per_section = []
    for section in sections:
        dic = extract_text_and_citations_per_citation_href(section)
        if not dic:
            continue

        text_links_per_citation.append(dic)

        dic = extract_text_and_citations_per_section_href(section)
        text_links_per_section.append(dic)

    return text_links_per_citation, text_links_per_section


def run_source(text: str):
 
    # II. split file
    sections = split_html_into_paragraphs(text)

    # III. parse file
    text_links_per_citation = []
    for section in sections:
        dic = extract_text_and_citations_per_citation_source(section)
        if not dic:
            continue
        text_links_per_citation.append(dic)


    return text_links_per_citation



    