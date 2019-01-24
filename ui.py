
import tkinter
from tkinter import *
import search
import pymssql


root =tkinter.Tk()
root.title("周报表数据查询")

class view(Frame):
    def __init__(self,master = NONE):
        Frame.__init__(self,master)
        self.root = master
        self.viewUi()
    def viewUi(self):

        Label(self,text = "欢迎使用 方象5000 衍生小程序！").grid(row=0,columnspan = 3)

class frist(Frame):
    def __init__(self,master = NONE):
        Frame.__init__(self,master)
        self.root = master
        self.fristUi()
    def fristUi(self):
        Label(self,text="菜单").pack()


class scend(Frame):
    def __init__(self,master = NONE):
        Frame.__init__(self,master)
        self.root=master
        self.scend()
    def scend(self):
        Label(self,text="测试").pack()

class three(Frame):
    def __init__(self,master = NONE):
        Frame.__init__(self,master)
        self.root=master
        self.scend()

    def cxTime(self):

        self.ip=self.e.get()
        self.serverName=self.f.get()
        self.sel0(),self.sel1(),self.sel2(),self.sel3(),self.sel4(),self.sel5()
        if self.ets0!=NONE and self.ete0!=NONE:
            print(self.ete0)
            sVal =search.run(self.ip,self.serverName,self.ets0,self.ete0)
            print(type(sVal))
            for k,v in enumerate(sVal):
                Label(self,text=v).grid(row=k+10,column=1)
        if self.ets1!=NONE and self.ete1!=NONE:
            print(self.ete1)
            sVal =search.run(self.ip,self.serverName,self.ets1,self.ete1)
            for k,v in enumerate(sVal):
                Label(self,text=v).grid(row=k+10,column=2)
        if self.ets2!=NONE and self.ete2!=NONE:
            print(self.ete2)
            sVal =search.run(self.ip,self.serverName,self.ets2,self.ete2)
            for k,v in enumerate(sVal):
                Label(self,text=v).grid(row=k+10,column=3)
        if self.ets3!=NONE and self.ete3!=NONE:
            print(self.ip)
            sVal =search.run(self.ip,self.serverName,self.ets3,self.ete3)
            for k,v in enumerate(sVal):
                Label(self,text=v).grid(row=k+10,column=4)
        if self.ets4!=NONE and self.ete4!=NONE:
            print(self.ip)
            sVal =search.run(self.ip,self.serverName,self.ets4,self.ete4)
            for k,v in enumerate(sVal):
                Label(self,text=v).grid(row=k+10,column=5)
        if self.ets5!=NONE and self.ete5!=NONE:
            print(self.ip)
            sVal =search.run(self.ip,self.serverName,self.ets5,self.ete5)
            for k,v in enumerate(sVal):
                Label(self,text=v).grid(row=k+10,column=6)

    def link(self):
        self.test = self.e.get()
        print(self.test)
        try :
            if self.test!="":
                if self.test=="192.168.8.251":
                    conn = pymssql.connect(host=self.test,user="sa",password='',database='newfdbmis5000')
                    conn.close()
                else:
                    conn = pymssql.connect(host=self.test,user="sa",password='',database='fdbmis5000')
                    conn.close()
        except BaseException:
               print( "测试链接失败")
        else:
               print( "测试链接成功")


    def clearTime(self):
        self.e.set("192.168.")
    def scend(self):
        Label(self,text= "查询结果").grid(row=0,column=3)
        row=1
        self.e=StringVar()
        self.f=StringVar()
        Entry(self,textvariable=self.e).grid(row=1 ,column =1,columnspan =2)
        Label(self,text="IP地址:").grid(row=1,column=0)
        Entry(self,textvariable=self.f,width=5).grid(row=1,column=3)
        Button(self,text = "连接",width=5,command=self.link).grid(row=1,column=4)
        Button(self,text = "查询",width=5,command=self.cxTime).grid(row=1,column=5)
        Button(self,text = "重输",width=5,command=self.clearTime).grid(row=1,column=6)
        for k,v in enumerate(["本周累计：","上周累计：","上月同期：","去年同期：","本月累计：","上月累计："]):
            Label(self,text=v).grid(row=k+2,column=0)
            Label(self,text="----").grid(row=k+2,column=3)
        self.ents0=StringVar()
        Entry(self,width=15,textvariable=self.ents0).grid(row=1+row,column=1,columnspan =2)
        self.ente0=StringVar()
        Entry(self,width=15,textvariable=self.ente0).grid(row=1+row,column=4,columnspan =2)
        self.ents1=StringVar()
        Entry(self,width=15,textvariable=self.ents1).grid(row=2+row,column=1,columnspan =2)
        self.ente1=StringVar()
        Entry(self,width=15,textvariable=self.ente1).grid(row=2+row,column=4,columnspan =2)
        self.ents2=StringVar()
        Entry(self,width=15,textvariable=self.ents2).grid(row=3+row,column=1,columnspan =2)
        self.ente2=StringVar()
        Entry(self,width=15,textvariable=self.ente2).grid(row=3+row,column=4,columnspan =2)
        self.ents3=StringVar()
        Entry(self,width=15,textvariable=self.ents3).grid(row=4+row,column=1,columnspan =2)
        self.ente3=StringVar()
        Entry(self,width=15,textvariable=self.ente3).grid(row=4+row,column=4,columnspan =2)
        self.ents4=StringVar()
        Entry(self,width=15,textvariable=self.ents4).grid(row=5+row,column=1,columnspan =2)
        self.ente4=StringVar()
        Entry(self,width=15,textvariable=self.ente4).grid(row=5+row,column=4,columnspan =2)
        self.ents5=StringVar()
        Entry(self,width=15,textvariable=self.ents5).grid(row=6+row,column=1,columnspan =2)
        self.ente5=StringVar()
        Entry(self,width=15,textvariable=self.ente5).grid(row=6+row,column=4,columnspan =2)



        self.v1,self.v2,self.v3,self.v4,self.v5,self.v6= IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

        Checkbutton(self,text = "本周累计",width=8,command=self.sel0,variable=self.v1).grid(row=7+2,column =1)

        Checkbutton(self,text = "上周累计",width=8,command=self.sel1,variable=self.v2).grid(row=7+2,column =2)

        Checkbutton(self,text = "上月同期",width=8,command=self.sel2,variable=self.v3).grid(row=7+2,column =3)

        Checkbutton(self,text = "去年同期",width=8,command=self.sel3,variable=self.v4).grid(row=7+2,column =4)

        Checkbutton(self,text = "本月累计",width=8,command=self.sel4,variable=self.v5).grid(row=7+2,column =5)

        Checkbutton(self,text = "上月累计",width=8,command=self.sel5,variable=self.v6).grid(row=7+2,column =6)


        for k,v in enumerate(["促销收入：","储值卡消费：","交易次数：","客单价："]):
            Label(self,text = v).grid(row=k+8+2,column = 0,sticky=E )






    def sel0(self):
        if self.v1.get()==1:
            self.ets0=self.ents0.get()
            self.ete0=self.ente0.get()
        else:
            self.ets0=NONE
            self.ete0=NONE
    def sel1(self):
        if self.v2.get()==1:
            self.ets1=self.ents1.get()
            self.ete1=self.ente1.get()
        else:
            self.ets1=NONE
            self.ete1=NONE
    def sel2(self):
        if self.v3.get()==1:
            self.ets2=self.ents2.get()
            self.ete2=self.ente2.get()
        else:
            self.ets2=NONE
            self.ete2=NONE

    def sel3(self):
        if self.v4.get()==1:
            self.ets3=self.ents3.get()
            self.ete3=self.ente3.get()
        else:
            self.ets3=NONE
            self.ete3=NONE
    def sel4(self):
        if self.v5.get()==1:
            self.ets4=self.ents4.get()
            self.ete4=self.ente4.get()
        else:
            self.ets4=NONE
            self.ete4=NONE
    def sel5(self):
        if self.v6.get()==1:
            self.ets5=self.ents5.get()
            self.ete5=self.ente5.get()
        else:
            self.ets5=NONE
            self.ete5=NONE
