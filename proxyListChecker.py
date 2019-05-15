import os
import urllib.request
import socket
import urllib.error
import asyncio
import mechanize #sudo pip install python-mechanize
import _thread

class StaticLand():
    workingList = "";
    countDown = 0;
    taskcount=0;
    CheackAddress="";
    

def LoadList():
    Address = str(input("Enter ProxyList Address(Example C:\X.txt):  "));
    StaticLand.CheackAddress = str(input("Enter URL :  "));
    exists = os.path.isfile(Address);
    if exists:
        # Store configuration file values
        print("Opening "+Address);
        with open(Address) as f:
            mylist = [line.rstrip('\n') for line in f];
            StaticLand.countDown = len(mylist);
            asyncio.run(Checker(mylist));
            WriteOutPut(StaticLand.workingList);
                    
    
			
        
    else:
        # Keep presets
        print("ProxyList NotFound !!!");

    input("To Exit Press Enter");
    return

async def Checker(mylist):
    threads = []
    
    for proxy in mylist:
        
        if StaticLand.taskcount>100:
            print("Waiting 8 S")
            WriteOutPut(StaticLand.workingList);
            await asyncio.sleep(8)
            _thread.start_new_thread( chp,(proxy,1) )
            
        else:
            StaticLand.taskcount=StaticLand.taskcount+1;
            StaticLand.countDown=StaticLand.countDown-1
            if StaticLand.countDown<2:
                WriteOutPut(StaticLand.workingList);
                print("Ending Wait "+str(StaticLand.taskcount*4)+" s")
                await asyncio.sleep(StaticLand.taskcount*4)
            _thread.start_new_thread( chp,(proxy,1) )
            

    
    

def chp(proxy,tasknumber):
        if ComboTester(proxy):
            StaticLand.workingList+=(proxy+'\n')
            print("%s is working" % (proxy) +"   ( "+str(StaticLand.countDown)+" Left)")
        StaticLand.taskcount=StaticLand.taskcount-1;

def ComboTester(proxy):
    try:
        br = mechanize.Browser() #initiating a browser
        br.set_handle_robots(False) #ignore robots.txt
        br.addheaders = [("User-agent","Mozilla/5.0")] #our identity
        br.set_proxies({"https":proxy})
        gitbot = br.open(StaticLand.CheackAddress)
        #requesting the github base url
        #the sign up form in github is in third position(search and sign informscome before signup)
        #br.form.field_with(placeholder="Sign-In ID (Email Address)")=username
        #br.form.field_with(placeholder="Password")=password
        #username for github
        #password for github
        #br.form.set_value(username, nr=0)
        #br.form.set_value(password, nr=1)
    except Exception as detail:
        return False
    return True

    
def is_Good_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'https': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request(StaticLand.CheackAddress)  # change the URL to test here
        sock=urllib.request.urlopen(req, timeout=4)
    except urllib.error.HTTPError as e:
        # print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        # print("ERROR:", detail)
        return False
    return True

def WriteOutPut(text):
    file1 = open("./output.txt","w")
    # \n is placed to indicate EOL (End of Line) 
    file1.write(text)
    file1.close() #to change file access modes
    return



LoadList()






