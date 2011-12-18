﻿#!/usr/bin/env python

import os, Tkinter, ttk, tkFileDialog
from Tkconstants import *
from pyftpdlib import ftpserver

tk = Tkinter.Tk()
tk.geometry("390x212")
tk.minsize(330,212)
tk.title("Course work FTP Server Lite")

#Values
root_dir = Tkinter.StringVar()
root_dir.set(os.getcwd() + os.sep + "share")
username = Tkinter.StringVar()
username.set("user")
password = Tkinter.StringVar()
password.set("passwd")
current_state = Tkinter.StringVar()
current_state.set("not running")
listen_ip = Tkinter.StringVar()
listen_ip.set("0.0.0.0")
listen_port = Tkinter.StringVar()
listen_port.set("21")

def directory_select_action():
    root_dir.set(tkFileDialog.askdirectory().replace("/","\\"))
def start_action():
    print "Start action performed"
    start_button.state(['disabled'])
    stop_button.state(['!disabled'])
def stop_action():
    print "Stop action performed"
    start_button.state(['!disabled'])
    stop_button.state(['disabled'])
    
#Frames
login_frame = ttk.Frame(tk,relief=SOLID, borderwidth=1)
login_frame.pack(fill=X, ipadx=3, ipady=3, pady=3, padx=3)

directory_frame = ttk.Frame(tk, relief=SOLID,borderwidth=1)
directory_frame.pack(fill=X, ipadx=3, ipady=3, pady=3, padx=3)

listen_frame = ttk.Frame(tk, relief=SOLID, borderwidth=1)
listen_frame.pack(fill=X, ipadx=3, ipady=3, pady=3, padx=3)

start_stop_frame = ttk.Frame(tk,relief=SOLID, borderwidth=1)
start_stop_frame.pack(fill=X, ipadx=3, ipady=3, pady=3, padx=3)

state_frame = ttk.Frame(tk, relief=SOLID, borderwidth=1)
state_frame.pack(fill=X, ipadx=3, ipady=3, pady=3, padx=3, side=BOTTOM)


#Username Password
user_label = ttk.Label(login_frame,text="Username:")
user_label.grid(row=0, column=0)

user_input = ttk.Entry(login_frame, textvariable=username)
user_input.grid(row=0, column=1,pady=3)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=1,column=0)

password_input = ttk.Entry(login_frame,textvariable=password)
password_input.grid(row=1, column=1)

#Directory Select
directory_label = ttk.Label(directory_frame, text="Share directory")
directory_label.pack(side=LEFT)

ttk.Button(directory_frame, text="Browse", command=directory_select_action).pack(side=RIGHT)

directory_input = ttk.Entry(directory_frame, width=64, textvariable=root_dir)
directory_input.pack(side=RIGHT, padx=3)

#Listen Frame
ttk.Label(listen_frame, text="Connection settings").pack(side=LEFT)

listen_port_input = ttk.Entry(listen_frame, textvariable=listen_port,width=6)
listen_port_input.pack(side=RIGHT)

listen_ip_input = ttk.Entry(listen_frame, textvariable=listen_ip, width=15)
listen_ip_input.pack(side=RIGHT)

#Start Stop
ttk.Label(start_stop_frame, text="Server control ").pack(side=LEFT)

stop_button = ttk.Button(start_stop_frame, text="Stop", state=['disabled'], command=stop_action)
stop_button.pack(side=RIGHT, padx=3)

start_button = ttk.Button(start_stop_frame, text="Start", command=start_action)
start_button.pack(side=RIGHT, padx=3)

#State Area
state_label = ttk.Label(state_frame, text="Server state").pack(side=LEFT)
state_value = ttk.Label(state_frame, textvariable=current_state)
state_value.pack(side=RIGHT)
state_value['foreground'] = "blue"

#FTP TOFO: Daemonise
authorizer = ftpserver.DummyAuthorizer()
authorizer.add_user('user', '12345', os.getcwd(), perm='elradfmw')
ftp_handler = ftpserver.FTPHandler
ftp_handler.authorizer = authorizer
ftp_handler.banner = "pyftpdlib %s based ftpd ready." %ftpserver.__ver__
address = ('0.0.0.0', 21)
ftpd = ftpserver.FTPServer(address, ftp_handler)
ftpd.max_cons = 256
ftpd.max_cons_per_ip = 5

    # start ftp server
ftpd.serve_forever()
tk.mainloop()