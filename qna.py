# system message to 'prime' the model
import openai
from IPython.core.display_functions import display

from test_query import query_weaviate
from IPython.display import Markdown

primer = f"""You are Q&A bot. A highly intelligent system that answers
user questions based on the information provided by the user above
each question. If the information can not be found in the information
provided by the user you truthfully say "I don't know".
"""

if __name__ == "__main__":
    query = "How many Grammys did Alanis Morissette win?"
    query_result = query_weaviate(query, "Article")

    prompt = [x['content'] for x in query_result]
    prompt.extend(['\n', query])
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": primer},
            {"role": "user", "content": '\n'.join(prompt)}
        ]
    )

    display(Markdown(res['choices'][0]['message']['content']))
