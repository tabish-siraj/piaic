import json
import os

file_path = "DATA\\dictData.json"
trans = {}
class funs():
    def __init__(self):
        pass
    def addWord(self):
        try:
            if os.stat(file_path).st_size!=0:
                with open(file_path, "r") as fr:
                    dictionary = json.load(fr)

                human = input("Human:\t")
                alien = input("Alien:\t")
                dictionary.update({human:alien})
                with open(file_path, "w") as fw:
                    json.dump(dictionary, fw)
                    print("New Word Added.")
            else:
                    
                human = input("Human:\t")
                alien = input("Alien:\t")
                data = {human:alien}
                with open(file_path, "w") as fw:
                    json.dump(data, fw)
                    print("New Word Added")

        except FileNotFoundError:
            print(FileNotFoundError)
        except Exception:
            print(Exception)

    def alienToHuman(self):
        alien = input("Alien: ")
        try:
            with open(file_path,'r') as d:
                dictData = json.load(d)
                for k,v in dictData.items():
                    if alien == v:
                        print(f"Human : {v}")
                        d.close()
        except FileNotFoundError:
            print(FileNotFoundError)
        except Exception:
            print(Exception)



    def humanToAlien(self):
        human = input("Human: ")
        try:
            with open(file_path,'r') as d:
                dictData = json.load(d)
                for k,v in dictData.items():
                    if human == k:
                        print(f"Alien : {v}")
                        d.close()
        except FileNotFoundError:
            print(FileNotFoundError)
        except Exception:
            print(Exception)

