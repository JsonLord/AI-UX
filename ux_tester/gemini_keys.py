import os

# These should be set as environment variables in Hugging Face Space Secrets
GLOBAL_SEARCH_API_KEY = os.environ.get("GLOBAL_SEARCH_API_KEY")
OPENAI_API_KEY_SULTAN = os.environ.get("OPENAI_API_KEY_SULTAN")

# Legacy/unused keys
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
AVIALDO_GEMINI_KEY = os.environ.get("AVIALDO_GEMINI_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
TEMP_TOKEN = os.environ.get("TEMP_TOKEN")
