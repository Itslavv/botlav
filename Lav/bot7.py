# -*- coding: utf-8 -*-
#Thaks to Hello world square
#Thaks to all suport team bot
from HEADER import *
from DATA.ttypes import Message
from DATA.ttypes import ContentType as Type
from DATA.ttypes import ChatRoomAnnouncementContents
from DATA.ttypes import ChatRoomAnnouncement
from thrift import transport, protocol, server
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from datetime import datetime, timedelta
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
import pyimgflip
from zalgo_text import zalgo
from threading import Thread,Event
#===============BOT 1===============#
yans = LINE("email","psswrd")
#===============BOT 2===============#
ki = LINE('email','psswrd')
#===============BOT 3===============#
kk = LINE('email','psswrd')
#===============BOT 4===============#
kc = LINE('email','psswrd')
#===============BOT 5===============#
kb = LINE('email','psswrd')
#===============BOT 6===============#
ke = LINE('email','psswrd')
#===============BOT 7===============#
sw = LINE('email','psswrd')

print("\nοΉ¦οΉ¦οΉ¦πΊ πππππππ πππ πΊοΉ¦οΉ¦οΉ¦\n")

oepoll = OEPoll(yans)
call = yans
creator = ["u843ac8156db57f9958394290e45f8e17"]
owner = ["MID"]
admin = ["MID"]
staff = ["MID"]
mid = yans.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = ke.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [yans,ki,kk,kc,kb,ke]
ABC = [ki,kk,kc,kb,ke]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid]
Squad = [mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid]
AKU = [yans]
TEAMBOTPROTECT = admin + owner + staff
Team = owner + admin + Bots + staff + Squad
Saints = owner + admin + Bots + staff + Squad
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

protectcancel = []
welcome = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []

responsename = yans.getProfile().displayName
responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName
responsename5 = ke.getProfile().displayName
responsename6 = sw.getProfile().displayName

settings = {
    "userAgent": ['Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'],
    "autoblock": False,
    "autoRead": True,
    "welcome": False,
    "javascrift": False,
    "leave": False,
    "expire" : True,
    "nCall" : True,
    "time": time.time(),
    "flood": 0,
    "temp_flood" : False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "changevp": False,
    "changeCover":False,
    "autoLike":{},
    "chatEvent": {},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":True,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "postId":False,
    "staff":{},
    "dhenza":{},
    "likeOn":{},
    "autoLike": {},
    "status":False,
    "autoBlock": False,
    "Timeline": True,
    "invite":False,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "Mentionkick":False,
    "addbots":False,
    "dellbots":False,
    "addsquads":False,
    "dellsquads":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "welcomeOn":False,
    "sticker":False,  
    "selfbot":True,
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "mention":"nah loh ketahuan ngintip msh aja sider",
    "Respontag":"Apa'an sihh π",
    "welcome":"Wellcome to my Fams",
    "comment":"α΄α΄α΄α΄ΚΙͺα΄α΄ ΚΚ: ΚΚα΄Ι΄κ±\n\n\nα΄Κα΄α΄α΄α΄Κ: http://line.me/ti/p/~gepengcharlez\nα΄α΄Ι΄α΄ΚΙͺα΄α΄ α΄α΄κ±α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)",
    "message":"α΄α΄α΄α΄sΙͺΚ Κα΄ sα΄α΄α΄Κ α΄α΄α΄..\n\n\n\nΚΚα΄Ι΄κ±\nα΄α΄Ι΄α΄ΚΙͺα΄α΄ α΄α΄κ±α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄\n\n\nα΄Κα΄α΄α΄α΄Κ: http://line.me/ti/p/~gepengcharlez",
}


read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
mulai = time.time()

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
yansProfile = yans.getProfile()
myProfile["displayName"] = yansProfile.displayName
myProfile["statusMessage"] = yansProfile.statusMessage
myProfile["pictureStatus"] = yansProfile.pictureStatus

contact = yans.getProfile()
backup = yans.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

with open('creator.json', 'r') as fp:
     creator = json.load(fp)
with open('owner.json', 'r') as fp:
     owner = json.load(fp)
with open('admin.json', 'r') as fp:
     admin = json.load(fp)
with open('squad.json', 'r') as fp:
     Squad = json.load(fp)

imagesOpen = codecs.open("image.json","r","utf-8")
images = json.load(imagesOpen)
videosOpen = codecs.open("video.json","r","utf-8")
videos = json.load(videosOpen)
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)
audiosOpen = codecs.open("audio.json","r","utf-8")
audios = json.load(audiosOpen)
mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
    
def cloneProfile(mid):
    contact = yans.getContact(mid)
    if contact.videoProfile == None:
        yans.cloneContactProfile(mid)
    else:
        profile = yans.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        yans.updateProfile(profile)
        pict = yans.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = yans.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = yans.getProfileDetail(mid)['result']['objectId']
    yans.updateProfileCoverById(coverId)
    
def restoreProfile():
    profile = yans.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        yans.updateProfileAttribute(8, profile.pictureStatus)
        yans.updateProfile(profile)
    else:
        yans.updateProfile(profile)
        pict = yans.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = yans.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    yans.updateProfileCoverById(coverId)
    
