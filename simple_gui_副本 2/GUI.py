
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:36:58 2021

@author: bing
"""

# import all the required  modules
import select
import threading
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from chat_utils import *
import json
import pygame
import sys
import time


# GUI class for the chat
class GUI:
    # constructor method
    def __init__(self, send, recv, sm, s):
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()
        self.send = send
        self.recv = recv
        self.socket = s
        self.sm = sm
        self.my_msg = ""
        self.system_msg = ""
        self.gamer = 2
        self.imready = False
        self.isgaming = False
        self.peer_ready = False
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def login(self):
        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Login or Register")
        self.login.resizable(width = False, 
                             height = False)
        self.login.configure(width = 750,
                             height = 550)
        # create a Label
        self.pls = Label(self.login, 
                       text = "Log in to continue",
                       justify = CENTER, 
                       font = "Chalkboard 18 bold")
          
        self.pls.place(relheight = 0.17,
                       relx = 0.2, 
                       rely = 0.07)
        # create a Label
        self.labelName = Label(self.login,
                               text = "UserName: ",
                               font = "Chalkboard 18 bold")
          
        self.labelName.place(relheight = 0.22,
                             relx = 0.11, 
                             rely = 0.25, anchor='center')
          
        # create a entry box for 
        # tyoing the message
        self.entryName = Entry(self.login, 
                             font = "Chalkboard 18 bold")
          
        self.entryName.place(relwidth = 0.42, 
                             relheight = 0.13,
                             relx = 0.2,
                             rely = 0.2)
          
        # set the focus of the curser
        self.entryName.focus()

        # create a Label
        self.labelPw = Label(self.login,
                               text = "Password: ",
                               font = "Chalkboard 18 bold")
          
        self.labelPw.place(relheight = 0.22,
                             relx = 0.12, 
                             rely = 0.4, anchor='center')
          
        # create a entry box for 
        # tyoing the message
        self.entryPw = Entry(self.login, 
                             font = "Chalkboard 18 bold")
          
        self.entryPw.place(relwidth = 0.49, 
                             relheight = 0.20,
                             relx = 0.22,
                             rely = 0.37)
          
        # set the focus of the curser
        self.entryPw.focus()
          
        # create a Continue Button 
        # along with action
        self.go = Button(self.login,
                         text = "CLICK2CONTINUE", 
                         font = "Chalkboard 15 bold", 
                         command = lambda: self.goAhead(self.entryName.get()+ "," +self.entryPw.get()))
          
        self.go.place(relx = 0.42,
                      rely = 0.54)
        
        self.reset_password = Button(self.login,
                         text = "Reset the password", 
                         font = "Chalkboard 14 bold", 
                         command = self.reset_password)
          
        self.reset_password.place(relx = 0.42,
                      rely = 0.6)
        
        self.Window.mainloop()

    def reset_password(self):
        self.reset_password = Toplevel()
        self.reset_password.title("Reset the password.")
        self.reset_password.resizable(width = False, height = False)
        self.reset_password.configure(width = 800,
                             height = 650)
        # create a Label
        self.please = Label(self.reset_password, 
                       text = "Please reset the password",
                       justify = CENTER, 
                       font = "Chalkboard 18 bold")
          
        self.please.place(relheight = 0.17,
                       relx = 0.3, 
                       rely = 0.06)
        # create a Label
        self.labelName = Label(self.reset_password,
                               text = "Name:",
                               font = "Chalkboard 18")
          
        self.labelName.place(relheight = 0.3,
                             relx = 0.22, 
                             rely = 0.27, anchor='center')
          
        # create a entry box for 
        # tyoing the message
        self.entryResetName = Entry(self.reset_password, 
                             font = "Chalkboard 18")
          
        self.entryResetName.place(relwidth = 0.42, 
                             relheight = 0.12,
                             relx = 0.4,
                             rely = 0.25)
          
        # set the focus of the curser
        self.entryName.focus()

        # create a Label
        self.label_old_Pw = Label(self.reset_password,
                               text = "Old password: ",
                               font = "Chalkboard 18")
          
        self.label_old_Pw.place(relheight = 0.22,
                             relx = 0.18, 
                             rely = 0.42, anchor='center')
          
        # create a entry box for 
        # tyoing the message
        self.entry_old_Pw = Entry(self.reset_password, 
                             font = "Chalkboard 18")
          
        self.entry_old_Pw.place(relwidth = 0.42, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.38)
        

        self.label_new_Pw = Label(self.reset_password,
                               text = "New password: ",
                               font = "Chalkboard 18")
          
        self.label_new_Pw.place(relheight = 0.22,
                             relx = 0.16, 
                             rely = 0.55, anchor='center')
          
        # create a entry box for 
        # tyoing the message
        self.entry_new_Pw = Entry(self.reset_password, 
                             font = "Helvetica 18")
          
        self.entry_new_Pw.place(relwidth = 0.42, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.5)

          
        # set the focus of the curser
        self.entry_new_Pw.focus()
        self.entry_old_Pw.focus()
          
        # create a Continue Button 
        # along with action
        self.reset_go = Button(self.reset_password,
                         text = "Reset", 
                         font = "Chalkboard 15 bold", 
                         command = lambda: self.reset_goAhead(f"{self.entryResetName.get()},{self.entry_old_Pw.get()},{self.entry_new_Pw.get()}"))
          
        self.reset_go.place(relx = 0.38,
                      rely = 0.7)
        
  
    def goAhead(self, name_and_pw):
        if len(name_and_pw) > 0:
            msg = json.dumps({"action":"login", "name": name_and_pw})
            self.send(msg)
            try:
                response = json.loads(self.recv())
            except:
                return
            if response["status"] == 'ok':
                # messagebox.showinfo("Logged in","Successfully logged in! ")
                self.login.destroy()
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(name_and_pw.split(",")[0])
                self.layout(name_and_pw.split(",")[0])
                self.textCons.config(state = NORMAL)
                # self.textCons.insert(END, "Hello" +"\n\n")   
                self.textCons.insert(END, Menu +"\n\n")      
                self.textCons.config(state = DISABLED)
                self.textCons.see(END)

                process = threading.Thread(target=self.proc)
                process.daemon = True
                process.start()
                # while True:
                #     self.proc()
        # the thread to receive messages
            elif response["status"] == 'wrong_pw':
                messagebox.showwarning("Try again","Incorrect Password")
                # self.login.destroy()
            elif response["status"] == 'duplicate':
                messagebox.showwarning("Try again", "The account is already signed in.")
            
    def reset_goAhead(self,name_and_pw):
        if len(name_and_pw) > 0:
            msg = json.dumps({"action":"reset_pw", "name": name_and_pw})
            self.send(msg)
            response = json.loads(self.recv())
            if response["re_status"] == 'ok2reset':
                self.login.destroy()
                self.reset_password.destroy()
                # messagebox.showinfo("Successfully reset your password", "Start Your Chat!")
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(name_and_pw.split(",")[0])
                self.layout(name_and_pw.split(",")[0])
                self.textCons.config(state = NORMAL)
                # self.textCons.insert(END, "hello" +"\n\n")   
                self.textCons.insert(END, menu +"\n\n")      
                self.textCons.config(state = DISABLED)
                self.textCons.see(END)
                process = threading.Thread(target=self.proc)
                process.daemon = True
                process.start()
                # while True:
                #     self.proc()
        # the thread to receive messages
            elif response["re_status"] == 'wrong_pw':
                messagebox.showinfo("Try again","Password is not correct.")
            elif response["re_status"] == 'new_user':
                messagebox.showinfo("Try again","You need to register first! ")
            elif response["re_status"] == 'duplicate':
                messagebox.showinfo("Try again","You are already logged in! ")       
  
    # The main layout of the chat
    def layout(self,name):
        
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width = False,
                              height = False)
        self.Window.configure(width = 475,
                              height = 550,
                              bg = "#1C2833")
        self.labelHead = Label(self.Window,
                             bg = "#1C2833", 
                              fg = "#F2F3F4",
                              text = self.name ,
                               font = "Chalkboard 14 bold",
                               pady = 5)
          
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                          width = 455,
                          bg = "#B0B7C3")
          
        self.line.place(relwidth = 1,
                        y = 0.07 * 550,
                        height = 0.012 * 550)
          
        self.textCons = Text(self.Window,
                             width = 18, 
                             height = 2,
                             bg = "#17202A",
                             fg = "#F2F3F4",
                             font = "Chalkboard 14", 
                             padx = 5,
                             pady = 5)
          
        self.textCons.place(height = 0.745 * 550,
                            relwidth = 1, 
                            y = 0.08 * 550)
          
        self.labelBottom = Label(self.Window,
                                 bg = "#B0B7C3",
                                 height = 80)
          
        self.labelBottom.place(relwidth = 1,
                               y = 0.825 * 550)
          
        self.entryMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#F2F3F4",
                              font = "Chalkboard 13")
          
        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth = 0.74,
                            height = 0.06 * 550,
                            y = 0.008 * 550,
                            relx = 0.011)
          
        self.entryMsg.focus()
          
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "Send",
                                font = "Chalkboard 10 bold", 
                                width = 18,
                                bg = "#B0B7C3",
                                command = lambda : self.sendButton(self.entryMsg.get()))
          
        self.buttonMsg.place(relx = 0.77,
                             y = 0.008 * 550,
                             height = 0.06 * 550, 
                             relwidth = 0.22)
        
        self.buttonG = Button(self.Window,
                             text = "Game with peer!!",
                             font="Helvetica 10 bold",
                             width=18,
                             bg="#B0B7C3",
                             command = self.start_game)
        self.buttonG.place(relx=0.01,
                              y= 520,
                              height=34,
                              relwidth=0.48)
        self.buttonB = Button(self.Window,
                             text = "Quit group",
                             font="Helvetica 10 bold",
                             width=18,
                             bg="#B0B7C3",
                             command = self.quit)
        self.buttonB.place(relx=0.51,
                              y= 520,
                              height=34,
                              relwidth=0.48)
        

        self.textCons.config(cursor = "arrow")
          
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
          
        # place the scroll bar 
        # into the gui window
        scrollbar.place(height = 555,
                        relx = 0.974)
          
        scrollbar.config(command = self.textCons.yview)
          
        self.textCons.config(state = DISABLED)
  
    def quit(self):
        self.my_msg = 'bye'
    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.my_msg = msg
        # print(msg)
        self.entryMsg.delete(0, END)

    def start_game(self):
        self.my_msg = "request_to_start_a_game"
        self.gamer = 1


    def play(self, player):
        pygame.init()

        # Define colors
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        BG_COLOR = (0,0,0)
        YELLOW = (255, 205, 67)
        WHITE = (255, 255, 255)

        # Initialize Pygame window
        width, height = 800, 600

        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Paint Battle")
        clock = pygame.time.Clock()

        # Initialize game variables
        self.x1, self.y1 = width // 4, height // 2
        self.x2, self.y2 = width * 3 // 4, height // 2
        game_start = 0
        game_started = False

        # Number countdown animation variables
        countdown_start = 10
        countdown_timer = pygame.time.get_ticks()
        countdown_text = str(countdown_start)

        # Initialize ball variables
        ball1_trace = []
        ball2_trace = []
        ball1_color = BLUE
        ball2_color = YELLOW
        ball1_size = 40
        ball2_size = 40

        # Game duration in seconds
        game_duration = 20
        game_end_time = 0


        # Game loop
        running = True
        screen.fill(BG_COLOR)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            

            if not game_started:
                font = pygame.font.SysFont(None, 80)
                if not self.imready:
                    text = font.render("CLICK TO GET READY", True, RED)
                    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

                if pygame.mouse.get_pressed()[0]:
                    self.imready = True
                    pygame.draw.rect(screen, BLACK, (width // 2 - 400, height // 2 - 400, 800, 800))
                    text = font.render(f"YOU (PLAYER{player}) ARE READY", True, RED)
                    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
                    # self.my_msg = "game_ready"
                    mysend(self.socket, json.dumps({"action":"gaming", "from":"[" + self.name + "]", 
                                                        'operation':'ready'}))
                    time.sleep(0.03)
                
                
                if self.imready and self.peer_ready:
                    game_started = True 
                    pygame.draw.rect(screen, BLACK, (width // 2 - 400, height // 2 - 400, 800, 800))
                    game_start = pygame.time.get_ticks()
                    game_end_time = game_start + game_duration * 1000  # Convert to milliseconds
                    system_process = threading.Thread(target=self.timing)
                    system_process.start()

            if game_started:
                current_time = (pygame.time.get_ticks() - game_start) / 1000

                if current_time <= game_duration:
                    keys = pygame.key.get_pressed()

                    # Player 1 controls (Blue)
                    if player == 1:
                        if keys[pygame.K_a]:
                            self.x1 -= 4
                            self.x1 %= 800
                        if keys[pygame.K_d]:
                            self.x1 += 4
                            self.x1 %= 800
                        if keys[pygame.K_w]:
                            self.y1 -= 4
                            self.y1 %= 600
                        if keys[pygame.K_s]:
                            self.y1 += 4
                            self.y1 %= 600
                        mysend(self.socket, json.dumps({"action":"gaming", "from":"[" + self.name + "]", 
                                                        'operation':'moving','coordinate':f"{self.x1},{self.y1}"}))

                    



                    # Player 2 controls (Yellow)
                    else:
                        if keys[pygame.K_a]:
                            self.x2 -= 4
                            self.x2 %= 800
                        if keys[pygame.K_d]:
                            self.x2 += 4
                            self.x2 %= 800
                        if keys[pygame.K_w]:
                            self.y2 -= 4
                            self.y2 %= 600
                        if keys[pygame.K_s]:
                            self.y2 += 4
                            self.y2 %= 600
                        mysend(self.socket, json.dumps({"action":"gaming", 'operation':"moving",
                                                        "from":"[" + self.name + "]", 'coordinate':f"{self.x2},{self.y2}"}))



                    # Add ball positions to traces with respective colors and timestamps
                    ball1_trace.append((self.x1, self.y1, BLUE, pygame.time.get_ticks()))
                    ball2_trace.append((self.x2, self.y2, YELLOW, pygame.time.get_ticks()))

                    # Draw ball traces with colors
                    all_traces = sorted(ball1_trace + ball2_trace, key=lambda x: x[3])
                    for pos in all_traces:
                        pygame.draw.circle(screen, pos[2], (pos[0], pos[1]), ball1_size if pos[2] == BLUE else ball2_size)
                    
                else:
                    time.sleep(10)
                    # Display final scene
                    pygame.draw.rect(screen, BLACK, (width, height, 650, 250))
                    font = pygame.font.SysFont(None, 50)

                    # Calculate total painted area for each player
                    screen_surface = pygame.surfarray.array3d(screen)
                    total_area_player1 = 0
                    total_area_player2 = 0
                    c = 0
                    for i in screen_surface:
                        c += 1
                        if c % 10 == 0:
                            for pixel in i:
                                if (pixel == BLUE).all():
                                    total_area_player1 += 1
                                elif (pixel == YELLOW).all():
                                    total_area_player2 += 1
                    # total_area_player1 = sum([ball1_size ** 2 for _ in ball1_trace])
                    # total_area_player2 = sum([ball2_size ** 2 for _ in ball2_trace])

                    # Determine the winner based on the total painted area
                    
                    blue_ratio = int(total_area_player1*100/(total_area_player1 + total_area_player2))
                    yellow_ratio = 100 - blue_ratio
                    self.winner = "Player 1 (Blue)" if blue_ratio > yellow_ratio else "Player 2 (Yellow)" if blue_ratio < yellow_ratio else "It's a tie!"
                    text = font.render(f"Winner: {self.winner}  {blue_ratio}:{yellow_ratio}", True, WHITE)
                    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
                    pygame.display.flip()
                    self.textCons.config(state = NORMAL)
                    self.textCons.insert(END, "[System INFO] Winner: "+ self.winner +"\n")      
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)
                    # Wait for a few seconds before quitting
                    pygame.time.delay(5000)
                    running = False
        

            pygame.display.flip()
            clock.tick(60)
            time.sleep(0.01)

        pygame.quit()
        sys.exit()



    def timing(self):
        for i in range(20):
            self.textCons.config(state = NORMAL)
            self.textCons.insert(END, "[System INFO] " + str(20-i) +"\n")      
            self.textCons.config(state = DISABLED)
            self.textCons.see(END)
            time.sleep(1)
        self.textCons.config(state = NORMAL)
        self.textCons.insert(END, "[System INFO] Calculating the result..." +"\n")      
        self.textCons.config(state = DISABLED)
        self.textCons.see(END)
       
       




    def proc(self):
        # print(self.msg)
        while True:
            read, write, error = select.select([self.socket], [], [], 0)
            peer_msg = []
            # print(self.msg)
            if self.socket in read:
                peer_msg = self.recv()
            if len(self.my_msg) > 0 or len(peer_msg) > 0:
                # print(self.system_msg)
                # if not self.isgaming:
                self.system_msg = self.my_msg + '\n'
                self.system_msg += self.sm.proc(self.my_msg, peer_msg)
                if self.system_msg.lstrip() == "[Server]: Enjoy the game!":
                    # print(self.system_msg + '------1')
                    self.system_msg += (' '+self.name + '\n')
                    self.system_msg += (f'You are gamer {self.gamer}')
                    self.my_msg = ''
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END, self.system_msg + "\n\n")
                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
                    game_proc = threading.Thread(target=self.play,args=(self.gamer,))
                # print(self.system_msg + '------2')
                    game_proc.start()
                elif self.system_msg.lstrip() == 'peer is ready':
                    self.peer_ready = True
                    self.my_msg = ''
                elif (self.system_msg.lstrip())[:7] == '114514:':
                    coordinate = self.system_msg.strip()[7:].split(',')
                    
                    if self.gamer == 1:
                        self.x2, self.y2 = int(coordinate[0]), int(coordinate[1])
                    else:
                        self.x1, self.y1 = int(coordinate[0]), int(coordinate[1])
                    
                else:
                    self.my_msg = ""
                    self.textCons.config(state = NORMAL)
                    self.textCons.insert(END, self.system_msg +"\n\n")      
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)

    def run(self):
        self.login()
# create a GUI class object
if __name__ == "__main__": 
    g = GUI()
