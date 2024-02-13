class BaseCommand: 
    def __init__(self): # __init__() function is called automatically every time the class is being used to create a new object.
        self.command = "docgen"
        

class HelloCommand: 
    def __init__(self):
        self.command = "hello"
        self.description = "Prints hello world"
        self.usage = "hello"
        
    def run(self, args):
        print("Hello, world!")
        