import tkinter as tk 
import time
import selenium
from selenium import webdriver
import os 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import string
import threading


uppercase_letters = string.ascii_uppercase
root = tk.Tk()
root.geometry("250x123")
root.title("Live Score")
root.resizable(False,False)
chrome_options = Options()
chrome_options.add_argument("--headless")
path = "C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(path)
url = "https://www.cricbuzz.com/cricket-match/live-scores"
driver = webdriver.Chrome(service=service, options=chrome_options) 
def live_score(Team_1,update_var): 
    while True:
        try:
            driver.get(url)
            i=0
            ele3 = driver.find_elements(By.CLASS_NAME,"cb-scr-wll-chvrn.cb-lv-scrs-col")
            lista  = []  
            flag = False   
            j = 0 
            hel = [] 
            for i in range(len(ele3)):
                hel.append(ele3[i].text)
            Team_1 = Team_1  
            Team_2 = '' 
            update = '' 
            i = 0 
            j = 0 
            HEL = [] 
            hel1 = [] 
            for i in range(len(hel)):
                for j in range(len(hel[i])):
                    if hel[i][j] in uppercase_letters:
                        HEL.append(hel[i][j])
                hel1.append(HEL)
                HEL = [] 
            count  = 0 
            hel2 = [] 
            hel3 = [] 
            Team_1_e  = '' 
            for i in range(len(hel1)):
                for j in range(len(hel1[i])):
                    if hel1[i][j] == "O" :
                        count+=1 
                        continue 
                    if count == 0  :
                        Team_1_e += hel1[i][j]
                    if count == 1 :
                        Team_2 += hel1[i][j]
                    if count ==  2:
                        hel2.append(Team_1_e)
                        hel2.append(Team_2)
                        break 
                hel3.append(hel2)
                Team_1_e = ''
                Team_2 = ''
                count = 0  
                hel2 = []  
            i = 0 
            match_no = 0 
            if Team_1.lower() != "recent" or Team_1.lower() != "now" or Team_1.lower() != "live" or Team_1.lower() != "current":
                for i in range(len(hel3)):
                    if Team_1 in hel3[i] :
                        match_no = i 
                        break 
            else:
                match_no = 0 
            data = list(hel3[match_no])
            for i in range(len(data)):
                if data[0] == Team_1 :
                    Team_2 = data[1]
                else:
                    Team_2 = Team_1
                    Team_1 = data[0]

                    Team_2  = data[0]
            match  = hel[match_no] 
            del HEL 
            del hel1 
            del hel2 
            del hel3 
            del hel 
            team = 0 
            match_list = match.split("\n")
            Team_1_info = match_list[0] 
            Team_2_info = match_list[1] 
            collective_info = match_list[2] 
            j =0 
            for i in range(len(Team_1_info)):
                if Team_1_info[i] in uppercase_letters:
                    j += 1  
            Team_1 = Team_1_info[:j-1]
            Team_1_info = Team_1_info[j- 1 :]
            k= 0 
            for i in range(len(Team_2_info)):
                if Team_2_info[i] in uppercase_letters:
                    k += 1  
            Team_2 = Team_2_info[:k]
            Team_2_info = Team_2_info[k- 1 :]

            if Team_2 == '':
                Team_2 = "---"
            
            if Team_2_info in uppercase_letters :
                Team_2_info = "Yet to play"
            
            update_var["Team_1"].set(Team_1)
            update_var["Team_2"].set(Team_2)
            update_var["Team_1_info"].set(Team_1_info)
            update_var["Team_2_info"].set(Team_2_info)
            update_var["collective_info"].set(collective_info)
        except Exception as e :
            update_var["collective_info"].set("error fetching data")
        time.sleep(1)

team_variable = tk.StringVar()
def submit():
    global Team_1

    team_var = team_variable.get()
    Team_1 = team_var.upper() 
    team_variable.set("")
    open_new_window(Team_1)
def open_new_window(Team_1):
    Team_1  = Team_1

    root.withdraw()
    new_window = tk.Toplevel()
    new_window.geometry("250x123")
    new_window.title("Live Score")
    new_window.resizable(False,False)

    Team_1_i = tk.StringVar(value= Team_1)
    Team_2_i = tk.StringVar(value = "---")
    Team_1_info_i = tk.StringVar(value = "0/0 (0 Ovs) ")
    Team_2_info_i = tk.StringVar(value = "0/0 (0 Ovs)")
    collective_info_i = tk.StringVar(value = "hello")
    
    label_team1 = tk.Label(new_window,textvariable= Team_1_i, font = ("Comic Sans MS",14))
    label_team2 = tk.Label(new_window,textvariable = Team_2_i, font = ("Comic Sans MS",14))
    label_team1_info = tk.Label(new_window,textvariable = Team_1_info_i, font = ("Comic Sans MS",14), bg = "light grey")
    label_team2_info = tk.Label(new_window,textvariable = Team_2_info_i, font = ("Comic Sans MS",14), bg= "light grey")
    label_col_info = tk.Label(new_window,textvariable= collective_info_i, font = ("Comic Sans MS",14),wraplength=230, justify="center")

    label_team1.place(x= 0 , y = 0)
    label_team2.place(x= 0 , y = 35)
    label_team1_info.place(x= 70 , y = 0)
    label_team2_info.place(x= 70 , y = 35)
    label_col_info.place(x= 10 , y = 65) 

    update_var  = {
        "Team_1": Team_1_i ,
        "Team_2": Team_2_i , 
        "Team_1_info" : Team_1_info_i ,
        "Team_2_info" : Team_2_info_i ,
        "collective_info" : collective_info_i
    }

    threading.Thread(target = live_score,args=(Team_1,update_var),daemon= True).start()

    
def combined():
    submit()
team_label = tk.Label(root, text = "Enter the team ", font = ("Comic Sans MS", 14))
team_entry = tk.Entry(root,textvariable = team_variable, font =("Comic Sans MS",14) )
sub_button = tk.Button(root,text= "Submit", command = combined , font = ("Comic Sans MS", 14), bg= 'Green')
team_label.place(x= 60 , y =10)
team_entry.place(x = 0 , y = 40 )
sub_button.place(x= 90 , y = 70 )
root.mainloop()
driver.quit()
