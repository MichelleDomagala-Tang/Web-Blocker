
# coding: utf-8

# In[1]:



hostPath = "C:\Windows\System32\drivers\etc"

#enter your local hosts ID
localHost = " "

#enter websites you want to block away
websitesBlockList = ["www.netflix.com/browse/", "www.facebook.com/"]

def userInput ():

    userRun = input("Would you like to block websites? Type yes or no.")

    if userRun == "yes":
        addWebsites = input("What webiste would you like to block? \n Paste link to add website \n Type 'none' to run the program or 'see websites' to see current blocked websites.")
        websiteIdent1 = "www."
        websiteIdent2 = "https://"

        if websiteIdent1 in addWebsites or websiteIdent2 in addWebsites:
            websitesBlockList.append(addWebsites)
            print("Website has been added")
            userInput()
        elif addWebsites == "none":
            blockWebsites()
            endProgram = input("Website blocker is active! Type 'end' to stop the program.")
            
            if endProgram == "end":
                stopBlock()
                print('Websites are no longer blocked.')
        else:
            print('Not a valid website')
            userInput()

    elif userRun == "no":
        print("No websites are currently blocked")

    else:
        print("Sorry, was that a yes or no?")
        
def blockWebsites():
    with open(localHost, "r+") as file:
        content = file.readlines()
        for website in websitesBlockList:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")

def stopBlock ():
    with open(localHost, "r+") as file:
        content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in websitesBlockList):
            file.write(line)
    file.truncate()
    
userInput()

