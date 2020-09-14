import tkinter as tk                
import os
import webbrowser
from tkinter import PhotoImage
import subprocess

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        #page names need to be added here
        self.frames = {}
        for F in (StartPage,basicpage,syspage,browserpage,qlinkpage,warrantypage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#5f68c3')
        self.controller = controller
        self.controller.title("Tool")
        self.controller.geometry("450x650+50+10")
        self.controller.resizable(0,0)
        hearingLabel=tk.Label(self,text="IT Assistant",font=("freemono",35,"bold"),foreground='white',background='#5f68c3')
        hearingLabel.pack(pady=25)
        self.controller.iconphoto(False,tk.PhotoImage(file="icons/computer.png"))
        
        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill="both",expand=True)

        #main page buttons
        def ba():
            controller.show_frame("basicpage")

        bai=tk.Button(button_frame,text="System Information",font=("freemono",12,"bold"),relief='raised',foreground='white',background='#5f68c3',borderwidth=6,width=25,height=2,command=ba)
        bai.grid(row=0,column=0,pady=20,padx=95)

        def sy():
            controller.show_frame("syspage")
        
        syp=tk.Button(button_frame,text="System Performance",font=("freemono",12,"bold"),relief='raised',foreground='white',background='#5f68c3',borderwidth=6,width=25,height=2,command=sy)
        syp.grid(row=1,column=0,pady=10)

        def br():
            controller.show_frame("browserpage")
        
        bro=tk.Button(button_frame,text="Browser",font=("freemono",12,"bold"),relief='raised',foreground='white',background='#5f68c3',borderwidth=6,width=25,height=2,command=br)
        bro.grid(row=2,column=0,pady=10)

        def ql():
            controller.show_frame("qlinkpage")
        
        qli=tk.Button(button_frame,text="Quick Links",font=("freemono",12,"bold"),relief='raised',foreground='white',background='#5f68c3',borderwidth=6,width=25,height=2,command=ql)
        qli.grid(row=3,column=0,pady=10)

        def wa():
            controller.show_frame("warrantypage")

        wart=tk.Button(button_frame,text="Warranty",font=("freemono",12,"bold"),relief='raised',foreground='white',background='#5f68c3',borderwidth=6,width=25,height=2,command=wa)
        wart.grid(row=4,column=0,pady=10)
class basicpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="",background='#5f68c3')
        self.controller = controller
        hearingLabel=tk.Label(self,text="Software Information",font=("freemono",25,"bold"),foreground='white',background='#5f68c3')
        hearingLabel.pack(pady=25)

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill="both",expand=True)

        #run
        run=tk.PhotoImage(file="icons/run.png")
        runl=tk.Label(button_frame,image=run,background='white')
        runl.image=run

        #to check windows version
        def win():
            Outputfileobject=os.popen('systeminfo | find "OS Name"')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text=Output,font=("freemono",12,"bold"),foreground='black',background='white')
            Outputfileobject.close()
            Text.after(5000 , lambda: Text.destroy()) 
            Text.place(x=30,y=600)
        prg=tk.PhotoImage(file="icons/version.png")
        prgl=tk.Label(button_frame,image=prg,background='white')
        prgl.place(x=20,y=60)
        prgl.image=prg    
        sym=tk.Label(self,text="Windows\nVersion",font=("freemono",14,'bold'),foreground='black',background='white')
        sym.place(x=120,y=155)

        insts=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=win)
        insts.place(x=270,y=70)

        #to check installed softwares
        def symb():
            Outputfileobject=os.popen('Appwiz.Cpl')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text=Output,font=("Courier",10,"bold"),foreground='#ffffff',background='white')
            Outputfileobject.close()
        prg=tk.PhotoImage(file="icons/programs.png")
        prgl=tk.Label(button_frame,image=prg,background='white')
        prgl.place(x=20,y=160)
        prgl.image=prg
        sym=tk.Label(self,text="Installed \n Softwares",font=("freemono",14,'bold'),foreground='black',background='white')
        sym.place(x=120,y=260)

        insts=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=symb)
        insts.place(x=270,y=175)

        #to check domain information
        def domainb():
            Outputfileobject=os.popen('set user')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text=Output,font=("freemono",12,"bold"),foreground='black',background='white')
            Outputfileobject.close()
            Text.after(5000 , lambda: Text.destroy()) 
            Text.place(x=0,y=560)
        pcp=tk.PhotoImage(file="icons/dom.png")
        pcpl=tk.Label(button_frame,image=pcp,background='white')
        pcpl.place(x=20,y=265)
        pcpl.image=pcp
        
        domain=tk.Label(self,text="Domain\nInformation",foreground='black',background='white',font=("freemono",14,"bold"))
        domain.place(x=120,y=363)

        domr=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=domainb)
        domr.place(x=270,y=277)

        #to check installed patches
        def patchb():
            Top=tk.Toplevel()
            Top.geometry("700x500")
            Top.title("Installed Patches")
            Outputfileobject=os.popen('wmic qfe list brief| find "Update"')
            Output=Outputfileobject.read()
            Text=tk.Label(Top,text="Patch Information:",font=("freemono",12,"bold"),foreground='black')
            tpatt=tk.Label(Top,text=Output,font=("freemono",12,"bold"),foreground='black')
            Outputfileobject.close()
            Text.after(60000, lambda: Text.destroy())
            tpatt.after(60000, lambda: tpatt.destroy())
            Text.place(x=0,y=0)
            tpatt.place(x=60,y=30)

        patp=tk.PhotoImage(file="icons/windows.png")
        patpl=tk.Label(button_frame,image=patp,background='white')
        patpl.place(x=25,y=355)
        patpl.image=patp

        rpat=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=patchb)
        rpat.place(x=270,y=360)
        
        pat=tk.Label(self,text="Patch\n Information",background='white',foreground='black',font=("freemono",14,"bold"))
        pat.place(x=120,y=450)


        def back():
            controller.show_frame("StartPage")
        home=tk.PhotoImage(file="icons/back.png")
        homl=tk.Label(button_frame,image=home,background='white')
        homl.image=home
        bk=tk.Button(button_frame,image=home,foreground="white",background="white",relief='raised',borderwidth=0,command=back)
        bk.place(x=350,y=7)


