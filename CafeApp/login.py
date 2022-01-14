import getpass
import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
from PIL.FontFile import WIDTH



class Login:

    def __init__(self,root):
        self.hesapTl =0
        self.root=root
        self.root.title("Giriş")
        self.root.geometry("850x700+500+100")

        self.a=[]
        self.hesapTl=[]
        self.root.resizable(False,False)
        self.kullaniciTipi()


    def kullaniciTipi(self):
        Frame_login = Frame(self.root, bg="orange")
        Frame_login.place(x=0, y=0, height=700, width=850)
        self.img1=PhotoImage(file="images/img_5.png")
        self.img2 = PhotoImage(file="images/kullanıcı.png")
        self.img3 = PhotoImage(file="images/admin.png")
        label=Label(Frame_login,image=self.img1)
        label.place(x=0,y=0,height=700,width=850)
        kullaniciButonu=Button(Frame_login,text="Kullanıcı",bg="orange",fg="black",image=self.img2,compound="top",font=("Goudy old style",40,"bold"),command=self.loginform)
        kullaniciButonu.place(x=100,y=200,height=300,width=300)
        adminButonu = Button(Frame_login, bg="orange", fg="black",image=self.img3,compound="top",text="Admin",font=("Goudy old style",40,"bold"),command=self.adminform)
        adminButonu.place(x=450, y=200, height=300, width=300)

    def adminform(self):
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, height=700, width=850)

        self.img = PhotoImage(file="images/img.png")
        self.img2=PhotoImage(file="images/cikis.png")
        img = Label(Frame_login, image=self.img, bg="black").place(height=700, width=450)

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=480, y=100, height=700, width=400)

        label2 = Label(frame_input, text="Admin email", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
        label2.place(x=30, y=95)

        self.email_txt = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
        self.email_txt.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
        label3.place(x=30, y=195)

        self.passwordlogin = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
        self.passwordlogin.place(x=30, y=245, width=270, height=35)

        buton2 = Button(frame_input, text="Login", command=self.adminLogin, cursor="hand2", font=("calibri", 10),
                        bg="orangered", fg="white", bd=0, width=15, height=1)
        buton2.place(x=110, y=340)

        buton_cikis = Button(frame_input, font=("Arial", 30, "bold"), image=self.img2,
                             compound="center", fg="white", bg="white", borderwidth=0, activebackground="white",
                             command=self.kullaniciTipi)
        buton_cikis.place(x=275, y=520, height=50, width=50)

    def loginform(self):
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=850)

        self.img=PhotoImage(file="images/img.png")
        img=Label(Frame_login,image=self.img,bg="black").place(height=700,width=450)
        self.img2 = PhotoImage(file="images/cikis.png")


        frame_input=Frame(self.root,bg="white")
        frame_input.place(x=480,y=100,height=700,width=400)



        label2=Label(frame_input,text="E-mail",font=("Goudy old style",20,"bold"),fg="orangered",bg="white")
        label2.place(x=30,y=95)

        self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg="lightgray")
        self.email_txt.place(x=30,y=145,width=270,height=35)

        label3 = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
        label3.place(x=30, y=195)

        self.passwordlogin = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
        self.passwordlogin.place(x=30, y=245, width=270, height=35)

        buton2 = Button(frame_input, text="Login",command=self.login, cursor="hand2", font=("calibri", 10), bg="orangered",fg="white", bd=0,width=15,height=1)
        buton2.place(x=110, y=340)

        buton3 = Button(frame_input, text="Not registered?Register",command=self.registerform, cursor="hand2", font=("calibri", 10), bg="white", fg="black", bd=0)
        buton3.place(x=100, y=390)

        buton_cikis = Button(frame_input, font=("Arial", 30, "bold"), image=self.img2,
                             compound="center", fg="white", bg="white", borderwidth=0, activebackground="white",
                             command=self.kullaniciTipi)
        buton_cikis.place(x=275, y=520, height=50, width=50)

    def adminLogin(self):
        if self.email_txt.get()=="" or self.passwordlogin.get()=="":
            messagebox.showerror("Error","Tüm Alanları Doldurunuz!",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="dgsgk102002os",database="pythonproject")
                cur=con.cursor()
                cur.execute("select * from admin where email=%s and password=%s",(self.email_txt.get(),self.passwordlogin.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Böyle bir hesap yok!",parent=self.root)
                else:

                    self.adminpanel()
                    con.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error Due to: {str(e)}",parent=self.root)

    def adminpanel(self):
        adminPanel=Frame(self.root,bg="white")
        adminPanel.place(x=0, y=0, height=700, width=850)
        self.img1 = PhotoImage(file="images/img_1.png")
        self.img2 = PhotoImage(file="images/img_2.png")
        self.img3 = PhotoImage(file="images/img_3.png")
        self.img4 = PhotoImage(file="images/img_4.png")
        self.img5 = PhotoImage(file="images/add.png")
        self.img6 = PhotoImage(file="images/edit.png")
        self.img7 = PhotoImage(file="images/delete.png")
        self.img8 = PhotoImage(file="images/cikis.png")
        self.img9 = PhotoImage(file="images/pngwing.com (3) (1).png")




        notebook=ttk.Notebook(adminPanel)

        tab1=Frame(notebook)
        tab2=Frame(notebook)

        notebook.add(tab1,text="Menü Düzenle")
        notebook.add(tab2,text="Kullanıcı Düzenle")
        notebook.place(x=0, y=0, height=700, width=850)

        self.duzenFrame=Frame(tab1,bg="black")
        self.duzenFrame.place(x=25,y=100,height=600,width=800)

        editFrame=Frame(self.duzenFrame,bg="white")
        editFrame.place(x=0,y=0,height=600,width=400)

        self.ürünId = Label(editFrame, bg="lightgray")
        self.ürünId.place(x=145, y=50, height=30, width=200)

        ürünIdLabel = Label(editFrame, text="Ürün Id", bg="white", font=25)
        ürünIdLabel.place(x=45, y=50)


        ürünAdLabel=Label(editFrame,text="Ürün Adı",bg="white",font=25)
        ürünAdLabel.place(x=45,y=150)


        self.ürünAd=Entry(editFrame,bg="lightgray")
        self.ürünAd.place(x=145,y=150,height=30,width=200)

        ürünFiyatLabel = Label(editFrame, text="Ürün Fiyatı", bg="white",font=25)
        ürünFiyatLabel.place(x=45, y=250)

        self.ürünFiyat = Entry(editFrame, bg="lightgray")
        self.ürünFiyat.place(x=145, y=250, height=30, width=200)

        ekle=Button(editFrame,bg="white",image=self.img5,borderwidth=0,command=self.ekle)
        ekle.place(x=75,y=400,height=50,width=50)

        duzenle = Button(editFrame, bg="white",image=self.img6,borderwidth=0,command=self.edit)
        duzenle.place(x=175, y=400, height=55, width=55)
        
        sil = Button(editFrame, bg="white",image=self.img7,borderwidth=0,command=self.delete)
        sil.place(x=275, y=400, height=50, width=50)

        self.buton_hotdrinks = Button(tab1, text="Sıcak İçecekler", font=("Arial", 15, "bold"), image=self.img1,
                                 compound="center", fg="white", command=self.adminhotdrinks)
        self.buton_hotdrinks.place(x=50, y=25, height=50, width=150)

        self.buton_cooldrinks = Button(tab1, text="Soğuk İçecekler", font=("Arial", 15, "bold"), image=self.img4,
                                  compound="center", fg="white", command=self.admincolddrinks)
        self.buton_cooldrinks.place(x=250, y=25, height=50, width=150)

        self.buton_anayemek = Button(tab1, text="Ana Yemekler", font=("Arial", 15, "bold"), image=self.img2,
                                compound="center",
                                fg="white", command=self.adminanayemekler)
        self.buton_anayemek.place(x=450, y=25, height=50, width=150)

        self.buton_arayemek = Button(tab1, text="Ara Yemekler", font=("Arial", 15, "bold"), image=self.img3,
                                compound="center", fg="white", command=self.adminarayemekler)
        self.buton_arayemek.place(x=650, y=25, height=50, width=150)

        buton_cikis = Button(editFrame, font=("Arial", 30, "bold"), image=self.img8,
                             compound="center", fg="white", bg="white", borderwidth=0, activebackground="white",
                             command=self.kullaniciTipi)
        buton_cikis.place(x=300, y=500, height=50, width=50)
        #--------------------------------------------------------------------------------------------------------------

        self.duzenFrame1 = Frame(tab2, bg="black")
        self.duzenFrame1.place(x=5, y=75, height=625, width=850)

        editFrame1 = Frame(self.duzenFrame1, bg="white")
        editFrame1.place(x=0, y=0, height=625, width=320)

        self.kullanicilar = Button(tab2, text="Kullanıcıları Görüntüle ", font=("Arial", 15, "bold"), image=self.img9,
                                     compound="left",
                                     fg="black", command=self.kullaniciTablo,borderwidth=0)
        self.kullanicilar.place(x=300, y=5, height=50, width=275)

        self.kullaniciId = Label(editFrame1, bg="lightgray")
        self.kullaniciId.place(x=110, y=50, height=30, width=200)
        kullaniciIdLabel = Label(editFrame1, text="Kullanıcı Id", bg="white", font=25)
        kullaniciIdLabel.place(x=10, y=50)

        kullaniciAdLabel = Label(editFrame1, text="Username", bg="white", font=25)
        kullaniciAdLabel.place(x=10, y=125)
        self.kullaniciAd = Entry(editFrame1, bg="lightgray")
        self.kullaniciAd.place(x=110, y=125, height=30, width=200)

        kullaniciMailLabel = Label(editFrame1, text="E-mail", bg="white", font=25)
        kullaniciMailLabel.place(x=10, y=200)
        self.kullaniciMail = Entry(editFrame1, bg="lightgray")
        self.kullaniciMail.place(x=110, y=200, height=30, width=200)

        passwordLabel = Label(editFrame1, text="Password", bg="white", font=25)
        passwordLabel.place(x=10, y=275)
        self.password1 = Entry(editFrame1, bg="lightgray")
        self.password1.place(x=110, y=275, height=30, width=200)

        kampanya1Label = Label(editFrame1, text="Kampanya-1", bg="white", font=25)
        kampanya1Label.place(x=10, y=350)
        self.kampanya1 = Entry(editFrame1, bg="lightgray")
        self.kampanya1.place(x=110, y=350, height=30, width=200)

        kampanya2Label = Label(editFrame1, text="Kampanya-2", bg="white", font=25)
        kampanya2Label.place(x=10, y=425)
        self.kampanya2 = Entry(editFrame1, bg="lightgray")
        self.kampanya2.place(x=110, y=425, height=30, width=200)

        ekle1 = Button(editFrame1, bg="white", image=self.img5, borderwidth=0, command=self.ekle1)
        ekle1.place(x=25, y=475, height=50, width=50)

        duzenle1 = Button(editFrame1, bg="white", image=self.img6, borderwidth=0, command=self.edit1)
        duzenle1.place(x=125, y=475, height=55, width=55)

        sil1 = Button(editFrame1, bg="white", image=self.img7, borderwidth=0, command=self.delete1)
        sil1.place(x=225, y=475, height=50, width=50)

        buton_cikis = Button(editFrame1, font=("Arial", 30, "bold"), image=self.img8,
                             compound="center", fg="white", bg="white", borderwidth=0, activebackground="white",
                             command=self.kullaniciTipi)
        buton_cikis.place(x=250, y=550, height=50, width=50)





    def edit(self):
        if self.ürünAd.get() == "" or self.ürünFiyat.get() == "":
            messagebox.showerror("Error", "Tüm Alanları Doldurunuz!", parent=self.root)

        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os",
                                              database="pythonproject")
                cur = con.cursor()
                value = self.ürünId.cget("text")
                if self.colddrinks_click:
                    query = "SELECT * FROM sogukicecekler1 WHERE id=%s"
                    datasql = "update sogukicecekler1 set ürünAd=%s ,ürünFiyat=%s where id=%s"
                    refresh = "SELECT * FROM sogukicecekler1"
                elif self.hotdrinks_click:
                    query = "SELECT * FROM sicakicecekler WHERE id=%s"
                    datasql = "update sicakicecekler set ürünAd=%s, ürünFiyat=%s where id=%s"
                    refresh = "SELECT * FROM sicakicecekler"
                elif self.anayemekler_click:
                    query = "SELECT * FROM anayemekler WHERE id=%s"
                    datasql ="update anayemekler set ürünAd=%s ,ürünFiyat=%s where id=%s"
                    refresh = "SELECT * FROM anayemekler"
                elif self.arayemekler_click:
                    query = "SELECT * FROM arayemekler WHERE id=%s"
                    datasql = "update arayemekler set ürünAd=%s, ürünFiyat=%s where id=%s"
                    refresh = "SELECT * FROM arayemekler"
                else:
                    messagebox.showerror("Error", "Lütfen Data Seçiniz")

                cur.execute(query, (value,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Ürün Yok", parent=self.root)
                else:

                    cur.execute(datasql,(self.ürünAd.get(),self.ürünFiyat.get(),self.ürünId.cget("text"),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Edit Başarılı", parent=self.root)
                    self.refresh(refresh)
            except IOError as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}")




    def delete(self):
        if self.ürünAd.get() == "" or self.ürünFiyat.get() == "":
            messagebox.showerror("Error", "Tüm Alanları Doldurunuz!", parent=self.root)

        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os",
                                              database="pythonproject")
                cur = con.cursor()
                value = self.ürünAd.get()
                if self.colddrinks_click:
                    query = "SELECT * FROM sogukicecekler1 WHERE ürünAd=%s"
                    datasql = "DELETE FROM sogukicecekler1 where id=%s"
                    refresh = "SELECT * FROM sogukicecekler1"
                elif self.hotdrinks_click:
                    query = "SELECT * FROM sicakicecekler WHERE ürünAd=%s"
                    datasql = "DELETE FROM sicakicecekler where id=%s"
                    refresh = "SELECT * FROM sicakicecekler"
                elif self.anayemekler_click:
                    query = "SELECT * FROM anayemekler WHERE ürünAd=%s"
                    datasql = "DELETE FROM anayemekler where id=%s"
                    refresh = "SELECT * FROM anayemekler"
                elif self.arayemekler_click:
                    query = "SELECT * FROM arayemekler WHERE ürünAd=%s"
                    datasql = "DELETE FROM arayemekler where id=%s"
                    refresh = "SELECT * FROM arayemekler"
                else:
                    messagebox.showerror("Error", "Lütfen Data Seçiniz")

                cur.execute(query, (value,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Ürün Yok", parent=self.root)
                else:

                    cur.execute(datasql,(self.ürünId.cget("text"),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Silme İşlemi Başarılı", parent=self.root)
                    self.refresh(refresh)
            except IOError as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}")

    def ekle(self):


        if self.ürünAd.get()=="" or self.ürünFiyat.get()=="":
            messagebox.showerror("Error","Tüm Alanları Doldurunuz!",parent=self.root)

        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os", database="pythonproject")
                cur = con.cursor()
                value=self.ürünAd.get()
                if self.colddrinks_click:
                    query = "SELECT * FROM sogukicecekler1 WHERE ürünAd=%s"
                    datasql="insert into sogukicecekler1 (ürünAd,ürünFiyat) values(%s,%s)"
                    refresh="SELECT * FROM sogukicecekler1"
                elif self.hotdrinks_click:
                    query = "SELECT * FROM sicakicecekler WHERE ürünAd=%s"
                    datasql = "insert into sicakicecekler (ürünAd,ürünFiyat) values(%s,%s)"
                    refresh = "SELECT * FROM sicakicecekler"
                elif self.anayemekler_click:
                    query = "SELECT * FROM anayemekler WHERE ürünAd=%s"
                    datasql = "insert into anayemekler (ürünAd,ürünFiyat) values(%s,%s)"
                    refresh = "SELECT * FROM anayemekler"
                elif self.arayemekler_click:
                    query = "SELECT * FROM arayemekler WHERE ürünAd=%s"
                    datasql = "insert into arayemekler (ürünAd,ürünFiyat) values(%s,%s)"
                    refresh = "SELECT * FROM arayemekler"
                else:
                    messagebox.showerror("Error","Lütfen Data Seçiniz!")


                cur.execute(query,(value,))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Bu Ürün Zaten Bulunmaktadır!",parent=self.root)
                else:

                    cur.execute(datasql,(self.ürünAd.get(),self.ürünFiyat.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Ekleme Başarılı!",parent=self.root)
                    self.refresh(refresh)
            except IOError as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}")

    def edit1(self):
        if self.kullaniciAd.get() == "" or self.kullaniciAd.get() == "" or self.kullaniciMail.get() == "" or self.password1.get() == ""\
                or self.kampanya1.get() == ""or self.kampanya2.get() == "":
            messagebox.showerror("Error", "Tüm Alanları Doldurunuz!", parent=self.root)

        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os",
                                              database="pythonproject")
                cur = con.cursor()
                value = self.kullaniciId.cget("text")


                cur.execute("SELECT * FROM kullanicilar WHERE id=%s", (value,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Ürün Yok", parent=self.root)
                else:

                    cur.execute("update kullanicilar set username=%s, email=%s, password=%s, girisKampanyası=%s, 2siparise1siparis=%s where id=%s",(self.kullaniciAd.get(),self.kullaniciMail.get(),
                                                                                                                                                    self.password1.get(),self.kampanya1.get(),self.kampanya2.get(),self.kullaniciId.cget("text"),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Edit Başarılı!", parent=self.root)
                    self.refresKullaniciAdmin()
            except IOError as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}")




    def delete1(self):
        if self.kullaniciAd.get() == "" or self.kullaniciAd.get() == "" or self.kullaniciMail.get() == "" or self.password1.get() == "" \
                or self.kampanya1.get() == "" or self.kampanya2.get() == "":
            messagebox.showerror("Error", "Tüm Alanları Doldurunuz!", parent=self.root)

        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os",
                                              database="pythonproject")
                cur = con.cursor()
                value = self.kullaniciMail.get()

                cur.execute("SELECT * FROM kullanicilar WHERE email=%s", (value,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Ürün Yok", parent=self.root)
                else:

                    cur.execute("DELETE FROM kullanicilar where id=%s",(self.kullaniciId.cget("text"),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Silme Başarılı!", parent=self.root)
                    self.refresKullaniciAdmin()
            except IOError as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}")

    def ekle1(self):

        if self.kullaniciAd.get() == "" or self.kullaniciAd.get() == "" or self.kullaniciMail.get() == "" or self.password1.get() == "" \
                or self.kampanya1.get() == "" or self.kampanya2.get() == "":
            messagebox.showerror("Error","Tüm Alanları Doldurunuz!",parent=self.root)

        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os", database="pythonproject")
                cur = con.cursor()
                value=self.kullaniciMail.get()

                cur.execute("SELECT * FROM kullanicilar WHERE email=%s",(value,))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
                else:

                    cur.execute("insert into kullanicilar (username,email,password,girisKampanyası,2siparise1siparis) values(%s,%s,%s,%s,%s)",
                                (self.kullaniciAd.get(),self.kullaniciMail.get(),self.password1.get(),self.kampanya1.get(),self.kampanya2.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Ekleme Başarılı!",parent=self.root)
                    self.refresKullaniciAdmin()
            except IOError as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}")


    def refresh(self,a):
        self.editekrani(a)
    def refresKullaniciAdmin(self):
        self.kullaniciTablo()

    def login(self):
        if self.email_txt.get()=="" or self.passwordlogin.get()=="":
            messagebox.showerror("Error","Tüm Alanları Doldurunuz!",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="dgsgk102002os",database="pythonproject")
                cur=con.cursor()
                cur.execute("select * from kullanicilar where email=%s and password=%s",(self.email_txt.get(),self.passwordlogin.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Böyle Bir Hesap Bulunamadı!",parent=self.root)
                else:

                    self.appscreen()
                    con.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error Due to: {str(e)}",parent=self.root)

    def registerform(self):
        Frame_regiter = Frame(self.root, bg="white")
        Frame_regiter.place(x=0, y=0, height=700, width=1366)

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=120, y=130, height=450, width=630)

        label1 = Label(frame_input, text="Register Here", font=("impact", 32, "bold"), fg="black", bg="white")
        label1.place(x=45, y=20)

        label2 = Label(frame_input, text="Username", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
        label2.place(x=30, y=95)

        self.username = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
        self.username.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
        label3.place(x=30, y=195)

        self.password = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
        self.password.place(x=30, y=245, width=270, height=35)

        label4 = Label(frame_input, text="Email", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
        label4.place(x=330, y=95)

        self.email = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
        self.email.place(x=330, y=145, width=270, height=35)

        label5 = Label(frame_input, text="Confirm Password", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
        label5.place(x=330, y=195)

        self.confirmpass = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
        self.confirmpass.place(x=330, y=245, width=270, height=35)

        buton1 = Button(frame_input, text="Register",command=self.register,cursor="hand2", font=("times new roman", 15), bg="orangered",
                        fg="white", bd=0,width=15,height=1)
        buton1.place(x=220, y=340)

        buton2 = Button(frame_input, text="Already Registered?Login", command=self.loginform, cursor="hand2", font=("calibri", 10),
                        bg="white", fg="black", bd=0)
        buton2.place(x=235, y=390)

    def register(self):
        if self.email.get()=="" or self.password.get()=="" or self.username.get()=="" or self.confirmpass.get()=="":
            messagebox.showerror("Error","Tüm Alanları Doldurunuz!",parent=self.root)
        elif self.password.get()!=self.confirmpass.get():
            messagebox.showerror("Error","Password ve Confirm Password Aynı Olmalı!")
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os", database="pythonproject")
                cur = con.cursor()
                value=self.email.get()
                query="SELECT * FROM kullanicilar WHERE email=%s"
                cur.execute(query,(value,))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Bu Mail Zaten Mevcut, Başka Mail Deneyiniz!",parent=self.root)
                else:
                    cur.execute("insert into kullanicilar (username,email,password,confirmpassword) values(%s,%s,%s,%s)",(self.username.get(),self.email.get(),self.password.get(),self.confirmpass.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Kayıt Başarılı!",parent=self.root)
            except IOError as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}")

    def appscreen(self):


        Frame_main = Frame(self.root, bg="white")
        Frame_main.place(x=0, y=0, height=700, width=1366)

        frame_top = Frame(self.root, bg="orange")
        frame_top.place(height=60, width=1000)

        frame_menu = Frame(self.root, bg="black")
        frame_menu.place(x=25,y=100,height=600, width=800)
        self.img1 = PhotoImage(file="images/img_1.png")
        self.img2 = PhotoImage(file="images/img_2.png")
        self.img3 = PhotoImage(file="images/img_3.png")
        self.img4 = PhotoImage(file="images/img_4.png")
        self.img5 = PhotoImage(file="images/shopping_basket (1).png")
        self.img6 = PhotoImage(file="images/pngwing.com (3) (1).png")
        self.img7 = PhotoImage(file="images/cikis.png")

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os",
                                          database="pythonproject")
            cur = con.cursor()
            sql = ("SELECT username FROM kullanicilar where email='"+str(self.email_txt.get())+"'")
            cur.execute(sql)
            rows = cur.fetchone()
            person=rows[0]
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.root)
            person=None



        buton_kisi = Button(frame_top, text=person, font=("impact", 20, "bold"), fg="black", bg="orange",
                       image=self.img6, compound="left",activebackground="orange",borderwidth=0)
        buton_kisi.place(x=25, y=5)

        buton_sepetim = Button(frame_top, font=("Arial", 30, "bold"), image=self.img5,
                                 compound="center", fg="white",bg="orange",borderwidth=0,activebackground="orange",command=self.sepetim)
        buton_sepetim.place(x=400, y=5, height=50, width=50)

        buton_cikis = Button(frame_top, font=("Arial", 30, "bold"), image=self.img7,
                               compound="center", fg="white", bg="orange", borderwidth=0, activebackground="orange",
                               command=self.cikis)
        buton_cikis.place(x=780, y=5, height=50, width=50)

        buton_hotdrinks = Button(frame_menu, text="Sıcak İçecekler", font=("Arial", 30, "bold"), image=self.img1,
                                 compound="center", fg="white",command=self.hotdrinks)
        buton_hotdrinks.place(x=50, y=50, height=200, width=300)

        buton_cooldrinks = Button(frame_menu, text="Soğuk İçecekler", font=("Arial", 30, "bold"), image=self.img4,
                                  compound="center", fg="white",command=self.colddrinks)
        buton_cooldrinks.place(x=50, y=350, height=200, width=300)

        buton_anayemek = Button(frame_menu, text="Ana Yemek", font=("Arial", 30, "bold"), image=self.img2, compound="center",
                                fg="white",command=self.anayemekler)
        buton_anayemek.place(x=450, y=50, height=200, width=300)

        buton_arayemek = Button(frame_menu, text="Ara Sıcaklar", font=("Arial", 30, "bold"), image=self.img3,
                                compound="center", fg="white",command=self.arayemekler)
        buton_arayemek.place(x=450, y=350, height=200, width=300)



    def hotdrinks(self):
        self.secenekekrani("SELECT ürünAd,ürünFiyat FROM sicakicecekler")
    def colddrinks(self):
        self.secenekekrani("SELECT ürünAd,ürünFiyat FROM sogukicecekler1")
    def anayemekler(self):
        self.secenekekrani("SELECT ürünAd,ürünFiyat FROM anayemekler")
    def arayemekler(self):
        self.secenekekrani("SELECT ürünAd,ürünFiyat FROM arayemekler")

    def adminhotdrinks(self):
        self.editekrani("SELECT * FROM sicakicecekler")
        self.hotdrinks_click=True
        self.colddrinks_click = False
        self.anayemekler_click = False
        self.arayemekler_click = False

    def admincolddrinks(self):
        self.editekrani("SELECT * FROM sogukicecekler1")
        self.hotdrinks_click = False
        self.colddrinks_click = True
        self.anayemekler_click = False
        self.arayemekler_click = False
    def adminanayemekler(self):
        self.editekrani("SELECT * FROM anayemekler")
        self.hotdrinks_click = False
        self.colddrinks_click = False
        self.anayemekler_click = True
        self.arayemekler_click = False
    def adminarayemekler(self):
        self.editekrani("SELECT * FROM arayemekler")
        self.hotdrinks_click = False
        self.colddrinks_click = False
        self.anayemekler_click = False
        self.arayemekler_click = True

    def kullaniciTablo(self):
        con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os", database="pythonproject")
        cur = con.cursor()
        sql = "SELECT id,username,email,password,girisKampanyası,2siparise1siparis FROM kullanicilar"
        cur.execute(sql)
        rows = cur.fetchall()
        total = cur.rowcount

        self.tv = ttk.Treeview(self.duzenFrame1, columns=(1, 2, 3,4,5,6), show="headings", height="30")
        self.tv.column(1, anchor="center", width=25)
        self.tv.column(2, anchor="center", width=75)
        self.tv.column(3, anchor="center", width=150)
        self.tv.column(4, anchor="center", width=75)
        self.tv.column(5, anchor="center", width=97)
        self.tv.column(6, anchor="center", width=97)

        self.tv.place(x=320, y=0)
        self.tv.bind('<ButtonRelease-1>', self.selecKullaniciAdmin)

        self.tv.heading(1, text="Id")
        self.tv.heading(2, text="Username")
        self.tv.heading(3, text="E-mail")
        self.tv.heading(4, text="Password")
        self.tv.heading(5, text="Giris Kampanyası")
        self.tv.heading(6, text="2'e 1 Kampanya")


        for i in rows:
            self.tv.insert("", "end", values=i)

    def editekrani(self,a):

        con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os", database="pythonproject")
        cur = con.cursor()
        sql = a
        cur.execute(sql)
        rows = cur.fetchall()
        total = cur.rowcount

        self.tv = ttk.Treeview(self.duzenFrame, columns=(1,2,3), show="headings", height="30")
        self.tv.column(1, anchor="center",width=133)
        self.tv.column(2, anchor="center",width=133)
        self.tv.column(3, anchor="center",width=133)
        self.tv.place(x=400, y=0)
        self.tv.bind('<ButtonRelease-1>', self.selectItemAdmin)

        self.tv.heading(1, text="Ürün Id")
        self.tv.heading(2, text="Ürün Adı")
        self.tv.heading(3, text="Fiyat")

        for i in rows:
            self.tv.insert("", "end", values=i)



    def secenekekrani(self,a):
        Frame_main = Frame(self.root, bg="#1A151A")
        Frame_main.place(x=0, y=0, height=700, width=1366)

        self.img2 = PhotoImage(file="images/sipariş.png")
        self.img = PhotoImage(file="images/arkaplan.png")
        self.img3 = PhotoImage(file="images/back-button-icon-png-21 (1).png")
        label = Label(Frame_main, image=self.img)
        label.place(x=0, y=0, height=703, width=400)

        con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os", database="pythonproject")
        cur = con.cursor()
        sql = a
        cur.execute(sql)
        rows = cur.fetchall()
        total = cur.rowcount

        self.tv = ttk.Treeview(Frame_main, columns=(1, 2), show="headings", height="20")
        self.tv.column(1, anchor="center")
        self.tv.column(2, anchor="center")

        self.tv.place(x=420, y=100)
        self.tv.bind('<ButtonRelease-1>', self.selectItem)


        self.tv.heading(1, text="Ürün Adı")
        self.tv.heading(2, text="Fiyat")

        for i in rows:
            self.tv.insert("", "end", values=i)

        ekleButon = Button(self.root, text="Sipariş Ver", image=self.img2, compound="center", bg="#1A151A",
                           borderwidth=0, activebackground="#1A151A", command=self.siparis)
        ekleButon.place(x=650, y=600, height=45, width=150)

        geriButon = Button(self.root, text="GERİ", image=self.img3, bg="#1A151A", borderwidth=0,
                           activebackground="#1A151A", command=self.appscreen)
        geriButon.place(x=760, y=10, height=60, width=60)





    def selectItemAdmin(self,a):
        self.ürünId.config(text="")
        self.ürünAd.delete(0,"end")
        self.ürünFiyat.delete(0, "end")
        self.item0=self.tv.selection()[0]
        self.item1=self.tv.selection()[0]
        self.item2=self.tv.selection()[0]
        self.ürünId.config(text=self.tv.item(self.item0)["values"][0])
        self.ürünAd.insert(0,self.tv.item(self.item1)["values"][1])
        self.ürünFiyat.insert(0,self.tv.item(self.item2)["values"][2])
        print(self.tv.item(self.item1)["values"][0])
        print(self.tv.item(self.item2)["values"][1])

    def selecKullaniciAdmin(self,a):
        self.kullaniciId.config(text="")
        self.kullaniciAd.delete(0, "end")
        self.kullaniciMail.delete(0, "end")
        self.password1.delete(0, "end")
        self.kampanya1.delete(0, "end")
        self.kampanya2.delete(0, "end")

        self.item0 = self.tv.selection()[0]
        self.item1 = self.tv.selection()[0]
        self.item2 = self.tv.selection()[0]
        self.item3 = self.tv.selection()[0]
        self.item4 = self.tv.selection()[0]
        self.item5 = self.tv.selection()[0]
        self.kullaniciId.config(text=self.tv.item(self.item0)["values"][0])
        self.kullaniciAd.insert(0, self.tv.item(self.item1)["values"][1])
        self.kullaniciMail.insert(0, self.tv.item(self.item2)["values"][2])
        self.password1.insert(0,self.tv.item(self.item3)["values"][3])
        self.kampanya1.insert(0, self.tv.item(self.item4)["values"][4])
        self.kampanya2.insert(0, self.tv.item(self.item5)["values"][5])
        print(self.tv.item(self.item1)["values"][0])
        print(self.tv.item(self.item2)["values"][1])



    def selectItem(self, a):
        self.item1 = self.tv.selection()[0]
        self.item2 = self.tv.selection()[0]

        print(self.tv.item(self.item1)["values"][0])
        print(self.tv.item(self.item2)["values"][1])

    def siparis(self):
        self.hesap = (str(self.tv.item(self.item1)["values"][0]) + "--- " + str(
            self.tv.item(self.item2)["values"][1]) + " TL")
        self.a.append(self.hesap)
        self.hesapTl.append(int(self.tv.item(self.item2)["values"][1]))
        messagebox.showinfo("Eklendi","Ürün Eklendi!")



    def sepetim(self):
        self.tl=0
        Frame_main = Frame(self.root, bg="#1A151A")
        Frame_main.place(x=0, y=0, height=700, width=1366)

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os",
                                          database="pythonproject")
            cur = con.cursor()
            sql = ("SELECT girisKampanyası,2siparise1siparis FROM kullanicilar where email='"+str(self.email_txt.get())+"'")
            print(self.email_txt.get())
            cur.execute(sql)
            rows = cur.fetchone()
            self.sepetteKampanya1=int(rows[0])
            self.sepetteKampanya2=int(rows[1])
            print(self.sepetteKampanya1,self.sepetteKampanya2)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.root)
            person=None



        self.img3 = PhotoImage(file="images/back-button-icon-png-21 (1).png")
        self.img = PhotoImage(file="images/arkaplan.png")
        label = Label(Frame_main, image=self.img)
        label.place(x=25, y=0, height=703, width=400)
        label2 = Label(Frame_main, image=self.img)
        label2.place(x=425, y=0, height=703, width=400)

        self.listbox = Listbox(Frame_main, bg="#f7ffde", font=("Constantia", 15))
        self.listbox.place(x=270, y=125, width=300,height=300)


        for i in range(0,len(self.a)) :
            self.listbox.insert(i,self.a[i])
        for i in range(0,len(self.hesapTl)):
            self.tl+=self.hesapTl[i]

        self.hesapLabel=Label(Frame_main,text=((str(self.tl)+" tl")),bg="#f7ffde")
        self.hesapLabel.place(x=500,y=575,width=80,height=30)



        kampanyalar = ["İlk Sipariş Kampanyası(%50 indirim)", "2 Siparişe Sonraki Siparis Hediye","--Kampanya İstemiyorum--"]
        self.kampanyaSec = ttk.Combobox(Frame_main,height=55,width =30)
        self.kampanyaSec.place(x=300, y=500)

        if self.sepetteKampanya1==1 and self.sepetteKampanya2==2:
            self.kampanyaSec.configure(value=kampanyalar)
        elif self.sepetteKampanya1==1 and self.sepetteKampanya2==0:
            self.kampanyaSec.configure(value=(kampanyalar[0],kampanyalar[2]))
        elif self.sepetteKampanya1==0 and self.sepetteKampanya2==2:
            self.kampanyaSec.configure(value=(kampanyalar[1],kampanyalar[2]))
        elif self.sepetteKampanya1==0 and self.sepetteKampanya2<2:
            self.kampanyaSec.configure(value="Bulunamadı!")

        self.kampanyaSec.bind("<<ComboboxSelected>>", self.comboBoxSelectedItem)





        onayButon=Button(Frame_main,text="Siparişi Onayla",bg="green",command=self.onay)
        onayButon.place(x=350,y=575,height=30,width=150)

        deleteButon = Button(Frame_main, text="Kaldır", command=self.siparisiSil,bg="red")
        deleteButon.place(x=265,y=575,height=30,width=75)

        geriButon = Button(self.root, text="GERİ", image=self.img3, bg="#1A151A", borderwidth=0,
                           activebackground="#1A151A", command=self.appscreen)
        geriButon.place(x=760, y=10, height=60, width=60)


    def comboBoxSelectedItem(self,a):
        self.selectedKampanya=self.kampanyaSec.get()
        if self.selectedKampanya=="İlk Sipariş Kampanyası(%50 indirim)":
            self.hesapLabel.config(text=((str(self.tl/2)+" tl")))
        elif self.selectedKampanya=="2 Siparişe Sonraki Siparis Hediye":
            self.hesapLabel.config(text="0 tl")
        elif self.selectedKampanya=="Bulunamadı!":
            pass
        elif self.selectedKampanya=="--Kampanya İstemiyorum--":
            pass
        print(self.kampanyaSec.get())

    def siparisiSil(self):
        for index in reversed(self.listbox.curselection()):
            self.listbox.delete(index)
            self.hesapTl.remove(self.hesapTl[index])
            self.a.remove(self.a[index])
        self.tl=0
        for i in range(0,len(self.hesapTl)):
            self.tl+=self.hesapTl[i]
        self.hesapLabel.config(text=(str(self.tl)+" tl"))
        self.listbox.config(height=self.listbox.size())


    def onay(self):
        if messagebox.askyesno("Onay","Siparişi Onaylamak İstiyor musunuz"):

         try:
            con = mysql.connector.connect(host="localhost", user="root", password="dgsgk102002os",
                                            database="pythonproject")
            cur = con.cursor()
            sql = ("SELECT id FROM kullanicilar where email='" + str(self.email_txt.get()) + "'")
            cur.execute(sql)
            rows = cur.fetchone()
            id = rows[0]

            print(id)
            if self.selectedKampanya=="2 Siparişe Sonraki Siparis Hediye":
               sql = ("update kullanicilar set 2siparise1siparis="+str(0)+" where id='"+str(id)+"'")

            elif self.selectedKampanya=="İlk Sipariş Kampanyası(%50 indirim)" and self.sepetteKampanya2<2:
              sql=("update kullanicilar set girisKampanyası="+str(0)+", 2siparise1siparis=%s where id='"+str(id)+"'")

            elif self.selectedKampanya=="İlk Sipariş Kampanyası(%50 indirim)":
               sql = ("update kullanicilar set girisKampanyası="+str(0)+" where id='"+str(id)+"'")

            elif self.selectedKampanya=="--Kampanya İstemiyorum--" and self.sepetteKampanya2<2:
                sql = ("update kullanicilar set 2siparise1siparis="+str(int(self.sepetteKampanya2)+1)+" where id='"+str(id)+"'")

            elif self.selectedKampanya=="Bulunamadı!":
                sql = ("update kullanicilar set 2siparise1siparis=" + str( int(self.sepetteKampanya2) + 1) + " where id='" + str(id) + "'")
            


            cur.execute(sql)
            con.commit()
            con.close()

         except Exception as e:
             messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.root)
        else:
            pass





    def cikis(self):
        if messagebox.askyesno("Çıkış","Çıkmak istediğinize emin misiniz?"):
            self.loginform()
        else:
            pass


root=Tk()
root.configure(bg="white")
ob=Login(root)
root.mainloop()