import sys
import json
import os
from pprint import pprint

from app.item import init
from app.item import login

if __name__=="__main__":
    arguments = sys.argv[1:]
    init(arguments)
    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
         if command == "login":
             login(*params )