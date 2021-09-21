#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import humanize
from pafy import new,get_playlist
import pafy
import os,sys
from os import path
import urllib.request
from colorama import init,Fore
import sys, os , re , wget
import requests as r
from prettytable import PrettyTable
text='''

███████  ██████  ██████  ██████  ██████  ██  ██████  ███    ██  
██      ██      ██    ██ ██   ██ ██   ██ ██ ██    ██ ████   ██  
███████ ██      ██    ██ ██████  ██████  ██ ██    ██ ██ ██  ██  
     ██ ██      ██    ██ ██   ██ ██      ██ ██    ██ ██  ██ ██  
███████  ██████  ██████  ██   ██ ██      ██  ██████  ██   ████  
                                                                
                                           Coded By Fares Emad

'''
init(autoreset=True)
print(Fore.RED + text)
#==============================================================#
table=PrettyTable()
table.field_names =["Number of download","Download Video from (Facebook / Youtube)"]
table.add_row(["1- ","Audio"])
table.add_row(["2- ","Video"])
table.add_row(["3- ","Playlist"])
table.add_row(["4- ","Facebook"])
print(table)
print(' [ S C O R P I O N ] '.center(65,"+"))
chose=input(":=> ")
#==============================================================#
def downaudio():
    try:
        url=input("Enter Id Or Link-Video: ")
        vobj = new(url)
        streams = vobj.audiostreams
        for stream in range(len(streams)):
            size=humanize.naturalsize(streams[stream].get_filesize())
            print(stream,'=> ',size)
        quality = input('Choose the Quality Number:- ')
        down=vobj.audiostreams[int(quality)]
        path=input("Which Path: ")
        down.download(path)
    except:
        print("OOPS!! General Error or Invalid URL")
#==============================================================#
def downvideo():
    try:
        url=input("Enter Id Or Link-Video: ")
        vobj = new(url)
        streams = vobj.streams
        for stream in range(len(streams)):
            size=humanize.naturalsize(streams[stream].get_filesize())
            print(stream,'=> ',size)
        quality = input('Choose the Quality Number:- ')
        down=vobj.streams[int(quality)]
        path=input("Which Path: ")
        down.download(path)
    except:
        print("OOPS!! General Error or Invalid URL")
#==============================================================#
def downlist():
    try:
        url = input('Enter ID or URL : ')
        print("-"*30)
        path=input("Which Path : ")
        print("-"*35)
        vobj = get_playlist(url)
        for video in range(len(vobj['items'])):
            down = vobj['items'][video]['pafy'].getbest()
            print("-"*35)
            down.download(path)
    except:
        print("OOPS!! General Error or Invalid URL")
#==============================================================#
filedir = os.path.join('C:\\Users\\Scorpion\\Desktop\\test python network\\beutifull')
ERASE_LINE = '\x1b[2K'
def menu():
    print("-------------------Facebook Video Downloader-------------------")
    print("1. Download Low Resolution Video")
    print("2. Download High Resolution Video")
    print("3. Exit")
    print("----------------------------*******----------------------------")
#==============================================================#
def choices():
    CHOICE = input("ENTER YOUR CHOICE: ")
    if CHOICE == "1":
        try:
            LINK = input("Enter a Facebook Video Post URL: ")
            html = r.get(LINK)
            sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
        except r.ConnectionError:
            print("OOPS!! Connection Error.")
        except r.Timeout:
            print("OOPS!! Timeout Error")
        except r.RequestException:
            print("OOPS!! General Error or Invalid URL")
        except (KeyboardInterrupt, SystemExit):
            print("Ok ok, quitting")
            sys.exit(1)
        except TypeError:
            print("Video May Private or Invalid URL")
        else:
            sd_url = sdvideo_url.replace('sd_src:"', '')
            print("\n")
            print("Normal Quality: " + sd_url)
            print("[+] Video Started Downloading")
            wget.download(sd_url, filedir)
            sys.stdout.write(ERASE_LINE)
            print("\n")
            print("Video downloaded")

    elif CHOICE == "2":
        try:
            LINK = input("Enter a Facebook Video Post URL: ")
            html = r.get(LINK)
            hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
        except r.ConnectionError:
            print("OOPS!! Connection Error.")
        except r.Timeout:
            print("OOPS!! Timeout Error")
        except r.RequestException:
            print("OOPS!! General Error or Invalid URL")
        except (KeyboardInterrupt, SystemExit):
            print("Ok ok, quitting")
            sys.exit(1)
        except TypeError:
            print("Video May Private or Hd version not avilable")
        else:
            hd_url = hdvideo_url.replace('hd_src:"', '')
            print("\n")
            print("High Quality: " + hd_url)
            print("[+] Video Started Downloading")
            wget.download(hd_url, filedir)
            sys.stdout.write(ERASE_LINE)
            print("\n")
            print("Video downloaded")

    elif CHOICE == "3":
        print("Exiting")
#==============================================================#
if chose=='audio' or chose=='1':
    downaudio()
elif chose=='video' or chose=='2':
    downvideo()
elif chose=='playlist' or chose=='3':
    downlist()
elif chose=='facebook' or chose=='4':
    menu()
    choices()
rload=input("Do You Want Download Again..? (yes / no) ")
if rload == "yes" or rload == "y":
    print(Fore.RED + text)
    print(table)
    print(' [ S C O R P I O N ] '.center(65,"+"))
    chose=input(":=> ")
    if chose=='audio' or chose=='1':
        downaudio()
    elif chose=='video' or chose=='2':
        downvideo()
    elif chose=='playlist' or chose=='3':
        downlist()
    elif chose=='facebook' or chose=='4':
        menu()
        choices()
else:
    sys.exit()