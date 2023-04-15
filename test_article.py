from client import client

test_article = (
    client.query
    .get("Article", ["title", "url", "content"])
    .with_limit(50)
    .do()
)["data"]["Get"]["Article"][30]

print(test_article['title'])
print(test_article['url'])
print(test_article['content'])