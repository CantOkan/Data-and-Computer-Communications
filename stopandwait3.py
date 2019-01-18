#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import random

import pandas as pd
from matplotlib import pyplot as plt

class Sender(object):

    def __init__(self,packets=[]):
        self.packets=packets
        self.ack=[]
        self.j=0
        self.i=0

    def pases(self):
        while(self.i<len(self.packets)): #0 ile len(self.packets)
            #print("turn {}".format(self.i))
            print("paket gidiyor")
            print("giden paket {}".format(self.packets[self.i]))
            con.trasmission(self.packets[self.i],self.i)#burda i'yi hangi paketin acki dönücek bunu anlayabilmek için gönderiyoruz




    def getack(self,ack,status,n):#burda n ack i'si
        print(ack)

        self.ack.append(status)
        if(self.ack[self.j]==True):
            #print("J {}".format(self.j))
            print("ack {}".format(n+1))
            self.j+=1
            print("Paket Ulasmis,Diger paket")
            print("----------------------")
            self.i+=1
            sender1.pases()

        elif(self.ack[self.j]==False):
            print("ack {}".format(n+1))
            self.j+=1
            #ACk false yani paket doğru ulaşmadı yolda bozuldu,bu duurumda packeti tekrar göndeririz
            print("paket olusmamis,Paketi tekar gonder")
            print("---------------------")
            sender1.pases()

class Medium(object):
    def __init__(self,sender,receiver):
        self.sender=sender
        self.receiver=receiver
    def trasmission(self,packet,i):

        print("----------------------")
        print("random test Uygula")
        #x=input()
        x=random.randint(0, 1)
        #Random test uyguluyoruz eğer 0 ise bit hatali gönderiliyor ve bize hatalı bir ack geliyor
        print("test sonucu(0-ise hatali) : {}".format(x))
        print("-----------------")
        if(x):
            time.sleep(1)#Paketin ulaşması için geçen süre (L/R)
            self.receiver.get(packet,i)
            #paket başarı ile ulaştı
        else:
            time.sleep(2)#Paketin ulaşması için geçen süre (L/R)
            self.receiver.get(None,i)
            #paketin yolda bozulup yanlış ulaşması durumu

    def acknowldege(self,ack,status,i):
        time.sleep(1)#acknowldege ulaşması için geçen süre
        self.sender.getack(ack,status,i)


class Receiver(object):

    def __init__(self,buffersize):
        self.buffersize=buffersize
        self.buffer=[]

    def show(self):
        print("Buffer'a ulasan paketler")
        for i in self.buffer:
            print("Frame {}".format(i))

    def get(self,packet,i):
        if(packet):
            self.buffer.append(packet)
            time.sleep(1)#Paket receiverda belirli bir processden geçiyor
                        #Bit test uygulanıyor


            print('ulasan paket:{}'.format(packet))
            self.ack(packet,True,i)
            #return True acknowldege
        else:
            #eğer paket yolda bozuldu ise return false acknowldege
            self.ack(packet,False,i)

    def ack(self,packet,status,i):
        if(packet):
            print("TRUE")
            con.acknowldege(packet,status,i)#True ise
        else:
            print("FALSE")
            #frame hatalı tekrar gönder
            con.acknowldege(packet, status,i)



sender1=Sender(['1','2','3'])

receiver1=Receiver(5)

con=Medium(sender1, receiver1)
then=time.time()


sender1.pases()

receiver1.show()


#errorrate=[0.1,0.01]
