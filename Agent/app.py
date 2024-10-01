from .LLMs.groq import GroqAPI

def BrainIt(user:str):
    agent = GroqAPI()
    return agent.Get(user)