def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return yans.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return yans.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = yans.genOBSParams({'oid': yans.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = yans.server.postContent('{}/talk/vp/upload.nhn'.format(str(yans.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return yans.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        yans.updateProfilePicture(path_p, 'vp')

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Mention Userγ{}γ\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nβββ[ {} ]".format(str(yans.getGroup(to).name))
                except:
                    no = "\nβββ[ Success ]"
        yans.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        yans.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider Userγ{}γ\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nβββ[ {} ]".format(str(yans.getGroup(to).name))
                except:
                    no = "\nβββ[ Success ]"
        yans.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        yans.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Member Masukγ{}γ\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = yans.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nβββ[ {} ]".format(str(yans.getGroup(to).name))
                except:
                    no = "\nβββ[ Success ]"
        yans.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        yans.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = yans.getAllContactIds()
        gid = yans.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :γGaje Botsγ  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n β’ "+bot
        yans.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        yans.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        yans.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        yans.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def removeCmd(cmd, text):
	key = Setmain["keyCommand"]
	rmv = len(key + cmd) + 1
	return text[rmv:]

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

        
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
 

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = " β―βΝΝ‘βΝΝ‘πππππππ πππ ΝΝ‘βΝΝ‘ββ―\nβ­ββββββββββββββ\n"
    helpMessage += "β " + " β­ββ’ πππππππ ππππ β’β\n"
    helpMessage += "β " + " βββββββββββββββ\n"
    helpMessage += "β " + " β 0%i)" % num + key + " πΈHelp2\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈHelp3\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈSet\n"
    helpMessage += "β " + " βββββββββββββββ\n"
    helpMessage += "β " + " β 0%i)" % num + key + " πΈ.Gettoken (Chert)\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈCek key\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈCatbot On/Off\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈCek\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈCreator\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈAbout\n"
    num = (num+1)
    helpMessage += "β " + " β 0%i)" % num + key + " πΈMe\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈmid\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈGet id @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈProfile @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈMybot\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈReject\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈRchat\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈBcast: text\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈCek name\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈName: text\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈReset name\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈReboot\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈTime\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈGinfo\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈInfogroup: no\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈInfomem: no\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈLeave: no\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈFlist\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈclone @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈRestore\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈGlist\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈCurl/Orl\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈTarik No\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈUpgroup\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈUpbot\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈUpfoto\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈChangedual\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈChangedualurl: url\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key +  " πΈMention\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈRname\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈSider ON/OFF\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈ.By /leave no\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈGift: @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈSpam: @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈLike @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈDelfriend @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈID line: idnya\n"
    num = (num+1)  
    helpMessage += "β " + " β %i)" % num + key + " πΈUnsend On/Off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈtimeline On/Off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈAutoblock on/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈListblok/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈCheck message\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈidcontact @\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈcontact mid\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈinviteme no\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈContact on/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈRespon on/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈAutojoin on/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈAutoadd on/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈSticker on/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈJointicket on/off\n"
    num = (num+1)
    helpMessage += "β " + " β %i)" % num + key + " πΈwelcome on/off\n"
    num = (num+1)
    helpMessage += "β " + " βββββββββββββββ\n"
    helpMessage += "β " + " β°ββββ’ sΚ ΚΚ: ΚΚα΄Ι΄κ± β’ββββ\n"
    helpMessage += "β°βββββββββββββββ \n"
    helpMessage += "Κα΄α΄α΄Κ Κα΄α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)\n"
    helpMessage += "line://ti/p/~gepengcharlez"
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage02 = " β―βΝΝ‘βΝΝ‘πππππππ πππ ΝΝ‘βΝΝ‘ββ―\nβ­ββββββββββββββ\n"
    helpMessage02 += "β" + " β­βββ’ ππππππππ πππ β’ββ\n"
    helpMessage02 += "β" + " βββββββββββββββ\n"
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈAutojoin on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈAutoadd on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈSettings\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈBan:on @\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈBan:on\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈBanlist\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈclearban\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈKick @\n"
    num = (num+1)
    helpMessage02 += "β" + " β 0%i)" % num + key + " πΈJointicket on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈTalkban:on @\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈTalkban:on\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈTalkbanlist\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈUntalkban:on @\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈUntalkban:on\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈUnban:on\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈList on\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈList off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈList sider\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈUnban:on @\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈIndo: kata \n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈInggris: kata \n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈKorea: kata \n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈJp: kata \n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈThai: kata \n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈArab: kata \n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈJawa: kata \n"
    num = (num+1)
    helpMessage02 += "β " + "βββββββββββββββ\n"
    helpMessage02 += "β" + " β  β’ ππππππππ ππππππ β’  \n"
    helpMessage02 += "β" + " βββββββββββββββ\n"
    helpMessage02 += "β" + " β %i)" % num + key + " πΈAllpro on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈProtecturl on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈProtectinvite on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈProtectjoin on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈProtectcancel on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈProtectkick on/off\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈJs ON/OFF\n"
    helpMessage02 += "β " + "βββββββββββββββ\n"
    helpMessage02 += "β" + " β  β’ πππ πππππ ππππ β’  \n"
    helpMessage02 += "β" + " βββββββββββββββ\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈα΄α΄α΄ΙͺΙ΄ α΄Ι΄\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈα΄α΄α΄ΙͺΙ΄ α΄??\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈα΄α΄α΄ΙͺΙ΄ @\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈα΄α΄α΄ΙͺΙ΄α΄α΄ΚΚ @\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈsα΄α΄??  α΄Ι΄\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈsα΄α΄?? α΄Ι΄\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈsα΄α΄?? @\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈsα΄α΄??α΄α΄ΚΚ @\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈΚα΄α΄ α΄Ι΄\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i) " % num + key + " πΈΚα΄α΄ α΄??\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈSpesan: kata\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈSwelcome: kata\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈSrespon: kata\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈSspam: kata\n"
    num = (num+1)
    helpMessage02 += "β" + " β %i)" % num + key + " πΈSsider: kata\n"
    num = (num+1)
    helpMessage02 += "β " + "βββββββββββββββ\n"
    helpMessage02 += "β " + "β°ββββ’ sΚ ΚΚ: ΚΚα΄Ι΄κ± β’ββββ\n"
    helpMessage02 += "β°ββββββββββββββ \n"
    helpMessage02 += "Κα΄α΄α΄Κ Κα΄α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)\n"
    helpMessage02 += "line://ti/p/~gepengcharlez"
    return helpMessage02
    
def helpmedia():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage03 = " β―βΝΝ‘βΝΝ‘πππππππ πππ ΝΝ‘βΝΝ‘ββ―\nβ­ββββββββββββββ\n"
    helpMessage03 += "β" + "  β­βββ’ πππππ πππππππ β’ββ\n"
    helpMessage03 += "β" + "  βββββββββββββββ\n"
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈImagetext: txt\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈal-qur'an no\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈTopnews\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈmeme fb\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈFs text\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈMp3: judul\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈListsticker\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈListimage\n"
    num = (num+1)
    helpMessage03 += "β " + " β 0%i)" % num + key + " πΈListvideo\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈListmp3\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈAddsticker nama\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈAddmp3 nama\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈAddimg nama\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈDellsticker nama\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈDellmp3 nama\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈDellvideo nama\n"
    num = (num+1)
    helpMessage03 += "β " + " β %i)" % num + key + " πΈDellimg nama\n"
    num = (num+1)
    helpMessage03 += "β " + " βββββββββββββββ\n"
    helpMessage03 += "β " + " β°ββββ’ sΚ ΚΚ: ΚΚα΄Ι΄κ± β’ββββ\n"
    helpMessage03 += "β°ββββββββββββββ \n"
    helpMessage03 += "Κα΄α΄α΄Κ Κα΄α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)\n"
    helpMessage03 += "line://ti/p/~gepengcharlez"
    return helpMessage03    

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if ki.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            ki.reissueGroupTicket(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventJoinByTicket = False
                            ki.updateGroup(X)
                            Ti = ki.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ti)
                            sw.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ Κα΄α΄α΄ Η«Κ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ..!!!")
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            X = sw.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            sw.updateGroup(X)
                            sw.leaveGroup(op.param1)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                yans.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    yans.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        yans.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            yans.updateGroup(X)
                                            yans.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ke.reissueGroupTicket(op.param1)
                                                X = ke.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ke.updateGroup(X)
                                                yans.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
                                        
        if op.type == 11:
            if wait['qr'] == True:
                try:
                    if yans.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            yans.reissueGroupTicket(op.param1)
                            X = yans.getGroup(op.param1)  
                            X.preventJoinByTicket = False
                            yans.updateGroup(X)   
                except:
                   pass                            
                                        
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        yans.acceptGroupInvitation(op.param1)
                        ginfo = yans.getGroup(op.param1)
                        
                        yans.leaveGroup(op.param1)
                    else:
                        yans.acceptGroupInvitation(op.param1)
                        ginfo = yans.getGroup(op.param1)
                        
            if Amid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        
            if Bmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        
            if Cmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        
            if Dmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        
            if Emid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
#============================================================                        

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        yans.acceptGroupInvitation(op.param1)
                        ginfo = yans.getGroup(op.param1)
                     
                    else:
                        yans.acceptGroupInvitation(op.param1)
                        ginfo = yans.getGroup(op.param1)
                        
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        
                        
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                        
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = yans.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            yans.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kc.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kb.cancelGroupInvitation(op.param1,[_mid])      
                                    except:
                                        try:
                                            group = kc.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                ke.cancelGroupInvitation(op.param1,[_mid])      
                                        except:
                                            pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = yans.getGroup(op.param1)
                contact = yans.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                yans.sendImageWithURL(op.param1, image)
                
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = yans.getGroup(op.param1)
                contact = yans.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2]) 
                yans.sendImageWithURL(op.param1, image)
                
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                            
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        yans.sendText(op.param1, wait["message"])
                        
        if op.type == 5:
            if settings['autoBlock'] == False:
                try:
                    usr = yans.getContact(op.param2)
                    yans.sendMessage(op.param1, "Κα΄ΙͺΙͺ... {} α΄α΄α΄? α΄α΄ α΄α΄α΄α΄ΚΚα΄α΄α΄ α΄Ι΄ \nΚΙͺΚα΄ Κα΄Κα΄α΄α΄©α΄Ι΄α΄ΙͺΙ΄Ι’α΄Ι΄ \nα΄α΄α΄α΄Ι΄ α΄α΄Κα΄ α΄Ιͺ α΄Κ ".format(usr.displayName))
                    yans.talk.blockContact(0, op.param1)
                except:
                	pass
                	
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                	pass
                
        if op.type == 19:
            if op.param3 in admin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).findAndAddContactsByMid("u042b866c381573d1e399d16b51ca2d8c")
                    random.choice(ABC).inviteIntoGroup(op.param1,["u042b866c381573d1e399d16b51ca2d8c"])
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                	pass
                
        if op.type == 19:
            if op.param3 in staff:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).findAndAddContactsByMid("u843ac8156db57f9958394290e45f8e17")
                    random.choice(ABC).inviteIntoGroup(op.param1,["u843ac8156db57f9958394290e45f8e17"])
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                	pass
           
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        invsend = 0
                        Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ α΄Ιͺα΄α΄ α΄Κα΄Ι΄Ι’ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ..!!!")
                        sw.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        sw.leaveGroup(op.param1)
                        X = random.choice(KAC).getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        random.choice(KAC).inviteIntoGroup(op.param1,[Zmid])    
                        random.choice(KAC).updateGroup(X)
                except:
                    pass
     
        if op.type == 19:
            if wait['ghost'] == True:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = random.choice(ABC).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(ABC).updateGroup(G)
                        Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid])
                        sw.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ α΄Ιͺα΄α΄ α΄Κα΄Ι΄Ι’ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ..!!!")
                        sw.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        sw.leaveGroup(op.param1)
                        X = yans.getGroup(op.param1)
                        yans.updateGroup(X)
                        X.preventedJoinByTicket = True
                        yans.inviteIntoGroup(op.param1,[Zmid])                        
                        wait["blacklist"][op.param2] = True
                except:
                    pass
      
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = yans.reissueGroupTicket(msg.to)
                        yans.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        random.choice(KAC).findAndAddContactsByMid(op.param1,[Zmid])
                        random.choice(KAC).inviteIntoGroup(op.param1,[Zmid])
                        random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        random.choice(ABC).sendMessage(op.param1,"α΄Ι΄α΄Ιͺ JS sΚα΄α΄ΙͺΙ΄Ι’")
                    else:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        random.choice(ABC).sendMessage(op.param1,"α΄Ι΄α΄Ιͺ JS sΚα΄α΄ΙͺΙ΄Ι’")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                            random.choice(ABC).sendMessage(op.param1,"=α΄α΄α΄ΙͺΙ΄ ΙͺΙ΄α΄ Ιͺα΄α΄α΄=")
                else:
                    pass
            except:
                pass
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        pass
         
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[Zmid])
                            ki.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ α΄α΄Ι΄α΄α΄Κ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ")
                            ki.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[Zmid])
                                kk.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ α΄α΄Ι΄α΄α΄Κ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ")
                                kk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[Zmid])
                                    kc.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ α΄α΄Ι΄α΄α΄Κ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ")
                                    kc.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[Zmid])
                                        kc.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ α΄α΄Ι΄α΄α΄Κ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ")
                                        kc.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[Zmid])
                                            ke.sendMessage(op.param1,"Κα΄Κ α΄α΄α΄α΄ α΄α΄ΙͺΙ΄ α΄α΄Ι΄α΄α΄Κ α΄Ιͺα΄©α΄α΄ Ι΄ΙͺΚ")
                                            ke.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:                                        
                                            pass
                return

        if op.type == 19 or op.type == 32:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[mid,Bmid,Cmid,Dmid,Emid])
                        yans.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        ke.acceptGroupInvitation(op.param1)
                        ki.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[mid,Amid,Cmid,Dmid,Emid])
                            yans.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            kk.cancelGroupInvitation(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Dmid,Emid])
                                yans.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                ke.acceptGroupInvitation(op.param1)
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    yans.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Emid])
                                        yans.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        ke.acceptGroupInvitation(op.param1)
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid])
                                            yans.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                            kb.acceptGroupInvitation(op.param1)
                                            ke.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[mid,Amid,Cmid,Dmid,Emid])
                        yans.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        ke.acceptGroupInvitation(op.param1)
                        kk.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Dmid,Emid])
                            yans.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            kc.cancelGroupInvitation(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                yans.kickoutFromGroup(op.param1,[op.param2])
                                yans.inviteIntoGroup(op.param1,[Amid,Bmid,Cmid,Dmid,Emid])
                                ki.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                ke.acceptGroupInvitation(op.param1)
                                yans.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    yans.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Emid])
                                        yans.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        ke.acceptGroupInvitation(op.param1)
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid])
                                            yans.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                            kb.acceptGroupInvitation(op.param1)
                                            ke.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Dmid,Emid])
                        yans.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        ke.acceptGroupInvitation(op.param1)
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            yans.kickoutFromGroup(op.param1,[op.param2])
                            yans.inviteIntoGroup(op.param1,[Amid,Bmid,Cmid,Dmid,Emid])
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            yans.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[mid,Bmid,Cmid,Dmid,Emid])
                                yans.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                ke.acceptGroupInvitation(op.param1)
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    yans.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid])
                                        yans.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        kb.acceptGroupInvitation(op.param1)
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Emid])
                                            yans.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                            ke.acceptGroupInvitation(op.param1)
                                            kb.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Emid])
                        yans.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        ke.acceptGroupInvitation(op.param1)
                        kb.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[mid,Bmid,Cmid,Dmid,Emid])
                            yans.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[mid,Amid,Dmid,Cmid,Emid])
                                yans.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                ke.acceptGroupInvitation(op.param1)
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                    yans.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = yans.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    yans.updateGroup(G)
                                    Ticket = yans.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        yans.kickoutFromGroup(op.param1,[op.param2])
                                        yans.inviteIntoGroup(op.param1,[Dmid,Amid,Bmid,Cmid,Emid])
                                        kc.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kb.acceptGroupInvitation(op.param1)
                                        ke.acceptGroupInvitation(op.param1)
                                        yans.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid])
                                            yans.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                            kb.acceptGroupInvitation(op.param1)
                                            ke.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            pass
                                    
                return
               
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid])
                        yans.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        ke.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            yans.kickoutFromGroup(op.param1,[op.param2])
                            yans.inviteIntoGroup(op.param1,[Dmid,Amid,Bmid,Cmid,Emid])
                            kb.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1) 
                            yans.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[mid,Dmid,Bmid,Cmid,Emid])
                                yans.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                ke.acceptGroupInvitation(op.param1)
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                    yans.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = yans.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    yans.updateGroup(G)
                                    Ticket = yans.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[mid,Amid,Dmid,Cmid,Emid])
                                        yans.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        kb.acceptGroupInvitation(op.param1)
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Dmid,Emid])
                                            yans.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kb.acceptGroupInvitation(op.param1)
                                            ke.acceptGroupInvitation(op.param1)
                                            kc.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            pass             

                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        yans.kickoutFromGroup(op.param1,[op.param2])
                        yans.inviteIntoGroup(op.param1,[Dmid,Amid,Bmid,Cmid,Emid])
                        ke.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        yans.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[mid,Dmid,Bmid,Cmid,Emid])
                            yans.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[mid,Amid,Dmid,Cmid,Emid])
                                yans.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                ke.acceptGroupInvitation(op.param1)
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    G = yans.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    yans.kickoutFromGroup(op.param1,[op.param2])
                                    yans.updateGroup(G)
                                    Ticket = yans.reissueGroupTicket(op.param1)
                                    yans.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = yans.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    yans.updateGroup(G)
                                    Ticket = yans.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Dmid,Emid])
                                        yans.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kb.acceptGroupInvitation(op.param1)
                                        ke.acceptGroupInvitation(op.param1)
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Emid])
                                            yans.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                            ke.acceptGroupInvitation(op.param1)
                                            kb.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            pass
                                            
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        yans.kickoutFromGroup(op.param1,[op.param2])
                        yans.findAndAddContactsByMid(op.param1,admin)
                        yans.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.findAndAddContactsByMid(op.param1,admin)
                                            ke.inviteIntoGroup(op.param1,admin)
                                        except:
                                            pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,staff)
                                    kb.inviteIntoGroup(op.param1,staff)    
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param1,staff)
                                        ke.inviteIntoGroup(op.param1,staff)    
                                    except:
                                        pass
                                    
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,staff)
                                    kb.inviteIntoGroup(op.param1,staff)    
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param1,staff)
                                        ke.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            yans.kickoutFromGroup(op.param1,[op.param2])
                                            yans.findAndAddContactsByMid(op.param1,staff)
                                            yans.inviteIntoGroup(op.param1,staff)    
                                        except:
                                            pass
                                    
                                    
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,staff)
                                    kb.inviteIntoGroup(op.param1,staff)    
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param1,staff)
                                        ke.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            yans.kickoutFromGroup(op.param1,[op.param2])
                                            yans.findAndAddContactsByMid(op.param1,staff)
                                            yans.inviteIntoGroup(op.param1,staff)    
                                        except:
                                            pass
                                            
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,staff)
                                    kb.inviteIntoGroup(op.param1,staff)    
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param1,staff)
                                        ke.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            yans.kickoutFromGroup(op.param1,[op.param2])
                                            yans.findAndAddContactsByMid(op.param1,staff)
                                            yans.inviteIntoGroup(op.param1,staff)    
                                        except:
                                            pass          
                                            
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,staff)
                                    kb.inviteIntoGroup(op.param1,staff)    
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param1,staff)
                                        ke.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            yans.kickoutFromGroup(op.param1,[op.param2])
                                            yans.findAndAddContactsByMid(op.param1,staff)
                                            yans.inviteIntoGroup(op.param1,staff)    
                                        except:
                                            pass
                                            
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,staff)
                                    kb.inviteIntoGroup(op.param1,staff)    
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param1,staff)
                                        ke.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            yans.kickoutFromGroup(op.param1,[op.param2])
                                            yans.findAndAddContactsByMid(op.param1,staff)
                                            yans.inviteIntoGroup(op.param1,staff)    
                                        except:
                                            pass            
                                            
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,staff)
                                    kb.inviteIntoGroup(op.param1,staff)    
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param1,staff)
                                        ke.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            yans.kickoutFromGroup(op.param1,[op.param2])
                                            yans.findAndAddContactsByMid(op.param1,staff)
                                            yans.inviteIntoGroup(op.param1,staff)    
                                        except:
                                            pass
                return

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = yans.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = yans.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        yans.sendImageWithURL(op.param1, image)
                        
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = yans.getGroup(at)
                                ryan = yans.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "βGambar Dihapus β\n Pengirim : "
                                ret_ = " Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                yans.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                yans.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = yans.getGroup(at)
                                ryan = yans.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "β Pesan Dihapus β\n"
                                ret_ += " Pengirim π {}".format(str(ryan.displayName))
                                ret_ += "\n Pesannya π {}".format(str(msg_dict[msg_id]["text"]))
                                yans.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = yans.getGroup(at)
                                ryan = yans.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "β Sticker Dihapus β\n"
                                ret_ += " Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                yans.sendMessage(at, str(ret_))
                                yans.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e) 
                        
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if sender != yans.profile.mid:
                    to = sender
                else:
                    to = receiver
                if msg.contentType == 6:
                  if settings["nCall"] == True:
                    if msg._from not in Bots:
                        try:
                            contact = yans.getContact(sender)
                            group = yans.getGroup(msg.to)
                            cover = yans.getProfileCoverURL(sender)
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            if msg.toType == 2:
                                b = msg.contentMetadata['GC_EVT_TYPE']
                                c = msg.contentMetadata["GC_MEDIA_TYPE"]
                                if c == 'AUDIO' and b == "S":
                                    arg = "β’ α΄α΄ΚΚ α΄α΄α΄Ιͺα΄"
                                    arg += "\nβ’ α΄Κα΄α΄ {} α΄α΄ΚΚ".format(c) 
                                    arg += "\nβ’ Ι΄α΄: {}".format(str(contact.displayName)) 
                                    arg += "\nβ’ Ι’α΄: {}".format(str(group.name))
                                    arg += "\nβ’ ΚΚ: {}".format(timeNow.strftime('%A'))
                                    arg += "\nβ’ α΄α΄: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\nβ’ α΄Ι’: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    yans.sendMessage(msg.to,arg)
                                if c == 'VIDEO' and b == "S":
                                    arg = "β’ α΄α΄ΚΚ α΄ Ιͺα΄α΄α΄"
                                    arg += "\nβ’ α΄Κα΄α΄ {} α΄α΄ΚΚ".format(c) 
                                    arg += "\nβ’ Ι΄α΄: {}".format(str(contact.displayName)) 
                                    arg += "\nβ’ Ι’α΄: {}".format(str(group.name))
                                    arg += "\nβ’ ΚΚ: {}".format(timeNow.strftime('%A'))
                                    arg += "\nβ’ α΄α΄: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\nβ’ α΄Ι’: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    yans.sendMessage(msg.to,arg)
                                if c == 'LIVE' and b == "S":
                                    arg = "β’ α΄α΄ΚΚ ΚΙͺα΄ α΄"
                                    arg += "\nβ’ α΄Κα΄α΄ {} α΄α΄ΚΚ".format(c) 
                                    arg += "\nβ’ Ι΄α΄: {}".format(str(contact.displayName)) 
                                    arg += "\nβ’ Ι’α΄: {}".format(str(group.name))
                                    arg += "\nβ’ ΚΚ: {}".format(timeNow.strftime('%A'))
                                    arg += "\nβ’ α΄α΄: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\nβ’ α΄Ι’: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    yans.sendMessage(msg.to,arg)
                                else:
                                    mills = int(msg.contentMetadata["DURATION"])
                                    seconds = (mills/1000)%60
                                    if c == "AUDIO" and b == "E":
                                        arg = "β’ α΄α΄ΚΚ α΄α΄α΄Ιͺα΄"
                                        arg += "\nβ’ α΄Ιͺα΄α΄ΚΙͺΚΙͺ {} α΄α΄ΚΚ".format(c)
                                        arg += "\nβ’ Ι΄α΄: {}".format(str(contact.displayName)) 
                                        arg += "\nβ’ Ι’α΄: {}".format(str(group.name))
                                        arg += "\nβ’ ΚΚ: {}".format(timeNow.strftime('%A'))
                                        arg += "\nβ’ α΄α΄: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\nβ’ α΄Ι’: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\nβ’ α΄Κ: {}".format(seconds)
                                        yans.sendMessage(msg.to,arg)
                                    if c == "VIDEO" and b == "E":
                                        arg = "β’ α΄α΄ΚΚ α΄ Ιͺα΄α΄α΄"
                                        arg += "\nβ’ α΄Ιͺα΄α΄ΚΙͺΚΙͺ {} α΄α΄ΚΚ".format(c)
                                        arg += "\nβ’ Ι΄α΄: {}".format(str(contact.displayName)) 
                                        arg += "\nβ’ Ι’α΄: {}".format(str(group.name))
                                        arg += "\nβ’ ΚΚ: {}".format(timeNow.strftime('%A'))
                                        arg += "\nβ’ α΄α΄: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\nβ’ α΄Ι’: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\nβ’ α΄Κ: {}".format(seconds)
                                        yans.sendMessage(msg.to,arg)
                                    if c == "LIVE" and b == "E":
                                        arg = "β’ α΄α΄ΚΚ ΚΙͺα΄ α΄"
                                        arg += "\nβ’ α΄Ιͺα΄α΄ΚΙͺΚΙͺ {} α΄α΄ΚΚ".format(c)
                                        arg += "\nβ’ Ι΄α΄: {}".format(str(contact.displayName)) 
                                        arg += "\nβ’ Ι’α΄: {}".format(str(group.name))
                                        arg += "\nβ’ ΚΚ: {}".format(timeNow.strftime('%A'))
                                        arg += "\nβ’ α΄α΄: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\nβ’ α΄Ι’: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\nβ’ α΄Κ: {}".format(seconds)
                                        yans.sendMessage(msg.to,arg)
                        except Exception as error:
                            print (error)
                              
        if op.type == 26:           
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nγLink Stickerγ" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 16:
                  if msg.toType in (2,1,0):
                     try:
                         mat = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                         yans.likePost(mat[0], mat[1], 1003)
                         yans.createComment(mat[0], mat[1], "α΄α΄α΄α΄ΚΙͺα΄α΄ ΚΚ: \n\n\n\nβ’ππ¬ππ£π¨π½ππ\n\n\n\nα΄Κα΄α΄α΄α΄Κ:\nhttp://line.me/ti/p/~gepengcharlez\n\n\n\nα΄α΄Ι΄α΄ΚΙͺα΄α΄ α΄α΄κ±α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)")
                     except Exception as e:
                         yans.sendMessage(msg.to, str(e))  
                            
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "γ α΄α΄α΄α΄ΙͺΚ α΄α΄sα΄ΙͺΙ΄Ι’α΄Ι΄ γ"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = yans.getContact(sender)
                                auth = "\nβ’ Λ’α΅βΉΰΌα΄α΄Ι΄α΄ΚΙͺs : {}".format(str(contact.displayName))
                            else:
                                auth = "\nβ’ Λ’α΅βΉ ΰΌα΄α΄Ι΄α΄ΚΙͺs : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\nβ’ Λ’α΅βΉΰΌsα΄Ιͺα΄α΄α΄Κ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\nβ’ Λ’α΅βΉΰΌ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\nβ’ Λ’α΅βΉΰΌMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\nβ’ Λ’α΅βΉΰΌObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\nβ’ Λ’α΅βΉΰΌMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\nβ’ Λ’α΅βΉΰΌObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\nβ’ Λ’α΅βΉΰΌObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\nβ’ Λ’α΅βΉΰΌTulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\nβ’ Λ’α΅βΉΰΌPost URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                                url = msg.contentMetadata['postEndUrl']
                            yans.sendMessage(to, str(ret_))
                            yans.likePost(purl[25:58], purl[66:], likeType=1005)
                            yans.createComment(purl[25:58], purl[66:], wait["comment"])
        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nΓ£ΒΒLink StickerΓ£ΒΒ" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = yans.getContact(msg.contentMetadata["mid"])
                        path = yans.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        yans.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        yans.sendImageWithURL(msg.to, image)
                        
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = yans.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n Sticker Info "
                   ret_ += "\n Sticker ID : {}".format(stk_id)
                   ret_ += "\n Sticker Version : {}".format(stk_ver)
                   ret_ += "\n Sticker Package : {}".format(pkg_id)
                   ret_ += "\n Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = yans.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if settings["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[yansass~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = " Sticker Info "
                            ret_ += "\nπ΄ STICKER ID : {}".format(stk_id)
                            ret_ += "\nπ΄ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\nπ΄ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\nπ΄STICKER URL : line://shop/detail/{}".format(pkg_id)
                            yans.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = yans.downloadFileURL(data)
                               yans.sendImage(msg.to,path)
                        else:
                            ret_ = " Sticker Info "
                            ret_ += "\nπ΄ PRICE : "+soup.findAll('p', attrs={'yansass':'mdCMN08Price'})[0].text
                            ret_ += "\nπ΄ AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\nπ΄ STICKER ID : {}".format(str(stk_id))
                            ret_ += "\nπ΄ STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\nπ΄ STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\nπ΄ STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\nπ΄ DESCRIPTION :\n"+soup.findAll('p', attrs={'yansass':'mdCMN08Desc'})[0].text
                            yans.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = yans.downloadFileURL(data)
                               yans.sendImage(msg.to,path)
                      
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = yans.getContact(msg.contentMetadata["mid"])
                        path = yans.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        yans.sendMessage(msg.to,"  Contact Info \nπ Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        yans.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = yans.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = yans.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            yans.sendMessage(msg.to, "πDia ke bl kak... hpus bl dulu lalu invite lagiπ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  yans.findAndAddContactsByMid(target)
                                  yans.inviteIntoGroup(msg.to,[target])
                                  ryan = yans.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  " Sukses Invite \nNama "
                                  ret_ = "Ketik Invite off jika sudah done"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  yans.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  yans.sendMessage(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
                            
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])                           
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           TEAMBOTPROTECT = yans.getContact(msg._from)
                           sendMention1(msg.to, TEAMBOTPROTECT.mid, "", wait["Respontag"])
                           yans.sendMessage(msg.to, None, contentMetadata={"STKID":"52002769","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                           break
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           yans.mentiontag(msg.to,[msg._from])
                           yans.sendMessage(msg.to, "No tag me....")
                           yans.kickoutFromGroup(msg.to, [msg._from])
                           break
#SPAMINVITE
               if op.type == 25:
                 if settings['SpamInvite'] == True:
                   msg = op.message
                   man = msg._from
                   send = msg.to
                   if msg.contentType == 13:
                       if msg._from in admin:
                           korban = msg.contentMetadata["displayName"]
                           invite = msg.contentMetadata["mid"]
                           groups = yans.getGroup(send)
                           pending = groups.invitee
                           targets = []
                           for x in groups.members:
                               if korban in x.displayName:
                                   yans.sendText(send, korban + " Sudah Berada DiGrup Ini")
                               else:
                                   targets.append(invite)
                           if targets == []:
                               pass
                           else:
                               for target in targets:
                                   try:
                                       yans.findAndAddContactsByMid(target)
                                       ki.findAndAddContactsByMid(target)
                                       kk.findAndAddContactsByMid(target)
                                       kb.findAndAddContactsByMid(target)
                                       kc.findAndAddContactsByMid(target)
                                       ke.findAndAddContactsByMid(target)
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       yans.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ki.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kk.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kc.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       kb.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target]) 
                                       ke.createGroup("Ι΄Ιͺα΄α΄α΄α΄ΙͺΙ΄ sα΄α΄α΄",[target])
                                       yans.sendText(send,"Spam Invite ke " + korban + "\nSUCCESS..")
                                       settings['SpamInvite'] = False
                                   except:             
                                        yans.sendText(send, 'Contact error')
                                        settings['SpamInvite'] = False
                                        break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nγLink Stickerγ" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = yans.getContact(msg.contentMetadata["mid"])
                        path = yans.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        yans.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        yans.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nγLink Stickerγ" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    yans.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = yans.getContact(msg.contentMetadata["mid"])
                        path = yans.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        yans.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        yans.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        yans.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = False
                    else:
                        target = msg.contentMetadata["mid"]
                        yans.findAndAddContactsByMid(target)
                        midd = (target)
                        Bots.append(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been promoted Bot by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["addbots"] = False
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        target = msg.contentMetadata["mid"]
                        midd = (target)
                        Bots.remove(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been Expel Bot by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["dellbots"] = False
                    else:
                        wait["dellbots"] = False
                        yans.sendMessage(msg.to,"Nothing in bot")
#ADD SQUAD
               if msg.contentType == 13:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addsquads"] == True:
                    if msg.contentMetadata["mid"] in Squad:
                        yans.sendMessage(msg.to,"Already in squad")
                        wait["addsquads"] = False
                    else:
                        target = msg.contentMetadata["mid"]
                        yans.findAndAddContactsByMid(target)
                        midd = (target)
                        Squad.append(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been promoted Squad by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["addsquads"] = False
                 if wait["dellsquads"] == True:
                    if msg.contentMetadata["mid"] in Squad:
                        target = msg.contentMetadata["mid"]
                        midd = (target)
                        Squad.remove(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been Expel Squad by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["dellsquads"] = False
                    else:
                        wait["dellsquads"] = False
                        yans.sendMessage(msg.to,"Nothing in Squad")
#ADD STAFF
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        yans.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = False
                    else:
                        target = msg.contentMetadata["mid"]
                        yans.findAndAddContactsByMid(target)
                        midd = (target)
                        staff.append(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been promoted Staff by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["addstaff"] = False
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        target = msg.contentMetadata["mid"]
                        midd = (target)
                        staff.remove(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been Expel Staff by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["dellstaff"] = False
                    else:
                        wait["dellstaff"] = False
                        yans.sendMessage(msg.to,"Nothing in staff")
#ADD ADMIN
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        yans.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = False
                    else:
                        target = msg.contentMetadata["mid"]
                        yans.findAndAddContactsByMid(target)
                        midd = (target)
                        admin.append(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been promoted Admin by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["addadmin"] = False
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        target = msg.contentMetadata["mid"]
                        midd = (target)
                        admin.remove(midd)
                        yans.sendMessage(msg.to, yans.getContact(target).displayName + " has been Expel Admin by " + yans.getContact(msg._from).displayName)
                        target = {}
                        wait["delladmin"] = False
                    else:
                        wait["delladmin"] = False
                        yans.sendMessage(msg.to,"Nothing in admin")
#ADD BLACKLIST
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        yans.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        yans.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        yans.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        yans.sendMessage(msg.to,"Nothing in blacklist")
#TALKBAN
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        yans.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        yans.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        yans.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        yans.sendMessage(msg.to,"Nothing in Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = yans.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         yans.sendMessage(msg.to, "α΄α΄Ι΄α΄ Ι’α΄α΄Κα΄Κ {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = yans.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         yans.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         yans.sendMessage(msg.to, "α΄α΄Ι΄α΄ sα΄Ιͺα΄α΄α΄Κ {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = yans.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         yans.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      yans.sendChatChecked(msg.to, msg_id)
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               yans.sendSticker(to, spkg, sid)
                         for image in images:
                            if text.lower() == image:
                               yans.sendImage(msg.to, images[image])
                         for audio in audios:
                            if text.lower() == audio:
                               yans.sendAudio(msg.to, audios[audio])
                         for video in videos:
                            if text.lower() == video:
                               yans.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate1(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate1(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate1(msg.to,"Nothing in bot")
                        
               if msg.contentType == 1:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = yans.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            yans.sendMessage(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
                      
               if msg.contentType == 2:
                   if msg._from in owner or msg._from in admin or msg._from in mid:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            yans.downloadObjectMsg(msg_id,'path','video.mp4')
                            yans.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in owner or msg._from in admin or msg._from in mid:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            yans.downloadObjectMsg(msg_id,'path','image.jpg')
                            yans.nadyacantikimut('video.mp4','image.jpg')
                            yans.sendMessage(msg.to,"Change Video Profile Success!!!")
                            
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = yans.getProfile()
               		path = yans.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = yans.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		yans.sendMessage(to, "α΄α΄Ι΄α΄ vΙͺα΄α΄α΄ α΄Κα΄?ΙͺΚα΄")

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                   if settings["groupPicture"] == True:
                     path = yans.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     yans.updateGroupPicture(msg.to, path)
                     yans.sendMessage(msg.to, "Succes change pict group")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if mid in Setmain["SKfoto"]:
                            path = yans.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][mid]
                            yans.updateProfilePicture(path)
                            yans.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if Amid in Setmain["SKfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if Bmid in Setmain["SKfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if Cmid in Setmain["SKfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if Dmid in Setmain["SKfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Dmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if Emid in Setmain["SKfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Emid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 1:
                   if msg._from in owner:
                       if Zmid in Setmain["SKfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 1:
                 if msg._from in owner:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kb.downloadObjectMsg(msg_id)
                     path5 = ke.downloadObjectMsg(msg_id)
                   if settings["changePicture"] == True:
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’α΄Κα΄Κ ?α΄α΄α΄ α΄©Κα΄?ΙͺΚα΄ Κα΄α΄")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’α΄Κα΄Κ ?α΄α΄α΄ α΄©Κα΄?ΙͺΚα΄ Κα΄α΄")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’α΄Κα΄Κ ?α΄α΄α΄ α΄©Κα΄?ΙͺΚα΄ Κα΄α΄")
                     kb.updateProfilePicture(path4)
                     kb.sendMessage(msg.to, "Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’α΄Κα΄Κ ?α΄α΄α΄ α΄©Κα΄?ΙͺΚα΄ Κα΄α΄")
                     ke.updateProfilePicture(path5)
                     ke.sendMessage(msg.to, "Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’α΄Κα΄Κ ?α΄α΄α΄ α΄©Κα΄?ΙͺΚα΄ Κα΄α΄")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        yans.sendChatChecked(msg.to, msg_id)
                        print ("Read")
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               helpMessage = help()
                               yans.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "chatbot on":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["selfbot"] = True
                                yans.sendMessage(msg.to, "Chatbot has been enable")
                                
                        elif cmd == "chatbot off":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["selfbot"] = False
                                yans.sendMessage(msg.to, "Chatbot has been disable")
                                            
                   
                        if cmd == "cek":
                            if msg._from in admin or msg._from in owner:
                               try:yans.inviteIntoGroup(to, ["uef19f4b2c942da00679172d0c941fc39"]);has = "OK"
                               except:has = "NOT"
                               try:yans.kickoutFromGroup(to, ["uef19f4b2c942da00679172d0c941fc39"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Normal"
                               else:sil = "Limit"
                               if has1 == "OK":sil1 = "Normal"
                               else:sil1 = "Limit"
                               yans.sendMessage(to, "Result:\n\nKick : {} \nInvite : {}".format(sil1,sil))

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               helpMessage02 = helpbot()
                               yans.sendMessage(msg.to, str(helpMessage02))
                               
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               helpMessage03 = helpmedia()
                               yans.sendMessage(msg.to, str(helpMessage03))
                               
                        elif cmd.startswith(".gettoken"):
                             if msg._from in owner or msg._from in admin or msg._from in mid:
                                try:
                                    sep = text.split(" ")
                                    auth = text.replace(sep[0] + " ","")
                                    r = requests.get("http://beta.moe.team/api/generateAuthToken?auth={}&apikey=f3XdIQlolsA7iJnxF3DADnkYye5IuxtFLqVsFxvcxQBSe2qDraEy7un8ZD6xxiTu".format(str(auth)))
                                    data=r.text
                                    data=json.loads(r.text)
                                    ret_ = "γ Token Primery γ"
                                    ret_ += "\n\nStatus : "+str(data["message"])
                                    ret_ += "\nToken : "+str(data["result"])
                                    yans.sendMessage(to, ret_)
                                except Exception as error:
                                    yans.sendMessage(to, str(error))
                               
                     
                        elif cmd == "set" or cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)                                
                                md = "ββββ[ ππ¬ππ£π¨π½ππ ] \n"                                
                                if wait["sticker"] == True: md+="ββ ββ[  ON  ] sα΄Ιͺα΄α΄α΄ΚβοΈ\n"
                                else: md+="ββ ββ[ OFF ] sα΄Ιͺα΄α΄α΄Κβ\n"
                                if wait["contact"] == True: md+="ββ ββ[  ON  ] α΄α΄Ι΄α΄α΄α΄α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄α΄Ι΄α΄α΄α΄α΄β\n"
                                if wait["detectMention"] == True: md+="ββ ββ[  ON  ] Κα΄sα΄α΄Ι΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] Κα΄sα΄α΄Ι΄β\n"
                                if wait["autoJoin"] == True: md+="ββ ββ[  ON  ] α΄α΄α΄α΄α΄α΄ΙͺΙ΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄α΄α΄α΄α΄α΄ΙͺΙ΄β\n"
                                if settings["autoJoinTicket"] == True: md+="ββ ββ[  ON  ] α΄α΄ΙͺΙ΄α΄Ιͺα΄α΄α΄α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄α΄ΙͺΙ΄α΄Ιͺα΄α΄α΄α΄β\n"
                                if wait["autoBlock"] == True: md+="ββ ββ[  ON  ] autoblock βοΈ\n"
                                else: md+="ββ ββ[ OFF ] autoblock β\n"
                                if settings["unsendMessage"] == True: md+="ββ ββ[  ON  ] α΄Ι΄sα΄Ι΄α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄Ι΄sα΄Ι΄α΄β\n"
                                if wait["autoAdd"] == True: md+="ββ ββ[  ON  ] α΄α΄α΄α΄α΄α΄α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄α΄α΄α΄α΄α΄α΄β\n"
                                if msg.to in welcome: md+="ββ ββ[  ON  ] α΄‘α΄Κα΄α΄α΄α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄‘α΄Κα΄α΄α΄α΄β\n"
                                if wait["autoLeave"] == True: md+="ββ ββ[  ON  ] α΄α΄α΄α΄Κα΄α΄α΄ α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄α΄α΄α΄Κα΄α΄α΄ α΄β\n"                               
                                if msg.to in protectqr: md+="ββ ββ[  ON  ] α΄Κα΄α΄α΄α΄α΄Η«ΚβοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄Κα΄α΄α΄α΄α΄Η«Κβ\n"
                                if msg.to in protectjoin: md+="ββ ββ[  ON  ] α΄Κα΄α΄α΄α΄α΄α΄α΄ΙͺΙ΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄Κα΄α΄α΄α΄α΄α΄α΄ΙͺΙ΄β\n"
                                if msg.to in protectkick: md+="ββ ββ[  ON  ] α΄Κα΄α΄α΄α΄α΄α΄Ιͺα΄α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄Κα΄α΄α΄α΄α΄α΄Ιͺα΄α΄β\n"
                                if msg.to in protectinvite: md+="ββ ββ[  ON  ] α΄Κα΄α΄α΄α΄α΄ΙͺΙ΄α΄ Ιͺα΄α΄βοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄Κα΄α΄α΄α΄α΄ΙͺΙ΄α΄ Ιͺα΄α΄β\n"
                                if msg.to in protectantijs: md+="ββ ββ[  ON  ] α΄sβοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄sβ\n"                                
                                if msg.to in protectcancel: md+="ββ ββ[  ON  ] α΄Κα΄α΄α΄α΄α΄α΄α΄Ι΄α΄α΄ΚβοΈ\n"
                                else: md+="ββ ββ[ OFF ] α΄Κα΄α΄α΄α΄α΄α΄α΄Ι΄α΄α΄Κβ\n"
                                md+= "ββββ[ ππ³ππ»π  πππ ]\n"
                                md+= "α΄α΄Ι΄α΄ΚΙͺα΄α΄ α΄α΄κ±α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)\n"
                                md+= "line://ti/p/~gepengcharlez\n"
                                yans.sendMessage(msg.to, md+"\nβα΄α΄Ι΄Ι’Ι’α΄Κ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nβα΄α΄α΄  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")   
                                
                          
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                yans.sendMessage(msg.to,"ππ«πππ­π¨π« π€ππ¦π’")
                                ma = ""
                                for i in creator:
                                    ma = yans.getContact(i)
                                    yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               sendMention(msg.to, sender, "ΙͺΙ΄?α΄ sα΄Κ?Κα΄α΄\n\n")
                               yans.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               yans.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                               

                        elif text.lower() == "mid":
                               yans.sendMessage(msg.to, msg._from)
                               
                        elif text.lower() == "ls":
                               yans.sendMessage(msg.to, "α΄α΄Ι΄α΄ΚΙͺα΄α΄ α΄α΄κ±α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)")

                        elif ("mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = yans.getContact(key1)
                               yans.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               yans.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Profile " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = yans.getContact(key1)
                               yans.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               yans.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(yans.getContact(key1)):
                                   yans.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   yans.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               yans.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "Komando":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               yans.sendContact(to, mid)
                               yans.sendContact(to, Amid)
                               yans.sendContact(to, Bmid)
                               yans.sendContact(to, Cmid)
                               yans.sendContact(to, Dmid)
                               yans.sendContact(to, Emid)
                               yans.sendContact(to, Zmid)
                               yans.sendMessage(msg.to, "sΙͺα΄α΄© α΄α΄α΄α΄Ι΄α΄α΄Ι΄, \nα΄α΄Ι΄α΄Ι΄Ι’Ι’α΄ α΄α΄α΄α΄Ι΄α΄α΄")

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              ginvited = yans.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      yans.rejectGroupInvitation(gid)
                                  yans.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  yans.sendMessage(to, "Nothing")

                        elif text.lower() == "rchat":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               try:
                                   yans.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   yans.sendMessage(msg.to,"α΄Κα΄α΄ Κα΄ΚΚα΄sΙͺΚ α΄Ιͺ Κα΄ΚsΙͺΚα΄α΄Ι΄")
                               except:
                                   pass

                        elif cmd.startswith("out "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = yans.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = yans.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    sw.leaveGroup(i)
                                    yans.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))
                                    
                        elif cmd == "berteman":
                          if msg._from in admin:
                            try:
                                yans.findAndAddContactsByMid(Amid)
                                yans.findAndAddContactsByMid(Bmid)
                                yans.findAndAddContactsByMid(Cmid)
                                yans.findAndAddContactsByMid(Dmid)
                                yans.findAndAddContactsByMid(Emid)
                                yans.findAndAddContactsByMid(Zmid)
                                ki.findAndAddContactsByMid(mid)
                                ki.findAndAddContactsByMid(Bmid)
                                ki.findAndAddContactsByMid(Cmid)
                                ki.findAndAddContactsByMid(Dmid)
                                ki.findAndAddContactsByMid(Emid)
                                ki.findAndAddContactsByMid(Zmid)
                                kk.findAndAddContactsByMid(mid)
                                kk.findAndAddContactsByMid(Amid)
                                kk.findAndAddContactsByMid(Cmid)
                                kk.findAndAddContactsByMid(Dmid)
                                kk.findAndAddContactsByMid(Emid)
                                kk.findAndAddContactsByMid(Zmid)
                                kc.findAndAddContactsByMid(mid)
                                kc.findAndAddContactsByMid(Amid)
                                kc.findAndAddContactsByMid(Bmid)
                                kc.findAndAddContactsByMid(Dmid)
                                kc.findAndAddContactsByMid(Emid)
                                kc.findAndAddContactsByMid(Zmid)
                                kb.findAndAddContactsByMid(mid)
                                kb.findAndAddContactsByMid(Amid)
                                kb.findAndAddContactsByMid(Bmid)
                                kb.findAndAddContactsByMid(Cmid)
                                kb.findAndAddContactsByMid(Emid)
                                kb.findAndAddContactsByMid(Zmid)
                                ke.findAndAddContactsByMid(mid)
                                ke.findAndAddContactsByMid(Amid)
                                ke.findAndAddContactsByMid(Bmid)
                                ke.findAndAddContactsByMid(Cmid)
                                ke.findAndAddContactsByMid(Dmid)
                                ke.findAndAddContactsByMid(Zmid)
                                sw.findAndAddContactsByMid(mid)
                                sw.findAndAddContactsByMid(Amid)
                                sw.findAndAddContactsByMid(Bmid)
                                sw.findAndAddContactsByMid(Cmid)
                                sw.findAndAddContactsByMid(Dmid)
                                sw.findAndAddContactsByMid(Emid)
                                yans.sendMessage(to,"Sucsess!!!")
                            except:
                                yans.sendMessage(to,"sα΄α΄α΄ss..!!! \n α΄α΄α΄Ιͺ sα΄α΄α΄Κ sα΄ΚΙͺΙ΄Ι’ α΄α΄α΄ Κα΄s.")            

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "β  " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"βββ[ GROUP LIST ]\nβ\n"+ma+"β\nβββ[ Totalγ"+str(len(gid))+"γGroups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "β  " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"βββ[ GROUP LIST ]\nβ\n"+ma+"β\nβββ[ Totalγ"+str(len(gid))+"γGroups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "β  " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"βββ[ GROUP LIST ]\nβ\n"+ma+"β\nβββ[ Totalγ"+str(len(gid))+"γGroups ]")
                               
                        elif cmd == "gruplist4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "β  " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"βββ[ GROUP LIST ]\nβ\n"+ma+"β\nβββ[ Totalγ"+str(len(gid))+"γGroups ]")       
                               
                        elif cmd == "gruplist5":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ke.getGroupIdsJoined()
                               for i in gid:
                                   G = ke.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "β  " + str(a) + ". " +G.name+ "\n"
                               ke.sendMessage(msg.to,"βββ[ GROUP LIST ]\nβ\n"+ma+"β\nβββ[ Totalγ"+str(len(gid))+"γGroups ]")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                yans.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["SKfoto"][mid] = True
                                yans.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "4up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Dmid] = True
                                kb.sendMessage(msg.to,"Send your images.....")
        
                        elif cmd == "5up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Emid] = True
                                ke.sendMessage(msg.to,"Send your images.....")
     
                        elif cmd == "jsup":
                            if msg._from in admin:
                                Setmain["SKfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send your images.....")

                        elif cmd.startswith("1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "") 

                        elif cmd.startswith("jsname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd == "js stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    G = yans.getGroup(msg.to)
                                    ginfo = yans.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    yans.inviteIntoGroup(msg.to, [Zmid])
                                except:
                                    pass
#===========BOT UPDATE============#
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getContact(m_id).displayName + "\n"
                                yans.sendMessage(msg.to,"β ΚΚα΄Ι΄κ± Κα΄α΄\n\n"+ma+"\nTotalγ%sγBots" %(str(len(Bots))))

                        elif cmd == "ryans" or cmd == "absen":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                yans.sendMessage(msg.to, "Pasukan mana?")
                                ki.sendMessage(msg.to, "1 hadir")
                                kk.sendMessage(msg.to, "2 hadir")
                                kc.sendMessage(msg.to, "3 hadir")
                                kb.sendMessage(msg.to, "4 hadir")
                                ke.sendMessage(msg.to, "5 hadir")
                                yans.sendMessage(msg.to,  "Ok,, mantabb")                              

                        elif cmd == "masuk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass                              

                        elif cmd == "1masuk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass                              

                        elif cmd == "2masuk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Bmid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    kk.acceptGroupInvitation(msg.to)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass                              

                        elif cmd == "3masuk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Cmid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    kc.acceptGroupInvitation(msg.to)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass                              

                        elif cmd == "4masuk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Dmid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    kb.acceptGroupInvitation(msg.to)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass                              

                        elif cmd == "5masuk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Emid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    ke.acceptGroupInvitation(msg.to)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass                              

                        elif cmd == "jsmasuk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Zmid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    sw.acceptGroupInvitation(msg.to)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass                              

                        elif cmd == "setajs":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Zmid]
                                    yans.inviteIntoGroup(msg.to, anggota)
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©"+str(ginfo.name)+"α΄α΄α΄Ι΄ α΄α΄ΚΙͺ Κα΄α΄α΄")
                                except:
                                    pass
                                    
                        elif cmd == "/stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    G = yans.getGroup(msg.to)
                                    ginfo = yans.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    yans.inviteIntoGroup(msg.to, [Zmid])
                                    yans.sendMessage(msg.to,"Ι’Κα΄α΄α΄©γ" +str(ginfo.name)+ "γsα΄α΄Κ α΄Ιͺ Κα΄α΄Κ α΄α΄Ι΄α΄Κα΄Κ")
                                except:
                                    pass           

                        elif cmd == "/in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.updateGroup(G)
                                invsend = 0
                                Ticket = yans.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)                                
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)                                
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)                                
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)                            
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)                                
                                G = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                yans.updateGroup(G)
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.inviteIntoGroup(msg.to, [Zmid])                                

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                yans.cancelGroupInvitation(msg.to, [Zmid])
                                ki.leaveGroup(msg.to)                               
                                kk.leaveGroup(msg.to)                                
                                kc.leaveGroup(msg.to)                                
                                kb.leaveGroup(msg.to)                                
                                ke.leaveGroup(msg.to)

                        elif cmd == "/r1":
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.updateGroup(G)
                                invsend = 0
                                Ticket = yans.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "/r2":
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.updateGroup(G)
                                invsend = 0
                                Ticket = yans.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "/r3":
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.updateGroup(G)
                                invsend = 0
                                Ticket = yans.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                
                        elif cmd == "/r4":
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.updateGroup(G)
                                invsend = 0
                                Ticket = yans.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)
                                
                        elif cmd == "/r5":
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.updateGroup(G)
                                invsend = 0
                                Ticket = yans.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "/jin":
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)
                                ginfo = yans.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                yans.updateGroup(G)
                                invsend = 0
                                Ticket = yans.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)                               
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "jsout":
                            if msg._from in admin:
                                G = yans.getGroup(msg.to)                                
                                sw.leaveGroup(msg.to)

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               time.sleep(0.0001)
                               elapsed_time = time.time() - start
                               yans.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))                             
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))                               
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))                               
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))                               
                               kb.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))                              
                               ke.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                                    
                        elif 'ajs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ajs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "α΄Ι΄α΄Ιͺ α΄s α΄α΄α΄Ιͺ?β"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "α΄Ι΄α΄Ιͺ α΄s α΄Ιͺ α΄α΄α΄Ιͺ?α΄α΄Ι΄\nα΄Ιͺ Ι’Κα΄α΄α΄© : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "α΄Ιͺα΄α΄α΄Ιͺ?α΄α΄Ι΄\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "α΄Ι΄α΄Ιͺ α΄s α΄Ιͺ Ι΄α΄Ι΄α΄α΄α΄Ιͺ?α΄α΄Ι΄\nα΄Ιͺ Ι’Κα΄α΄α΄© : " +str(ginfo.name)
                                    else:
                                         msgs = "α΄Ι΄α΄Ιͺ α΄s Ι΄α΄Ι΄α΄α΄α΄Ιͺ?β"
                                    yans.sendMessage(msg.to, "α΄ΙͺΙ΄α΄Ι΄α΄α΄α΄Ιͺ?α΄α΄Ι΄\n" + msgs)
                                    
                        elif 'gs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ι’Κα΄sα΄ α΄α΄α΄Ιͺ?β"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "Ι’Κα΄sα΄ α΄Ιͺ α΄α΄α΄Ιͺ?α΄α΄Ι΄\nα΄Ιͺ Ι’Κα΄α΄α΄© : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "α΄Ιͺα΄α΄α΄Ιͺ?α΄α΄Ι΄\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Ι’Κα΄sα΄ α΄Ιͺ Ι΄α΄Ι΄α΄α΄α΄Ιͺ?α΄α΄Ι΄\nα΄Ιͺ Ι’Κα΄α΄α΄© : " +str(ginfo.name)
                                    else:
                                         msgs = "Ι’Κα΄sα΄ Ι΄α΄Ι΄α΄α΄α΄Ιͺ?β"
                                    yans.sendMessage(msg.to, "α΄ΙͺΙ΄α΄Ι΄α΄α΄α΄Ιͺ?α΄α΄Ι΄\n" + msgs)

                        elif cmd == "curut" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    yans.sendMessage(msg.to,"α΄Ιͺα΄α΄α΄ α΄α΄α΄ ΚΚα΄α΄α΄ΚΙͺsα΄")
                                    ki.sendMessage(msg.to,"α΄Ιͺα΄α΄α΄ α΄α΄α΄ ΚΚα΄α΄α΄ΚΙͺsα΄")
                                    kk.sendMessage(msg.to,"α΄Ιͺα΄α΄α΄ α΄α΄α΄ ΚΚα΄α΄α΄ΚΙͺsα΄")
                                    kc.sendMessage(msg.to,"α΄Ιͺα΄α΄α΄ α΄α΄α΄ ΚΚα΄α΄α΄ΚΙͺsα΄")
                                    kb.sendMessage(msg.to,"α΄Ιͺα΄α΄α΄ α΄α΄α΄ ΚΚα΄α΄α΄ΚΙͺsα΄")
                                    ke.sendMessage(msg.to,"α΄Ιͺα΄α΄α΄ α΄α΄α΄α΄ ΚΚα΄α΄α΄ΚΙͺsα΄")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = yans.getContact(i)
                                        yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'ceban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = yans.getContacts(wait["blacklist"])
                              mc = "γ%iγUser Blacklist" % len(ragets)
                              yans.sendMessage(msg.to,"α΄α΄ΚΙͺα΄Ι΄ sα΄α΄α΄Κ α΄α΄α΄Ιͺ α΄α΄α΄©α΄Ι΄Ιͺ " +mc)
                              ki.sendMessage(msg.to,"α΄α΄ΚΙͺα΄Ι΄ sα΄α΄α΄Κ α΄α΄α΄Ιͺ α΄α΄α΄©α΄Ι΄Ιͺ " +mc)
                              kk.sendMessage(msg.to,"α΄α΄ΚΙͺα΄Ι΄ sα΄α΄α΄Κ α΄α΄α΄Ιͺ α΄α΄α΄©α΄Ι΄Ιͺ " +mc)
                              kc.sendMessage(msg.to,"α΄α΄ΚΙͺα΄Ι΄ sα΄α΄α΄Κ α΄α΄α΄Ιͺ α΄α΄α΄©α΄Ι΄Ιͺ " +mc)
                              kb.sendMessage(msg.to,"α΄α΄ΚΙͺα΄Ι΄ sα΄α΄α΄Κ α΄α΄α΄Ιͺ α΄α΄α΄©α΄Ι΄Ιͺ " +mc)
                              ke.sendMessage(msg.to,"α΄α΄ΚΙͺα΄Ι΄ sα΄α΄α΄Κ α΄α΄α΄Ιͺ α΄α΄α΄©α΄Ι΄Ιͺ " +mc)
