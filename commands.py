class Commands:
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description
        self.list = []

    def add(self,c):
        self.list.append(c)
    

class Command:
    def __init__(self,id,name,commandLine,description):
        self.commandLine = commandLine
        self.description = description
        self.name = name
        self.id = id


stdCmd = Commands(0,"Standard Commands","This object contains a list of all the standard commands")

stdCmd.add(Command( 0,"Help", [ "h" , "help" ] , "Get information about all standard commands" ))
stdCmd.add(Command( 1,"Create Form", [ "cf" , "createForm" ] , "Create an HTML form" ))


cfCmd = Commands(1,"Change Form Commands","This objecto contains a list of all commands that follows the Change Form command")

cfCmd.add(Command( 0, "Help", [ "h", "help" ], "Get information about all Create Form commands" ) )
cfCmd.add(Command( 1, "Input", ["i", "Input"], "Create an Input" ) )