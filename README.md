# corrector-agent-experiments

A Streamlit-based document analysis tool that provides two main functionalities: fact-checking and link relevancy checking.

## Overview

CORRECTOR-AGENT is a web application built with Streamlit and LangChain that helps users analyze documents for factual accuracy and reference link relevancy. The tool supports multiple AI models and provides detailed analysis reports.

## Features

### 1. Fact-Checking (`main_fact_checker.py`)
- **Purpose**: Verify factual accuracy of document content against provided reference links
- **Functionality**: 
  - Identifies factually incorrect information in documents
  - Provides corrections with explanations
  - Assigns confidence scores to each correction
  - Supports multiple AI models (OpenAI, Groq, etc.)

### 2. Link Relevancy Checking (`main_relevancy_checker.py`)
- **Purpose**: Assess whether reference links are relevant and sufficient for the associated text
- **Functionality**:
  - Evaluates if website links provide relevant information to document content
  - Determines relevancy status (Yes/No) for each text-link pair
  - Provides detailed explanations for relevancy assessments
  - Generates comprehensive reports with confidence scores

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd corrector-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### Running the Applications

#### Fact-Checker
```bash
streamlit run main_fact_checker.py
```

#### Relevancy Checker
```bash
streamlit run main_relevancy_checker.py
```

### How to Use

1. **Select AI Model**: Choose from available models (OpenAI GPT-4o, GPT-4.1 Mini, Groq Llama, etc.)
2. **Enter API Key**: Provide the required API key for your selected model
3. **Upload Document**: Upload a Word (.docx) or PDF document
4. **Choose Analysis Type**:
   - **Analyze Document**: Process the entire document
   - **Analyze Section**: Process a specific section (if available)
5. **Review Results**: Examine the analysis results and download reports

## Supported File Formats

- **Microsoft Word Documents** (.docx)
- **PDF Files** (.pdf)

## Supported AI Models

- **OpenAI**: GPT-4o, GPT-4.1 Mini
- **Groq**: Llama-3.3 70B
- **Anthropic**: Claude models (if configured)

## Output Features

### Fact-Checker Output
- Overall accuracy score
- List of factual corrections with:
  - Original text
  - Corrected text
  - Explanation
  - Confidence score

### Relevancy Checker Output
- Total number of links analyzed
- Number of irrelevant links
- Detailed analysis for each text-link pair:
  - Original text
  - Website link
  - Relevancy status (Yes/No)
  - Explanation
  - Confidence score
- Export functionality for Word document reports

## Requirements

- Python 3.8+
- Streamlit
- LangChain
- Pydantic
- Mammoth (for Word document processing)
- PyPDF2 (for PDF processing)
- python-docx (for Word document generation)

## Project Structure

```
corrector-agent/
├── main_fact_checker.py          # Fact-checking application
├── main_relevancy_checker.py     # Link relevancy checking application
├── preprocess.py                 # Document preprocessing utilities
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── .env                          # Environment variables (create this)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions, please open an issue in the repository. 
