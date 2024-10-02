import importlib.util
from Handler.handler import Handler 



if __name__ == "__main__":
    handlerbot = Handler()
    while True:
        user = input("MineOS> ")
        response = handlerbot.Handle(user)
        print(response)