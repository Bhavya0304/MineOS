import importlib
from Agent.app import BrainIt
import json
import os

def import_module_from_path(path):
    spec = importlib.util.spec_from_file_location("module_name", path)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module

def ReadActions():
    cwd = os.getcwd()
    path = "Actions/actions.json"
    finalpath = os.path.join(cwd,path)
    with open(finalpath, 'r') as file:
        data = json.load(file)
    return data

class Handler:
    def __init__(self):
        pass
    def Handle(self,userInput):
        actions = ReadActions()
        #print(str(actions))
        prompt = "you are a agent who's task is to select most suitable action from json of actions and its description provided based on user query. you will get input in the form 'JSON::User_query' and you should give one word ouput of chosen actions without any preamble"
        finalprompt = prompt + "\n" + str(actions) + ":" + userInput
        action = BrainIt(finalprompt)
        print(action)
        if(action.lower() == "question"):
            return BrainIt(userInput)
        else:
            pathToAction = actions[action.lower()]
            print(pathToAction)
            module = import_module_from_path(pathToAction["path"])
            module.Run(1,2,3,4)
        