class syspage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="",background='#5f68c3')
        self.controller = controller
        hearingLabel=tk.Label(self,text="System Performance",font=("freemono",25,"bold"),foreground='white',background='#5f68c3')
        hearingLabel.pack(pady=25)

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill="both",expand=True)

        run=tk.PhotoImage(file="icons/run.png")
        runl=tk.Label(button_frame,image=run,background='white')
        runl.image=run

        #to cleanup c drive
        def winb():
            Outputfileobject=os.popen('external/cleanupdrive.bat')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text="Temp files deleted successfully",font=("freemono",14,"bold"),foreground='black',bg='white')
            Outputfileobject.close()
            Text.after(4000 , lambda: Text.destroy()) 
            Text.place(x=50,y=600)

        prg=tk.PhotoImage(file="icons/tt.png")
        prgl=tk.Label(button_frame,image=prg,background='white')
        prgl.place(x=20,y=50)
        prgl.image=prg
        temp=tk.Label(self,text="Temp \nCleanup ",font=("freemono",14,'bold'),foreground='black',background='white')
        temp.place(x=120,y=160)

        runtemp=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=winb)
        runtemp.place(x=270,y=70)

        #to update gp policy
        def gpupdateb():
            Outputfileobject=os.popen('gpupdate')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text="GP Policy has been updated successfully",font=("freemono",14,"bold"),foreground='black',background='white')
            Outputfileobject.close()
            Text.after(5000, lambda: Text.destroy()) 
            Text.place(x=30,y=600)

        pcp=tk.PhotoImage(file="icons/gpudt.png")
        pcpl=tk.Label(button_frame,image=pcp,background='white')
        pcpl.place(x=0,y=150)
        pcpl.image=pcp

        domain=tk.Label(self,text="Group Policy\n Update",foreground='black',background='white',font=("freemono",14,"bold"))
        domain.place(x=105,y=270)

        gpb=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=gpupdateb)
        gpb.place(x=270,y=175)

        def back():
            controller.show_frame("StartPage")
        home=tk.PhotoImage(file="icons/back.png")
        homl=tk.Label(button_frame,image=home,background='white')
        homl.image=home
        bk=tk.Button(button_frame,image=home,foreground="white",background="white",relief='raised',borderwidth=0,command=back)
        bk.place(x=350,y=7)

class browserpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="",background='#5f68c3')
        self.controller = controller
        hearingLabel=tk.Label(self,text="Browser Setting",font=("freemono",25,"bold"),foreground='white',background='#5f68c3')
        hearingLabel.pack(pady=25)

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill="both",expand=True)

        run=tk.PhotoImage(file="icons/run.png")
        runl=tk.Label(button_frame,image=run,background='white')
        runl.image=run

        #IE cleanup
        def cleanb():
            Outputfileobject=os.popen('ipconfig/flushdns')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text="Internet Explorer Cleaned",font=("freemono",14,"bold"),foreground='black',background='white')
            Outputfileobject.close()
            Text.after(5000 , lambda: Text.destroy()) 
            Text.place(x=55,y=600)
        iero=tk.PhotoImage(file="icons/internet-explorer.png")
        ierol=tk.Label(button_frame,image=iero,background='white')
        ierol.place(x=20,y=60)
        ierol.image=iero

        iec=tk.Label(self,text="IE Cleanup",font=("freemono",14,'bold'),foreground='black',background='white')
        iec.place(x=120,y=170)

        ieclean=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=cleanb)
        ieclean.place(x=270,y=67)

        #IE reset
        def resetb():
            Outputfileobject=os.popen('RunDll32.exe InetCpl.cpl,ResetIEtoDefaults')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text="IE settings changed to default",font=("freemono",14,"bold"),foreground='black',background='white')
            Outputfileobject.close()
            Text.after(5000 , lambda: Text.destroy()) 
            Text.place(x=50,y=600)

        ier=tk.PhotoImage(file="icons/internet-explorer.png")
        ierl=tk.Label(button_frame,image=ier,background='white')
        ierl.place(x=20,y=170)
        ierl.image=ier

        domain=tk.Label(self,text="IE Reset",foreground='black',background='white',font=("freemono",14,"bold"))
        domain.place(x=120,y=280)

        domr=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=resetb)
        domr.place(x=270,y=175)

        #chrome cleanup
        def ccb():
            Outputfileobject=os.popen('external/clean.bat')
            Output=Outputfileobject.read()
            Text=tk.Label(self,text="Chrome Browser Cleaned",font=("freemono",14,"bold"),foreground='black',background='white')
            Outputfileobject.close()
            Text.after(5000 , lambda: Text.destroy()) 
            Text.place(x=50,y=600)

        chp=tk.PhotoImage(file="icons/chrbs.png")
        chpl=tk.Label(button_frame,image=chp,background='white')
        chpl.place(x=30,y=290)
        chpl.image=chp

        
        rpat=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=ccb)
        rpat.place(x=270,y=293)
        
        pat=tk.Label(self,text="Chrome\n Cleanup",background='white',foreground='black',font=("freemono",14,"bold"))
        pat.place(x=120,y=390)

        def back():
            controller.show_frame("StartPage")
        home=tk.PhotoImage(file="icons/back.png")
        homl=tk.Label(button_frame,image=home,background='white')
        homl.image=home
        bk=tk.Button(button_frame,image=home,foreground="white",background="white",relief='raised',borderwidth=0,command=back)
        bk.place(x=350,y=7)


class qlinkpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="",background='#5f68c3')
        self.controller = controller
        hearingLabel=tk.Label(self,text="Quick Links",font=("freemono",25,"bold"),foreground='white',background='#5f68c3')
        hearingLabel.pack(pady=25)

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill="both",expand=True)

        #run
        run=tk.PhotoImage(file="icons/run.png")
        runl=tk.Label(button_frame,image=run,background='white')
        runl.image=run

        #open google
        def ggl():
            url='https://google.com'
            webbrowser.get().open(url)

        goo=tk.PhotoImage(file="icons/google.png")
        gool=tk.Label(button_frame,image=goo,background='white')
        gool.place(x=20,y=60)
        gool.image=goo
        
        google=tk.Label(self,text="Google",font=("freemono",14,'bold'),foreground='black',background='white')
        google.place(x=120,y=170)

        
        rgoo=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=ggl)
        rgoo.place(x=270,y=70)

        #open twitter
        def twt():
            url='https://twitter.com'
            webbrowser.get().open(url)
        
        pwsy=tk.PhotoImage(file="icons/twitter.png")
        pwsyl=tk.Label(button_frame,image=pwsy,background='white')
        pwsyl.place(x=20,y=144)
        pwsyl.image=pwsy        
        
        spw=tk.Label(self,text="Twitter",foreground='black',background='white',font=("freemono",14,"bold"))
        spw.place(x=120,y=250)

        sypw=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=twt)
        sypw.place(x=270,y=164)

        #yt
        def yt():
            url='https://youtube.com'
            webbrowser.get().open(url)


        pcp=tk.PhotoImage(file="icons/youtube.png")
        pcpl=tk.Label(button_frame,image=pcp,background='white')
        pcpl.place(x=20,y=250)
        pcpl.image=pcp

        newl=tk.Label(self,text="YouTube",foreground='black',background='white',font=("freemono",14,"bold"))
        newl.place(x=120,y=355)

        rnewl=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=yt)
        rnewl.place(x=270,y=265)

        #mail
        def mail():
            url='https:/gmail.com'
            webbrowser.get().open(url)
        bitli=tk.PhotoImage(file="icons/gmail.png")
        bitlil=tk.Label(button_frame,image=bitli,background='white')
        bitlil.place(x=20,y=345)
        bitlil.image=bitli

        bitl=tk.Label(self,text="Gmail",foreground='black',background='white',font=("freemono",14,"bold"))
        bitl.place(x=125,y=455)

        rnewl=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=mail)
        rnewl.place(x=270,y=355)

        
        def back():
            controller.show_frame("StartPage")
        home=tk.PhotoImage(file="icons/back.png")
        homl=tk.Label(button_frame,image=home,background='white')
        homl.image=home
        bk=tk.Button(button_frame,image=home,foreground="white",background="white",relief='raised',borderwidth=0,command=back)
        bk.place(x=350,y=7)

