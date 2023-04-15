from client import client


def query_weaviate(query, collection_name):
    nearText = {
        "concepts": [query],
        "distance": 0.7,
    }

    properties = [
        "title", "content", "url",
        "_additional {certainty distance}"
    ]

    result = (
        client.query
        .get(collection_name, properties)
        .with_near_text(nearText)
        .with_limit(100)
        .do()
    )

    # Check for errors
    if ("errors" in result):
        print(
            "\033[91mYou probably have run out of OpenAI API calls for the current minute – the limit is set at 60 per minute.")
        raise Exception(result["errors"][0]['message'])

    return result["data"]["Get"][collection_name]


if __name__ == "__main__":
    query_result = query_weaviate("Alanis Morissette", "Article")

    for i, article in enumerate(query_result):
        print(f"{i + 1}. {article['title']} (Score: {round(article['_additional']['certainty'], 3)})")
