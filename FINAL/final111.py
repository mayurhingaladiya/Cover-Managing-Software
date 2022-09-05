##Programming Project 2022 NEA
##Mayur Hingaladiya
##Cover Managing System
##finished 19/03/2022

from tkinter import *
import tkinter.messagebox
import tkinter as tk
import sqlite3
from tkinter import ttk
import hashlib
import numpy as np
import matplotlib.pyplot as plt



#class for the SQL database
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect('coversInfo.db')
        self.cursor = self.conn.cursor()
        
        #creating the cover table
        sqlCommand = """
        CREATE TABLE IF NOT EXISTS tblcovers
        (
            id INTEGER PRIMARY KEY,
            Teacher string,
            Department string,
            Date string,
            timeFrom string,
            timeTo string,
            Duration integer,
            Notes string
        
        ); 
        
        """
        #creating the teachers table
        sqlCommand1 = """

        CREATE TABLE IF NOT EXISTS tblteachers
        (
            id INTEGER PRIMARY KEY,
            coverid INTEGER,
            Firstname string,
            Surname string,
            Department string,
            Email string,
            FOREIGN KEY(coverid) REFERENCES tblcovers(id)
        
        );
        
        
        """
        #creating the threshold table
        sqlCommand2 = """

        CREATE TABLE IF NOT EXISTS tblthresholds
        (
            Department string PRIMARY KEY,
            Threshold INTEGER
        
        );
        
        
        """

        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute(sqlCommand)
        self.cursor.execute(sqlCommand1)
        self.cursor.execute(sqlCommand2)
        self.conn.commit()

    #fetch all data from the table covers
    def fetch(self):
        self.cursor.execute('SELECT * FROM tblcovers')
        rows = self.cursor.fetchall()
        return rows

    #fetch all the teachers from the cover table
    def fetchteachers(self, searchbyteacher):
        self.cursor.execute('SELECT * FROM tblcovers WHERE Teacher like ?', (searchbyteacher,))
        rows = self.cursor.fetchall()
        return rows

    #fetch all the departments from the cover table
    def fetchdeparts(self, searchbydepart):
        self.cursor.execute('SELECT * FROM tblcovers WHERE Department like ?', (searchbydepart,))
        rows = self.cursor.fetchall()
        return rows

    #fetch all the dates from the cover table
    def fetchdates(self, searchbydate):
        self.cursor.execute('SELECT * FROM tblcovers WHERE Date like ?', (searchbydate,))
        rows = self.cursor.fetchall()
        return rows

    #insert data in the relavent fields into the cover table
    def insert(self, teacher, department, date1, timeFrom, timeTo, duration, notes):
        self.cursor.execute('INSERT INTO tblcovers VALUES (NULL,?,?,?,?,?,?,?)', (teacher, department, date1, timeFrom, timeTo, duration, notes))
        self.conn.commit()

    #remove the data from the selected rowid in the cover table
    def remove(self, id):
        self.cursor.execute('DELETE FROM tblcovers WHERE id=?', (id,))
        self.conn.commit()


    ##### calculating the sum of duration for each department #####
    def sumof_art(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Art'")
        sumofart = self.cursor.fetchone()[0]
        return sumofart

    def sumof_business(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Business'")
        sumofbusiness = self.cursor.fetchone()[0]
        return sumofbusiness
    
    def sumof_biology(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Biology'")
        sumofbiology = self.cursor.fetchone()[0]
        return sumofbiology
    
    def sumof_chem(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Chemistry'")
        sumofchem = self.cursor.fetchone()[0]
        return sumofchem

    def sumof_compsci(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Computer Science'")
        sumofcompsci = self.cursor.fetchone()[0]
        return sumofcompsci

    def sumof_drama(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Drama'")
        sumofdrama = self.cursor.fetchone()[0]
        return sumofdrama
    
    def sumof_economics(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Economics'")
        sumofeco = self.cursor.fetchone()[0]
        return sumofeco

    def sumof_english(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'English'")
        sumofenglish = self.cursor.fetchone()[0]
        return sumofenglish

    def sumof_geography(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Geography'")
        sumofgeo = self.cursor.fetchone()[0]
        return sumofgeo
    
    def sumof_hsc(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'HSC'")
        sumofhsc = self.cursor.fetchone()[0]
        return sumofhsc
    
    def sumof_history(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'History'")
        sumofhistory = self.cursor.fetchone()[0]
        return sumofhistory
    
    def sumof_languages(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Languages'")
        sumoflang = self.cursor.fetchone()[0]
        return sumoflang
    
    def sumof_mathematics(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Mathematics'")
        sumofmaths = self.cursor.fetchone()[0]
        return sumofmaths
    
    def sumof_music(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Music'")
        sumofmusic = self.cursor.fetchone()[0]
        return sumofmusic
    
    def sumof_pe(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'PE'")
        sumofpe = self.cursor.fetchone()[0]
        return sumofpe
    
    def sumof_physics(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Physics'")
        sumofphysics = self.cursor.fetchone()[0]
        return sumofphysics
    
    def sumof_politics(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Politics'")
        sumofpolitics = self.cursor.fetchone()[0]
        return sumofpolitics
    
    def sumof_psychology(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Psychology'")
        sumofpsych = self.cursor.fetchone()[0]
        return sumofpsych
    
    def sumof_RE(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'RE'")
        sumofre = self.cursor.fetchone()[0]
        return sumofre
    
    def sumof_sociology(self):
        self.cursor.execute("SELECT TOTAL(Duration) FROM tblcovers WHERE Department = 'Sociology'")
        sumofsocio = self.cursor.fetchone()[0]
        return sumofsocio

    ###################################
    


    # insert the threshold into the threshold table
    def insert_thresh(self, department1, threshold1):
        self.cursor.execute('INSERT INTO tblthresholds VALUES (?,?)', (department1, threshold1))
        self.conn.commit()
    
    # fetch all the data in the threshold table
    def fetch_thresh(self):
        self.cursor.execute('SELECT * FROM tblthresholds')
        thresh1 = self.cursor.fetchall()
        return thresh1
    
    # remove a threshold
    def remove_thresh(self, department1):
        self.cursor.execute('DELETE FROM tblthresholds WHERE Department=?', (department1,))
        self.conn.commit()
    


    #### fetching the tresholds by department #####

    def fetch_threshart(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Art'")
        threshart = self.cursor.fetchone()[0]
        return threshart

    def fetch_threshbiology(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Biology'")
        threshbiology = self.cursor.fetchone()[0]
        return threshbiology

    def fetch_threshBusiness(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Business'")
        threshBusiness = self.cursor.fetchone()[0]
        return threshBusiness

    def fetch_threshChemistry(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Chemistry'")
        threshChemistry = self.cursor.fetchone()[0]
        return threshChemistry

    def fetch_threshcompsci(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Computer Science'")
        threshcompsci = self.cursor.fetchone()[0]
        return threshcompsci

    def fetch_threshDrama(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Drama'")
        threshDrama = self.cursor.fetchone()[0]
        return threshDrama

    def fetch_threshEconomics(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Economics'")
        threshEconomics = self.cursor.fetchone()[0]
        return threshEconomics

    def fetch_threshEnglish(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'English'")
        threshEnglish = self.cursor.fetchone()[0]
        return threshEnglish

    def fetch_threshGeography(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Geography'")
        threshGeography = self.cursor.fetchone()[0]
        return threshGeography

    def fetch_threshHSC(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'HSC'")
        threshHSC = self.cursor.fetchone()[0]
        return threshHSC

    def fetch_threshHistory(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'History'")
        threshHistory = self.cursor.fetchone()[0]
        return threshHistory

    def fetch_threshLanguages(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Languages'")
        threshLanguages = self.cursor.fetchone()[0]
        return threshLanguages

    def fetch_threshMathematics(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Mathematics'")
        threshMathematics = self.cursor.fetchone()[0]
        return threshMathematics

    def fetch_threshMusic(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Music'")
        threshMusic = self.cursor.fetchone()[0]
        return threshMusic

    def fetch_threshPE(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'PE'")
        threshPE = self.cursor.fetchone()[0]
        return threshPE

    def fetch_threshPhysics(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Physics'")
        threshPhysics = self.cursor.fetchone()[0]
        return threshPhysics

    def fetch_threshPolitics(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Politics'")
        threshPolitics = self.cursor.fetchone()[0]
        return threshPolitics

    def fetch_threshPsychology(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Psychology'")
        threshPsychology = self.cursor.fetchone()[0]
        return threshPsychology

    def fetch_threshRE(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'RE'")
        threshRE = self.cursor.fetchone()[0]
        return threshRE

    def fetch_threshSociology(self):
        self.cursor.execute("SELECT Threshold FROM tblthresholds WHERE Department = 'Sociology'")
        threshSociology = self.cursor.fetchone()[0]
        return threshSociology

    #######################

 
    #close the database
    def __del__(self):
        self.conn.close()
    

db = Database('coversInfo.db')


# main root tkinter window
def main():

    root = Tk()
    app = MainWindow(root)
    root.mainloop()


# login window
class MainWindow:
    def __init__(self,master):
        self.master = master
        self.master.geometry('1000x600')
        self.master.resizable(height=False,width=False)
        self.master.title('Cover Managing System')
        root_icon = PhotoImage(file='fhs.png')
        self.master.iconphoto(False, root_icon)
        self.frame = Frame(self.master)
        self.frame.grid()

        #creating menu bar
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        
        edit_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='Help', menu=edit_menu)
        edit_menu.add_command(label='Documentation')
        edit_menu.add_separator()
        edit_menu.add_command(label='Exit', command = self.master.destroy)


        #initialising username/password variables
        self.username_entry = StringVar()
        self.password_entry = StringVar()

        #title 
        self.main_title_frame = Frame(self.master,width=400,height=75)
        self.main_title_frame.place(relx=0.3,y=10)
        self.main_label = Label(self.main_title_frame, text='Cover Managing System', fg='black', font='Arial 18 bold underline', padx=20, pady=20)
        self.main_label.place(x=40, y=0)


        #login frame
        self.login_frame = LabelFrame(self.master, text='Login', width=400,height=250,bg="#e6e6e6")
        self.login_frame.place(relx=0.55,y=150)

        #login widgets
        self.username_loginLabel = Label(self.login_frame, text="Username:",bg="#e6e6e6", font='Arial 12 bold')
        self.username_loginLabel.place(x=35, y=35)
        self.username_loginEntry = Entry(self.login_frame, textvariable=self.username_entry)
        self.username_loginEntry.place(x=135, y=38, width=205)

        self.password_loginLabel = Label(self.login_frame, text="Password:",bg="#e6e6e6", font='Arial 12 bold')
        self.password_loginLabel.place(x=35, y=80)
        self.password_loginEntry = Entry(self.login_frame,textvariable=self.password_entry, show='*')
        self.password_loginEntry.place(x=135, y=83, width=205)

        #logo
        self.photo_frame = Frame(self.master,width=400,height=280)
        self.photo_frame.place(relx=0.05,y=120)
        self.canvas = Canvas(self.photo_frame, width = 350, height = 280)      
        self.canvas.place(relx=0.05, y=0)      
        self.img = PhotoImage(file="fhs.png")      
        self.canvas.create_image(160,160, image=self.img)

        #buttons for the login page
        login_Button = Button(self.login_frame, text="Log In",font='Arial 10 bold', bg='white', bd=3, relief='raised', command=self.login_verif)
        login_Button.place(x=275, y=125, width=65)
        exit_Button = Button(self.login_frame, text="Exit",font='Arial 10 bold', bg='white', bd=3, relief='raised', command=self.master.quit)
        exit_Button.place(x=275, y=160, width=65)


    #login function for when user presses the login button
    def login_verif(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_hashed = hashlib.sha256(str.encode(password)).hexdigest()
        hashed1 = 'c7e41b31dc20fac52622613326cc599ae51f2d17881693744987a02e0b5e876a'

        if username == 'cover1' and password_hashed == hashed1:
            tkinter.messagebox.showinfo('Login System','You have successfully logged in!')
            self.username_entry.set("")
            self.password_entry.set("")
            self.username_loginEntry.focus()

            self.newWindow = Toplevel(self.master)
            self.app = MenuWindow(self.newWindow)
        
        elif username == '' and password == '':
            tkinter.messagebox.showerror('Login System','Login Failed\nCannot be left blank, must be filled in')

        else:
            tkinter.messagebox.showerror('Login System','Login Failed\nPlease try again')
            self.username_entry.set("")
            self.password_entry.set("")
            self.username_loginEntry.focus()  

    #creating the menu window instance
    def newWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = MenuWindow(self.newWindow)



# main menu
class MenuWindow:
    def __init__(self,master):
        self.master = master
        #confiuging the window
        self.master.geometry('1000x600')
        self.master.resizable(height=False,width=False)
        self.master.title('Cover Managing System | Menu')
        root_icon = PhotoImage(file='fhs.png')
        self.master.iconphoto(False, root_icon)
        self.frame = Frame(self.master)
        self.frame.grid()

        #configuring menu bar
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        file_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='Options', menu=file_menu)
        file_menu.add_command(label='Night Mode On', command=self.night_on)
        #file_menu.add_command(label='Night Mode Off', command=self.night_off)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command = self.master.destroy)
        edit_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='Help', menu=edit_menu)
        edit_menu.add_command(label='Documentation')
        edit_menu.add_separator()
        edit_menu.add_command(label='Exit', command = self.master.destroy)

        
        #title
        self.main_title_frame = Frame(self.master,width=400,height=75)
        self.main_title_frame.place(relx=0.3,y=10)
        self.main_label = Label(self.main_title_frame, text='Cover Managing System', fg='black', font='Arial 18 bold underline', padx=20, pady=20)
        self.main_label.place(x=40, y=0)

        #buttons
        self.buttons_frame = LabelFrame(self.master, text='Select a Option', width=750,height=450, bg="#e6e6e6")
        self.buttons_frame.place(relx=0.13,y=100)
        self.add_cover_btn = Button(self.buttons_frame, text='Add a Cover', font='Arial 16 bold',bg='white', padx=60, pady=20, command=self.addacover_btn)
        self.add_cover_btn.place(x=245,y=30)
        self.view_cover_btn = Button(self.buttons_frame, text='View Covers', font='Arial 16 bold',bg='white', padx=61, pady=20, command=self.viewacover_btn)
        self.view_cover_btn.place(x=245,y=150)
        self.generate_reports_btn = Button(self.buttons_frame, text='Generate Reports', font='Arial 16 bold',bg='white', padx=35, pady=20, command=self.generateReports_btn)
        self.generate_reports_btn.place(x=245,y=270)
        self.options_btn = Button(self.buttons_frame, text='Options', font='Arial 11 ',bg='white', padx=8, pady=3, command=self.option_btn)
        self.options_btn.place(x=660,y=10)
        self.logout_btn = Button(self.buttons_frame, text='Log Out', font='Arial 11 ',bg='white', padx=8, pady=3, command=self.master.destroy)
        self.logout_btn.place(x=660,y=390)

        #logo  
        self.photo_frame = Frame(self.master,width=100,height=100)
        self.photo_frame.place(relx=0.9,y=0)
        self.canvas_mainmenu = Canvas(self.photo_frame, width = 100, height = 100)      
        self.canvas_mainmenu.place(relx=0, y=0)      
        self.img_mainmenu = PhotoImage(file="fhsmall.png")      
        self.canvas_mainmenu.create_image(36,53, image=self.img_mainmenu)

        #checking for alerts
        optionsWindow.alert_breachart(self)
        optionsWindow.alert_breachbiology(self)
        optionsWindow.alert_breachbusiness(self)
        optionsWindow.alert_breachchemistry(self)
        optionsWindow.alert_breachcompsci(self)
        optionsWindow.alert_breachdrama(self)
        optionsWindow.alert_breacheconomics(self)
        optionsWindow.alert_breachenglish(self)
        optionsWindow.alert_breachgeo(self)
        optionsWindow.alert_breachHSC(self)
        optionsWindow.alert_breachhistory(self)
        optionsWindow.alert_breachlang(self)
        optionsWindow.alert_breachmaths(self)
        optionsWindow.alert_breachmusic(self)
        optionsWindow.alert_breachPE(self)
        optionsWindow.alert_breachphysics(self)
        optionsWindow.alert_breachpolitics(self)
        optionsWindow.alert_breachpsych(self)
        optionsWindow.alert_breachRE(self)
        optionsWindow.alert_breachsocio(self)
        
    

    #function for add a cover window
    def addacover_btn(self):
        self.addacover_btn = Toplevel(self.master)
        self.app = addacoverWindow(self.addacover_btn)

    #function for view a cover window
    def viewacover_btn(self):
        self.viewacover_btn = Toplevel(self.master)
        self.app = viewacoverWindow(self.viewacover_btn)

    #function for generate a report window
    def generateReports_btn(self):
        self.generateReports_btn = Toplevel(self.master)
        self.app = generateReportsWindow(self.generateReports_btn)

    #function for options window
    def option_btn(self):
        self.option_btn = Toplevel(self.master)
        self.app = optionsWindow(self.option_btn)

    #night mode experiment#  
    def night_on(self):
        main_color = '#000000'
        self.master.config(bg=main_color)



# Add a cover window
class addacoverWindow:

    #departments
    department_list = ['Art', 
                        'Biology', 
                        'Business', 
                        'Chemistry', 
                        'Computer Science', 
                        'Drama',
                        'Economics', 
                        'English',
                        'Geography',
                        'HSC',
                        'History',
                        'Languages',
                        'Mathematics',
                        'Music',
                        'PE',
                        'Physics',
                        'Politics',
                        'Psychology',
                        'RE',
                        'Sociology'
                        ]
    
    #teachers
    teachers_list = ['R Holden', 
                        'S Shaikh', 
                        'B Williams', 
                        'L Emerson', 
                        'D Pather',
                        'S Cherrouk',
                        'T Embaye',
                        'A Webb',
                        'K Paterson',
                        'P Darron',
                        'J Coulter',
                        'J Moses',
                        'A Hughes',
                        'R Grewal',
                        'S Akhter',
                        'E Sanz',
                        'S El-Yamlahi',
                        'A Patel',
                        'S Ludlow',
                        'M Thorely',
                        'C Briggs',
                        'A Mcghee',
                        'N Hind',
                        'N Predrosa',
                        'T Maroof',
                        'T Moghal',
                        'S Hurlstone',
                        'T Hodge'
                        
                        ]
    

    def __init__(self,master):
        self.master = master
        #configuring the window
        self.master.geometry('1000x600')
        self.master.resizable(height=False,width=False)
        self.master.title('Cover Managing System | Add a Cover')
        root_icon = PhotoImage(file='fhs.png')
        self.master.iconphoto(False, root_icon)
        self.frame = Frame(self.master)
        self.frame.grid()

        #menu bar
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        file_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Add a new Teacher', command=self.addnewteacher)
        file_menu.add_command(label='Add a new Department', command=self.addadepart)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command = self.master.destroy)
        help_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='Documentation')
        help_menu.add_command(label='About')

        #logo
        self.photo_frame = Frame(self.master,width=100,height=100)
        self.photo_frame.place(relx=0.9,y=0)
        self.canvas_mainmenu = Canvas(self.photo_frame, width = 100, height = 100)      
        self.canvas_mainmenu.place(relx=0, y=0)      
        self.img_mainmenu = PhotoImage(file="fhsmall.png")      
        self.canvas_mainmenu.create_image(36,53, image=self.img_mainmenu)

        #title
        self.main_title_frame = Frame(self.master,width=400,height=75)
        self.main_title_frame.place(relx=0.3,y=10)
        self.main_label = Label(self.main_title_frame, text='Cover Managing System', fg='black', font='Arial 18 bold underline', padx=20, pady=20)
        self.main_label.place(x=40, y=0)


        #entering details widgets
        self.add_frame = LabelFrame(self.master, text='Enter the details', width=350,height=455,bg="#e6e6e6")
        self.add_frame.place(relx=0.03,y=100)

        #initial cover details
        self.teacher = StringVar()
        self.teacher.set('R Holden')
        self.department = StringVar()
        self.department.set('Computer Science')
        self.date = StringVar()
        self.date.set('--/--/----')
        self.between = StringVar()
        self.between.set('--:-- (24hrs)')
        self.and1 = StringVar()
        self.and1.set('--:-- (24hrs)')
        self.duration = IntVar()
        self.notes = StringVar()
        self.rowid = StringVar()

        #teacher widget
        self.teacher_label = Label(self.add_frame, text='Teacher:', fg='black', bg='#e6e6e6', font='Arial 12 bold')
        self.teacher_label.place(x=30, y=35)
        self.teacher_drop = OptionMenu(self.add_frame, self.teacher, *self.teachers_list)
        self.teacher_drop.place(x=140, y=30, width=160)
        
        #department widget
        self.department_label = Label(self.add_frame, text='Department:', fg='black', bg='#e6e6e6', font='Arial 12 bold')
        self.department_label.place(x=30, y=85)
        self.department_drop = OptionMenu(self.add_frame, self.department, *self.department_list)
        self.department_drop.place(x=140, y=80, width=160)

        #date widget
        self.date_label = Label(self.add_frame, text='Date:', fg='black', bg='#e6e6e6', font='Arial 12 bold')
        self.date_label.place(x=30, y=135)
        self.date_entry = Entry(self.add_frame, textvariable=self.date)
        self.date_entry.place(x=140, y=137, width=160)

        #timeFrom widget
        self.timeFrom_label = Label(self.add_frame, text='Time From:', fg='black', bg='#e6e6e6', font='Arial 12 bold')
        self.timeFrom_label.place(x=30, y=185)
        self.timeFrom_entry = Entry(self.add_frame, textvariable=self.between)
        self.timeFrom_entry.place(x=140, y=187, width=160)

        #timeTo widget
        self.timeTo_label = Label(self.add_frame, text='Time To:', fg='black', bg='#e6e6e6', font='Arial 12 bold')
        self.timeTo_label.place(x=30, y=235)
        self.timeTo_entry = Entry(self.add_frame, textvariable=self.and1)
        self.timeTo_entry.place(x=140, y=237, width=160)

        #duration widget
        self.duration_label = Label(self.add_frame, text='Duration:', fg='black', bg='#e6e6e6', font='Arial 12 bold')
        self.duration_label.place(x=30, y=285)
        self.duration_entry = Entry(self.add_frame, textvariable=self.duration)
        self.duration_entry.place(x=140, y=287, width=160)

        #duration calculate button
        self.calculate_btn = Button(self.add_frame, text='Calculate', command=self.calculate_btn1)
        self.calculate_btn.place(x=240,y=285)

        #notes widget
        self.notes_label = Label(self.add_frame, text='Notes:', fg='black', bg='#e6e6e6', font='Arial 12 bold')
        self.notes_label.place(x=30, y=335)
        self.notes_entry = Entry(self.add_frame, textvariable=self.notes)
        self.notes_entry.place(x=140, y=337, width=160)

        #buttons
        self.submit_btn = Button(self.add_frame, text='Submit', command=self.submit_btn1)
        self.submit_btn.place(x=155, y=365)
        self.clear_btn = Button(self.add_frame, text='Clear', command=self.clear_btn1)
        self.clear_btn.place(x=160, y=400)


        ##### Configuring treeview for adding a cover #####
        self.addtree_frame = Frame(self.master,width=580,height=480)
        self.addtree_frame.place(relx=0.4,y=105)

        self.remove_btn = Button(self.addtree_frame, text='Remove', command=self.remove_btn1)
        self.remove_btn.place(x=500, y=430)
        
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Treeview",
	                        background="#e6e6e6",
	                        foreground="black",
	                        rowheight=20,
	                        fieldbackground="#e6e6e6")
        self.style.map('Treeview',background=[('selected', "#347083")])


        self.my_tree = ttk.Treeview(self.addtree_frame, height=20)
        
        self.my_tree['columns'] = ('Teacher', 'Department', 'Date', 'timeFrom', 'timeTo', 'Duration', 'Notes')
        
        self.my_tree.column('#0', width=0, stretch=NO)
        self.my_tree.column('Teacher', anchor=W, width=90, minwidth=90)
        self.my_tree.column('Department', anchor=W, width=110, minwidth=110)
        self.my_tree.column('Date', anchor=W, width=80, minwidth=80)
        self.my_tree.column('timeFrom', anchor=W, width=70, minwidth=70)
        self.my_tree.column('timeTo', anchor=W, width=60, minwidth=60)
        self.my_tree.column('Duration', anchor=W, width=60, minwidth=60)
        self.my_tree.column('Notes', anchor=W, width=90, minwidth=250)
       
        self.my_tree.heading('#0', text='', anchor=W)
        self.my_tree.heading('Teacher', text='Teacher', anchor=W)
        self.my_tree.heading('Department', text='Department', anchor=W)
        self.my_tree.heading('Date', text='Date', anchor=W)
        self.my_tree.heading('timeFrom', text='timeFrom', anchor=W)
        self.my_tree.heading('timeTo', text='timeTo', anchor=W)
        self.my_tree.heading('Duration', text='Duration', anchor=W)
        self.my_tree.heading('Notes', text='Notes', anchor=W)
       
        self.my_tree.place(x=0, y=0)
        self.selected_item = self.my_tree.selection()

        self.my_tree.bind("<Double-1>", self.select_record)

        #vertical scrollbar for the treeview
        self.scrollbar = Scrollbar(self.addtree_frame, orient=tk.VERTICAL, command=self.my_tree.yview)
        self.my_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(x=560, y=0, height=400+20)

        #horizontal scrollbar for the treeview
        self.xscrollbar = Scrollbar(self.addtree_frame, orient=tk.HORIZONTAL, command=self.my_tree.xview)
        self.my_tree.configure(xscroll=self.xscrollbar.set)
        self.xscrollbar.place(x=0, y=420, width=470)

        #populating the treeview
        self.populate_listaddwindow()

        ###################################


    #add a new teacher temporarily within the menu bar
    def addnewteacher(self):
        addnewteach = Toplevel(self.master)
        addnewteach.title('Add a new Teacher')
        addnewteach.geometry("200x100")
        addnewteach.resizable(height=False,width=False)
        root_icon = PhotoImage(file='fhs.png')
        addnewteach.iconphoto(False, root_icon)
        addnewteach.frame = Frame(addnewteach)
        addnewteach.frame.grid()

        #add a teacher temporarily widgets
        self.addnewt = StringVar()
        addteach_entry = Entry(addnewteach, textvariable=self.addnewt)
        addteach_entry.place(x=5, y=10)
        addteach_button = Button(addnewteach, text='Add Teacher', command=self.add_teacher_btn)
        addteach_button.place(x=5, y=35)


    #add temp teacher button function
    def add_teacher_btn(self):
        newteacher = self.addnewt.get()
        self.teachers_list.append(newteacher)


    #add a new department temporarily within the menu bar  
    def addadepart(self):
        addnewdepart = Toplevel(self.master)
        addnewdepart.title('Add a new Department')
        addnewdepart.geometry("200x100")
        addnewdepart.resizable(height=False,width=False)
        root_icon = PhotoImage(file='fhs.png')
        addnewdepart.iconphoto(False, root_icon)
        addnewdepart.frame = Frame(addnewdepart)
        addnewdepart.frame.grid()

        self.addnewd = StringVar()
        addteach_entry = Entry(addnewdepart, textvariable=self.addnewd)
        addteach_entry.place(x=5, y=10)
        addteach_button = Button(addnewdepart, text='Add Department', command=self.add_department_btn)
        addteach_button.place(x=5, y=35)

    #add a temp department function
    def add_department_btn(self):
        newDepartment = self.addnewd.get()
        self.department_list.append(newDepartment)


    #duration calculation function
    def calculate_btn1(self):
        timeStart = self.between.get()
        (h,m) = timeStart.split(':')
        timeStartinSecs = int(h) * 3600 + int(m) * 60

        timeEnd = self.and1.get()
        (h1,m1) = timeEnd.split(':')
        timeEndinSecs = int(h1) * 3600 + int(m1) * 60

        timeDiff = (timeEndinSecs - timeStartinSecs)
        totalDiffinMin = int(timeDiff / 60) 

        self.duration.set(totalDiffinMin)

 
    #adding a cover function
    def submit_btn1(self):
        #getting all the data inputted
        teacher = self.teacher.get()
        department = self.department.get()
        date1 = self.date.get()
        timeFrom = self.between.get()
        timeTo = self.and1.get()
        duration = self.duration.get()
        notes = self.notes.get()

        #presence check
        if teacher == '' or department == '' or date1 == '' or timeFrom == '' or timeTo == '' or  duration == '':
            tkinter.messagebox.showerror('Add a Cover','Failed\nFields cannot be left blank, must be filled in', parent=self.master)

        else:
            db.insert(teacher, department, date1, timeFrom, timeTo, duration, notes)
            self.my_tree.insert(parent='', index='end', iid=db.cursor.lastrowid, values = (teacher, department, date1, timeFrom, timeTo, duration, notes))        

            tkinter.messagebox.showinfo('Add a Cover','Success\nCover added!', parent=self.master)

    #populating the treeview for when window is open
    def populate_listaddwindow(self):
        for row in db.fetch():
            self.my_tree.insert('', 'end', iid=row[0], values=row[1:])


    #double click treeview populating the entry boxes
    def select_record(self, e):
        #clearing the entry boxes
        self.teacher.set('')
        self.department.set('')
        self.date_entry.delete(0, END)
        self.timeFrom_entry.delete(0, END)
        self.timeTo_entry.delete(0, END)
        self.duration_entry.delete(0, END)
        self.notes_entry.delete(0, END)

        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')

        #setting the values to the ones that was double clicked
        self.teacher.set(values[0])
        self.department.set(values[1])
        self.date_entry.insert(0, values[2])
        self.timeFrom_entry.insert(0, values[3])
        self.timeTo_entry.insert(0, values[4])
        self.duration_entry.insert(0, values[5])
        self.notes_entry.insert(0, values[6])


    #remove a cover function
    def remove_btn1(self):
        id = self.rowid.get()

        for id in self.my_tree.selection():
            self.my_tree.delete(id)
            db.remove(id)
        tkinter.messagebox.showinfo('Add a cover', 'Successfully removed', parent=self.master)

    #clearing the entry boxes
    def clear_btn1(self):
        self.teacher.set('')
        self.department.set('')
        self.date_entry.delete(0, END)
        self.timeFrom_entry.delete(0, END)
        self.timeTo_entry.delete(0, END)
        self.duration_entry.delete(0, END)
        self.notes_entry.delete(0, END)

        self.duration.set('0')
    


#options window for setting thresholds
class optionsWindow:
    def __init__(self,master):
        self.master = master
        #configuring the window
        self.master.geometry('300x350')
        self.master.resizable(height=False,width=False)
        self.master.title('Cover Managing System | Options')
        root_icon = PhotoImage(file='fhs.png')
        self.master.iconphoto(False, root_icon)
        self.frame = Frame(self.master)
        self.frame.grid()

        #menu bar
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='Help', menu=edit_menu)
        edit_menu.add_command(label='Documentation')
        edit_menu.add_separator()
        edit_menu.add_command(label='Exit', command = self.master.destroy)

        #title
        self.main_frame = LabelFrame(self.master, text='Set a Threshold', width=250,height=315)
        self.main_frame.place(x=25,y=10)

        #initialising threshold data
        self.department = StringVar()
        self.department.set('Computer Science')
        self.thresholdlimit = IntVar()
        self.departs = addacoverWindow.department_list
        self.list1 = StringVar()

        #department widgets
        self.department1_label = Label(self.main_frame, text='Department:', fg='black', font='Arial 9')
        self.department1_label.place(x=10, y=23)
        self.department1_drop = OptionMenu(self.main_frame, self.department, *self.departs)
        self.department1_drop.place(x=90, y=16, width=130)

        #threshold widget
        self.threshold_label = Label(self.main_frame, text='Threshold:', fg='black', font='Arial 9')
        self.threshold_label.place(x=10, y=73)
        self.threshold_entry = Entry(self.main_frame, textvariable=self.thresholdlimit)
        self.threshold_entry.place(x=90, y=73, width=127)
        self.thresholdinfo_label = Label(self.main_frame, text='in minutes*', fg='red', font='Arial 8')
        self.thresholdinfo_label.place(x=12, y=93)
        
        #set button
        self.set_Button = Button(self.main_frame, text="Set Threshold",font='Arial 9', relief='raised', command=self.set_thresh)
        self.set_Button.place(x=85, y=115)

        ###listbox to show the thresholds###
        self.listbox1 = Listbox(self.main_frame, listvariable=self.list1, height=7, width=33, selectmode='extended')
        self.listbox1.place(x=15, y=150)

        #scroll bar
        self.scrollbar111 = ttk.Scrollbar(self.main_frame, orient='vertical', command=self.listbox1.yview)
        self.listbox1['yscrollcommand'] = self.scrollbar111.set
        self.scrollbar111.place(x=217,y=150, height=115)
        #mouse click select
        self.listbox1.bind('<<ListboxSelect>>', self.select_thresh)

        #remove button
        self.remove_Button = Button(self.main_frame, text="Remove",font='Arial 8', relief='raised', command= self.remove_listbox1)
        self.remove_Button.place(x=180, y=270)
        self.populate_listbox1()
        

    #selecting the desired selected item in listbox
    def select_thresh(self, event):
        try:
            self.index = self.listbox1.curselection()[0]
            self.selected_thresh = self.listbox1.get(self.index)
        
        except IndexError:
            pass


    #setting the threshold
    def set_thresh(self):
        #get the data from the entry boxes
        department1 = self.department.get()
        threshold1 = self.thresholdlimit.get()
               
        db.insert_thresh(department1, threshold1)
        self.listbox1.insert(END, (department1, threshold1))
        tkinter.messagebox.showinfo('Threshold', str(threshold1) + ' minute threshold set for ' + str(department1), parent=self.master)

     

    #removing a threshold
    def remove_listbox1(self):
        db.remove_thresh(self.selected_thresh[0])
        self.listbox1.delete(0, END)
        self.populate_listbox1()
       
    #populating the listbox
    def populate_listbox1(self):
        for thresh1 in db.fetch_thresh():
            self.listbox1.insert(END, thresh1)   

    
    ##### alerts for breaching the threshold limit for each department #####
    def alert_breachart(self):
        #fetch the threshold set
        fetchart = db.fetch_threshart()
        #fetch the sum of the durations in that department
        sumofart = db.sumof_art()

        if fetchart == 0 or fetchart == None:
            return 0
        elif sumofart > fetchart:
            tkinter.messagebox.showwarning('Threshold Alert','Art Department has breached the Threshold limit', parent=self.master)
        
    def alert_breachbiology(self):
        fetchbio = db.fetch_threshbiology()
        sumofbio = db.sumof_biology()

        if fetchbio == 0 or fetchbio == None:
            return 0
        elif sumofbio > fetchbio:
            tkinter.messagebox.showwarning('Threshold Alert','Biology Department has breached the Threshold limit', parent=self.master)

    def alert_breachbusiness(self):
        fetchbusiness = db.fetch_threshBusiness()
        sumofbusiness = db.sumof_business()
        if fetchbusiness == 0 or fetchbusiness == None:
            return 0
        elif sumofbusiness > fetchbusiness:
            tkinter.messagebox.showwarning('Threshold Alert','Business Department has breached the Threshold limit', parent=self.master)

    def alert_breachchemistry(self):
        fetchchemistry = db.fetch_threshChemistry()
        sumofchemistry = db.sumof_chem()
        if fetchchemistry == 0 or fetchchemistry == None:
            return 0
        elif sumofchemistry > fetchchemistry:
            tkinter.messagebox.showwarning('Threshold Alert','Chemistry Department has breached the Threshold limit', parent=self.master)

    def alert_breachcompsci(self):
        fetchcompsci = db.fetch_threshcompsci()
        sumofcompsci = db.sumof_compsci()
        if fetchcompsci == 0 or fetchcompsci == None:
            return 0
        elif sumofcompsci > fetchcompsci:
            tkinter.messagebox.showwarning('Threshold Alert','Computer Science Department has breached the Threshold limit', parent=self.master)

    def alert_breachdrama(self):
        fetchdrama = db.fetch_threshDrama()
        sumofdrama = db.sumof_drama()
        if fetchdrama == 0 or fetchdrama == None:
            return 0
        elif sumofdrama > fetchdrama:
            tkinter.messagebox.showwarning('Threshold Alert','Drama Department has breached the Threshold limit', parent=self.master)

    def alert_breacheconomics(self):
        fetcheconomics = db.fetch_threshEconomics()
        sumofeconomics = db.sumof_economics()
        if fetcheconomics == 0 or fetcheconomics == None:
            return 0
        elif sumofeconomics > fetcheconomics:
            tkinter.messagebox.showwarning('Threshold Alert','Economics Department has breached the Threshold limit', parent=self.master)

    def alert_breachenglish(self):
        fetchenglish = db.fetch_threshEnglish()
        sumofenglish = db.sumof_english()
        if fetchenglish == 0 or fetchenglish == None:
            return 0
        elif sumofenglish > fetchenglish:
            tkinter.messagebox.showwarning('Threshold Alert','English Department has breached the Threshold limit', parent=self.master)

    def alert_breachgeo(self):
        fetchgeo = db.fetch_threshGeography()
        sumofgeo = db.sumof_geography()
        if fetchgeo == 0 or fetchgeo == None:
            return 0
        elif sumofgeo > fetchgeo:
            tkinter.messagebox.showwarning('Threshold Alert','Geography Department has breached the Threshold limit', parent=self.master)

    def alert_breachHSC(self):
        fetchHSC = db.fetch_threshHSC()
        sumofHSC = db.sumof_hsc()
        if fetchHSC == 0 or fetchHSC == None:
            return 0
        elif sumofHSC > fetchHSC:
            tkinter.messagebox.showwarning('Threshold Alert','Health and Social Care Department has breached the Threshold limit', parent=self.master)

    def alert_breachhistory(self):
        fetchhistory = db.fetch_threshHistory()
        sumofhistory = db.sumof_history()
        if fetchhistory == 0 or fetchhistory == None:
            return 0
        elif sumofhistory > fetchhistory:
            tkinter.messagebox.showwarning('Threshold Alert','History Department has breached the Threshold limit', parent=self.master)

    def alert_breachlang(self):
        fetchlang = db.fetch_threshLanguages()
        sumoflang = db.sumof_languages()
        if fetchlang == 0 or fetchlang == None:
            return 0
        elif sumoflang > fetchlang:
            tkinter.messagebox.showwarning('Threshold Alert','Languages Department has breached the Threshold limit', parent=self.master)

    def alert_breachmaths(self):
        fetchmaths = db.fetch_threshMathematics()
        sumofmaths = db.sumof_mathematics()
        if fetchmaths == 0 or fetchmaths == None:
            return 0
        elif sumofmaths > fetchmaths:
            tkinter.messagebox.showwarning('Threshold Alert','Mathematics Department has breached the Threshold limit', parent=self.master)

    def alert_breachmusic(self):
        fetchmusic = db.fetch_threshMathematics()
        sumofmusic = db.sumof_mathematics()
        if fetchmusic == 0 or fetchmusic == None:
            return 0
        elif sumofmusic > fetchmusic:
            tkinter.messagebox.showwarning('Threshold Alert','Music Department has breached the Threshold limit', parent=self.master)

    def alert_breachPE(self):
        fetchPE = db.fetch_threshPE()
        sumofPE = db.sumof_pe()
        if fetchPE == 0 or fetchPE == None:
            return 0
        elif sumofPE > fetchPE:
            tkinter.messagebox.showwarning('Threshold Alert','PE Department has breached the Threshold limit', parent=self.master)

    def alert_breachphysics(self):
        fetchphysics = db.fetch_threshPhysics()
        sumofphysics = db.sumof_physics()
        if fetchphysics == 0 or fetchphysics == None:
            return 0
        elif sumofphysics > fetchphysics:
            tkinter.messagebox.showwarning('Threshold Alert','Physics Department has breached the Threshold limit', parent=self.master)

    def alert_breachpolitics(self):
        fetchpolitics = db.fetch_threshPolitics()
        sumofpolitics = db.sumof_politics()
        if fetchpolitics == 0 or fetchpolitics == None:
            return 0
        elif sumofpolitics > fetchpolitics:
            tkinter.messagebox.showwarning('Threshold Alert','Politics Department has breached the Threshold limit', parent=self.master)

    def alert_breachpsych(self):
        fetchpsych = db.fetch_threshPsychology()
        sumofpsych = db.sumof_psychology()
        if fetchpsych == 0 or fetchpsych == None:
            return 0
        elif sumofpsych > fetchpsych:
            tkinter.messagebox.showwarning('Threshold Alert','Psychology Department has breached the Threshold limit', parent=self.master)

    def alert_breachRE(self):
        fetchRE = db.fetch_threshRE()
        sumofRE = db.sumof_RE()
        if fetchRE == 0 or fetchRE == None:
            return 0
        elif sumofRE > fetchRE:
            tkinter.messagebox.showwarning('Threshold Alert','RE Department has breached the Threshold limit', parent=self.master)

    def alert_breachsocio(self):
        fetchsocio = db.fetch_threshSociology()
        sumofsocio = db.sumof_sociology()
        if fetchsocio == 0 or fetchsocio == None:
            return 0
        elif sumofsocio > fetchsocio:
            tkinter.messagebox.showwarning('Threshold Alert','Sociology Department has breached the Threshold limit', parent=self.master)


    ##################################################




#view a cover window
class viewacoverWindow:
    def __init__(self,master):
        self.master = master
        #configuring the window
        self.master.geometry('1000x600')
        self.master.resizable(height=False,width=False)
        self.master.title('Cover Managing System | View a Cover')
        root_icon = PhotoImage(file='fhs.png')
        self.master.iconphoto(False, root_icon)
        self.frame = Frame(self.master)
        self.frame.grid()

        #menu bar
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='Help', menu=edit_menu)
        edit_menu.add_command(label='Documentation')
        edit_menu.add_separator()
        edit_menu.add_command(label='Exit', command = self.master.destroy)

        #logo
        self.photo_frame = Frame(self.master,width=100,height=100)
        self.photo_frame.place(relx=0.9,y=0)
        self.canvas_mainmenu = Canvas(self.photo_frame, width = 100, height = 100)      
        self.canvas_mainmenu.place(relx=0, y=0)      
        self.img_mainmenu = PhotoImage(file="fhsmall.png")      
        self.canvas_mainmenu.create_image(36,53, image=self.img_mainmenu)


        #title
        self.main_title_frame = Frame(self.master,width=400,height=75)
        self.main_title_frame.place(relx=0.3,y=10)
        self.main_label = Label(self.main_title_frame, text='Cover Managing System', fg='black', font='Arial 18 bold underline', padx=20, pady=20)
        self.main_label.place(x=40, y=0)

        #searching frame 
        self.lookup_frame = LabelFrame(self.master, text='Search', width=840,height=65)
        self.lookup_frame.place(x=70,y=80)

        self.searchbydate = StringVar()
        self.searchbydepart = StringVar()
        self.searchbyteacher = StringVar()

        #search by teacher
        self.searchteacher_label = Label(self.lookup_frame, text='Search by Teacher:', fg='black', font='Arial 9')
        self.searchteacher_label.place(x=5, y=10)
        self.searchteacher_entry = Entry(self.lookup_frame, textvariable=self.searchbyteacher)
        self.searchteacher_entry.place(x=120, y=10, width=100)
        self.go1_Button = Button(self.lookup_frame, text="Go",font='Arial 8', bg='white', bd=3, relief='raised', command=self.searchbyteacher1)
        self.go1_Button.place(x=225, y=7)

        #search by department
        self.searchdepart_label = Label(self.lookup_frame, text='Search by Department:', fg='black', font='Arial 9')
        self.searchdepart_label.place(x=290, y=10)
        self.searchdepart_entry = Entry(self.lookup_frame, textvariable=self.searchbydepart)
        self.searchdepart_entry.place(x=427, y=10, width=110)
        self.go2_Button = Button(self.lookup_frame, text="Go",font='Arial 8', bg='white', bd=3, relief='raised', command=self.searchbydepart1)
        self.go2_Button.place(x=545, y=7)

        #search by date
        self.searchdate_label = Label(self.lookup_frame, text='Search by Date:', fg='black', font='Arial 9')
        self.searchdate_label.place(x=610, y=10)
        self.searchdate_entry = Entry(self.lookup_frame, textvariable=self.searchbydate)
        self.searchdate_entry.place(x=705, y=10, width=100)
        self.go3_Button = Button(self.lookup_frame, text="Go",font='Arial 8', bg='white', bd=3, relief='raised', command=self.searchbydate1)
        self.go3_Button.place(x=810, y=7)
        
        #reset treeview
        self.resettree_Button = Button(self.lookup_frame, text="Reset View",font='Arial 7', relief='raised', command=self.resettree)
        self.resettree_Button.place(x=780, y=33)



        ##### Configuring treeview for view a cover window ######
        self.viewtree_frame = Frame(self.master,width=855,height=425)
        self.viewtree_frame.place(x=70,y=150)


        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Treeview",
	                        background="#e6e6e6",
	                        foreground="black",
	                        rowheight=20,
	                        fieldbackground="#e6e6e6")
        self.style.map('Treeview',background=[('selected', "#347083")])

        self.my_tree = ttk.Treeview(self.viewtree_frame, height=19)
        self.my_tree.place(x=0, y=10)
            
        self.my_tree['columns'] = ('Teacher', 'Department', 'Date', 'timeFrom', 'timeTo', 'Duration', 'Notes')
            
        self.my_tree.column('#0', width=0, stretch=NO)
        self.my_tree.column('Teacher', anchor=W, width=110, minwidth=110)
        self.my_tree.column('Department', anchor=W, width=130, minwidth=130)
        self.my_tree.column('Date', anchor=W, width=90, minwidth=90)
        self.my_tree.column('timeFrom', anchor=W, width=90, minwidth=90)
        self.my_tree.column('timeTo', anchor=W, width=90, minwidth=90)
        self.my_tree.column('Duration', anchor=W, width=90, minwidth=90)
        self.my_tree.column('Notes', anchor=W, width=270, minwidth=320)

        self.my_tree.heading('#0', text='', anchor=W)
        self.my_tree.heading('Teacher', text='Teacher', anchor=W)
        self.my_tree.heading('Department', text='Department', anchor=W)
        self.my_tree.heading('Date', text='Date', anchor=W)
        self.my_tree.heading('timeFrom', text='timeFrom', anchor=W)
        self.my_tree.heading('timeTo', text='timeTo', anchor=W)
        self.my_tree.heading('Duration', text='Duration', anchor=W)
        self.my_tree.heading('Notes', text='Notes', anchor=W)

        #vertical scrollbar
        self.scrollbar = Scrollbar(self.viewtree_frame, orient=tk.VERTICAL, command=self.my_tree.yview)
        self.my_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(x=840, y=10, height=380+20)

        #horizontal scrollbar
        self.xscrollbar = Scrollbar(self.viewtree_frame, orient=tk.HORIZONTAL, command=self.my_tree.xview)
        self.my_tree.configure(xscroll=self.xscrollbar.set)
        self.xscrollbar.place(x=0, y=410, width=830)

        #tag for when searched
        self.my_tree.tag_configure('selectedrow',background='lightblue')

        self.populate_listviewwindow()

    
    #populate the treeview
    def populate_listviewwindow(self):
        for row in db.fetch():
            self.my_tree.insert('', 'end', iid=row[0], values=row[1:])
    
    #search by teacher function
    def searchbyteacher1(self):
        teacher_get = self.searchbyteacher.get()

        if teacher_get == '':
            tkinter.messagebox.showerror('View a Cover', 'Field cannot be left blank!', parent=self.master)
        else:
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)
    
            for row in db.fetchteachers(teacher_get):
                self.my_tree.insert('', 'end', iid=row[0], values=row[1:], tags='selectedrow')

            teacher_count = len(self.my_tree.get_children())
            tkinter.messagebox.showinfo('View a Cover', str(teacher_count) + ' found', parent=self.master)

    #search by department function
    def searchbydepart1(self):
        department_get = self.searchbydepart.get()

        if department_get == '':
            tkinter.messagebox.showerror('View a Cover', 'Field cannot be left blank!', parent=self.master)
        else:
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)

            for row in db.fetchdeparts(department_get):
                self.my_tree.insert('', 'end', iid=row[0], values=row[1:], tags='selectedrow')
            
            depart_count = len(self.my_tree.get_children())
            tkinter.messagebox.showinfo('View a Cover', str(depart_count) + ' found', parent=self.master)
            



    #search by date function
    def searchbydate1(self):
        date_get = self.searchbydate.get()

        if date_get == '':
            tkinter.messagebox.showerror('View a Cover', 'Field cannot be left blank!', parent=self.master)
        else:
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)
        
            for row in db.fetchdates(date_get):
                self.my_tree.insert('', 'end', iid=row[0], values=row[1:], tags='selectedrow')
            
            date_count = len(self.my_tree.get_children())
            tkinter.messagebox.showinfo('View a Cover', str(date_count) + ' found', parent=self.master)


    #reset the treeview
    def resettree(self):
        self.searchteacher_entry.delete(0, END)
        self.searchdepart_entry.delete(0, END)
        self.searchdate_entry.delete(0, END)

        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

        for row in db.fetch():
            self.my_tree.insert('', 'end', iid=row[0], values=row[1:])






#generate reports window
class generateReportsWindow():
    def __init__(self,master):
        self.master = master
        #configuring the window
        self.master.geometry('1000x600')
        self.master.resizable(height=False,width=False)
        self.master.title('Cover Managing System | Generate Reports')
        root_icon = PhotoImage(file='fhs.png')
        self.master.iconphoto(False, root_icon)
        self.frame = Frame(self.master)
        self.frame.grid()

        #menu bar
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        edit_menu = Menu(my_menu, tearoff=OFF)
        my_menu.add_cascade(label='Help', menu=edit_menu)
        edit_menu.add_command(label='Documentation')
        edit_menu.add_separator()
        edit_menu.add_command(label='Exit', command = self.master.destroy)

        #logo
        self.photo_frame = Frame(self.master,width=100,height=100)
        self.photo_frame.place(relx=0.9,y=0)
        self.canvas_mainmenu = Canvas(self.photo_frame, width = 100, height = 100)      
        self.canvas_mainmenu.place(relx=0, y=0)      
        self.img_mainmenu = PhotoImage(file="fhsmall.png")      
        self.canvas_mainmenu.create_image(36,53, image=self.img_mainmenu)

        #title
        self.main_title_frame = Frame(self.master,width=400,height=75)
        self.main_title_frame.place(relx=0.3,y=10)
        self.main_label = Label(self.main_title_frame, text='Cover Managing System', fg='black', font='Arial 18 bold underline', padx=20, pady=20)
        self.main_label.place(x=40, y=0)

        #generate graph button
        self.generategraph_Button = Button(self.master, text="Generate Graph",font='Arial 9', relief='raised', command=self.generateGraph)
        self.generategraph_Button.place(x=50, y=100)
        
        #generate txt report button
        self.generatetxt_Button = Button(self.master, text="Generate Textfile",font='Arial 9', relief='raised', command=self.generateTxt)
        self.generatetxt_Button.place(x=50, y=170)
    

    #generate graph function
    def generateGraph(self):
        #gets the department list from the add a cover class
        departs = addacoverWindow.department_list
     
        ##sum of durations for each department##
        sumofart = db.sumof_art()
        sumofbiology = db.sumof_biology()
        sumofbusiness = db.sumof_business()
        sumofchem = db.sumof_chem()
        sumofcompsci = db.sumof_compsci()
        sumofdrama = db.sumof_drama()
        sumofeco = db.sumof_economics()
        sumofenglish = db.sumof_english()
        sumofgeo = db.sumof_geography()
        sumofhsc = db.sumof_hsc()
        sumofhistory = db.sumof_history()
        sumoflang = db.sumof_languages()
        sumofmaths = db.sumof_mathematics()
        sumofmusic = db.sumof_music()
        sumofpe = db.sumof_pe()
        sumofphysics = db.sumof_physics()
        sumofpolitics = db.sumof_politics()
        sumofpsych = db.sumof_psychology()
        sumofre = db.sumof_RE()
        sumofsocio = db.sumof_sociology()

        #creates a list of all the sums
        departs_times = [sumofart, 
                        sumofbiology,
                        sumofbusiness,
                        sumofchem, 
                        sumofcompsci, 
                        sumofdrama,
                        sumofeco, 
                        sumofenglish,
                        sumofgeo,
                        sumofhsc,
                        sumofhistory,
                        sumoflang,
                        sumofmaths,
                        sumofmusic,
                        sumofpe,
                        sumofphysics,
                        sumofpolitics,
                        sumofpsych,
                        sumofre,
                        sumofsocio

                        ]

        #initialising x and y variables
        x = np.array(departs)
        y = np.array(departs_times)

        #adding colors
        colors = ['green','blue','red','blue','pink','olive', 
                    'red','cyan','green','teal','purple','yellow',
                    'orange','gray','cyan','blue','olive','olive', 'pink', 'olive']
            
        plt.bar(x, y, color = colors)
        plt.xticks(rotation = 90)
        plt.title('The Total Cover times per Department', fontsize=12, fontweight='bold', color = 'blue')
        plt.xlabel('Departments', fontsize=12, fontweight='bold', color = 'blue')
        plt.ylabel('Total Cover times in Minutes', fontsize=12, fontweight='bold', color = 'blue')

        plt.show()
 


    def generateTxt(self):
        ##sum of durations for each department##
        sumofart = db.sumof_art()
        sumofbiology = db.sumof_biology()
        sumofbusiness = db.sumof_business()
        sumofchem = db.sumof_chem()
        sumofcompsci = db.sumof_compsci()
        sumofdrama = db.sumof_drama()
        sumofeco = db.sumof_economics()
        sumofenglish = db.sumof_english()
        sumofgeo = db.sumof_geography()
        sumofhsc = db.sumof_hsc()
        sumofhistory = db.sumof_history()
        sumoflang = db.sumof_languages()
        sumofmaths = db.sumof_mathematics()
        sumofmusic = db.sumof_music()
        sumofpe = db.sumof_pe()
        sumofphysics = db.sumof_physics()
        sumofpolitics = db.sumof_politics()
        sumofpsych = db.sumof_psychology()
        sumofre = db.sumof_RE()
        sumofsocio = db.sumof_sociology()


        file = open("DepartmentCoverTimes.txt","a")
        file.write("-----------------------------------------------------" + "\n" + "\n")

        file.write("Art Department has put in: " + str(sumofart) + "minutes" + "\n")
        file.write("Biology Department has put in: " + str(sumofbiology) + "minutes" + "\n")        
        file.write("Business Department has put in: " + str(sumofbusiness) + "minutes" + "\n")        
        file.write("Chemistry Department has put in: " + str(sumofchem) + "minutes" + "\n")        
        file.write("Computer Science Department has put in: " + str(sumofcompsci) + "minutes" + "\n")        
        file.write("Drama Department has put in: " + str(sumofdrama) + "minutes" + "\n")        
        file.write("Economics Department has put in: " + str(sumofeco) + "minutes" + "\n")        
        file.write("English Department has put in: " + str(sumofenglish) + "minutes" + "\n")        
        file.write("Geography Department has put in: " + str(sumofgeo) + "minutes" + "\n")        
        file.write("HSC Department has put in: " + str(sumofhsc) + "minutes" + "\n")        
        file.write("History Department has put in: " + str(sumofhistory) + "minutes" + "\n")        
        file.write("Languages Department has put in: " + str(sumoflang) + "minutes" + "\n")        
        file.write("Mathematics Department has put in: " + str(sumofmaths) + "minutes" + "\n")        
        file.write("Music Department has put in: " + str(sumofmusic) + "minutes" + "\n")        
        file.write("PE Department has put in: " + str(sumofpe) + "minutes" + "\n")        
        file.write("Physics Department has put in: " + str(sumofphysics) + "minutes" + "\n")        
        file.write("Politics Department has put in: " + str(sumofpolitics) + "minutes" + "\n")        
        file.write("Psychology Department has put in: " + str(sumofpsych) + "minutes" + "\n")        
        file.write("RE Department has put in: " + str(sumofre) + "minutes" + "\n")        
        file.write("Sociology Department has put in: " + str(sumofsocio) + "minutes" + "\n")        

        tkinter.messagebox.showinfo('Generate Reports','Successfully Written', parent=self.master)

#######
if __name__ =='__main__':
    main()
#######