import urllib
import upload
from bs4 import BeautifulSoup

def geturl(html):
    imgurlist = []
    imgnamlist = []
    htmltree  = BeautifulSoup(html)
    imgtaglist = htmltree.find_all('img')
    for i in range(len(imgtaglist)):
        link = imgtaglist[i].get('src')
        name = link.split('/')[-1]
        imgurlist.append(link)
        imgnamlist.append(name)
    return imgurlist, imgnamlist


def getimg(imgurlist,imgnamlist):
    for i in range(len(imgurlist)):
        imgname = 'images/'+imgnamlist[i]
        imgname = imgname.replace('?','')
        try:
            urllib.urlretrieve(imgurlist[i], imgname)
            fob = open(imgname,'rb')
            #print(imgurlist[i])
            #print(imgname)
            #upload.upimg(imgnamlist[i].replace('%20', ' '),fob) #replace any %20 with white space.
            fob.close()
        except Exception as e:
            print(e)
            pass

def getimg_ftp(imgurlist,imgnamlist):
    import os, ftplib
    FTPUSER = os.environ.get("FTPUSER", '')
    FTPPASS = os.environ.get("FTPPASS", '')
    ftps = ftplib.FTP('www.sda-archives.com', FTPUSER, FTPPASS)
    for i in range(len(imgurlist)):
        imgname = 'images/'+imgnamlist[i]
        imgname = imgname.replace('?','')
        try:
            urllib.urlretrieve(imgurlist[i], imgname)
            fob = open(imgname,'rb')
            #print(imgurlist[i])
            #print(imgname)
            upload.upimg(imgnamlist[i],fob, ftps) #replace any %20 with white space.
            fob.close()
        except Exception as e:
            print(e)
            pass






