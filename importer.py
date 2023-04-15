from datasets import load_dataset
from typing import List, Iterator

from client import client

# We'll use the datasets library to pull the Simple Wikipedia dataset for embedding
dataset = list(load_dataset("wikipedia", "20220301.simple")["train"])

# For testing, limited to 2.5k articles for demo purposes
# dataset = dataset[:2_500]

# Limited to 25k articles for larger demo purposes
# dataset = dataset[:25_000]

# for free OpenAI acounts, you can use 50 objects
dataset = dataset[50:500]

client.batch.configure(
    batch_size=10,
    dynamic=True,
    timeout_retries=3,
    #   callback=None,
)

print("Importing Articles")

counter = 0
with client.batch as batch:
    for article in dataset:
        if (counter % 10 == 0):
            print(f"Import {counter} / {len(dataset)} ")

        properties = {
            "title": article["title"],
            "content": article["text"],
            "url": article["url"]
        }

        batch.add_data_object(properties, "Article")
        counter = counter + 1

print("Importing Articles complete")
