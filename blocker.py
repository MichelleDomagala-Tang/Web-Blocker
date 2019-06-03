#Created with the aid of a guide from boostlog.io and geeksforgeeks.org
hosts_file=r"C:\Windows\System32\drivers\etc"
local="192.168.0.17"
website_list=['www.facebook.com', 'facebook.com','www.youtube.com']
block=False

while True: #runs an indefinate loop
    block = bool(input('Run blocker? Type True or False.')) 
#If the user has set Block to True, then block the specified website
    if block == True:     
        with open(hosts_file, 'r+') as file:
            content = file.read()
            for website in content:
                pass
            else:
                #mapping hostnames to your localhost IP adress
                file.write(local+" "+website+"\n")
    else:
        with open(hosts_file,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            #removing hostnames from host file
            file.truncate()