#===========KICKERS================#
                        elif ("tebas " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = yans.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           yans.updateGroup(G)
                                           invsend = 0
                                           Ticket = yans.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = yans.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           yans.updateGroup(X)
                                       except:
                                           pass
#====================================================================            

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                yans.sendMessage1(msg)
                                            except Exception as e:
                                                yans.sendText(msg.to,str(e))
                                    else:
                                        yans.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd.startswith("panggil "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(key1)
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                yans.sendMessage1(msg)
                                            except Exception as e:
                                                yans.sendText(msg.to,str(e))

                        elif cmd == "call":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = yans.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                yans.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd.startswith("call "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = yans.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jumlah = int(strnum)
                                yans.sendText(msg.to,"Undangan call grup {} sukses".format(str(strnum)))
                                if jumlah <= 1000:
                                   for x in range(jumlah):
                                   	try:
                                           call.acquireGroupCallRoute(to)
                                           call.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          yans.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              yans.sendText(msg.to,"γ Spam Gift γ\nBerhasil spamgift {} kali".format(str(jumlah)))
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      yans.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                        elif 'Spaminvite: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spaminvite: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      yans.sendMessage(midd, str(Setmain["RAmessage1"]))      
#================================================================          
                             
                        elif cmd == "promo":
                          if msg._from in admin:
                             yans.sendMessage(msg.to,"ββββββββΝΝ‘βΝΝ‘βΝΝ‘βΝΝ‘ββββββββ\nα΄Όα΄Ύα΄±α΄Ί α΄Όα΄Ώα΄°α΄±α΄Ώ\nβββββββββββββββββ\nβ£κ±α΄Κκ°Κα΄α΄ α΄Ι΄ΚΚ\nβ£κ±α΄Κκ°Κα΄α΄ + α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 2 α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 3 α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 4 α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 5 α΄κ±Ιͺκ±α΄\nβ£Κα΄α΄α΄Κα΄α΄α΄α΄α΄ 3-11 Κα΄α΄ α΄κ±Ιͺκ±α΄\nβ£Ι΄α΄α΄‘ κ±α΄ΚΙͺα΄α΄\nβ£ΚΚΙ’α΄ ΚΙͺκ±α΄ Ι΄α΄Ι’α΄\nββββββββββββββββββββ\n  β―βΝΝ‘βΝΝ‘βοΈπΊπ πππππππ πππ ππΊβοΈβΝΝ‘ββ―\nline.me/ti/p/~gepengcharlez\nβ£ΡΡΚ?Π²ΠΎΡ ΞΊΙͺcΞΊΡΚ_+_α΄Κα΄α΄α΄α΄α΄\nββββββββββΝΝ‘βΝΝ‘βΝΝ‘βΝΝ‘ββββββββββ")
                             yans.sendMessage(msg.to," β­ββββββββββ\nββ«β[     DAFTAR HARGA     ]ββ« \nβSELFBOT ONLY = 50K /BLN\nβ2 ASSIST = 75K /BLN\nβ5 ASSIST = 150K /BLN\nβ10 ASSIST = 250K /BLN\nβ\nβPROTECT ANTIJS\nβ\nβ2 BOT + ANTIJS = 100K /BLN\nβ5 BOT + ANTIJS = 250K /BLN\nβ10 BOT + ANTIJS = 450K /BLN\nβ\nββΰ¦\βANDA BERMINAT\nβ SILAHKAN ADD CONTACT \nβ DIBAWAH INI   \nβ\nβhttp://line.me/ti/p/~gepengcharlez\nβ       TERIMA KASIH      \nβ\nβ°ββββββββββββ")
                             msg.contentType = 13
                             msg.contentMetadata = {'mid': admin}
                             tanya = msg.text.replace("promo ","")
                             jawab = ("ββββββββΝΝ‘βΝΝ‘βΝΝ‘βΝΝ‘ββββββββ\nα΄Όα΄Ύα΄±α΄Ί α΄Όα΄Ώα΄°α΄±α΄Ώ\nβββββββββββββββββ\nβ£κ±α΄Κκ°Κα΄α΄ α΄Ι΄ΚΚ\nβ£κ±α΄Κκ°Κα΄α΄ + α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 2 α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 3 α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 4 α΄κ±Ιͺκ±α΄\nβ£1 α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄ + 5 α΄κ±Ιͺκ±α΄\nβ£Κα΄α΄α΄Κα΄α΄α΄α΄α΄ 3-11 Κα΄α΄ α΄κ±Ιͺκ±α΄\nβ£Ι΄α΄α΄‘ κ±α΄ΚΙͺα΄α΄\nβ£ΚΚΙ’α΄ ΚΙͺκ±α΄ Ι΄α΄Ι’α΄\nββββββββββββββββββββ\n  β―βΝΝ‘βΝΝ‘βοΈπΊπ πππππππ πππ ππΊβοΈ ΝΝ‘βΝΝ‘ββ―\nline.me/ti/p/~gepengcharlez\nβ£ΡΡΚ?Π²ΠΎΡ ΞΊΙͺcΞΊΡΚ_+_α΄Κα΄α΄α΄α΄α΄\nββββββββββΝΝ‘βΝΝ‘βΝΝ‘βΝΝ‘ββββββββββ")
                             jawaban = random.choice(jawab)
                             tts = gTTS(text=jawaban, lang='id')
                             tts.save('tts.mp3')
                             yans.sendAudio(msg.to,'tts.mp3')
                             yans.sendMessage(msg)         
                             yans.sendMessage(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasihππ")    
                             
                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = yans.getGroupIdsJoined()
                               for group in saya:
                                   yans.sendMessage(group,"ΚΚα΄α΄α΄α΄α΄sα΄ ΚΚ ΚΚα΄Ι΄κ±\n\n" + str(pesan))
                                                           
                        elif text.lower() == "cek name":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "sα΄α΄α΄α΄s Ι΄α΄α΄α΄ \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("name: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = yans.getProfile()
                                profile.displayName = string
                                yans.updateProfile(profile)
                                yans.sendMessage(msg.to,"Ι΄α΄α΄α΄ α΄Ιͺ Ι’α΄Ι΄α΄Ιͺ α΄α΄Ι΄α΄α΄α΄Ιͺ " + string + "")  

                        elif text.lower() == "reset Ι΄ame":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               Setmain["keyCommand"] = ""
                               yans.sendMessage(msg.to, "Κα΄ΚΚα΄sΙͺΚ α΄α΄Κα΄sα΄α΄ Ι΄α΄α΄α΄ ")

                        elif cmd == "reboot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "please wait")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               yans.sendMessage(msg.to, "Κα΄α΄ Κα΄ΚΚα΄sΙͺΚ α΄Ιͺ Κα΄sα΄α΄Κα΄...")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               yans.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            try:
                                G = yans.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(yans.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                yans.sendMessage(msg.to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                yans.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                yans.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                yans.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = yans.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = yans.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(yans.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "ππππ ππππ\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                yans.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = yans.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = yans.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                yans.sendMessage(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except:
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = yans.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = yans.getGroup(i)
                                if ginfo == group:
                                    yans.leaveGroup(i)
                                    yans.sendMessage(msg.to,"Leave in groups " +str(ginfo.name))

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               ma = ""
                               a = 0
                               gid = yans.getAllContactIds()
                               for i in gid:
                                   G = yans.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               yans.sendMessage(msg.to,"βFRIEND LIST\n\n"+ma+"\nTotal"+str(len(gid))+"Friends")
                               
                        
                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               ma = ""
                               a = 0
                               gid = yans.getGroupIdsJoined()
                               for i in gid:
                                   G = yans.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               yans.sendMessage(msg.to,"βππππ ππππ\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                if msg.toType == 2:
                                   X = yans.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   yans.updateGroup(X)
                                   yans.sendMessage(msg.to, "Url closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                if msg.toType == 2:
                                   x = yans.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      yans.updateGroup(x)
                                   gurl = yans.reissueGroupTicket(msg.to)
                                   yans.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#                                                     
                        elif cmd.startswith("tarik "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            args = cmd.replace("tarik ","")
                            mes = 0
                            try:
                                mes = int(args[1])
                            except:
                                mes = 1
                            M = yans.getRecentMessagesV2(to, 101)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == yans.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                yans.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.start()
                                thread1.join()
                            yans.sendMessage(msg.to, "Success unsend {} message".format(len(MId))) 
 #===========BOT UPDATE SC NEW============#                                                                  
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                yans.sendMessage(msg.to,"Send Picture")

                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                Setmain["SKfoto"][mid,Amid,Bmid,Cmid,Dmid,Emid] = True
                                yans.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                Setmain["SKfoto"][mid] = True
                                yans.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "changedual":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                yans.sendMessage(msg.to,"?‘Δ±ΡΔ±αΉ αΉΏΔ±ΤΡΘ αΉΚΡ§...")
                                
                          elif cmd.startswith("changedualurl: "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                yans.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                yans.sendMessage(msg.to, "?‘Δ±ΡΔ±αΉ ?ΘαΉ­ΘαΉΚΡ§.....")

#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == 'tagall':
                           if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                             group = yans.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                yans.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getContact(m_id).displayName + "\n"
                                yans.sendMessage(msg.to,"βBotlistβ\n\n\n"+ma+"\n%s Bots" %(str(len(Bots))))

                        elif cmd == "squadlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getContact(m_id).displayName + "\n"
                                for m_id in Squad:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getContact(m_id).displayName + "\n"
                                yans.sendMessage(msg.to,"βκ±Qα΄α΄α΄ΚΙͺκ±α΄β\n\n\n"+ma+"\n%s α΄α΄α΄α΄Κα΄α΄" %(str(len(Bots)+len(Squad))))

                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +yans.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +yans.getContact(m_id).displayName + "\n"
                                yans.sendMessage(msg.to,"βAdminlistβ\n\nβOwner\n"+ma+"\nβAdmin\n"+mb+"\nβStaff:\n"+mc+"\n%s Adminlist" %(str(len(owner)+len(admin)+len(staff))))
                  
                        elif cmd == "prolist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0            
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +yans.getGroup(group).name + "\n"
                                gid = protectantijs
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +yans.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +yans.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +yans.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(e) + ". " +yans.getGroup(group).name + "\n"
                                yans.sendMessage(msg.to,"πα΄α΄?α΄α΄Κ ΚΙͺsα΄ α΄Κα΄α΄α΄α΄α΄ π πππππππ πππ ππ\n\nπα΄Κα΄α΄α΄α΄α΄ Η«Κ:\n"+ma+"\nπα΄Κα΄α΄α΄α΄α΄ ΙͺΙ΄α΄ Ιͺα΄α΄:\n"+mb+"\nπα΄Κα΄α΄α΄α΄α΄α΄Ι΄α΄Ιͺα΄Ιͺα΄α΄α΄Κ:\n"+mc+"\nπα΄Κα΄α΄α΄α΄α΄α΄Ιͺα΄α΄:\n"+md+"\nπα΄Κα΄α΄α΄α΄α΄α΄α΄Ι΄α΄α΄Κ:\n"+me+"\nπα΄Κα΄α΄α΄α΄α΄α΄α΄ΙͺΙ΄:\n"+mf+"\n\nπα΄Κα΄α΄α΄α΄α΄ ΚΙͺsα΄ %s Ι’Κα΄α΄α΄ α΄Κα΄α΄α΄α΄α΄π" %(str(len(protectqr)+len(protectinvite)+len(protectantijs)+len(protectcancel)+len(protectkick)+len(protectjoin))))

                        elif cmd == "rname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                yans.sendMessage(msg.to,responsename)

                        elif cmd == ".bye":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                G = yans.getGroup(msg.to)
                                yans.sendMessage(msg.to, "See you next again "+str(G.name))
                                yans.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = yans.getGroupIdsJoined()
                                for i in gid:
                                    h = yans.getGroup(i).name
                                    if h == ng:
                                        yans.sendMessage(i, " Silahkan invite Ownernya ")
                                        yans.leaveGroup(i)
                                        yans.sendMessage(to,"Succes leave group " +h)

                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                get_profile_time_start = time.time()
                                get_profile = yans.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = yans.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = yans.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                yans.sendMessage(msg.to, "βTime Responβ\n\n βGet Profile\n   %.10f\n βGet Contact\n   %.10f\n βGet Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               start = time.time()
                               yans.sendMessage(to, "..")
                               elapsed_time = time.time() - start
                               yans.sendMessage(to,"%s"%str(round(elapsed_time,4)))

                        elif cmd == "list on":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['SKreadPoint'][msg.to] = msg_id
                                 Setmain['SKreadMember'][msg.to] = {}
                                 yans.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "list off":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['SKreadPoint'][msg.to]
                                 del Setmain['SKreadMember'][msg.to]
                                 yans.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "list sider":
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            if msg.to in Setmain['SKreadPoint']:
                                if Setmain['SKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['SKreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ List sider ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(yans.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        yans.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SKreadPoint'][msg.to]
                                        del Setmain['SKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SKreadPoint'][msg.to] = msg.id
                                    Setmain['SKreadMember'][msg.to] = {}
                                else:
                                    yans.sendMessage(msg.to, "User kosong tidak terdetect")
                            else:
                                yans.sendMessage(msg.to, "Ketik List on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  yans.sendMessage(msg.to, "Cek sider diaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  yans.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  yans.sendMessage(msg.to, "Sudak tidak aktif")
                      
#===========KAMUS============#
                        elif cmd.startswith("inggris:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=en&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                yans.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                                
                        elif cmd.startswith("indo:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                yans.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)

                        elif cmd.startswith("korea:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ko&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                yans.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jp:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ja&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                yans.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                                
                        elif cmd.startswith("thai:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=th&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                yans.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("arab:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ar&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                yans.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)  
                        elif cmd.startswith("jawa:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=jw&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                yans.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                                                                                 
                        elif "https://www.smule.com/" in msg.text.lower():
                        	if msg._from in owner or msg._from in admin or msg._from in mid:
                                       sep = msg.text.split("https://www.smule.com/")
                                       textnya = msg.text.replace(sep[0]+"https://www.smule.com/","")
                                       p = requests.get("https://api.fckveza.com/getsmule?link=https://www.smule.com/{}&apikey=Urara77".format(textnya))
                                       data = p.json()
                                       genstar = "JUDUL OC : {}".format(data["result"]["title"])
                                       genstar += "\n\nFILE VIDEO AND AUDIO SUCSES"
                                       yans.sendVideoWithURL(to, data["result"]["url"])
                                       yans.sendAudioWithURL(to, data["result"]["url"])
                                       yans.sendMessage(to, str(genstar))
                                                     
                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      yans.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      yans.sendMessage(midd, str(Setmain["SKmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              msgs = msg.text.replace('ID line: ','')
                              conn = yans.findContactsByUserid(msgs)
                              if True:
                                  yans.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  yans.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                  
                           
                          elif cmd.startswith("al-qur'an"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                web = requests.get("http://api.alquran.yansoud/surah/{}".format(txt))
                                data = web.json()
                                result = "β­βββγ {} γ".format(data["data"]["englishName"])
                                quran = data["data"]
                                result += "\nββ½ Surah keγ {} γ".format(quran["number"])
                                result += "\nββ½ Nama Surahγ {} γ".format(quran["name"])
                                result += "\nββ½ {} Ayat β’".format(quran["numberOfAyahs"])
                                result += "\nββ½ {} β’".format(quran["name"])
                                result += "\nββ½ Ayat Sajadah γ {} γ".format(quran["ayahs"][0]["sajda"])
                                result += "\nβ°ββββββββββββ\n"
                                no = 0
                                for ayat in data["data"]["ayahs"]:
                                    no += 1
                                    result += "\n{}. {}".format(no,ayat['text'])
                                k = len(result)//10000
                                for aa in range(k+1):
                                    yans.sendMessage(to,'{}'.format(result[aa*10000 : (aa+1)*10000]))
                                    
                        elif cmd.startswith("imagetext "):
                            text_ = removeCmd("imagetext", text)
                            web = _session
                            web.headers["User-Agent"] = random.choice(settings["userAgent"])
                            font = random.choice(["arial","comic"])
                            r = web.get("http://api.img4me.com/?text=%s&font=%s&fcolor=FFFFFF&size=35&bcolor=000000&type=jpg" %(urllib.parse.quote(text_),font))
                            data = str(r.text)
                            if "Error" not in data:
                                path = data
                                yans.sendImageWithURL(to,path)
                            else:
                                yans.sendMessage(msg.to,"[RESULT] %s" %(data.replace("Error: ")))
                                
                        elif cmd.startswith("topnews"):
                              if msg._from in owner or msg._from in admin or msg._from in mid: 
                                  dpk=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=dpk.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  yans.sendMessage(msg.to, str(hasil))
                                  yans.sendImageWithURL(msg.to, str(path))
                                  
                        elif cmd.startswith("meme fb"):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"]) 
                              hasil += "\nVotes : " + str(data["votes"])
                              yans.sendMessage(msg.to, str(hasil))
                              
                        elif cmd.startswith("fs "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            try:
                                separate = msg.text.split(" ")
                                nama = msg.text.replace(separate[0] + " ","")                                
                                nmor = ["1","2","3","4","5","6","7"]
                                plih = random.choice(nmor)
                                url =  ("http://api.farzain.com/special/fansign/cosplay/cosplay.php?apikey=tkj-api12&text={}").format(str(nama))
                                yans.sendImageWithURL(msg.to, url)
                            except Exception as error:
                                pass
   #New                      	
                        elif cmd.startswith('like '):
                        	if msg._from in owner or msg._from in admin or msg._from in mid:
                                    try:
                                        typel = [1001,1002,1003,1004,1005,1006]
                                        key = eval(msg.contentMetadata["MENTION"])
                                        u = key["MENTIONEES"][0]["M"]
                                        a = yans.getContact(u).mid
                                        s = yans.getContact(u).displayName
                                        hasil = yans.getHomeProfile(a)
                                        st = hasil['result']['feeds']
                                        for i in range(len(st)):
                                            test = st[i]
                                            result = test['post']['postInfo']['postId']
                                            yans.likePost(str(sender), str(result), likeType=random.choice(typel))
                                            yans.createComment(str(sender), str(result), 'Autolike by ππ¬ππ£π¨π½ππ\nhttp://line.me/ti/p/~gepengcharlez\n\nα΄α΄Ι΄α΄ΚΙͺα΄α΄ α΄α΄κ±α΄ α΄Κα΄α΄α΄α΄α΄ Ι’Κα΄α΄ (Κα΄α΄ Ι’α΄Κα΄Ι΄Ι’)')
                                        yans.sendMessage(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                    except Exception as e:
                                        yans.sendMessage(receiver, str(e))
                                        
                        elif cmd.startswith("add friend "):
                        	if msg._from in owner or msg._from in admin or msg._from in mid:
                                    if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            yans.findAndAddContactsByMid(str(ls))
                                        yans.sendMessage(to, "Success Add Friend "+yans.getContact(str(ls)).displayName)
                                        
                        elif cmd.startswith("delfriend "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                   yans.deleteContact(ls)
                                yans.sendMessage(to, "Succes Delete Contact \n")
                                
                        elif cmd == "mykey":
                            yans.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                            
                        elif cmd.startswith('inviteme '):
                              if msg._from in owner or msg._from in admin or msg._from in mid:    
                               text = msg.text.split()
                               number = text[1]
                               if number.isdigit():
                                groups = yans.getGroupIdsJoined()
                                if int(number) < len(groups) and int(number) >= 0:
                                    groupid = groups[int(number)]
                                    group = yans.getGroup(groupid)
                                    target = sender
                                    try:
                                        yans.getGroup(groupid)
                                        yans.findAndAddContactsByMid(target)
                                        yans.inviteIntoGroup(groupid, [target])
                                        yans.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                    except:
                                        yans.sendMessage(msg.to,"I no there baby")                                                                                                       
                        elif cmd.startswith("idcontact "):
                        	if msg._from in owner or msg._from in admin or msg._from in mid: 
                                   if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                                contact = yans.getContact(ls)
                                                mi_d = contact.mid
                                                yans.sendContact(msg.to, mi_d)
                                                
                        elif cmd.startswith("contact "):
                        	if msg._from in owner or msg._from in admin or msg._from in mid: 
                                       sep = cmd.split(" ")
                                       asu = cmd.replace(sep[0] + " ","")
                                       try:
                                          yans.sendContact(to, asu)
                                       except:
                                          pass
                                          
                        elif cmd.startswith("mp3: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", yansass_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                yans.sendMessage(msg.to, "Hasil pencarian.....")
                                yans.sendAudioWithURL(msg.to, me)
                            except Exception as e:
                                yans.sendMessage(msg.to,str(e))
                                
                        elif cmd.startswith("clone "):
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                             if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    yans.cloneContactProfile(contact)
                                    ryan = yans.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "γ clone Profile γ\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    yans.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    yans.sendMessage(msg.to, "Gagal clone profile")
                                    
                        elif text.lower() == 'restore':
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              try:
                                  yansProfile.displayName = str(myProfile["displayName"])
                                  yansProfile.statusMessage = str(myProfile["statusMessage"])
                                  yansProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  yans.updateProfileAttribute(8, yansProfile.pictureStatus)
                                  yans.updateProfile(yansProfile)
                                  yans.sendMessage(msg.to, sender, "γ Restore Profile γ\nNama ", " \nBerhasil restore profile")
                              except:
                                  yans.sendMessage(msg.to, "Gagal restore profile")
                                  
                        elif cmd == 'listblock':
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            blockedlist = yans.getBlockedContactIds()
                            kontak = yans.getContacts(blockedlist)
                            num=1
                            msgs="List Blocked"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            yans.sendMessage(to, msgs)
                            
#===============MEDIA JSON============================#
                        elif cmd.startswith("addmp3 "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    yans.sendMessage(msg.to,"Silahkan kirim mp3 nya...") 
                                else:
                                    yans.sendMessage(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    yans.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    yans.sendMessage(msg.to, "Berhasil hapus mp3 {}".format( str(name.lower())))
                                else:
                                    yans.sendMessage(msg.to, "Maaf mp3 tidak terdaftar dalam list") 
                                 
                        elif cmd == "listmp3":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                no = 0
                                ret_ = "β­βββγ My Music γ\n"
                                for audio in audios:
                                    ret_ += "ββ½β  " + audio.title() + "\n"
                                ret_ += "βββγ{} Record  γ".format(str(len(audios)))
                                yans.sendMessage(to, ret_)

                        elif cmd.startswith("addsticker "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("Sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    yans.sendMessage(to, "Silahkan kirim stickernya...") 
                                else:
                                    yans.sendMessage(to, "Maff stiker dlam list silahkan ganti nama") 
                                
                        elif cmd.startswith("dellsticker "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    yans.sendMessage(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    yans.sendMessage(to, "Maaf sticker tidak ada dalam list") 
                                                   
                        elif cmd == "liststicker":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                no = 0
                                ret_ = "β­βββγ My Sticker γ\n"
                                for sticker in stickers:
                                    ret_ += "ββ½β  " + sticker.title() + "\n"
                                ret_ += "β°βββγ {} Stickers γ ".format(str(len(stickers)))
                                yans.sendMessage(to, ret_)

                        elif cmd.startswith("addimg "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim fotonya")
                                else:
                                    yans.sendMessage(to, "Foto sudah dalam list")

                        elif cmd.startswith("dellimg "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   yans.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   yans.sendMessage(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   yans.sendMessage(to, "Maff poto tidak ada dalam list")

                        elif cmd == "listimage":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                no = 0
                                ret_ = "β­βββγ Daftar Image γ\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("ββ½") + " " + audio.title() + "\n"
                                ret_ += "β°βββγ Total {} Image γ".format(str(len(audios)))
                                yans.sendMessage(to, ret_)
#==============add video========================================================
                        elif cmd.startswith("addvideo"):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    yans.sendMessage(to, "Silahkan kirim video nya...")
                                else:
                                    yans.sendMessage(to, "video sudah ada")
                        elif cmd.startswith("dellvideo "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   yans.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   yans.sendMessage(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   yans.sendMessage(to, "Maaf video tidak ada dalam list")

                        elif cmd == "listvideo":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                no = 0
                                ret_ = "β­βββγ Daftar Video γ\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("ββ½") + " " + audio.title() + "\n"
                                ret_ += "β°βββγ Total {} Video γ".format(str(len(audios)))
                                yans.sendMessage(to, ret_)
#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = ""
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = ""
                                  yans.sendMessage(msg.to, "Welcome Has Been Active")
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = ""
                                    yans.sendMessage(msg.to, "Welcome has been Deactive")

                        elif 'Protecturl ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "γ Status Protect Url γ\n" + msgs)
                                  ki.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                  kk.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                  kc.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                  kb.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                  ke.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    yans.sendMessage(msg.to, "γ Status Protect Url γ\n" + msgs)
                                    ki.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                    kk.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                    kc.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                    kb.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)
                                    ke.sendMessage(msg.to,"γ Status Protect Url γ\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "γ Status Protect kick γ\n" + msgs)
                                  ki.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                  kk.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                  kc.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                  kb.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                  ke.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    yans.sendMessage(msg.to, "γ Status Protect kick γ\n" + msgs)
                                    ki.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                    kk.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                    kc.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                    kb.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)
                                    ke.sendMessage(msg.to,"γ Status Protect kick γ\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "γ Status Protect Join γ\n" + msgs)
                                  ki.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                  kk.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                  kc.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                  kb.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                  ke.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    yans.sendMessage(msg.to, "γ Status Protect Join γ\n" + msgs)
                                    ki.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                    kk.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                    kc.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                    kb.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)
                                    ke.sendMessage(msg.to,"γ Status Protect Join γ\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "γ Status Protect Cancel γ\n" + msgs)
                                  ki.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                  kk.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                  kc.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                  kb.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                  ke.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    yans.sendMessage(msg.to, "γ Status Protect Cancel γ\n" + msgs)
                                    ki.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                    kk.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                    kc.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                    kb.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)
                                    ke.sendMessage(msg.to,"γ Status Protect Cancel γ\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "γ Status Protect Invite γ\n" + msgs)
                                  ki.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                  kk.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                  kc.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                  kb.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                  ke.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    yans.sendMessage(msg.to, "γ Status Protect Invite γ\n" + msgs)
                                    ki.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                    kk.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                    kc.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                    kb.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                    ke.sendMessage(msg.to,"γ Status Protect Invite γ\n" + msgs)
                                    
                        elif 'Js ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Protect Antikicker sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = yans.getGroup(msg.to)
                                       msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                  yans.sendMessage(msg.to, "γ Status Protect Anti Kicker γ\n" + msgs)
                                  ki.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                  kk.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                  kc.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                  kb.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                  ke.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect Anti Kicker sudah tidak aktif"
                                    yans.sendMessage(msg.to, "γ Status Protect Antikicker γ\n" + msgs)
                                    ki.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                    kk.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                    kc.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                    kb.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)
                                    ke.sendMessage(msg.to,"γ Status Anti Kicker γ\n" + msgs)

                        elif 'allpro ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectantijs:
                                      msgs = ""
                                  else:
                                      protectantijs.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = yans.getGroup(msg.to)
                                      msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protecttion sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = yans.getGroup(msg.to)
                                      msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  yans.sendMessage(msg.to, "γ Status Protection γ\n" + msgs)
                                  ki.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                  kk.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                  kc.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                  kb.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                  ke.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""                               
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection sudah dimatikan"
                                    else:
                                         ginfo = yans.getGroup(msg.to)
                                         msgs = "Status : [ β ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    yans.sendMessage(msg.to, "γ Status Protection γ\n" + msgs)
                                    ki.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                    kk.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                    kc.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                    kb.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)
                                    ke.sendMessage(msg.to,"γ Status Protection γ\n" + msgs)

#===========KICKOUT============#
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       if target not in owner:
                                           if target not in admin:
                                               if target not in staff:
                                                   if target not in Team:
                                                       try:
                                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                                           print ("kicker1 kick user")
                                                       except:
                                                           yans.sendMessage(msg.to,"limit")
                                                           
#===========ADMIN ADD============#
                        elif ("addstaff " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ sα΄α΄??")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ sα΄α΄??")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ sα΄α΄??")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ sα΄α΄??")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ sα΄α΄??")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ sα΄α΄??")
                                       except:
                                           pass

                        elif ("addbot " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ Κα΄α΄")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ Κα΄α΄")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ Κα΄α΄")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ Κα΄α΄")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ Κα΄α΄")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ Κα΄α΄")
                                       except:
                                           pass

                        elif ("addsquad " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Squad.append(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ κ±Qα΄α΄α΄")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ κ±Qα΄α΄α΄")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ κ±Qα΄α΄α΄")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ κ±Qα΄α΄α΄")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ κ±Qα΄α΄α΄")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ κ±Qα΄α΄α΄")
                                       except:
                                           pass

                        elif ("addadmin " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.append(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ admin")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ admin")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ admin")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ admin")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ admin")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄α΄α΄Κα΄Κα΄α΄Ι΄ admin")
                                       except:
                                           pass
                                           
                        elif ("Admindell " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s  admin")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s admin")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s admin")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s admin")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s admin")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s admin")
                                       except:
                                           pass                  

                        elif ("Staffdell " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s sα΄α΄??")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s sα΄α΄??")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s sα΄α΄??")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s sα΄α΄??")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s sα΄α΄??")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s sα΄α΄??")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s Κα΄α΄s")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s Κα΄α΄s")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s Κα΄α΄s")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s Κα΄α΄s")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s Κα΄α΄s")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s Κα΄α΄s")
                                       except:
                                           pass

                        elif ("Squaddell " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Squad.remove(target)
                                           yans.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s κ±Qα΄α΄α΄")
                                           ki.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s κ±Qα΄α΄α΄")
                                           kk.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s κ±Qα΄α΄α΄")
                                           kc.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s κ±Qα΄α΄α΄")
                                           kb.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s κ±Qα΄α΄α΄")
                                           ke.sendMessage(msg.to,"Κα΄ΚΚα΄sΙͺΚ α΄α΄Ι΄Ι’Κα΄α΄α΄s κ±Qα΄α΄α΄")
                                       except:
                                           pass
                                           
                        elif cmd == "admin on" or text.lower() == 'admin:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addadmin"] = True
                                yans.sendMessage(msg.to,"Send Contact")

                        elif cmd == "admin off" or text.lower() == 'adminexpl:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["delladmin"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addstaff"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff off" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["dellstaff"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addbots"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot off" or text.lower() == 'botexpl:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["dellbots"] = True
                                yans.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "squad on" or text.lower() == 'squad:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addsquads"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "squad off" or text.lower() == 'squadexpl:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["dellsquads"] = True
                                yans.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "abort" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                yans.sendMessage(msg.to,"All refresh")
                                ki.sendMessage(msg.to,"All refresh")
                                kk.sendMessage(msg.to,"All refresh")
                                kc.sendMessage(msg.to,"All refresh")
                                kb.sendMessage(msg.to,"All refresh")
                                ke.sendMessage(msg.to,"All refresh")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                for i in admin:
                                    ma = yans.getContact(i)
                                    yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                for i in staff:
                                    ma = yans.getContact(i)
                                    yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "bot" or text.lower() == 'contact bot':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                for i in Bots:
                                    ma = yans.getContact(i)
                                    yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "squad" or text.lower() == 'contact squad':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                for i in Bots:
                                    ma = yans.getContact(i)
                                    yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                                for i in Squad:
                                    ma = yans.getContact(i)
                                    yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#        
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Timeline"] = True
                                yans.sendMessage(msg.to,"detect timeline on")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Timeline"] = False
                                yans.sendMessage(msg.to,"detect timleline off ")
                                
                        elif cmd == "autoblock on" or text.lower() == 'blockadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoblock"] = True
                                yans.sendMessage(msg.to,"autoblock berhasil di hidupkan")

                        elif cmd == "autoblock off" or text.lower() == 'blockadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoblock"] = False
                                yans.sendMessage(msg.to,"autoblock berhasil di matikan")
                                
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["unsendMessage"] = True
                                yans.sendMessage(msg.to,"detect unsend diaktifkan")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["unsendMessage"] = False
                                yans.sendMessage(msg.to,"detect unsend dinonaktifkan")
                                
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["contact"] = True
                                yans.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["contact"] = False
                                yans.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["detectMention"] = True
                                yans.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["detectMention"] = False
                                yans.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoJoin"] = True
                                yans.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoJoin"] = False
                                yans.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoAdd"] = True
                                yans.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoAdd"] = False
                                yans.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["sticker"] = True
                                yans.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["sticker"] = False
                                yans.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["autoJoinTicket"] = True
                                yans.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["autoJoinTicket"] = False
                                yans.sendMessage(msg.to,"Join ticket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           yans.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass
                                           
                          elif "Invite " in msg.text:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      yans.findAndAddContactsByMid(target)
                                      yans.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 

                        elif ("Untalkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           yans.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Talkwblacklist"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Talkdblacklist"] = True
                                yans.sendMessage(msg.to,"Send contact")
                                
                        
                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       if target not in Bots:
                                           if target not in owner:
                                               if target not in admin:
                                                   if target not in staff:
                                                       try:
                                                           wait["blacklist"][target] = True
                                                           yans.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                                       except:
                                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           yans.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["wblacklist"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["dblacklist"] = True
                                yans.sendMessage(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if wait["blacklist"] == {}:
                                yans.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getContact(m_id).displayName + "\n"
                                yans.sendMessage(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if wait["Talkblacklist"] == {}:
                                yans.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +yans.getContact(m_id).displayName + "\n"
                                yans.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotalγ%sγTalkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if wait["blacklist"] == {}:
                                    yans.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = yans.getContact(i)
                                        yans.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'cban':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              wait["blacklist"] = {}
                              ragets = yans.getContacts(wait["blacklist"])
                              mc = ""
                              yans.sendMessage(msg.to,"Succes clearall baned" + mc)
#===========COMMAND SET============#
                        elif 'Spesan: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  yans.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  yans.sendMessage(msg.to, "γPesan Msgγ\nPesan Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Swelcome: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Swelcome: ','')
                              if spl in [""," ","\n",None]:
                                  yans.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  yans.sendMessage(msg.to, "γWelcome Msgγ\nWelcome Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Srespon: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Srespon: ','')
                              if spl in [""," ","\n",None]:
                                  yans.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  yans.sendMessage(msg.to, "γRespon Msgγ\nRespon Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Sspam: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Sspam: ','')
                              if spl in [""," ","\n",None]:
                                  yans.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["SKmessage1"] = spl
                                  yans.sendMessage(msg.to, "γSpam Msgγ\nSpam Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Ssider: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Ssider: ','')
                              if spl in [""," ","\n",None]:
                                  yans.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  yans.sendMessage(msg.to, "γSider Msgγ\nSider Msg diganti jadi :\n\nγ{}γ".format(str(spl)))
                                  
                                  
                        elif text.lower() == "cek msg":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "Msg add:\nγ " + str(wait["message"]) + " γ")
                               yans.sendMessage(msg.to, "Msg welcome:\nγ " + str(wait["welcome"]) + " γ")
                               yans.sendMessage(msg.to, "Msg Respon:\nγ " + str(wait["Respontag"]) + " γ")
                               yans.sendMessage(msg.to, "Msg welcome:\nγ " + str(Setmain["SKmessage1"]) + " γ")
                               yans.sendMessage(msg.to, "Msg sider:\nγ " + str(wait["mention"]) + " γ")

                        elif text.lower() == "cpesan":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "γPesan Msgγ\nPesan Msg mu :\n\nγ " + str(wait["message"]) + " γ")

                        elif text.lower() == "cwelcome":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "γWelcome Msgγ\nWelcome Msg mu :\n\nγ " + str(wait["welcome"]) + " γ")

                        elif text.lower() == "crespon":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "γRespon Msgγ\nRespon Msg mu :\n\nγ " + str(wait["Respontag"]) + " γ")

                        elif text.lower() == "cspam":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "γSpam Msgγ\nSpam Msg mu :\n\nγ " + str(Setmain["SKmessage1"]) + " γ")

                        elif text.lower() == "csider":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               yans.sendMessage(msg.to, "γSider Msgγ\nSider Msg mu :\n\nγ " + str(wait["mention"]) + " γ")
                                                      
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = yans.findGroupByTicket(ticket_id)
                                     yans.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     yans.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)
        
def runningProgram():
    if Setmain['restartPoint'] is not None:
        try:
            yans.sendMessage(settings['restartPoint'], 'BOT ON AGAIN')
        except TalkException:
            pass
        Setmain['restartPoint'] = None
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('[ SYSTEM MESSAGE : *KEYBOARD INTERRUPT.')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print (' [β’] SYSTEM MESSAGE : *BOT BERHASIL DI INSTALL.\n______________________________\n')
    runningProgram()
      
            
    
