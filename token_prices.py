# Token pricing per million tokens for different language models
# Prices are in USD per 1M tokens

token_prices_per_million = {
    "openai:gpt-4o": {
        "input": 5.00,     # $5.00 per 1M input tokens
        "output": 15.00    # $15.00 per 1M output tokens
    },
    "openai:gpt-4o-mini": {
        "input": 0.25,
        "output": 0.50
    },
    "openai:gpt-4.1-mini": {
        "input": 1.00,
        "output": 2.00
    },
    "openai:o3": {
        "input": 0.50,
        "output": 1.50
    },
    "gemini:models/gemini-2.0-flash": {
        "input": 0.35,
        "output": 1.05
    },
    "gemini:models/gemini-2.5-pro": {
        "input": 0.50,
        "output": 1.50
    }
} 