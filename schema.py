# Clear up the schema, so that we can recreate it
from client import client

client.schema.delete_all()
client.schema.get()

# Define the Schema object to use `text-embedding-ada-002` on `title` and `content`, but skip it for `url`
article_schema = {
    "class": "Article",
    "description": "A collection of articles",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {
            "model": "ada",
            "modelVersion": "002",
            "type": "text"
        }
    },
    "properties": [{
        "name": "title",
        "description": "Title of the article",
        "dataType": ["string"]
    },
        {
            "name": "content",
            "description": "Contents of the article",
            "dataType": ["text"]
        },
        {
            "name": "url",
            "description": "URL to the article",
            "dataType": ["string"],
            "moduleConfig": {"text2vec-openai": {"skip": True}}
        }]
}

# add the Article schema
client.schema.create_class(article_schema)

# get the schema to make sure it worked
_schema = client.schema.get()
print(_schema)
