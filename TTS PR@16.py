# Simply Click F5 to Run the Program
try:
    import pyautogui
    pyautogui.click(655,43) # Closes Editor
    pyautogui.click(1284,47) # Minimises Interpreter
    user=pyautogui.prompt('Enter UserName : ')
    passw=pyautogui.password('Enter Password : ')
    if user == "pranav" and passw=="1234":
        pass
    else:
        pyautogui.alert("Error")
        op=pyautogui.confirm("Retry ?")
        if op=='OK':
            exec(open("TTS PR@16.py").read())
        else:
            pyautogui.alert("Couldn't Identify User !")
            exit()
    from urllib.request import urlopen
    import random
    import PySimpleGUI as sg
    theme=['Black','BlueMono','BluePurple','BrightColors','BrownBlue','Dark','Dark2','DarkAmber',
       'DarkBlack','DarkBlack1','DarkBlue','DarkBlue1','DarkBlue10','DarkBlue11','DarkBlue12','DarkBlue13','DarkBlue14','DarkBlue15','DarkBlue16','DarkBlue17',
       'DarkBlue2','DarkBlue3','DarkBlue4','DarkBlue5','DarkBlue6','DarkBlue7','DarkBlue8','DarkBlue9','DarkBrown',
       'DarkBrown1','DarkBrown2','DarkBrown3','DarkBrown4','DarkBrown5','DarkBrown6','DarkBrown7',
       'DarkGreen1','DarkGreen2','DarkGreen3','DarkGreen4','DarkGreen5','DarkGreen6','DarkGreen7','DarkGreen',
       'DarkGrey','DarkGrey1','DarkGrey2','DarkGrey3','DarkGrey4','DarkGrey5','DarkGrey6','DarkGrey7','DarkGrey8','DarkGrey9','DarkGrey10','DarkGrey11','DarkGrey12','DarkGrey13','DarkGrey14','DarkGrey15','DarkGrey16','DarkGrey17',
       'DarkPurple','DarkPurple1','DarkPurple2','DarkPurple3','DarkPurple4','DarkPurple5','DarkPurple6','DarkPurple7',
       'DarkRed','DarkRed1','DarkRed2','DarkTanBlue','DarkTeal','DarkTeal1',
       'DarkTeal2','DarkTeal3','DarkTeal4','DarkTeal5','DarkTeal6','DarkTeal7','DarkTeal8','DarkTeal9','DarkTeal10','DarkTeal11','DarkTeal12',
       'Default','Default1','DeafultNoMoreNagging','Green','GreenMono','GreenTan','HotDogStand','Kayak',
       'LightBlue','LightBlue1','LightBlue2','LightBlue3','LightBlue4','LightBlue5','LightBlue6','LightBlue7','LightBrown',
       'LightBrown1','LightBrown2','LightBrown3','LightBrown4','LightBrown5','LightBrown6','LightBrown7','LightBrown8','LightBrown9','LightBrown10','LightBrown11','LightBrown12','LightBrown13','LightGreen',
       'LightGray1','LightGreen1','LightGreen2','LightGreen3','LightGreen4','LightGreen5','LightGreen6','LightGreen7','LightGreen8','LightGreen9',
       'LightGrey','LightGrey1','LightGrey2','LightGrey3','LightGrey4','LightGrey5','LightGrey6',
       'LightPurple','LightTeal','LightYellow','Material1','Material2','NeutralBlue','Purple','Python','Reddit','Reds',
       'SandyBeach','SystemDefault','SystemDefault1','SystemDefaultForReal','Tan','TanBlue','TealMono','Topanga']
    theme1=random.choice(theme)
    sg.theme(theme1)
    def net_connection():
        try:
            urlopen('https://www.google.com',timeout=2)
            return True
        except:
            layout6=[[sg.Text("\tNot Connected To Internet !\t \n \tPlease Check Your Connection Status !\t")],[sg.Button('Exit', bind_return_key=True)]]
            window6=sg.Window('No Internet Connection',layout6)
            event,values=window6.read()
            window6.close()
            exit()
    net_connection()
    from gtts import gTTS
    import shutil,random,os,time
    from playsound import playsound
    l=os.path.abspath('Pictures')
    d=l.split("/")
    f=d[2]
    if not os.path.exists("/home/"+f+"/Voice_Saves/"):
        os.makedirs("/home/"+f+"/Voice_Saves/")
    def tts(text):
        language="en"
        voice=gTTS(text=mytext,lang=language,slow=False)
        t=random.randint(97,122)
        t2=random.randint(65,90)
        t3=random.randint(1,100)
        k=chr(t)+chr(t2)+str(t3)
        name="voice"+k+".mp3"
        voice.save("/home/"+f+"/Voice_Saves/voice"+name)
        playsound("/home/"+f+"/Voice_Saves/voice"+name)
        layout5=[[sg.Text("*** Voice Successfully Saved at Voice_Saves Folder in Home as "+name+" ***")],[sg.Button('OK', bind_return_key=True)]]
        window5=sg.Window('Voice_Save',layout5)
        event,values=window5.read()
        window5.close()
        eth=random.choice(theme)
        sg.theme(eth)
    layout2 = [[sg.Text("\n\n\n\n \t??????????????????????????????????????????????????\t \n\n \t????????? ^^^^^ Text To Voice Converter ^^^^^ ?????????\t \n\n \t??????? <<<<< By PR@16 Creations ! >>>>>>>> ??????\t \n\n \t?????????????????????????????????????????????????? \t \n\n\n\n")] ,[sg.Button('Next >>>', bind_return_key=True)] ]
    window2 = sg.Window('TTS PR@16', layout2)
    event, values = window2.read() 
    window2.close()
    layout3 = [[sg.Text("\t--------------------------------------------\t\n \n \t* Make Sure to turn on the Internet !\t\n \n \t* For Exiting type %exit%\t\n \n \t* For Clearing Audio files type %clear%\t\n \n  \t--------------------------------------------\t\n") , sg.Button('Continue >>>', bind_return_key=True)]]
    window3 = sg.Window('TTS PR@16', layout3)
    event,values=window3.read()
    window3.close()
    while True:
        layout = [  [sg.Text("Enter or Paste the Text Here :")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('OK', bind_return_key=True)] ]
        window = sg.Window('Text-To-Speech @ 16', layout)
        event, values = window.read()
        window.close()
        if values[0]=="clear":
            shutil.rmtree("/home/"+f+"/Voice_Saves/")
            os.mkdir("/home/"+f+"/Voice_Saves/")
            layout4=[[sg.Text("Cleared Successfully")],[sg.Button('OK', bind_return_key=True)]]
            window4=sg.Window('Voice_Clear',layout4)
            event,values=window4.read()
            window4.close()
        elif values[0]=="exit":
            exit()
        else:
            if len(values[0])>0:
                mytext=str(values[0])
                tts(mytext)
            else:
                layout7=[[sg.Text('Don\'t Leave Blank Space For TTS !')],[sg.Button('Restart Program >', bind_return_key=True)]]
                window7=sg.Window('Blank Space',layout7)
                event,values=window7.read()
                window7.close()
                exec(open("TTS PR@16.py").read())
except:
    layout8=[[sg.Text("\n \t!!!!!!!!!! PROGRAM CRASHED UNEXPECTEDLY !!!!!!!!!!\t \n")],[sg.Button(" >>> ", bind_return_key=True)]]
    window8=sg.Window('Program_Crash',layout8)
    event,values=window8.read()
    window8.close()
    layout9=[[sg.Text("\n \t$$$$$$$$$$ Restarting Program... $$$$$$$$$$\t \n")],[sg.Button(" >>> ", bind_return_key=True)]]
    window9=sg.Window('Program_Crash',layout9)
    event,values=window9.read()
    window9.close()
    exec(open("TTS PR@16.py").read())
