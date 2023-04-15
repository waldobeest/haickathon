import weaviate
import os

# Connect to your Weaviate instance
client = weaviate.Client(
    url="http://localhost:8080/",
    additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Check if your instance is live and ready
# This should return `True`
