from Agent.Agent import Agent
from groq import Groq

class GroqAPI(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.client = Groq(
            api_key="", #API Key
        )

    def Get(self,query):
        chat_completion = self.client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": query,
        }
    ],
    model="llama3-8b-8192",
)
        return chat_completion.choices[0].message.content