class about(Frame):
    def __init__(self,master = NONE):
        Frame.__init__(self,master)
        self.root=master
        self.scend()
    def scend(self):
        Label(self,text="关于").pack()
class UI(object):
    def __init__(self,master = NONE):
        self.root = master
        self.root.geometry("800x800")
        self.createPage()
        self.viewData()
    def createPage(self):
        self.viewPage = view(self.root)
        self.fristPage = frist(self.root)
        self.scendPage = scend(self.root)
        self.threePage = three(self.root)
        self.aboutPage = about(self.root)
        menubar = Menu(self.root)
        fm = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='菜单',menu=fm)
        fm.add_command(label='新增', command = self.addData)
        fm.add_command(label='删除', command = self.delData)
        fm.add_command(label='退出', command = self.quit)
        menubar.add_cascade(label='测试', command = self.scendData)
        menubar.add_cascade(label='查询', command = self.threeData)
        menubar.add_cascade(label='关于', command = self.aboutDisp)
        self.root['menu'] = menubar
    def addData(self):
        pass
    def delData(self):
        pass
    def quit(self):
        quit()
    def viewData(self):
        self.viewPage.pack()
        self.fristPage.pack_forget()
        self.scendPage.pack_forget()
        self.threePage.pack_forget()
        self.aboutPage.pack_forget()
    def fristData(self):
        self.viewPage.pack_forget()
        self.fristPage.pack()
        self.scendPage.pack_forget()
        self.threePage.pack_forget()
        self.aboutPage.pack_forget()
    def scendData(self):
        self.viewPage.pack_forget()
        self.fristPage.pack_forget()
        self.scendPage.pack()
        self.threePage.pack_forget()
        self.aboutPage.pack_forget()
    def threeData(self):
        self.viewPage.pack_forget()
        self.fristPage.pack_forget()
        self.scendPage.pack_forget()
        self.threePage.pack()
        self.aboutPage.pack_forget()
    def aboutDisp(self):
        self.viewPage.pack_forget()
        self.fristPage.pack_forget()
        self.scendPage.pack_forget()
        self.threePage.pack_forget()
        self.aboutPage.pack()
UI(root)
root.mainloop()