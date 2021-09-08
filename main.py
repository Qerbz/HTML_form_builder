import commands as c

def writeToFile(fileText):
    with open(fileName, 'w') as file:
        file.write(fileText)


while True:
    consoleInput = input()

    for i in c.stdCmd.list:
        if consoleInput in i.commandLine:
            commandId = i.id
            break
    
    if commandId == 0:
        print("\n")
        for i in c.stdCmd.list:
            print(i.name + ": " + i.description + "\n    " + "commands: " + str(i.commandLine) + "\n")
    
    if commandId == 1:
        fileName = input("File Name: ")
        fileContent = ""
        while True:
            consoleInput = input()

            for i in c.cfCmd.list:
                if consoleInput in i.commandLine:
                    commandId = i.id
                    break

            if commandId == 0:
                print("\n")
                for i in c.cfCmd.list:
                    print(i.name + ": " + i.description + "\n    " + "commands: " + str(i.commandLine) + "\n")

            if commandId == 1:
                inputId = input("id: ")
                inputClass = input("class: ")
                inputType = input("type: ")
                fileContent += '<input type = "'+inputType+'" class = "'+inputClass+'" id = "'+inputId+'">'
            print(fileContent)


<label for="Zip/City">Zip/City: </label>[text Zip/City id:Zip/City]
<label for="Country">Country: </label>[text Country id:Country]
<label for="Phone">Phone: </label>[text Phone id:Phone]
<label for="EMail">E-Mail: </label>[text E-Mail E-Mail id:Email]
<label for="Nationality">Nationality: </label>[text Nationality id:Nationality]
<label for="dob">Date of Birth: </label>[text Date of Birth id:dob]
<label for="CurrentPosition">Current Position: </label>[text CurrentPosition id:CurrentPosition]
<label for="TermOfNoticeCurrentJob">Term of Notice Current Job (Months): </label>[text TermOfNoticeCurrentJob id:TermOfNoticeCurrentJob]
<label for="RelevantJobExperience">Relevant Job Experience (Years): </label>[text RelevantJobExperience id:RelevantJobExperience]