#超级高端集截图批量重命名器V1.0
#驯龙高手中文维基 - 荣誉出品
#https://howtotrainyourdragon.huijiwiki.com/
#一窗夕月 制作
#使用说明：')
#1、使用前请将图片和本文件放在一个单独文件夹中，目录最好不要有中文；
#2、为了保证安全性，请提前备份这些图片文件；
#衷心祝您使用愉快、编辑顺利！

import os
import re
import tkinter
import tkinter.messagebox
import tkinter.filedialog as filedialog

#GUI
root = tkinter.Tk()
root.title('超高端批量重命名大师3000 - 驯龙高手中文维基专供')
root['height']=250
root['width']=500
varpath = tkinter.StringVar()
varpath.set('')
varhouzhui = tkinter.StringVar()
varhouzhui.set('')
varseason = tkinter.StringVar()
varseason.set('')
varepisode = tkinter.StringVar()
varepisode.set('')

labelpath = tkinter.Label(root,text='图片路径',justify=tkinter.RIGHT,width=80)
labelpath.place(x=10,y=5,width=80,height=20)
entrypath = tkinter.Entry(root,width=200,textvariable=varpath)
entrypath.place(x=100,y=5,width=200,height=20)
labelhouzhui = tkinter.Label(root,text='后缀',justify=tkinter.RIGHT,width=80)
labelhouzhui.place(x=10,y=30,width=80,height=20)
entryhouzhui = tkinter.Entry(root,width=200,textvariable=varhouzhui)
entryhouzhui.place(x=100,y=30,width=200,height=20)
labelseason = tkinter.Label(root,text='季',justify=tkinter.RIGHT,width=80)
labelseason.place(x=10,y=60,width=80,height=20)
entryseason = tkinter.Entry(root,width=200,textvariable=varseason)
entryseason.place(x=100,y=60,width=200,height=20)
labelepisode = tkinter.Label(root,text='集',justify=tkinter.RIGHT,width=80)
labelepisode.place(x=10,y=90,width=80,height=20)
entryepisode = tkinter.Entry(root,width=200,textvariable=varepisode)
entryepisode.place(x=100,y=90,width=200,height=20)


entryhouzhui.insert(0,'png')

def getpath():
    global path
    path = filedialog.askdirectory()
    if path:
        entrypath.insert(0,path)
    else:
        path = entrypath.get()

def getname():
    if path:
        season0 = path[-3]
        episode0 = path[-2]+path[-1]
        entryseason.insert(0,season0)
        entryepisode.insert(0,episode0)
    else:
        tkinter.messagebox.showerroe(title='出现问题',message='未检测到有效路径。')
    
def rename():
    houzhui = entryhouzhui.get()
    season = entryseason.get()
    episode = entryepisode.get()
    path = entrypath.get()
    if path and season and episode and houzhui:
        #字典
        seasonname = {'1':'博克岛的骑手','2':'博克岛的卫士','3':'飞越边界第一季','4':'飞越边界第二季','5':'飞越边界第三季','6':'飞越边界第四季','7':'飞越边界第五季','8':'飞越边界'}
        episodename = {"01":"第一集","02":"第二集","03":"第三集","04":"第四集","05":"第五集","06":"第六集","07":"第七集","08":"第八集","09":"第九集","10":"第十集","11":"第十一集","12":"第十二集","13":"第十三集","14":"第十四集","15":"第十五集","16":"第十六集","17":"第十七集","18":"第十八集","19":"第十九集","20":"第二十集"}
        path = path.replace('\\','/').replace('：',':',1)
        count = 1
        seasoncheck = seasonname[season]
        episodecheck = episodename[episode]
        if seasoncheck == None and episodecheck == None:
            tkinter.messagebox.showerror(title='出现问题',message='季数或集数与现有字典不匹配。')
        else:
            if int(season) >= 3 and int(episode) >= 14:
                      tkinter.messagebox.showerror(title='出现问题',message='季数和集数无法对应，请检查。')
            else:
                for file in os.listdir(path):
                    ji4 = seasonname[season]
                    ji2 = episodename[episode]
                    if count <= 9:
                        os.rename(os.path.join(path,file),os.path.join(path,'TV'+season+episode+'-'+ji4+ji2+'-'+'驯龙高手中文维基-'+'0'+str(count)+"."+houzhui))
                        count+=1
                    else:
                        os.rename(os.path.join(path,file),os.path.join(path,'TV'+season+episode+'-'+ji4+ji2+'-'+'驯龙高手中文维基-'+str(count)+"."+houzhui))
                        count+=1
                tkinter.messagebox.showinfo(title='完成',message='运行完成！')
    else:
        tkinter.messagebox.showerror(title='出现问题',message='信息不全。')

#GUI
buttonStart=tkinter.Button(root,text="选择路径",command=getpath)
buttonStart.place(x=320,y=5,width=80,height=40)
buttonStart=tkinter.Button(root,text="获取季和集",command=getname)
buttonStart.place(x=320,y=50,width=80,height=40)
buttonStart=tkinter.Button(root,text="开始",command=rename)
buttonStart.place(x=320,y=95,width=80,height=40)

labelcontent1 = tkinter.Label(root,text='季数和集数输入阿拉伯数字即可，季数前不必输入TV，集数小于10者需要手动补充0。',justify=tkinter.RIGHT,width=80)
labelcontent1.place(x=5,y=150,width=500,height=15)
labelcontent2 = tkinter.Label(root,text='本程序将一次性将目标文件夹中的所有文件自动命名，请提前做好备份。',justify=tkinter.RIGHT,width=80)
labelcontent2.place(x=5,y=170,width=500,height=15)
labelcontent3 = tkinter.Label(root,text='驯龙高手中文维基 2018年2月8日',justify=tkinter.RIGHT,width=80)
labelcontent3.place(x=5,y=190,width=500,height=15)
labelcontent3 = tkinter.Label(root,text='https://howtotrainyourdragon.huijiwiki.com/',justify=tkinter.RIGHT,width=80)
labelcontent3.place(x=5,y=210,width=500,height=15)

root.mainloop()


