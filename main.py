import random, string, requests, time, re, threading #lib
from colorama import init, Fore, Back, Style #lib
init() #import for color
print(Fore.RED+ Style.BRIGHT +"""
 
 
 
 _________  _   __      _________       __              ______  __                    __                     
|  _   _  |(_) [  |  _ |  _   _  |     [  |  _        .' ___  |[  |                  [  |  _                 
|_/ | | \_|__   | | / ]|_/ | | \_|.--.  | | / ]      / .'   \_| | |--.  .---.  .---.  | | / ] .---.  _ .--.  
    | |   [  |  | '' <     | |  / .'`\ \| '' <       | |        | .-. |/ /__\\/ /'`\] | '' < / /__\\[ `/'`\] 
   _| |_   | |  | |`\ \   _| |_ | \__. || |`\ \      \ `.___.'\ | | | || \__.,| \__.  | |`\ \| \__., | |     
  |_____| [___][__|  \_] |_____| '.__.'[__|  \_]      `.____ .'[___]|__]'.__.''.___.'[__|  \_]'.__.'[___]    
 
 
 
"""+ Style.RESET_ALL)#Style.RESET_ALL This Rest All colors For Default To Avoid errors And This (Style.BRIGHT) Make Color Show With Out Errors in terminal
num = int(input("4L OR 3L? Choose By Number :"))#i recommended Put 4 :(
def webhook(usr): #function for web hook
    import json # i import this lib here to Avoid errors If You Use var.Json TO get json info from get or post method
    user = usr
    r = requests.session()
    url = "https://discord.com/api/webhooks/806876123752300544/DkdSuVYv_7U66lSaF_rY9ogWX97sIJSvLwm_Cn9WJep5ZjBM_4ypGjGG2dHLEKRLd-1H"#your web hook url
    data = {}
    data["username"] = "TikTok Checker V1"#Name Of The Bot
    data["embeds"] = []
    embed = {}
    embed["description"] = f"Username @{user}\n | Might be Available or Banned |" 
    embed["title"] = "5G7 Catch !"
    data["embeds"].append(embed)
    result = r.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"}).text
def get_random_acc(): #function that create random 4L
    letters = string.ascii_letters #this for get all alphabet
    return ''.join(random.choice(letters).lower() for i in range(num))
def chk():
    while True:
                    username = get_random_acc()
                    useragent = open('user-agent.txt', 'r').read().splitlines()#i use random user-agent to avoid get block its not work 100% But it fulfills the purpose 
                    randomagent = str(random.choice(useragent))#choose random
                    url = f'https://m.tiktok.com/node/share/user/@{username}'  
                    r = requests.get(url, headers={'user-agent': '{}'.format(randomagent)})
                    try:#Becuse i use regex ---------- i must use try cuse regex if not find the text it well stopped and close the app
                        responsecode = re.search(r'"statusCode":(.*?),', str(r.text)).group(1)#I like Regex ;)
                        if ('{"statusCode":10202,"statusMsg":"","userInfo":{}}') in r.text:
                            print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {username}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
                            f = open("availables.txt", "a", encoding='utf-8')
                            f.write(f"{username} | Might be Available or Banned |\n")
                            webhook(username)#Send User IN Discord
                        elif responsecode == "10222":
                           print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+ Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                        elif responsecode == "0":
                             print(Fore.CYAN+"[-] "+Fore.RED + "Maybe You Get blocked OR UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+ Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                        elif responsecode == "10221":
                            print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                        elif responsecode == "10223":
                            print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+Style.BRIGHT +" [-]"+ Style.RESET_ALL)
               
                    except:
                            #('statusCode: 0')<-(this to search for a word that You are the one who determines) in <- (this mean where you want to search) r.text <- (we want to search in response Who has come From Tik Tok)
                          if ('statusCode: 0') in r.text: #0 status its Indicates tHAT You Get Blocked Or User Isn't UnAvailable
                                      print(Fore.CYAN+"[-] "+Fore.RED + "if this repeat alot Maybe You Get blocked OR User UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+ Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                          else:
                            print(r.text)
thrd = int(input("Thread 1 Best More than 150 Danger:"))
for _ in range(thrd):
    threading.Thread(target=chk).start()#If I want to explain to you what is threading Just Dm Cuse Its Long Stoy :( @8r18