class warrantypage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="",background='#5f68c3')
        self.controller = controller
        hearingLabel=tk.Label(self,text="Warranty",font=("freemono",25,"bold"),foreground='white',background='#5f68c3')
        hearingLabel.pack(pady=25)

        button_frame=tk.Frame(self,bg='white')
        button_frame.pack(fill="both",expand=True)

        #run
        run=tk.PhotoImage(file="icons/run.png")
        runl=tk.Label(button_frame,image=run,background='white')
        runl.image=run

        #hp
        def hpw():
            Top=tk.Toplevel()
            Top.geometry("500x500")
            Top.title("HP Warranty Check")
            tlb=tk.Label(Top,text="Enter Product Number:",font=("freemono",10,"bold"),foreground='black')
            tlb.place(x=0,y=0)
            info=tk.Label(Top,text="Product Number is printed on a label adhered to the underside of the laptop.",font=("freemono",10,"bold"),foreground='red')
            info.place(x=0,y=20)
            e=tk.Entry(Top,width=50)
            e.place(x=50,y=40)
            photo=tk.PhotoImage(file="icons/hp.png")
            photol=tk.Label(Top,image=photo,background='white')
            photol.place(x=50,y=150)
            photol.image=photo
            def page():
                a=e.get()
                serial=subprocess.check_output('wmic bios get serialnumber').decode().split('\n')[1].strip()
                url=("https://support.hp.com/us-en/warrantyresult?&sku="+a+"&serialNo="+serial)
                webbrowser.get().open(url)
            submit=tk.Button(Top,text="Check warranty",font=("freemono",12,"bold"),relief='raised',foreground='white',background='#5f68c3',borderwidth=3,width=15,height=1,command=page)
            submit.place(x=130,y=60)
            
         

        pcp=tk.PhotoImage(file="icons/hplogo.png")
        pcpl=tk.Label(button_frame,image=pcp,background='white')
        pcpl.place(x=20,y=60)
        pcpl.image=pcp

        rnewl=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=hpw)
        rnewl.place(x=120,y=70)

        def delw():
            serial=subprocess.check_output('wmic bios get serialnumber').decode().split('\n')[1].strip()
            url=("https://www.dell.com/support/home/en-in/product-support/servicetag/"+serial)
            webbrowser.get().open(url)


        dell=tk.PhotoImage(file="icons/dell.png")
        delll=tk.Label(button_frame,image=dell,background='white')
        delll.place(x=20,y=160)
        delll.image=dell

        delw=tk.Button(button_frame,image=run,foreground="white",background="white",relief='raised',borderwidth=0,command=delw)
        delw.place(x=120,y=175)


        def back():
            controller.show_frame("StartPage")
        home=tk.PhotoImage(file="icons/back.png")
        homl=tk.Label(button_frame,image=home,background='white')
        homl.image=home
        bk=tk.Button(button_frame,image=home,foreground="white",background="white",relief='raised',borderwidth=0,command=back)
        bk.place(x=350,y=7)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()