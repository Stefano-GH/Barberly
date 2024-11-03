##############################
# IMPORT LIBRARIES
##############################
from calendar import weekday
import os
import sqlite3
import datetime as dt
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, filedialog, colorchooser, messagebox


##############################
# FUNCTIONS AND CLASSES DEFINITION
##############################
class main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1600x1000')
        self.root.title('Automatic Management System - CopyAssignment')
        #self.root.iconphoto(False, ImageTk.PhotoImage(Image.open('C:/Users/stumi/Desktop/universe.png')))
        self.root.state('zoomed')

        # Save informations
        conn = sqlite3.connect(s_key)
        c = conn.cursor()
        c.execute('SELECT * FROM settings WHERE oid=1')
        self.img_bg = c.fetchall()[0][1]
        conn.commit()
        c.execute("SELECT * FROM settings WHERE oid=2")
        self.font = c.fetchall()[0][1]
        conn.commit()
        c.execute("SELECT * FROM settings WHERE oid=3")
        self.color_bg = c.fetchall()[0][1]
        conn.commit()
        c.execute("SELECT * FROM settings WHERE oid=4")
        self.color_fg_dami = c.fetchall()[0][1]
        conn.commit()
        c.execute("SELECT * FROM settings WHERE oid=5")
        self.color_fg_salvo = c.fetchall()[0][1]
        conn.commit()
        conn.close()

        # Create Menu and Menu items
        my_menu = Menu(self.root)
        self.root.configure(menu=my_menu)

        file_menu = Menu(my_menu)
        my_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Nuovo >> Damiano', command=lambda: self.dami_new(dami_data_e1, dami_ora_e1, dami_cust_e1))
        file_menu.add_command(label='Salva >> Damiano', command=lambda: self.dami_update(dami_data_e1, dami_ora_e1, dami_cust_e1, dami_tv_day1))
        file_menu.add_command(label='Elimina >> Damiano', command=lambda: self.dami_remove(dami_tv_day1))
        file_menu.add_separator()
        file_menu.add_command(label='Nuovo >> Salvo', command=lambda: self.salvo_new(salvo_data_e1, salvo_ora_e1, salvo_cust_e1))
        file_menu.add_command(label='Salva >> Salvo', command=lambda: self.salvo_update(salvo_data_e1, salvo_ora_e1, salvo_cust_e1, salvo_tv_day1))
        file_menu.add_command(label='Elimina >> Salvo', command=lambda: self.salvo_remove(salvo_tv_day1))
        file_menu.add_separator()
        file_menu.add_command(label='Aggiorna', command=self.reload)

        settings_menu = Menu(my_menu)
        my_menu.add_cascade(label='Impostazioni', menu=settings_menu)
        settings_menu.add_command(label='Cambia sfondo', command=self.change_background)
        settings_menu.add_command(label='Cambia font', command=self.change_font)
        settings_menu.add_separator()
        settings_menu.add_command(label='Cambia colore sfondo', command=self.change_color_bg)
        settings_menu.add_command(label='Cambia colore font Damiano', command=self.change_color_fg_dami)
        settings_menu.add_command(label='Cambia colore font Salvo', command=self.change_color_fg_salvo)
        settings_menu.add_separator()
        settings_menu.add_command(label='Default', command=self.default_settings)

        exit_menu = Menu(my_menu)
        my_menu.add_cascade(label='Esci', menu=exit_menu)
        exit_menu.add_command(label='Esci', command=self.root.destroy)
        
        # Manage time
        week_dic = ('Lunedí', 'Martedí', 'Mercoledí', 'Giovedí', 'Venerdí', 'Sabato', 'Domenica')
        day0 = dt.datetime.now()
        if day0.weekday() == 0:
                day0 = day0 + dt.timedelta(days=1)
        elif day0.weekday() == 6:
                day0 = day0 + dt.timedelta(days=2)

        day1 = day0 + dt.timedelta(days=1)
        if day1.weekday() == 0:
                day1 = day1 + dt.timedelta(days=1)
        elif day1.weekday() == 6:
                day1 = day1 + dt.timedelta(days=2)

        day2 = day1 + dt.timedelta(days=1)
        if day2.weekday() == 0:
                day2 = day2 + dt.timedelta(days=1)
        elif day2.weekday() == 6:
                day2 = day2 + dt.timedelta(days=2)

        day3 = day2 + dt.timedelta(days=1)
        if day3.weekday() == 0:
                day3 = day3 + dt.timedelta(days=1)
        elif day3.weekday() == 6:
                day3 = day3 + dt.timedelta(days=2)

        day4 = day3 + dt.timedelta(days=1)
        if day4.weekday() == 0:
                day4 = day4 + dt.timedelta(days=1)
        elif day4.weekday() == 6:
                day4 = day4 + dt.timedelta(days=2)

        day5 = day4 + dt.timedelta(days=1)
        if day5.weekday() == 0:
                day5 = day5 + dt.timedelta(days=1)
        elif day5.weekday() == 6:
                day5 = day5 + dt.timedelta(days=2)

        day6 = day5 + dt.timedelta(days=1)
        if day6.weekday() == 0:
                day6 = day6 + dt.timedelta(days=1)
        elif day6.weekday() == 6:
                day6 = day6 + dt.timedelta(days=2)

        day7 = day6 + dt.timedelta(days=1)
        if day7.weekday() == 0:
                day7 = day7 + dt.timedelta(days=1)
        elif day7.weekday() == 6:
                day7 = day7 + dt.timedelta(days=2)

        day8 = day7 + dt.timedelta(days=1)
        if day8.weekday() == 0:
                day8 = day8 + dt.timedelta(days=1)
        elif day8.weekday() == 6:
                day8 = day8 + dt.timedelta(days=2)

        day9 = day8 + dt.timedelta(days=1)
        if day9.weekday() == 0:
                day9 = day9 + dt.timedelta(days=1)
        elif day9.weekday() == 6:
                day9 = day9 + dt.timedelta(days=2)

        day10 = day9 + dt.timedelta(days=1)
        if day10.weekday() == 0:
                day10 = day10 + dt.timedelta(days=1)
        elif day10.weekday() == 6:
                day10 = day10 + dt.timedelta(days=2)

        day11 = day10 + dt.timedelta(days=1)
        if day11.weekday() == 0:
                day11 = day11 + dt.timedelta(days=1)
        elif day11.weekday() == 6:
                day11 = day11 + dt.timedelta(days=2)

        day12 = day11 + dt.timedelta(days=1)
        if day12.weekday() == 0:
                day12 = day12 + dt.timedelta(days=1)
        elif day12.weekday() == 6:
                day12 = day12 + dt.timedelta(days=2)

        day13 = day12 + dt.timedelta(days=1)
        if day13.weekday() == 0:
                day13 = day13 + dt.timedelta(days=1)
        elif day13.weekday() == 6:
                day13 = day13 + dt.timedelta(days=2)

        day14 = day13 + dt.timedelta(days=1)
        if day14.weekday() == 0:
                day14 = day14 + dt.timedelta(days=1)
        elif day14.weekday() == 6:
                day14 = day14 + dt.timedelta(days=2)
        
        # Creatre Notebook
        my_notebook = ttk.Notebook()
        my_notebook.pack()

        self.day1 = Frame(my_notebook, width=1600, height=1000)
        self.day1.pack()
        self.day2 = Frame(my_notebook, width=1600, height=1000)
        self.day2.pack()
        self.day3 = Frame(my_notebook, width=1600, height=1000)
        self.day3.pack()
        self.day4 = Frame(my_notebook, width=1600, height=1000)
        self.day4.pack()
        self.day5 = Frame(my_notebook, width=1600, height=1000)
        self.day5.pack()
        self.day6 = Frame(my_notebook, width=1600, height=1000)
        self.day6.pack()
        self.day7 = Frame(my_notebook, width=1600, height=1000)
        self.day7.pack()
        self.day8 = Frame(my_notebook, width=1600, height=1000)
        self.day8.pack()
        self.day9 = Frame(my_notebook, width=1600, height=1000)
        self.day9.pack()
        self.day10 = Frame(my_notebook, width=1600, height=1000)
        self.day10.pack()
        self.day11 = Frame(my_notebook, width=1600, height=1000)
        self.day11.pack()
        self.day12 = Frame(my_notebook, width=1600, height=1000)
        self.day12.pack()
        self.day13 = Frame(my_notebook, width=1600, height=1000)
        self.day13.pack()
        self.day14 = Frame(my_notebook, width=1600, height=1000)
        self.day14.pack()
        self.day15 = Frame(my_notebook, width=1600, height=1000)
        self.day15.pack()
        my_notebook.add(self.day1, text=week_dic[day0.weekday()])
        my_notebook.add(self.day2, text=week_dic[day1.weekday()])
        my_notebook.add(self.day3, text=week_dic[day2.weekday()] + ' ' + dt.datetime.strftime(day2, '%d-%m'))
        my_notebook.add(self.day4, text=week_dic[day3.weekday()] + ' ' + dt.datetime.strftime(day3, '%d-%m'))
        my_notebook.add(self.day5, text=week_dic[day4.weekday()] + ' ' + dt.datetime.strftime(day4, '%d-%m'))
        my_notebook.add(self.day6, text=week_dic[day5.weekday()] + ' ' + dt.datetime.strftime(day5, '%d-%m'))
        my_notebook.add(self.day7, text=week_dic[day6.weekday()] + ' ' + dt.datetime.strftime(day6, '%d-%m'))
        my_notebook.add(self.day8, text=week_dic[day7.weekday()] + ' ' + dt.datetime.strftime(day7, '%d-%m'))
        my_notebook.add(self.day9, text=week_dic[day8.weekday()] + ' ' + dt.datetime.strftime(day8, '%d-%m'))
        my_notebook.add(self.day10, text=week_dic[day9.weekday()] + ' ' + dt.datetime.strftime(day9, '%d-%m'))
        my_notebook.add(self.day11, text=week_dic[day10.weekday()] + ' ' + dt.datetime.strftime(day10, '%d-%m'))
        my_notebook.add(self.day12, text=week_dic[day11.weekday()] + ' ' + dt.datetime.strftime(day11, '%d-%m'))
        my_notebook.add(self.day13, text=week_dic[day12.weekday()] + ' ' + dt.datetime.strftime(day12, '%d-%m'))
        my_notebook.add(self.day14, text=week_dic[day13.weekday()] + ' ' + dt.datetime.strftime(day13, '%d-%m'))
        my_notebook.add(self.day15, text=week_dic[day14.weekday()] + ' ' + dt.datetime.strftime(day14, '%d-%m'))

        # Create backgrounds
        try:
            img = ImageTk.PhotoImage(Image.open(self.img_bg))
            l1 = Label(self.day1, image=img)
            l1.place(x=0, y=0, relheight=1, relwidth=1)
            l2 = Label(self.day2, image=img)
            l2.place(x=0, y=0, relheight=1, relwidth=1)
            l3 = Label(self.day3, image=img)
            l3.place(x=0, y=0, relheight=1, relwidth=1)
            l4 = Label(self.day4, image=img)
            l4.place(x=0, y=0, relheight=1, relwidth=1)
            l5 = Label(self.day5, image=img)
            l5.place(x=0, y=0, relheight=1, relwidth=1)
            l6 = Label(self.day6, image=img)
            l6.place(x=0, y=0, relheight=1, relwidth=1)
            l7 = Label(self.day7, image=img)
            l7.place(x=0, y=0, relheight=1, relwidth=1)
            l8 = Label(self.day8, image=img)
            l8.place(x=0, y=0, relheight=1, relwidth=1)
            l9 = Label(self.day9, image=img)
            l9.place(x=0, y=0, relheight=1, relwidth=1)
            l10 = Label(self.day10, image=img)
            l10.place(x=0, y=0, relheight=1, relwidth=1)
            l11 = Label(self.day11, image=img)
            l11.place(x=0, y=0, relheight=1, relwidth=1)
            l12 = Label(self.day12, image=img)
            l12.place(x=0, y=0, relheight=1, relwidth=1)
            l13 = Label(self.day13, image=img)
            l13.place(x=0, y=0, relheight=1, relwidth=1)
            l14 = Label(self.day14, image=img)
            l14.place(x=0, y=0, relheight=1, relwidth=1)
            l15 = Label(self.day15, image=img)
            l15.place(x=0, y=0, relheight=1, relwidth=1)
        except:
            self.day1.config(bg=str(self.color_bg))
            self.day2.config(bg=str(self.color_bg))
            self.day3.config(bg=str(self.color_bg))
            self.day4.config(bg=str(self.color_bg))
            self.day5.config(bg=str(self.color_bg))
            self.day6.config(bg=str(self.color_bg))
            self.day7.config(bg=str(self.color_bg))
            self.day8.config(bg=str(self.color_bg))
            self.day9.config(bg=str(self.color_bg))
            self.day10.config(bg=str(self.color_bg))
            self.day11.config(bg=str(self.color_bg))
            self.day12.config(bg=str(self.color_bg)) 
            self.day13.config(bg=str(self.color_bg))
            self.day14.config(bg=str(self.color_bg))
            self.day15.config(bg=str(self.color_bg))

        ####################
        # DAY 1 
        ####################
        # Create frames
        dami_tv_frame1 = LabelFrame(self.day1, text='Damiano - Oggi', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame1.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame1 = LabelFrame(self.day1, text='Salvo - Oggi', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame1.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame1 = Frame(self.day1, bg=str(self.color_bg))
        dami_data_frame1.place(x=200, y=580)
        salvo_data_frame1 = Frame(self.day1, bg=str(self.color_bg))
        salvo_data_frame1.place(x=970, y=580)
        dami_button_frame1 = Frame(self.day1, bg=str(self.color_bg))
        dami_button_frame1.place(x=240, y=650)
        salvo_button_frame1 = Frame(self.day1, bg=str(self.color_bg))
        salvo_button_frame1.place(x=1010, y=650)

        # Add some Style
        dami_style_day1 = ttk.Style()
        dami_style_day1.theme_use('clam')
        dami_style_day1.configure('Treeview', background='#D3D3D3', foreground='black', rowheight=20, fieldbackground='#D3D3D3')
        dami_style_day1.map('Treeview', background=[('selected', 'red')])

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day1 = ttk.Treeview(dami_tv_frame1)
        dami_tv_day1.place(relwidth=1, relheight=1)
        dami_scrolly1 = Scrollbar(dami_tv_frame1, orient=VERTICAL, command=dami_tv_day1.yview)
        dami_scrolly1.pack(side=RIGHT, fill=Y)
        dami_tv_day1.configure(yscrollcommand=dami_scrolly1.set)

        # Set columns DAMIANO
        dami_tv_day1['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day1.column('#0', width=0, stretch=NO)
        dami_tv_day1.column('ID', width=10, anchor=CENTER)
        dami_tv_day1.column('Data', width=100, anchor=CENTER)
        dami_tv_day1.column('Ora', width=70, anchor=CENTER)
        dami_tv_day1.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day1.heading('#0', text='')
        dami_tv_day1.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day1.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day1.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day1.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day1.tag_configure('evenrow', background='white')
        dami_tv_day1.tag_configure('oddrow', background='lightblue')
        self.dami_count = 0
        n = 1
        for t in orari:
                confront_time = day0 - dt.timedelta(hours=n)
                if confront_time.time() < dt.datetime.strptime(t, '%H:%M').time():
                        if self.dami_count%2 == 0:
                                dami_tv_day1.insert(parent='', index='end', iid=self.dami_count, values=('', day0.date(), t, ''), tags=('evenrow',))
                        else:
                                dami_tv_day1.insert(parent='', index='end', iid=self.dami_count, values=('', day0.date(), t, ''), tags=('oddrow',))
                        self.dami_count += 1
        controllo = True
        confront_time = day0 - dt.timedelta(hours=n)
        while controllo:
                controllo = False
                for i in range(0, len(orari)):
                        if confront_time.time() > dt.datetime.strptime(orari[i], '%H:%M').time():
                                orari.remove(orari[i])
                                controllo = True
                                break
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day0.date():
                        confront_time = day0 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i in dami_tv_day1.get_children():
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[int(i)], '%H:%M').time():
                                                dami_tv_day1.delete(int(i))
                                                if int(i)%2 == 0:
                                                        dami_tv_day1.insert(parent='', index=i, iid=int(i), values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day1.insert(parent='', index=i, iid=int(i), values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l1 = Label(dami_data_frame1, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l1.grid(row=0, column=0)
        dami_ora_l1 = Label(dami_data_frame1, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l1.grid(row=0, column=1)
        dami_cust_l1 = Label(dami_data_frame1, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l1.grid(row=0, column=2)
        dami_data_e1 = Entry(dami_data_frame1)
        dami_data_e1.grid(row=1, column=0)
        dami_ora_e1 = Entry(dami_data_frame1)
        dami_ora_e1.grid(row=1, column=1)
        dami_cust_e1 = Entry(dami_data_frame1)
        dami_cust_e1.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame1, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_check(dami_data_e1, dami_ora_e1, dami_cust_e1))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame1, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e1, dami_ora_e1, dami_cust_e1, dami_tv_day1))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame1, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day1))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame1, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e1, dami_ora_e1, dami_cust_e1))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day1.bind("<Double-1>", lambda x:self.dami_select(dami_data_e1, dami_ora_e1, dami_cust_e1, dami_tv_day1))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day1 = ttk.Treeview(salvo_tv_frame1)
        salvo_tv_day1.place(relwidth=1, relheight=1)
        salvo_scrolly1 = Scrollbar(salvo_tv_frame1, orient=VERTICAL, command=salvo_tv_day1.yview)
        salvo_scrolly1.pack(side=RIGHT, fill=Y)
        salvo_tv_day1.configure(yscrollcommand=salvo_scrolly1.set)

        # Set columns SALVO
        salvo_tv_day1['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day1.column('#0', width=0, stretch=NO)
        salvo_tv_day1.column('ID', width=10, anchor=CENTER)
        salvo_tv_day1.column('Data', width=100, anchor=CENTER)
        salvo_tv_day1.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day1.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day1.heading('#0', text='')
        salvo_tv_day1.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day1.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day1.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day1.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day1.tag_configure('evenrow', background='white')
        salvo_tv_day1.tag_configure('oddrow', background='lightblue')
        self.salvo_count = 0
        n = 1
        for t in orari:
                confront_time = day0 - dt.timedelta(hours=n)
                if confront_time.time() < dt.datetime.strptime(t, '%H:%M').time():
                        if self.salvo_count%2 == 0:
                                salvo_tv_day1.insert(parent='', index='end', iid=self.salvo_count, values=('', day0.date(), t, ''), tags=('evenrow',))
                        else:
                                salvo_tv_day1.insert(parent='', index='end', iid=self.salvo_count, values=('', day0.date(), t, ''), tags=('oddrow',))
                        self.salvo_count += 1
        controllo = True
        confront_time = day0 - dt.timedelta(hours=n)
        while controllo:
                controllo = False
                for i in range(0, len(orari)):
                        if confront_time.time() > dt.datetime.strptime(orari[i], '%H:%M').time():
                                orari.remove(orari[i])
                                controllo = True
                                break
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day0.date():
                        confront_time = day0 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i in salvo_tv_day1.get_children():
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[int(i)], '%H:%M').time():
                                                salvo_tv_day1.delete(int(i))
                                                if int(i)%2 == 0:
                                                        salvo_tv_day1.insert(parent='', index=i, iid=int(i), values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day1.insert(parent='', index=i, iid=int(i), values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes SALVO
        salvo_data_l1 = Label(salvo_data_frame1, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l1.grid(row=0, column=0)
        salvo_ora_l1 = Label(salvo_data_frame1, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l1.grid(row=0, column=1)
        salvo_cust_l1 = Label(salvo_data_frame1, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l1.grid(row=0, column=2)
        salvo_data_e1 = Entry(salvo_data_frame1)
        salvo_data_e1.grid(row=1, column=0)
        salvo_ora_e1 = Entry(salvo_data_frame1)
        salvo_ora_e1.grid(row=1, column=1)
        salvo_cust_e1 = Entry(salvo_data_frame1)
        salvo_cust_e1.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame1, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e1, salvo_ora_e1, salvo_cust_e1))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame1, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e1, salvo_ora_e1, salvo_cust_e1, salvo_tv_day1))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame1, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day1))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame1, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e1, salvo_ora_e1, salvo_cust_e1))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day1.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e1, salvo_ora_e1, salvo_cust_e1, salvo_tv_day1))

        ####################
        # DAY 2
        ####################
        # Create frames
        dami_tv_frame2 = LabelFrame(self.day2, text='Damiano - Domani', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame2.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame2 = LabelFrame(self.day2, text='Salvo - Domani', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame2.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame2 = Frame(self.day2, bg=str(self.color_bg))
        dami_data_frame2.place(x=200, y=580)
        salvo_data_frame2 = Frame(self.day2, bg=str(self.color_bg))
        salvo_data_frame2.place(x=970, y=580)
        dami_button_frame2 = Frame(self.day2, bg=str(self.color_bg))
        dami_button_frame2.place(x=240, y=650)
        salvo_button_frame2 = Frame(self.day2, bg=str(self.color_bg))
        salvo_button_frame2.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day2 = ttk.Treeview(dami_tv_frame2)
        dami_tv_day2.place(relwidth=1, relheight=1)
        dami_scrolly2 = Scrollbar(dami_tv_frame2, orient=VERTICAL, command=dami_tv_day2.yview)
        dami_scrolly2.pack(side=RIGHT, fill=Y)
        dami_tv_day2.configure(yscrollcommand=dami_scrolly2.set)

        # Set columns DAMIANO
        dami_tv_day2['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day2.column('#0', width=0, stretch=NO)
        dami_tv_day2.column('ID', width=10, anchor=CENTER)
        dami_tv_day2.column('Data', width=100, anchor=CENTER)
        dami_tv_day2.column('Ora', width=70, anchor=CENTER)
        dami_tv_day2.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day2.heading('#0', text='')
        dami_tv_day2.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day2.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day2.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day2.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day2.tag_configure('evenrow', background='white')
        dami_tv_day2.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day2.insert(parent='', index='end', iid=self.dami_count, values=('', day1.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day2.insert(parent='', index='end', iid=self.dami_count, values=('', day1.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day1.date():
                        for i,j in enumerate(dami_tv_day2.get_children()):
                                if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                        dami_tv_day2.delete(j)
                                        if int(j)%2 == 0:
                                                dami_tv_day2.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                        else:
                                                dami_tv_day2.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
                                
        # Create labels and  entry boxes DAMIANO
        dami_data_l2 = Label(dami_data_frame2, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l2.grid(row=0, column=0)
        dami_ora_l2 = Label(dami_data_frame2, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l2.grid(row=0, column=1)
        dami_cust_l2 = Label(dami_data_frame2, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l2.grid(row=0, column=2)
        dami_data_e2 = Entry(dami_data_frame2)
        dami_data_e2.grid(row=1, column=0)
        dami_ora_e2 = Entry(dami_data_frame2)
        dami_ora_e2.grid(row=1, column=1)
        dami_cust_e2 = Entry(dami_data_frame2)
        dami_cust_e2.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame2, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e2, dami_ora_e2, dami_cust_e2))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame2, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e2, dami_ora_e2, dami_cust_e2, dami_tv_day2))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame2, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day2))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame2, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e2, dami_ora_e2, dami_cust_e2))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day2.bind("<Double-1>", lambda x:self.dami_select(dami_data_e2, dami_ora_e2, dami_cust_e2, dami_tv_day2))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day2 = ttk.Treeview(salvo_tv_frame2)
        salvo_tv_day2.place(relwidth=1, relheight=1)
        salvo_scrolly2 = Scrollbar(salvo_tv_frame2, orient=VERTICAL, command=salvo_tv_day2.yview)
        salvo_scrolly2.pack(side=RIGHT, fill=Y)
        salvo_tv_day2.configure(yscrollcommand=salvo_scrolly2.set)

        # Set columns SALVO
        salvo_tv_day2['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day2.column('#0', width=0, stretch=NO)
        salvo_tv_day2.column('ID', width=10, anchor=CENTER)
        salvo_tv_day2.column('Data', width=100, anchor=CENTER)
        salvo_tv_day2.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day2.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day2.heading('#0', text='')
        salvo_tv_day2.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day2.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day2.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day2.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day2.tag_configure('evenrow', background='white')
        salvo_tv_day2.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day2.insert(parent='', index='end', iid=self.salvo_count, values=('', day1.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day2.insert(parent='', index='end', iid=self.salvo_count, values=('', day1.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1

        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day1.date():
                        for i,j in enumerate(salvo_tv_day2.get_children()):
                                if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                        salvo_tv_day2.delete(j)
                                        if int(j)%2 == 0:
                                                salvo_tv_day2.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                        else:
                                                salvo_tv_day2.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes SALVO
        salvo_data_l2 = Label(salvo_data_frame2, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l2.grid(row=0, column=0)
        salvo_ora_l2 = Label(salvo_data_frame2, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l2.grid(row=0, column=1)
        salvo_cust_l2 = Label(salvo_data_frame2, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l2.grid(row=0, column=2)
        salvo_data_e2 = Entry(salvo_data_frame2)
        salvo_data_e2.grid(row=1, column=0)
        salvo_ora_e2 = Entry(salvo_data_frame2)
        salvo_ora_e2.grid(row=1, column=1)
        salvo_cust_e2 = Entry(salvo_data_frame2)
        salvo_cust_e2.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame2, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e2, salvo_ora_e2, salvo_cust_e2))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame2, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e2, salvo_ora_e2, salvo_cust_e2, salvo_tv_day2))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame2, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day2))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame2, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e2, salvo_ora_e2, salvo_cust_e2))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day2.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e2, salvo_ora_e2, salvo_cust_e2, salvo_tv_day2))

        ####################
        # DAY 3
        ####################
        # Create frames
        dami_tv_frame3 = LabelFrame(self.day3, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame3.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame3 = LabelFrame(self.day3, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame3.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame3 = Frame(self.day3, bg=str(self.color_bg))
        dami_data_frame3.place(x=200, y=580)
        salvo_data_frame3 = Frame(self.day3, bg=str(self.color_bg))
        salvo_data_frame3.place(x=970, y=580)
        dami_button_frame3 = Frame(self.day3, bg=str(self.color_bg))
        dami_button_frame3.place(x=240, y=650)
        salvo_button_frame3 = Frame(self.day3, bg=str(self.color_bg))
        salvo_button_frame3.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day3 = ttk.Treeview(dami_tv_frame3)
        dami_tv_day3.place(relwidth=1, relheight=1)
        dami_scrolly3 = Scrollbar(dami_tv_frame3, orient=VERTICAL, command=dami_tv_day3.yview)
        dami_scrolly3.pack(side=RIGHT, fill=Y)
        dami_tv_day3.configure(yscrollcommand=dami_scrolly3.set)

        # Set columns DAMIANO
        dami_tv_day3['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day3.column('#0', width=0, stretch=NO)
        dami_tv_day3.column('ID', width=10, anchor=CENTER)
        dami_tv_day3.column('Data', width=100, anchor=CENTER)
        dami_tv_day3.column('Ora', width=70, anchor=CENTER)
        dami_tv_day3.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day3.heading('#0', text='')
        dami_tv_day3.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day3.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day3.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day3.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day3.tag_configure('evenrow', background='white')
        dami_tv_day3.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day3.insert(parent='', index='end', iid=self.dami_count, values=('', day2.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day3.insert(parent='', index='end', iid=self.dami_count, values=('', day2.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day2.date():
                        confront_time = day2 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day3.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day3.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day3.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day3.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l3 = Label(dami_data_frame3, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l3.grid(row=0, column=0)
        dami_ora_l3 = Label(dami_data_frame3, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l3.grid(row=0, column=1)
        dami_cust_l3 = Label(dami_data_frame3, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l3.grid(row=0, column=2)
        dami_data_e3 = Entry(dami_data_frame3)
        dami_data_e3.grid(row=1, column=0)
        dami_ora_e3 = Entry(dami_data_frame3)
        dami_ora_e3.grid(row=1, column=1)
        dami_cust_e3 = Entry(dami_data_frame3)
        dami_cust_e3.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame3, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e3, dami_ora_e3, dami_cust_e3))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame3, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e3, dami_ora_e3, dami_cust_e3, dami_tv_day3))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame3, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day3))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame3, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e3, dami_ora_e3, dami_cust_e3))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day3.bind("<Double-1>", lambda x:self.dami_select(dami_data_e3, dami_ora_e3, dami_cust_e3, dami_tv_day3))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day3 = ttk.Treeview(salvo_tv_frame3)
        salvo_tv_day3.place(relwidth=1, relheight=1)
        salvo_scrolly3 = Scrollbar(salvo_tv_frame3, orient=VERTICAL, command=salvo_tv_day3.yview)
        salvo_scrolly3.pack(side=RIGHT, fill=Y)
        salvo_tv_day3.configure(yscrollcommand=salvo_scrolly3.set)

        # Set columns SALVO
        salvo_tv_day3['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day3.column('#0', width=0, stretch=NO)
        salvo_tv_day3.column('ID', width=10, anchor=CENTER)
        salvo_tv_day3.column('Data', width=100, anchor=CENTER)
        salvo_tv_day3.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day3.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day3.heading('#0', text='')
        salvo_tv_day3.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day3.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day3.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day3.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day3.tag_configure('evenrow', background='white')
        salvo_tv_day3.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day3.insert(parent='', index='end', iid=self.salvo_count, values=('', day2.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day3.insert(parent='', index='end', iid=self.salvo_count, values=('', day2.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day2.date():
                        confront_time = day2 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day3.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day3.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day3.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day3.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l3 = Label(salvo_data_frame3, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l3.grid(row=0, column=0)
        salvo_ora_l3 = Label(salvo_data_frame3, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l3.grid(row=0, column=1)
        salvo_cust_l3 = Label(salvo_data_frame3, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l3.grid(row=0, column=2)
        salvo_data_e3 = Entry(salvo_data_frame3)
        salvo_data_e3.grid(row=1, column=0)
        salvo_ora_e3 = Entry(salvo_data_frame3)
        salvo_ora_e3.grid(row=1, column=1)
        salvo_cust_e3 = Entry(salvo_data_frame3)
        salvo_cust_e3.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame3, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e3, salvo_ora_e3, salvo_cust_e3))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame3, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e3, salvo_ora_e3, salvo_cust_e3, salvo_tv_day3))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame3, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day3))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame3, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e3, salvo_ora_e3, salvo_cust_e3))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day3.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e3, salvo_ora_e3, salvo_cust_e3, salvo_tv_day3))

        ####################
        # DAY 4
        ####################
        # Create frames
        dami_tv_frame4 = LabelFrame(self.day4, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame4.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame4 = LabelFrame(self.day4, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame4.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame4 = Frame(self.day4, bg=str(self.color_bg))
        dami_data_frame4.place(x=200, y=580)
        salvo_data_frame4 = Frame(self.day4, bg=str(self.color_bg))
        salvo_data_frame4.place(x=970, y=580)
        dami_button_frame4 = Frame(self.day4, bg=str(self.color_bg))
        dami_button_frame4.place(x=240, y=650)
        salvo_button_frame4 = Frame(self.day4, bg=str(self.color_bg))
        salvo_button_frame4.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day4 = ttk.Treeview(dami_tv_frame4)
        dami_tv_day4.place(relwidth=1, relheight=1)
        dami_scrolly4 = Scrollbar(dami_tv_frame4, orient=VERTICAL, command=dami_tv_day4.yview)
        dami_scrolly4.pack(side=RIGHT, fill=Y)
        dami_tv_day4.configure(yscrollcommand=dami_scrolly4.set)

        # Set columns DAMIANO
        dami_tv_day4['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day4.column('#0', width=0, stretch=NO)
        dami_tv_day4.column('ID', width=10, anchor=CENTER)
        dami_tv_day4.column('Data', width=100, anchor=CENTER)
        dami_tv_day4.column('Ora', width=70, anchor=CENTER)
        dami_tv_day4.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day4.heading('#0', text='')
        dami_tv_day4.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day4.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day4.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day4.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day4.tag_configure('evenrow', background='white')
        dami_tv_day4.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day4.insert(parent='', index='end', iid=self.dami_count, values=('', day3.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day4.insert(parent='', index='end', iid=self.dami_count, values=('', day3.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day3.date():
                        confront_time = day3 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day4.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day4.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day4.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day4.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l4 = Label(dami_data_frame4, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l4.grid(row=0, column=0)
        dami_ora_l4 = Label(dami_data_frame4, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l4.grid(row=0, column=1)
        dami_cust_l4 = Label(dami_data_frame4, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l4.grid(row=0, column=2)
        dami_data_e4 = Entry(dami_data_frame4)
        dami_data_e4.grid(row=1, column=0)
        dami_ora_e4 = Entry(dami_data_frame4)
        dami_ora_e4.grid(row=1, column=1)
        dami_cust_e4 = Entry(dami_data_frame4)
        dami_cust_e4.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame4, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e4, dami_ora_e4, dami_cust_e4))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame4, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e4, dami_ora_e4, dami_cust_e4, dami_tv_day4))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame4, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day4))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame4, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e4, dami_ora_e4, dami_cust_e4))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day4.bind("<Double-1>", lambda x:self.dami_select(dami_data_e4, dami_ora_e4, dami_cust_e4, dami_tv_day4))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day4 = ttk.Treeview(salvo_tv_frame4)
        salvo_tv_day4.place(relwidth=1, relheight=1)
        salvo_scrolly4 = Scrollbar(salvo_tv_frame4, orient=VERTICAL, command=salvo_tv_day4.yview)
        salvo_scrolly4.pack(side=RIGHT, fill=Y)
        salvo_tv_day4.configure(yscrollcommand=salvo_scrolly4.set)

        # Set columns SALVO
        salvo_tv_day4['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day4.column('#0', width=0, stretch=NO)
        salvo_tv_day4.column('ID', width=10, anchor=CENTER)
        salvo_tv_day4.column('Data', width=100, anchor=CENTER)
        salvo_tv_day4.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day4.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day4.heading('#0', text='')
        salvo_tv_day4.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day4.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day4.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day4.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day4.tag_configure('evenrow', background='white')
        salvo_tv_day4.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day4.insert(parent='', index='end', iid=self.salvo_count, values=('', day3.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day4.insert(parent='', index='end', iid=self.salvo_count, values=('', day3.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day3.date():
                        confront_time = day3 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day4.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day4.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day4.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day4.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l4 = Label(salvo_data_frame4, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l4.grid(row=0, column=0)
        salvo_ora_l4 = Label(salvo_data_frame4, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l4.grid(row=0, column=1)
        salvo_cust_l4 = Label(salvo_data_frame4, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l4.grid(row=0, column=2)
        salvo_data_e4 = Entry(salvo_data_frame4)
        salvo_data_e4.grid(row=1, column=0)
        salvo_ora_e4 = Entry(salvo_data_frame4)
        salvo_ora_e4.grid(row=1, column=1)
        salvo_cust_e4 = Entry(salvo_data_frame4)
        salvo_cust_e4.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame4, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e4, salvo_ora_e4, salvo_cust_e4))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame4, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e4, salvo_ora_e4, salvo_cust_e4, salvo_tv_day4))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame4, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day4))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame4, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e4, salvo_ora_e4, salvo_cust_e4))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day4.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e4, salvo_ora_e4, salvo_cust_e4, salvo_tv_day4))

        ####################
        # DAY 5
        ####################
        # Create frames
        dami_tv_frame5 = LabelFrame(self.day5, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame5.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame5 = LabelFrame(self.day5, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame5.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame5 = Frame(self.day5, bg=str(self.color_bg))
        dami_data_frame5.place(x=200, y=580)
        salvo_data_frame5 = Frame(self.day5, bg=str(self.color_bg))
        salvo_data_frame5.place(x=970, y=580)
        dami_button_frame5 = Frame(self.day5, bg=str(self.color_bg))
        dami_button_frame5.place(x=240, y=650)
        salvo_button_frame5 = Frame(self.day5, bg=str(self.color_bg))
        salvo_button_frame5.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day5 = ttk.Treeview(dami_tv_frame5)
        dami_tv_day5.place(relwidth=1, relheight=1)
        dami_scrolly5 = Scrollbar(dami_tv_frame5, orient=VERTICAL, command=dami_tv_day5.yview)
        dami_scrolly5.pack(side=RIGHT, fill=Y)
        dami_tv_day5.configure(yscrollcommand=dami_scrolly5.set)

        # Set columns DAMIANO
        dami_tv_day5['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day5.column('#0', width=0, stretch=NO)
        dami_tv_day5.column('ID', width=10, anchor=CENTER)
        dami_tv_day5.column('Data', width=100, anchor=CENTER)
        dami_tv_day5.column('Ora', width=70, anchor=CENTER)
        dami_tv_day5.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day5.heading('#0', text='')
        dami_tv_day5.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day5.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day5.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day5.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day5.tag_configure('evenrow', background='white')
        dami_tv_day5.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day5.insert(parent='', index='end', iid=self.dami_count, values=('', day4.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day5.insert(parent='', index='end', iid=self.dami_count, values=('', day4.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day4.date():
                        confront_time = day4 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day5.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day5.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day5.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day5.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l5 = Label(dami_data_frame5, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l5.grid(row=0, column=0)
        dami_ora_l5 = Label(dami_data_frame5, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l5.grid(row=0, column=1)
        dami_cust_l5 = Label(dami_data_frame5, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l5.grid(row=0, column=2)
        dami_data_e5 = Entry(dami_data_frame5)
        dami_data_e5.grid(row=1, column=0)
        dami_ora_e5 = Entry(dami_data_frame5)
        dami_ora_e5.grid(row=1, column=1)
        dami_cust_e5 = Entry(dami_data_frame5)
        dami_cust_e5.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame5, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e5, dami_ora_e5, dami_cust_e5))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame5, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e5, dami_ora_e5, dami_cust_e5, dami_tv_day5))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame5, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day5))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame5, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e5, dami_ora_e5, dami_cust_e5))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day5.bind("<Double-1>", lambda x:self.dami_select(dami_data_e5, dami_ora_e5, dami_cust_e5, dami_tv_day5))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day5 = ttk.Treeview(salvo_tv_frame5)
        salvo_tv_day5.place(relwidth=1, relheight=1)
        salvo_scrolly5 = Scrollbar(salvo_tv_frame5, orient=VERTICAL, command=salvo_tv_day5.yview)
        salvo_scrolly5.pack(side=RIGHT, fill=Y)
        salvo_tv_day5.configure(yscrollcommand=salvo_scrolly5.set)

        # Set columns SALVO
        salvo_tv_day5['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day5.column('#0', width=0, stretch=NO)
        salvo_tv_day5.column('ID', width=10, anchor=CENTER)
        salvo_tv_day5.column('Data', width=100, anchor=CENTER)
        salvo_tv_day5.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day5.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day5.heading('#0', text='')
        salvo_tv_day5.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day5.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day5.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day5.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day5.tag_configure('evenrow', background='white')
        salvo_tv_day5.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day5.insert(parent='', index='end', iid=self.salvo_count, values=('', day4.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day5.insert(parent='', index='end', iid=self.salvo_count, values=('', day4.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day4.date():
                        confront_time = day4 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day5.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day5.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day5.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day5.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l5 = Label(salvo_data_frame5, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l5.grid(row=0, column=0)
        salvo_ora_l5 = Label(salvo_data_frame5, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l5.grid(row=0, column=1)
        salvo_cust_l5 = Label(salvo_data_frame5, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l5.grid(row=0, column=2)
        salvo_data_e5 = Entry(salvo_data_frame5)
        salvo_data_e5.grid(row=1, column=0)
        salvo_ora_e5 = Entry(salvo_data_frame5)
        salvo_ora_e5.grid(row=1, column=1)
        salvo_cust_e5 = Entry(salvo_data_frame5)
        salvo_cust_e5.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame5, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e5, salvo_ora_e5, salvo_cust_e5))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame5, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e5, salvo_ora_e5, salvo_cust_e5, salvo_tv_day5))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame5, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day5))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame5, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e5, salvo_ora_e5, salvo_cust_e5))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day5.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e5, salvo_ora_e5, salvo_cust_e5, salvo_tv_day5))

        ####################
        # DAY 6
        ####################
        # Create frames
        dami_tv_frame6 = LabelFrame(self.day6, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame6.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame6 = LabelFrame(self.day6, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame6.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame6 = Frame(self.day6, bg=str(self.color_bg))
        dami_data_frame6.place(x=200, y=580)
        salvo_data_frame6 = Frame(self.day6, bg=str(self.color_bg))
        salvo_data_frame6.place(x=970, y=580)
        dami_button_frame6 = Frame(self.day6, bg=str(self.color_bg))
        dami_button_frame6.place(x=240, y=650)
        salvo_button_frame6 = Frame(self.day6, bg=str(self.color_bg))
        salvo_button_frame6.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day6 = ttk.Treeview(dami_tv_frame6)
        dami_tv_day6.place(relwidth=1, relheight=1)
        dami_scrolly6 = Scrollbar(dami_tv_frame6, orient=VERTICAL, command=dami_tv_day6.yview)
        dami_scrolly6.pack(side=RIGHT, fill=Y)
        dami_tv_day6.configure(yscrollcommand=dami_scrolly6.set)

        # Set columns DAMIANO
        dami_tv_day6['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day6.column('#0', width=0, stretch=NO)
        dami_tv_day6.column('ID', width=10, anchor=CENTER)
        dami_tv_day6.column('Data', width=100, anchor=CENTER)
        dami_tv_day6.column('Ora', width=70, anchor=CENTER)
        dami_tv_day6.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day6.heading('#0', text='')
        dami_tv_day6.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day6.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day6.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day6.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day6.tag_configure('evenrow', background='white')
        dami_tv_day6.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day6.insert(parent='', index='end', iid=self.dami_count, values=('', day5.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day6.insert(parent='', index='end', iid=self.dami_count, values=('', day5.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day5.date():
                        confront_time = day5 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day6.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day6.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day6.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day6.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l6 = Label(dami_data_frame6, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l6.grid(row=0, column=0)
        dami_ora_l6 = Label(dami_data_frame6, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l6.grid(row=0, column=1)
        dami_cust_l6 = Label(dami_data_frame6, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l6.grid(row=0, column=2)
        dami_data_e6 = Entry(dami_data_frame6)
        dami_data_e6.grid(row=1, column=0)
        dami_ora_e6 = Entry(dami_data_frame6)
        dami_ora_e6.grid(row=1, column=1)
        dami_cust_e6 = Entry(dami_data_frame6)
        dami_cust_e6.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame6, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e6, dami_ora_e6, dami_cust_e6))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame6, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e6, dami_ora_e6, dami_cust_e6, dami_tv_day6))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame6, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day6))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame6, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e6, dami_ora_e6, dami_cust_e6))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day6.bind("<Double-1>", lambda x:self.dami_select(dami_data_e6, dami_ora_e6, dami_cust_e6, dami_tv_day6))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day6 = ttk.Treeview(salvo_tv_frame6)
        salvo_tv_day6.place(relwidth=1, relheight=1)
        salvo_scrolly6 = Scrollbar(salvo_tv_frame6, orient=VERTICAL, command=salvo_tv_day6.yview)
        salvo_scrolly6.pack(side=RIGHT, fill=Y)
        salvo_tv_day6.configure(yscrollcommand=salvo_scrolly6.set)

        # Set columns SALVO
        salvo_tv_day6['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day6.column('#0', width=0, stretch=NO)
        salvo_tv_day6.column('ID', width=10, anchor=CENTER)
        salvo_tv_day6.column('Data', width=100, anchor=CENTER)
        salvo_tv_day6.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day6.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day6.heading('#0', text='')
        salvo_tv_day6.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day6.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day6.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day6.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day6.tag_configure('evenrow', background='white')
        salvo_tv_day6.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day6.insert(parent='', index='end', iid=self.salvo_count, values=('', day5.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day6.insert(parent='', index='end', iid=self.salvo_count, values=('', day5.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day5.date():
                        confront_time = day5 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day6.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day6.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day6.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day6.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l6 = Label(salvo_data_frame6, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l6.grid(row=0, column=0)
        salvo_ora_l6 = Label(salvo_data_frame6, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l6.grid(row=0, column=1)
        salvo_cust_l6 = Label(salvo_data_frame6, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l6.grid(row=0, column=2)
        salvo_data_e6 = Entry(salvo_data_frame6)
        salvo_data_e6.grid(row=1, column=0)
        salvo_ora_e6 = Entry(salvo_data_frame6)
        salvo_ora_e6.grid(row=1, column=1)
        salvo_cust_e6 = Entry(salvo_data_frame6)
        salvo_cust_e6.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame6, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e6, salvo_ora_e6, salvo_cust_e6))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame6, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e6, salvo_ora_e6, salvo_cust_e6, salvo_tv_day6))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame6, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day6))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame6, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e6, salvo_ora_e6, salvo_cust_e6))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day6.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e6, salvo_ora_e6, salvo_cust_e6, salvo_tv_day6))

        ####################
        # DAY 7
        ####################
        # Create frames
        dami_tv_frame7 = LabelFrame(self.day7, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame7.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame7 = LabelFrame(self.day7, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame7.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame7 = Frame(self.day7, bg=str(self.color_bg))
        dami_data_frame7.place(x=200, y=580)
        salvo_data_frame7 = Frame(self.day7, bg=str(self.color_bg))
        salvo_data_frame7.place(x=970, y=580)
        dami_button_frame7 = Frame(self.day7, bg=str(self.color_bg))
        dami_button_frame7.place(x=240, y=650)
        salvo_button_frame7 = Frame(self.day7, bg=str(self.color_bg))
        salvo_button_frame7.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day7 = ttk.Treeview(dami_tv_frame7)
        dami_tv_day7.place(relwidth=1, relheight=1)
        dami_scrolly7 = Scrollbar(dami_tv_frame7, orient=VERTICAL, command=dami_tv_day7.yview)
        dami_scrolly7.pack(side=RIGHT, fill=Y)
        dami_tv_day7.configure(yscrollcommand=dami_scrolly7.set)

        # Set columns DAMIANO
        dami_tv_day7['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day7.column('#0', width=0, stretch=NO)
        dami_tv_day7.column('ID', width=10, anchor=CENTER)
        dami_tv_day7.column('Data', width=100, anchor=CENTER)
        dami_tv_day7.column('Ora', width=70, anchor=CENTER)
        dami_tv_day7.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day7.heading('#0', text='')
        dami_tv_day7.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day7.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day7.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day7.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day7.tag_configure('evenrow', background='white')
        dami_tv_day7.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day7.insert(parent='', index='end', iid=self.dami_count, values=('', day6.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day7.insert(parent='', index='end', iid=self.dami_count, values=('', day6.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day6.date():
                        confront_time = day6 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day7.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day7.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day7.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day7.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l7 = Label(dami_data_frame7, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l7.grid(row=0, column=0)
        dami_ora_l7 = Label(dami_data_frame7, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l7.grid(row=0, column=1)
        dami_cust_l7 = Label(dami_data_frame7, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l7.grid(row=0, column=2)
        dami_data_e7 = Entry(dami_data_frame7)
        dami_data_e7.grid(row=1, column=0)
        dami_ora_e7 = Entry(dami_data_frame7)
        dami_ora_e7.grid(row=1, column=1)
        dami_cust_e7 = Entry(dami_data_frame7)
        dami_cust_e7.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame7, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e7, dami_ora_e7, dami_cust_e7))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame7, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e7, dami_ora_e7, dami_cust_e7, dami_tv_day7))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame7, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day7))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame7, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e7, dami_ora_e7, dami_cust_e7))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day7.bind("<Double-1>", lambda x:self.dami_select(dami_data_e7, dami_ora_e7, dami_cust_e7, dami_tv_day7))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day7 = ttk.Treeview(salvo_tv_frame7)
        salvo_tv_day7.place(relwidth=1, relheight=1)
        salvo_scrolly7 = Scrollbar(salvo_tv_frame7, orient=VERTICAL, command=salvo_tv_day7.yview)
        salvo_scrolly7.pack(side=RIGHT, fill=Y)
        salvo_tv_day7.configure(yscrollcommand=salvo_scrolly7.set)

        # Set columns SALVO
        salvo_tv_day7['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day7.column('#0', width=0, stretch=NO)
        salvo_tv_day7.column('ID', width=10, anchor=CENTER)
        salvo_tv_day7.column('Data', width=100, anchor=CENTER)
        salvo_tv_day7.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day7.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day7.heading('#0', text='')
        salvo_tv_day7.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day7.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day7.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day7.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day7.tag_configure('evenrow', background='white')
        salvo_tv_day7.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day7.insert(parent='', index='end', iid=self.salvo_count, values=('', day6.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day7.insert(parent='', index='end', iid=self.salvo_count, values=('', day6.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day6.date():
                        confront_time = day6 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day7.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day7.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day7.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day7.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l7 = Label(salvo_data_frame7, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l7.grid(row=0, column=0)
        salvo_ora_l7 = Label(salvo_data_frame7, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l7.grid(row=0, column=1)
        salvo_cust_l7 = Label(salvo_data_frame7, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l7.grid(row=0, column=2)
        salvo_data_e7 = Entry(salvo_data_frame7)
        salvo_data_e7.grid(row=1, column=0)
        salvo_ora_e7 = Entry(salvo_data_frame7)
        salvo_ora_e7.grid(row=1, column=1)
        salvo_cust_e7 = Entry(salvo_data_frame7)
        salvo_cust_e7.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame7, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e7, salvo_ora_e7, salvo_cust_e7))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame7, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e7, salvo_ora_e7, salvo_cust_e7, salvo_tv_day7))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame7, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day7))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame7, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e7, salvo_ora_e7, salvo_cust_e7))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day7.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e7, salvo_ora_e7, salvo_cust_e7, salvo_tv_day7))

        ####################
        # DAY 8
        ####################
        # Create frames
        dami_tv_frame8 = LabelFrame(self.day8, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame8.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame8 = LabelFrame(self.day8, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame8.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame8 = Frame(self.day8, bg=str(self.color_bg))
        dami_data_frame8.place(x=200, y=580)
        salvo_data_frame8 = Frame(self.day8, bg=str(self.color_bg))
        salvo_data_frame8.place(x=970, y=580)
        dami_button_frame8 = Frame(self.day8, bg=str(self.color_bg))
        dami_button_frame8.place(x=240, y=650)
        salvo_button_frame8 = Frame(self.day8, bg=str(self.color_bg))
        salvo_button_frame8.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day8 = ttk.Treeview(dami_tv_frame8)
        dami_tv_day8.place(relwidth=1, relheight=1)
        dami_scrolly8 = Scrollbar(dami_tv_frame8, orient=VERTICAL, command=dami_tv_day8.yview)
        dami_scrolly8.pack(side=RIGHT, fill=Y)
        dami_tv_day8.configure(yscrollcommand=dami_scrolly8.set)

        # Set columns DAMIANO
        dami_tv_day8['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day8.column('#0', width=0, stretch=NO)
        dami_tv_day8.column('ID', width=10, anchor=CENTER)
        dami_tv_day8.column('Data', width=100, anchor=CENTER)
        dami_tv_day8.column('Ora', width=70, anchor=CENTER)
        dami_tv_day8.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day8.heading('#0', text='')
        dami_tv_day8.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day8.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day8.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day8.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day8.tag_configure('evenrow', background='white')
        dami_tv_day8.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day8.insert(parent='', index='end', iid=self.dami_count, values=('', day7.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day8.insert(parent='', index='end', iid=self.dami_count, values=('', day7.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day7.date():
                        confront_time = day7 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day8.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day8.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day8.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day8.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l8 = Label(dami_data_frame8, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l8.grid(row=0, column=0)
        dami_ora_l8 = Label(dami_data_frame8, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l8.grid(row=0, column=1)
        dami_cust_l8 = Label(dami_data_frame8, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l8.grid(row=0, column=2)
        dami_data_e8 = Entry(dami_data_frame8)
        dami_data_e8.grid(row=1, column=0)
        dami_ora_e8 = Entry(dami_data_frame8)
        dami_ora_e8.grid(row=1, column=1)
        dami_cust_e8 = Entry(dami_data_frame8)
        dami_cust_e8.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame8, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e8, dami_ora_e8, dami_cust_e8))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame8, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e8, dami_ora_e8, dami_cust_e8, dami_tv_day8))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame8, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day8))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame8, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e8, dami_ora_e8, dami_cust_e8))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day8.bind("<Double-1>", lambda x:self.dami_select(dami_data_e8, dami_ora_e8, dami_cust_e8, dami_tv_day8))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day8 = ttk.Treeview(salvo_tv_frame8)
        salvo_tv_day8.place(relwidth=1, relheight=1)
        salvo_scrolly8 = Scrollbar(salvo_tv_frame8, orient=VERTICAL, command=salvo_tv_day8.yview)
        salvo_scrolly8.pack(side=RIGHT, fill=Y)
        salvo_tv_day8.configure(yscrollcommand=salvo_scrolly8.set)

        # Set columns SALVO
        salvo_tv_day8['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day8.column('#0', width=0, stretch=NO)
        salvo_tv_day8.column('ID', width=10, anchor=CENTER)
        salvo_tv_day8.column('Data', width=100, anchor=CENTER)
        salvo_tv_day8.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day8.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day8.heading('#0', text='')
        salvo_tv_day8.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day8.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day8.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day8.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day8.tag_configure('evenrow', background='white')
        salvo_tv_day8.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day8.insert(parent='', index='end', iid=self.salvo_count, values=('', day7.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day8.insert(parent='', index='end', iid=self.salvo_count, values=('', day7.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day7.date():
                        confront_time = day7 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day8.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day8.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day8.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day8.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l8 = Label(salvo_data_frame8, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l8.grid(row=0, column=0)
        salvo_ora_l8 = Label(salvo_data_frame8, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l8.grid(row=0, column=1)
        salvo_cust_l8 = Label(salvo_data_frame8, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l8.grid(row=0, column=2)
        salvo_data_e8 = Entry(salvo_data_frame8)
        salvo_data_e8.grid(row=1, column=0)
        salvo_ora_e8 = Entry(salvo_data_frame8)
        salvo_ora_e8.grid(row=1, column=1)
        salvo_cust_e8 = Entry(salvo_data_frame8)
        salvo_cust_e8.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame8, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e8, salvo_ora_e8, salvo_cust_e8))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame8, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e8, salvo_ora_e8, salvo_cust_e8, salvo_tv_day8))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame8, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day8))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame8, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e8, salvo_ora_e8, salvo_cust_e8))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day8.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e8, salvo_ora_e8, salvo_cust_e8, salvo_tv_day8))

        ####################
        # DAY 9
        ####################
        # Create frames
        dami_tv_frame9 = LabelFrame(self.day9, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame9.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame9 = LabelFrame(self.day9, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame9.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame9 = Frame(self.day9, bg=str(self.color_bg))
        dami_data_frame9.place(x=200, y=580)
        salvo_data_frame9 = Frame(self.day9, bg=str(self.color_bg))
        salvo_data_frame9.place(x=970, y=580)
        dami_button_frame9 = Frame(self.day9, bg=str(self.color_bg))
        dami_button_frame9.place(x=240, y=650)
        salvo_button_frame9 = Frame(self.day9, bg=str(self.color_bg))
        salvo_button_frame9.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day9 = ttk.Treeview(dami_tv_frame9)
        dami_tv_day9.place(relwidth=1, relheight=1)
        dami_scrolly9 = Scrollbar(dami_tv_frame9, orient=VERTICAL, command=dami_tv_day9.yview)
        dami_scrolly9.pack(side=RIGHT, fill=Y)
        dami_tv_day9.configure(yscrollcommand=dami_scrolly9.set)

        # Set columns DAMIANO
        dami_tv_day9['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day9.column('#0', width=0, stretch=NO)
        dami_tv_day9.column('ID', width=10, anchor=CENTER)
        dami_tv_day9.column('Data', width=100, anchor=CENTER)
        dami_tv_day9.column('Ora', width=70, anchor=CENTER)
        dami_tv_day9.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day9.heading('#0', text='')
        dami_tv_day9.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day9.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day9.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day9.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day9.tag_configure('evenrow', background='white')
        dami_tv_day9.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day9.insert(parent='', index='end', iid=self.dami_count, values=('', day8.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day9.insert(parent='', index='end', iid=self.dami_count, values=('', day8.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day8.date():
                        confront_time = day8 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day9.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day9.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day9.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day9.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l9 = Label(dami_data_frame9, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l9.grid(row=0, column=0)
        dami_ora_l9 = Label(dami_data_frame9, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l9.grid(row=0, column=1)
        dami_cust_l9 = Label(dami_data_frame9, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l9.grid(row=0, column=2)
        dami_data_e9 = Entry(dami_data_frame9)
        dami_data_e9.grid(row=1, column=0)
        dami_ora_e9 = Entry(dami_data_frame9)
        dami_ora_e9.grid(row=1, column=1)
        dami_cust_e9 = Entry(dami_data_frame9)
        dami_cust_e9.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame9, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e9, dami_ora_e9, dami_cust_e9))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame9, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e9, dami_ora_e9, dami_cust_e9, dami_tv_day9))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame9, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day9))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame9, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e9, dami_ora_e9, dami_cust_e9))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day9.bind("<Double-1>", lambda x:self.dami_select(dami_data_e9, dami_ora_e9, dami_cust_e9, dami_tv_day9))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day9 = ttk.Treeview(salvo_tv_frame9)
        salvo_tv_day9.place(relwidth=1, relheight=1)
        salvo_scrolly9 = Scrollbar(salvo_tv_frame9, orient=VERTICAL, command=salvo_tv_day9.yview)
        salvo_scrolly9.pack(side=RIGHT, fill=Y)
        salvo_tv_day9.configure(yscrollcommand=salvo_scrolly9.set)

        # Set columns SALVO
        salvo_tv_day9['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day9.column('#0', width=0, stretch=NO)
        salvo_tv_day9.column('ID', width=10, anchor=CENTER)
        salvo_tv_day9.column('Data', width=100, anchor=CENTER)
        salvo_tv_day9.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day9.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day9.heading('#0', text='')
        salvo_tv_day9.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day9.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day9.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day9.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day9.tag_configure('evenrow', background='white')
        salvo_tv_day9.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day9.insert(parent='', index='end', iid=self.salvo_count, values=('', day8.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day9.insert(parent='', index='end', iid=self.salvo_count, values=('', day8.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day8.date():
                        confront_time = day8 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day9.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day9.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day9.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day9.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l9 = Label(salvo_data_frame9, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l9.grid(row=0, column=0)
        salvo_ora_l9 = Label(salvo_data_frame9, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l9.grid(row=0, column=1)
        salvo_cust_l9 = Label(salvo_data_frame9, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l9.grid(row=0, column=2)
        salvo_data_e9 = Entry(salvo_data_frame9)
        salvo_data_e9.grid(row=1, column=0)
        salvo_ora_e9 = Entry(salvo_data_frame9)
        salvo_ora_e9.grid(row=1, column=1)
        salvo_cust_e9 = Entry(salvo_data_frame9)
        salvo_cust_e9.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame9, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e9, salvo_ora_e9, salvo_cust_e9))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame9, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e9, salvo_ora_e9, salvo_cust_e9, salvo_tv_day9))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame9, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day9))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame9, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e9, salvo_ora_e9, salvo_cust_e9))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day9.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e9, salvo_ora_e9, salvo_cust_e9, salvo_tv_day9))

        ####################
        # DAY 10
        ####################
        # Create frames
        dami_tv_frame10 = LabelFrame(self.day10, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame10.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame10 = LabelFrame(self.day10, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame10.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame10 = Frame(self.day10, bg=str(self.color_bg))
        dami_data_frame10.place(x=200, y=580)
        salvo_data_frame10 = Frame(self.day10, bg=str(self.color_bg))
        salvo_data_frame10.place(x=970, y=580)
        dami_button_frame10 = Frame(self.day10, bg=str(self.color_bg))
        dami_button_frame10.place(x=240, y=650)
        salvo_button_frame10 = Frame(self.day10, bg=str(self.color_bg))
        salvo_button_frame10.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day10 = ttk.Treeview(dami_tv_frame10)
        dami_tv_day10.place(relwidth=1, relheight=1)
        dami_scrolly10 = Scrollbar(dami_tv_frame10, orient=VERTICAL, command=dami_tv_day10.yview)
        dami_scrolly10.pack(side=RIGHT, fill=Y)
        dami_tv_day10.configure(yscrollcommand=dami_scrolly10.set)

        # Set columns DAMIANO
        dami_tv_day10['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day10.column('#0', width=0, stretch=NO)
        dami_tv_day10.column('ID', width=10, anchor=CENTER)
        dami_tv_day10.column('Data', width=100, anchor=CENTER)
        dami_tv_day10.column('Ora', width=70, anchor=CENTER)
        dami_tv_day10.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day10.heading('#0', text='')
        dami_tv_day10.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day10.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day10.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day10.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day10.tag_configure('evenrow', background='white')
        dami_tv_day10.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day10.insert(parent='', index='end', iid=self.dami_count, values=('', day9.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day10.insert(parent='', index='end', iid=self.dami_count, values=('', day9.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day9.date():
                        confront_time = day9 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day10.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day10.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day10.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day10.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l10 = Label(dami_data_frame10, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l10.grid(row=0, column=0)
        dami_ora_l10 = Label(dami_data_frame10, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l10.grid(row=0, column=1)
        dami_cust_l10 = Label(dami_data_frame10, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l10.grid(row=0, column=2)
        dami_data_e10 = Entry(dami_data_frame10)
        dami_data_e10.grid(row=1, column=0)
        dami_ora_e10 = Entry(dami_data_frame10)
        dami_ora_e10.grid(row=1, column=1)
        dami_cust_e10 = Entry(dami_data_frame10)
        dami_cust_e10.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame10, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e10, dami_ora_e10, dami_cust_e10))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame10, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e10, dami_ora_e10, dami_cust_e10, dami_tv_day10))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame10, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day10))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame10, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e10, dami_ora_e10, dami_cust_e10))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day10.bind("<Double-1>", lambda x:self.dami_select(dami_data_e10, dami_ora_e10, dami_cust_e10, dami_tv_day10))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day10 = ttk.Treeview(salvo_tv_frame10)
        salvo_tv_day10.place(relwidth=1, relheight=1)
        salvo_scrolly10 = Scrollbar(salvo_tv_frame10, orient=VERTICAL, command=salvo_tv_day10.yview)
        salvo_scrolly10.pack(side=RIGHT, fill=Y)
        salvo_tv_day10.configure(yscrollcommand=salvo_scrolly10.set)

        # Set columns SALVO
        salvo_tv_day10['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day10.column('#0', width=0, stretch=NO)
        salvo_tv_day10.column('ID', width=10, anchor=CENTER)
        salvo_tv_day10.column('Data', width=100, anchor=CENTER)
        salvo_tv_day10.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day10.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day10.heading('#0', text='')
        salvo_tv_day10.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day10.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day10.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day10.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day10.tag_configure('evenrow', background='white')
        salvo_tv_day10.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day10.insert(parent='', index='end', iid=self.salvo_count, values=('', day9.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day10.insert(parent='', index='end', iid=self.salvo_count, values=('', day9.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day9.date():
                        confront_time = day9 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day10.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day10.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day10.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day10.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l10 = Label(salvo_data_frame10, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l10.grid(row=0, column=0)
        salvo_ora_l10 = Label(salvo_data_frame10, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l10.grid(row=0, column=1)
        salvo_cust_l10 = Label(salvo_data_frame10, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l10.grid(row=0, column=2)
        salvo_data_e10 = Entry(salvo_data_frame10)
        salvo_data_e10.grid(row=1, column=0)
        salvo_ora_e10 = Entry(salvo_data_frame10)
        salvo_ora_e10.grid(row=1, column=1)
        salvo_cust_e10 = Entry(salvo_data_frame10)
        salvo_cust_e10.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame10, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e10, salvo_ora_e10, salvo_cust_e10))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame10, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e10, salvo_ora_e10, salvo_cust_e10, salvo_tv_day10))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame10, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day10))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame10, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e10, salvo_ora_e10, salvo_cust_e10))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day10.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e10, salvo_ora_e10, salvo_cust_e10, salvo_tv_day10))

        ####################
        # DAY 11
        ####################
        # Create frames
        dami_tv_frame11 = LabelFrame(self.day11, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame11.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame11 = LabelFrame(self.day11, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame11.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame11 = Frame(self.day11, bg=str(self.color_bg))
        dami_data_frame11.place(x=200, y=580)
        salvo_data_frame11 = Frame(self.day11, bg=str(self.color_bg))
        salvo_data_frame11.place(x=970, y=580)
        dami_button_frame11 = Frame(self.day11, bg=str(self.color_bg))
        dami_button_frame11.place(x=240, y=650)
        salvo_button_frame11 = Frame(self.day11, bg=str(self.color_bg))
        salvo_button_frame11.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day11 = ttk.Treeview(dami_tv_frame11)
        dami_tv_day11.place(relwidth=1, relheight=1)
        dami_scrolly11 = Scrollbar(dami_tv_frame11, orient=VERTICAL, command=dami_tv_day11.yview)
        dami_scrolly11.pack(side=RIGHT, fill=Y)
        dami_tv_day11.configure(yscrollcommand=dami_scrolly11.set)

        # Set columns DAMIANO
        dami_tv_day11['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day11.column('#0', width=0, stretch=NO)
        dami_tv_day11.column('ID', width=10, anchor=CENTER)
        dami_tv_day11.column('Data', width=100, anchor=CENTER)
        dami_tv_day11.column('Ora', width=70, anchor=CENTER)
        dami_tv_day11.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day11.heading('#0', text='')
        dami_tv_day11.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day11.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day11.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day11.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day11.tag_configure('evenrow', background='white')
        dami_tv_day11.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day11.insert(parent='', index='end', iid=self.dami_count, values=('', day10.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day11.insert(parent='', index='end', iid=self.dami_count, values=('', day10.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day10.date():
                        confront_time = day10 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day11.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day11.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day11.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day11.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l11 = Label(dami_data_frame11, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l11.grid(row=0, column=0)
        dami_ora_l11 = Label(dami_data_frame11, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l11.grid(row=0, column=1)
        dami_cust_l11 = Label(dami_data_frame11, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l11.grid(row=0, column=2)
        dami_data_e11 = Entry(dami_data_frame11)
        dami_data_e11.grid(row=1, column=0)
        dami_ora_e11 = Entry(dami_data_frame11)
        dami_ora_e11.grid(row=1, column=1)
        dami_cust_e11 = Entry(dami_data_frame11)
        dami_cust_e11.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame11, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e11, dami_ora_e11, dami_cust_e11))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame11, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e11, dami_ora_e11, dami_cust_e11, dami_tv_day11))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame11, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day11))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame11, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e11, dami_ora_e11, dami_cust_e11))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day11.bind("<Double-1>", lambda x:self.dami_select(dami_data_e11, dami_ora_e11, dami_cust_e11, dami_tv_day11))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day11 = ttk.Treeview(salvo_tv_frame11)
        salvo_tv_day11.place(relwidth=1, relheight=1)
        salvo_scrolly11 = Scrollbar(salvo_tv_frame11, orient=VERTICAL, command=salvo_tv_day11.yview)
        salvo_scrolly11.pack(side=RIGHT, fill=Y)
        salvo_tv_day11.configure(yscrollcommand=salvo_scrolly11.set)

        # Set columns SALVO
        salvo_tv_day11['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day11.column('#0', width=0, stretch=NO)
        salvo_tv_day11.column('ID', width=10, anchor=CENTER)
        salvo_tv_day11.column('Data', width=100, anchor=CENTER)
        salvo_tv_day11.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day11.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day11.heading('#0', text='')
        salvo_tv_day11.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day11.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day11.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day11.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day11.tag_configure('evenrow', background='white')
        salvo_tv_day11.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day11.insert(parent='', index='end', iid=self.salvo_count, values=('', day10.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day11.insert(parent='', index='end', iid=self.salvo_count, values=('', day10.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day10.date():
                        confront_time = day10 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day11.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day11.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day11.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day11.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l11 = Label(salvo_data_frame11, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l11.grid(row=0, column=0)
        salvo_ora_l11 = Label(salvo_data_frame11, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l11.grid(row=0, column=1)
        salvo_cust_l11 = Label(salvo_data_frame11, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l11.grid(row=0, column=2)
        salvo_data_e11 = Entry(salvo_data_frame11)
        salvo_data_e11.grid(row=1, column=0)
        salvo_ora_e11 = Entry(salvo_data_frame11)
        salvo_ora_e11.grid(row=1, column=1)
        salvo_cust_e11 = Entry(salvo_data_frame11)
        salvo_cust_e11.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame11, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e11, salvo_ora_e11, salvo_cust_e11))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame11, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e11, salvo_ora_e11, salvo_cust_e11, salvo_tv_day11))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame11, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day11))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame11, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e11, salvo_ora_e11, salvo_cust_e11))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day11.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e11, salvo_ora_e11, salvo_cust_e11, salvo_tv_day11))

        ####################
        # DAY 12
        ####################
        # Create frames
        dami_tv_frame12 = LabelFrame(self.day12, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame12.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame12 = LabelFrame(self.day12, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame12.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame12 = Frame(self.day12, bg=str(self.color_bg))
        dami_data_frame12.place(x=200, y=580)
        salvo_data_frame12 = Frame(self.day12, bg=str(self.color_bg))
        salvo_data_frame12.place(x=970, y=580)
        dami_button_frame12 = Frame(self.day12, bg=str(self.color_bg))
        dami_button_frame12.place(x=240, y=650)
        salvo_button_frame12 = Frame(self.day12, bg=str(self.color_bg))
        salvo_button_frame12.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day12 = ttk.Treeview(dami_tv_frame12)
        dami_tv_day12.place(relwidth=1, relheight=1)
        dami_scrolly12 = Scrollbar(dami_tv_frame12, orient=VERTICAL, command=dami_tv_day12.yview)
        dami_scrolly12.pack(side=RIGHT, fill=Y)
        dami_tv_day12.configure(yscrollcommand=dami_scrolly12.set)

        # Set columns DAMIANO
        dami_tv_day12['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day12.column('#0', width=0, stretch=NO)
        dami_tv_day12.column('ID', width=10, anchor=CENTER)
        dami_tv_day12.column('Data', width=100, anchor=CENTER)
        dami_tv_day12.column('Ora', width=70, anchor=CENTER)
        dami_tv_day12.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day12.heading('#0', text='')
        dami_tv_day12.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day12.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day12.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day12.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day12.tag_configure('evenrow', background='white')
        dami_tv_day12.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day12.insert(parent='', index='end', iid=self.dami_count, values=('', day11.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day12.insert(parent='', index='end', iid=self.dami_count, values=('', day11.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day11.date():
                        confront_time = day11 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day12.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day12.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day12.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day12.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l12 = Label(dami_data_frame12, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l12.grid(row=0, column=0)
        dami_ora_l12 = Label(dami_data_frame12, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l12.grid(row=0, column=1)
        dami_cust_l12 = Label(dami_data_frame12, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l12.grid(row=0, column=2)
        dami_data_e12 = Entry(dami_data_frame12)
        dami_data_e12.grid(row=1, column=0)
        dami_ora_e12 = Entry(dami_data_frame12)
        dami_ora_e12.grid(row=1, column=1)
        dami_cust_e12 = Entry(dami_data_frame12)
        dami_cust_e12.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame12, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e12, dami_ora_e12, dami_cust_e12))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame12, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e12, dami_ora_e12, dami_cust_e12, dami_tv_day12))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame12, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day12))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame12, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e12, dami_ora_e12, dami_cust_e12))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day12.bind("<Double-1>", lambda x:self.dami_select(dami_data_e12, dami_ora_e12, dami_cust_e12, dami_tv_day12))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day12 = ttk.Treeview(salvo_tv_frame12)
        salvo_tv_day12.place(relwidth=1, relheight=1)
        salvo_scrolly12 = Scrollbar(salvo_tv_frame12, orient=VERTICAL, command=salvo_tv_day12.yview)
        salvo_scrolly12.pack(side=RIGHT, fill=Y)
        salvo_tv_day12.configure(yscrollcommand=salvo_scrolly12.set)

        # Set columns SALVO
        salvo_tv_day12['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day12.column('#0', width=0, stretch=NO)
        salvo_tv_day12.column('ID', width=10, anchor=CENTER)
        salvo_tv_day12.column('Data', width=100, anchor=CENTER)
        salvo_tv_day12.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day12.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day12.heading('#0', text='')
        salvo_tv_day12.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day12.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day12.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day12.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day12.tag_configure('evenrow', background='white')
        salvo_tv_day12.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day12.insert(parent='', index='end', iid=self.salvo_count, values=('', day11.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day12.insert(parent='', index='end', iid=self.salvo_count, values=('', day11.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day11.date():
                        confront_time = day11 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day12.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day12.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day12.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day12.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l12 = Label(salvo_data_frame12, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l12.grid(row=0, column=0)
        salvo_ora_l12 = Label(salvo_data_frame12, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l12.grid(row=0, column=1)
        salvo_cust_l12 = Label(salvo_data_frame12, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l12.grid(row=0, column=2)
        salvo_data_e12 = Entry(salvo_data_frame12)
        salvo_data_e12.grid(row=1, column=0)
        salvo_ora_e12 = Entry(salvo_data_frame12)
        salvo_ora_e12.grid(row=1, column=1)
        salvo_cust_e12 = Entry(salvo_data_frame12)
        salvo_cust_e12.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame12, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e12, salvo_ora_e12, salvo_cust_e12))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame12, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e12, salvo_ora_e12, salvo_cust_e12, salvo_tv_day12))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame12, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day12))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame12, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e12, salvo_ora_e12, salvo_cust_e12))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day12.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e12, salvo_ora_e12, salvo_cust_e12, salvo_tv_day12))

        ####################
        # DAY 13
        ####################
        # Create frames
        dami_tv_frame13 = LabelFrame(self.day13, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame13.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame13 = LabelFrame(self.day13, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame13.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame13 = Frame(self.day13, bg=str(self.color_bg))
        dami_data_frame13.place(x=200, y=580)
        salvo_data_frame13 = Frame(self.day13, bg=str(self.color_bg))
        salvo_data_frame13.place(x=970, y=580)
        dami_button_frame13 = Frame(self.day13, bg=str(self.color_bg))
        dami_button_frame13.place(x=240, y=650)
        salvo_button_frame13 = Frame(self.day13, bg=str(self.color_bg))
        salvo_button_frame13.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day13 = ttk.Treeview(dami_tv_frame13)
        dami_tv_day13.place(relwidth=1, relheight=1)
        dami_scrolly13 = Scrollbar(dami_tv_frame13, orient=VERTICAL, command=dami_tv_day13.yview)
        dami_scrolly13.pack(side=RIGHT, fill=Y)
        dami_tv_day13.configure(yscrollcommand=dami_scrolly13.set)

        # Set columns DAMIANO
        dami_tv_day13['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day13.column('#0', width=0, stretch=NO)
        dami_tv_day13.column('ID', width=10, anchor=CENTER)
        dami_tv_day13.column('Data', width=100, anchor=CENTER)
        dami_tv_day13.column('Ora', width=70, anchor=CENTER)
        dami_tv_day13.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day13.heading('#0', text='')
        dami_tv_day13.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day13.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day13.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day13.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day13.tag_configure('evenrow', background='white')
        dami_tv_day13.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day13.insert(parent='', index='end', iid=self.dami_count, values=('', day12.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day13.insert(parent='', index='end', iid=self.dami_count, values=('', day12.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day12.date():
                        confront_time = day12 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day13.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day13.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day13.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day13.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l13 = Label(dami_data_frame13, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l13.grid(row=0, column=0)
        dami_ora_l13 = Label(dami_data_frame13, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l13.grid(row=0, column=1)
        dami_cust_l13 = Label(dami_data_frame13, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l13.grid(row=0, column=2)
        dami_data_e13 = Entry(dami_data_frame13)
        dami_data_e13.grid(row=1, column=0)
        dami_ora_e13 = Entry(dami_data_frame13)
        dami_ora_e13.grid(row=1, column=1)
        dami_cust_e13 = Entry(dami_data_frame13)
        dami_cust_e13.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame13, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e13, dami_ora_e13, dami_cust_e13))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame13, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e13, dami_ora_e13, dami_cust_e13, dami_tv_day13))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame13, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day13))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame13, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e13, dami_ora_e13, dami_cust_e13))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day13.bind("<Double-1>", lambda x:self.dami_select(dami_data_e13, dami_ora_e13, dami_cust_e13, dami_tv_day13))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day13 = ttk.Treeview(salvo_tv_frame13)
        salvo_tv_day13.place(relwidth=1, relheight=1)
        salvo_scrolly13 = Scrollbar(salvo_tv_frame13, orient=VERTICAL, command=salvo_tv_day13.yview)
        salvo_scrolly13.pack(side=RIGHT, fill=Y)
        salvo_tv_day13.configure(yscrollcommand=salvo_scrolly13.set)

        # Set columns SALVO
        salvo_tv_day13['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day13.column('#0', width=0, stretch=NO)
        salvo_tv_day13.column('ID', width=10, anchor=CENTER)
        salvo_tv_day13.column('Data', width=100, anchor=CENTER)
        salvo_tv_day13.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day13.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day13.heading('#0', text='')
        salvo_tv_day13.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day13.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day13.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day13.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day13.tag_configure('evenrow', background='white')
        salvo_tv_day13.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day13.insert(parent='', index='end', iid=self.salvo_count, values=('', day12.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day13.insert(parent='', index='end', iid=self.salvo_count, values=('', day12.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day12.date():
                        confront_time = day12 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day13.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day13.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day13.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day13.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l13 = Label(salvo_data_frame13, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l13.grid(row=0, column=0)
        salvo_ora_l13 = Label(salvo_data_frame13, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l13.grid(row=0, column=1)
        salvo_cust_l13 = Label(salvo_data_frame13, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l13.grid(row=0, column=2)
        salvo_data_e13 = Entry(salvo_data_frame13)
        salvo_data_e13.grid(row=1, column=0)
        salvo_ora_e13 = Entry(salvo_data_frame13)
        salvo_ora_e13.grid(row=1, column=1)
        salvo_cust_e13 = Entry(salvo_data_frame13)
        salvo_cust_e13.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame13, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e13, salvo_ora_e13, salvo_cust_e13))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame13, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e13, salvo_ora_e13, salvo_cust_e13, salvo_tv_day13))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame13, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day13))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame13, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e13, salvo_ora_e13, salvo_cust_e13))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day13.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e13, salvo_ora_e13, salvo_cust_e13, salvo_tv_day13))

        ####################
        # DAY 14
        ####################
        # Create frames
        dami_tv_frame14 = LabelFrame(self.day14, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame14.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame14 = LabelFrame(self.day14, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame14.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame14 = Frame(self.day14, bg=str(self.color_bg))
        dami_data_frame14.place(x=200, y=580)
        salvo_data_frame14 = Frame(self.day14, bg=str(self.color_bg))
        salvo_data_frame14.place(x=970, y=580)
        dami_button_frame14 = Frame(self.day14, bg=str(self.color_bg))
        dami_button_frame14.place(x=240, y=650)
        salvo_button_frame14 = Frame(self.day14, bg=str(self.color_bg))
        salvo_button_frame14.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day14 = ttk.Treeview(dami_tv_frame14)
        dami_tv_day14.place(relwidth=1, relheight=1)
        dami_scrolly14 = Scrollbar(dami_tv_frame14, orient=VERTICAL, command=dami_tv_day14.yview)
        dami_scrolly14.pack(side=RIGHT, fill=Y)
        dami_tv_day14.configure(yscrollcommand=dami_scrolly14.set)

        # Set columns DAMIANO
        dami_tv_day14['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day14.column('#0', width=0, stretch=NO)
        dami_tv_day14.column('ID', width=10, anchor=CENTER)
        dami_tv_day14.column('Data', width=100, anchor=CENTER)
        dami_tv_day14.column('Ora', width=70, anchor=CENTER)
        dami_tv_day14.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day14.heading('#0', text='')
        dami_tv_day14.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day14.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day14.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day14.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day14.tag_configure('evenrow', background='white')
        dami_tv_day14.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day14.insert(parent='', index='end', iid=self.dami_count, values=('', day13.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day14.insert(parent='', index='end', iid=self.dami_count, values=('', day13.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day13.date():
                        confront_time = day13 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day14.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day14.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day14.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day14.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l14 = Label(dami_data_frame14, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l14.grid(row=0, column=0)
        dami_ora_l14 = Label(dami_data_frame14, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l14.grid(row=0, column=1)
        dami_cust_l14 = Label(dami_data_frame14, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l14.grid(row=0, column=2)
        dami_data_e14 = Entry(dami_data_frame14)
        dami_data_e14.grid(row=1, column=0)
        dami_ora_e14 = Entry(dami_data_frame14)
        dami_ora_e14.grid(row=1, column=1)
        dami_cust_e14 = Entry(dami_data_frame14)
        dami_cust_e14.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame14, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e14, dami_ora_e14, dami_cust_e14))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame14, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e14, dami_ora_e14, dami_cust_e14, dami_tv_day14))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame14, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day14))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame14, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e14, dami_ora_e14, dami_cust_e14))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day14.bind("<Double-1>", lambda x:self.dami_select(dami_data_e14, dami_ora_e14, dami_cust_e14, dami_tv_day14))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day14 = ttk.Treeview(salvo_tv_frame14)
        salvo_tv_day14.place(relwidth=1, relheight=1)
        salvo_scrolly14 = Scrollbar(salvo_tv_frame14, orient=VERTICAL, command=salvo_tv_day14.yview)
        salvo_scrolly14.pack(side=RIGHT, fill=Y)
        salvo_tv_day14.configure(yscrollcommand=salvo_scrolly14.set)

        # Set columns SALVO
        salvo_tv_day14['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day14.column('#0', width=0, stretch=NO)
        salvo_tv_day14.column('ID', width=10, anchor=CENTER)
        salvo_tv_day14.column('Data', width=100, anchor=CENTER)
        salvo_tv_day14.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day14.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day14.heading('#0', text='')
        salvo_tv_day14.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day14.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day14.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day14.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day14.tag_configure('evenrow', background='white')
        salvo_tv_day14.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day14.insert(parent='', index='end', iid=self.salvo_count, values=('', day13.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day14.insert(parent='', index='end', iid=self.salvo_count, values=('', day13.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day13.date():
                        confront_time = day13 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day14.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day14.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day14.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day14.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l14 = Label(salvo_data_frame14, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l14.grid(row=0, column=0)
        salvo_ora_l14 = Label(salvo_data_frame14, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l14.grid(row=0, column=1)
        salvo_cust_l14 = Label(salvo_data_frame14, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l14.grid(row=0, column=2)
        salvo_data_e14 = Entry(salvo_data_frame14)
        salvo_data_e14.grid(row=1, column=0)
        salvo_ora_e14 = Entry(salvo_data_frame14)
        salvo_ora_e14.grid(row=1, column=1)
        salvo_cust_e14 = Entry(salvo_data_frame14)
        salvo_cust_e14.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame14, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e14, salvo_ora_e14, salvo_cust_e14))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame14, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e14, salvo_ora_e14, salvo_cust_e14, salvo_tv_day14))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame14, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day14))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame14, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e14, salvo_ora_e14, salvo_cust_e14))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day14.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e14, salvo_ora_e14, salvo_cust_e14, salvo_tv_day14))

        ####################
        # DAY 15
        ####################
        # Create frames
        dami_tv_frame15 = LabelFrame(self.day15, text='Damiano', font=(str(self.font), 18),bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_tv_frame15.place(x=2, y=0, relheight=0.75, relwidth=0.5)
        salvo_tv_frame15 = LabelFrame(self.day15, text='Salvo', font=(str(self.font), 18), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_tv_frame15.place(x=770, y=0, relheight=0.75, relwidth=0.5)
        dami_data_frame15 = Frame(self.day15, bg=str(self.color_bg))
        dami_data_frame15.place(x=200, y=580)
        salvo_data_frame15 = Frame(self.day15, bg=str(self.color_bg))
        salvo_data_frame15.place(x=970, y=580)
        dami_button_frame15 = Frame(self.day15, bg=str(self.color_bg))
        dami_button_frame15.place(x=240, y=650)
        salvo_button_frame15 = Frame(self.day15, bg=str(self.color_bg))
        salvo_button_frame15.place(x=1010, y=650)

        # Create Treeview and Scrollbar DAMIANO
        dami_tv_day15 = ttk.Treeview(dami_tv_frame15)
        dami_tv_day15.place(relwidth=1, relheight=1)
        dami_scrolly15 = Scrollbar(dami_tv_frame15, orient=VERTICAL, command=dami_tv_day15.yview)
        dami_scrolly15.pack(side=RIGHT, fill=Y)
        dami_tv_day15.configure(yscrollcommand=dami_scrolly15.set)

        # Set columns DAMIANO
        dami_tv_day15['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        dami_tv_day15.column('#0', width=0, stretch=NO)
        dami_tv_day15.column('ID', width=10, anchor=CENTER)
        dami_tv_day15.column('Data', width=100, anchor=CENTER)
        dami_tv_day15.column('Ora', width=70, anchor=CENTER)
        dami_tv_day15.column('Cliente', width=120, anchor=CENTER)

        dami_tv_day15.heading('#0', text='')
        dami_tv_day15.heading('ID', text='ID', anchor=CENTER)
        dami_tv_day15.heading('Data', text='Data', anchor=CENTER)
        dami_tv_day15.heading('Ora', text='Ora', anchor=CENTER)
        dami_tv_day15.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records DAMIANO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        dami_tv_day15.tag_configure('evenrow', background='white')
        dami_tv_day15.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.dami_count%2 == 0:
                        dami_tv_day15.insert(parent='', index='end', iid=self.dami_count, values=('', day14.date(), t, ''), tags=('evenrow',))
                else:
                        dami_tv_day15.insert(parent='', index='end', iid=self.dami_count, values=('', day14.date(), t, ''), tags=('oddrow',))
                self.dami_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day14.date():
                        confront_time = day14 - dt.timedelta(hours=n)
                        if confront_time.time() < dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(dami_tv_day15.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                dami_tv_day15.delete(j)
                                                if int(j)%2 == 0:
                                                        dami_tv_day15.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        dami_tv_day15.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))

        # Create labels and  entry boxes DAMIANO
        dami_data_l15 = Label(dami_data_frame15, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_data_l15.grid(row=0, column=0)
        dami_ora_l15 = Label(dami_data_frame15, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_ora_l15.grid(row=0, column=1)
        dami_cust_l15 = Label(dami_data_frame15, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami))
        dami_cust_l15.grid(row=0, column=2)
        dami_data_e15 = Entry(dami_data_frame15)
        dami_data_e15.grid(row=1, column=0)
        dami_ora_e15 = Entry(dami_data_frame15)
        dami_ora_e15.grid(row=1, column=1)
        dami_cust_e15 = Entry(dami_data_frame15)
        dami_cust_e15.grid(row=1, column=2)

        # Create buttons DAMIANO
        dami_new_button = Button(dami_button_frame15, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_new(dami_data_e15, dami_ora_e15, dami_cust_e15))
        dami_new_button.grid(row=0, column=0)
        dami_update_button = Button(dami_button_frame15, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_update(dami_data_e15, dami_ora_e15, dami_cust_e15, dami_tv_day15))
        dami_update_button.grid(row=0, column=1)
        dami_remove_button = Button(dami_button_frame15, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.dami_remove(dami_tv_day15))
        dami_remove_button.grid(row=0, column=2)
        dami_clean_button = Button(dami_button_frame15, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_dami), command=lambda: self.clean(dami_data_e15, dami_ora_e15, dami_cust_e15))
        dami_clean_button.grid(row=0, column=3)
        dami_tv_day15.bind("<Double-1>", lambda x:self.dami_select(dami_data_e15, dami_ora_e15, dami_cust_e15, dami_tv_day15))

        # Create Treeview and Scrollbar SALVO
        salvo_tv_day15 = ttk.Treeview(salvo_tv_frame15)
        salvo_tv_day15.place(relwidth=1, relheight=1)
        salvo_scrolly15 = Scrollbar(salvo_tv_frame15, orient=VERTICAL, command=salvo_tv_day15.yview)
        salvo_scrolly15.pack(side=RIGHT, fill=Y)
        salvo_tv_day15.configure(yscrollcommand=salvo_scrolly15.set)

        # Set columns SALVO
        salvo_tv_day15['columns'] = ('ID', 'Data', 'Ora', 'Cliente')
        salvo_tv_day15.column('#0', width=0, stretch=NO)
        salvo_tv_day15.column('ID', width=10, anchor=CENTER)
        salvo_tv_day15.column('Data', width=100, anchor=CENTER)
        salvo_tv_day15.column('Ora', width=70, anchor=CENTER)
        salvo_tv_day15.column('Cliente', width=120, anchor=CENTER)

        salvo_tv_day15.heading('#0', text='')
        salvo_tv_day15.heading('ID', text='ID', anchor=CENTER)
        salvo_tv_day15.heading('Data', text='Data', anchor=CENTER)
        salvo_tv_day15.heading('Ora', text='Ora', anchor=CENTER)
        salvo_tv_day15.heading('Cliente', text='Cliente', anchor=CENTER)

        # Show records SALVO
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        conn.commit()
        conn.close()
        orari = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30']
        salvo_tv_day15.tag_configure('evenrow', background='white')
        salvo_tv_day15.tag_configure('oddrow', background='lightblue')
        n = 1
        for t in orari:
                if self.salvo_count%2 == 0:
                        salvo_tv_day15.insert(parent='', index='end', iid=self.salvo_count, values=('', day14.date(), t, ''), tags=('evenrow',))
                else:
                        salvo_tv_day15.insert(parent='', index='end', iid=self.salvo_count, values=('', day14.date(), t, ''), tags=('oddrow',))
                self.salvo_count += 1
        for record in records:
                if dt.datetime.strptime(record[1], '%Y-%m-%d').date() == day14.date():
                        confront_time = day14 - dt.timedelta(hours=n)
                        if confront_time.time() > dt.datetime.strptime(record[2], '%H:%M').time():
                                for i,j in enumerate(salvo_tv_day15.get_children()):
                                        if dt.datetime.strptime(record[2], '%H:%M').time() == dt.datetime.strptime(orari[i], '%H:%M').time():
                                                salvo_tv_day15.delete(j)
                                                if int(j)%2 == 0:
                                                        salvo_tv_day15.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                                                else:
                                                        salvo_tv_day15.insert(parent='', index=str(i), iid=j, values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        
        # Create labels and  entry boxes SALVO
        salvo_data_l15 = Label(salvo_data_frame15, text='Data', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_data_l15.grid(row=0, column=0)
        salvo_ora_l15 = Label(salvo_data_frame15, text='Ora', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_ora_l15.grid(row=0, column=1)
        salvo_cust_l15 = Label(salvo_data_frame15, text='Cliente', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo))
        salvo_cust_l15.grid(row=0, column=2)
        salvo_data_e15 = Entry(salvo_data_frame15)
        salvo_data_e15.grid(row=1, column=0)
        salvo_ora_e15 = Entry(salvo_data_frame15)
        salvo_ora_e15.grid(row=1, column=1)
        salvo_cust_e15 = Entry(salvo_data_frame15)
        salvo_cust_e15.grid(row=1, column=2)

        # Create buttons SALVO
        salvo_new_button = Button(salvo_button_frame15, text='Nuovo', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_new(salvo_data_e15, salvo_ora_e15, salvo_cust_e15))
        salvo_new_button.grid(row=0, column=0)
        salvo_update_button = Button(salvo_button_frame15, text='Salva', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_update(salvo_data_e15, salvo_ora_e15, salvo_cust_e15, salvo_tv_day15))
        salvo_update_button.grid(row=0, column=1)
        salvo_remove_button = Button(salvo_button_frame15, text='Elimina', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.salvo_remove(salvo_tv_day15))
        salvo_remove_button.grid(row=0, column=2)
        salvo_clean_button = Button(salvo_button_frame15, text='Pulisci', font=(str(self.font), 14), bg=str(self.color_bg), fg=str(self.color_fg_salvo), command=lambda: self.clean(salvo_data_e15, salvo_ora_e15, salvo_cust_e15))
        salvo_clean_button.grid(row=0, column=3)
        salvo_tv_day15.bind("<Double-1>", lambda x:self.salvo_select(salvo_data_e15, salvo_ora_e15, salvo_cust_e15, salvo_tv_day15))

        self.root.mainloop()


    def dami_new(self, e1, e2, e3):
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM cust_damiano')
        length = c.fetchall()[0][0]
        conn.commit()
        c.execute("INSERT INTO cust_damiano VALUES (:l, :d, :o, :c)",
                {'l':int(length)+1, 'd':str(e1.get()), 'o':str(e2.get()), 'c':str(e3.get())})
        conn.commit()
        conn.close()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        self.reload()


    def dami_select(self, e1, e2, e3, tv):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        selected = tv.focus()
        values = tv.item(selected, 'values')
        e1.insert(0, values[1])
        e2.insert(0, values[2])
        e3.insert(0, values[3])
        self.id = values[0]


    def dami_update(self, e1, e2, e3, tv):
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute("""UPDATE cust_damiano
                SET Data= :data, Ora= :ora, Cliente= :cust
                WHERE ID=""" + str(self.id),
                {'data':str(e1.get()), 'ora':str(e2.get()), 'cust':str(e3.get())})
        conn.commit()
        conn.close()
        selected = tv.focus()
        tv.item(selected, text='', values=(self.id, e1.get(), e2.get(), e3.get()))
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)


    def dami_remove(self, tv):
        selected = tv.focus()
        values = tv.item(selected, 'values')
        id = values[0]
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute("DELETE FROM cust_damiano WHERE ID=" + str(id))
        conn.commit()
        conn.close()
        tv.delete(selected)


    def salvo_new(self, e1, e2, e3):
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM cust_salvo')
        length = c.fetchall()[0][0]
        conn.commit()
        c.execute("INSERT INTO cust_salvo VALUES (:l, :d, :o, :c)",
                {'l':int(length)+1, 'd':str(e1.get()), 'o':str(e2.get()), 'c':str(e3.get())})
        conn.commit()
        conn.close()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        self.reload()


    def salvo_select(self, e1, e2, e3, tv):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        selected = tv.focus()
        values = tv.item(selected, 'values')
        e1.insert(0, values[1])
        e2.insert(0, values[2])
        e3.insert(0, values[3])
        self.id = values[0]


    def salvo_update(self, e1, e2, e3, tv):
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute("""UPDATE cust_salvo
                SET Data= :data, Ora= :ora, Cliente= :cust
                WHERE ID=""" + str(self.id),
                {'data':str(e1.get()), 'ora':str(e2.get()), 'cust':str(e3.get())})
        conn.commit()
        conn.close()
        selected = tv.focus()
        tv.item(selected, text='', values=(self.id, e1.get(), e2.get(), e3.get()))
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)


    def salvo_remove(self, tv):
        selected = tv.focus()
        values = tv.item(selected, 'values')
        id = values[0]
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute("DELETE FROM cust_salvo WHERE ID=" + str(id))
        conn.commit()
        conn.close()
        tv.delete(selected)


    def clean(self, e1, e2, e3):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)


    def reload(self):
        # Damiano
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute("SELECT *,oid FROM cust_damiano")
        records = c.fetchall()
        day0 = dt.datetime.now()
        for i in range(1, len(records)+1):
                c.execute("SELECT Data FROM cust_damiano WHERE oid=" + str(i))
                date_str = c.fetchone()[0]
                date = dt.datetime.strptime(date_str, '%Y-%m-%d').date()
                if day0.date() > date:
                        c.execute("SELECT Ora FROM cust_damiano WHERE oid=" + str(i))
                        time_str = c.fetchone()[0]
                        time = dt.datetime.strptime(time_str, '%H:%M').time()
                        if day0.time() > time:
                                c.execute("""DELETE FROM cust_damiano WHERE oid=""" + str(i))
                                conn.commit()
        c.execute('SELECT *,oid FROM cust_damiano')
        records = c.fetchall()
        c.execute('DELETE FROM cust_damiano')
        new_records1 = []
        new_records2 = []
        new_records3 = []
        for i in range(0, len(records)):
                new_records1.append(records[i][1])
                new_records2.append(records[i][2])
                new_records3.append(records[i][3])
        scambi = True
        while scambi:
            scambi = False
            for i in range(0, len(records)-1):
                first_date = dt.datetime.strptime(new_records1[i], '%Y-%m-%d').date()
                second_date = dt.datetime.strptime(new_records1[i+1], '%Y-%m-%d').date()
                if first_date > second_date:
                    temp_date = new_records1[i]
                    new_records1[i] = new_records1[i+1]
                    new_records1[i+1] = temp_date
                    temp_time = new_records2[i]
                    new_records2[i] = new_records2[i+1]
                    new_records2[i+1] = temp_time
                    temp_cust = new_records3[i]
                    new_records3[i] = new_records3[i+1]
                    new_records3[i+1] = temp_cust
                    scambi = True
                elif first_date == second_date:
                    first_time = dt.datetime.strptime(new_records2[i], '%H:%M').time()
                    second_time = dt.datetime.strptime(new_records2[i+1], '%H:%M').time()
                    if first_time > second_time:
                        temp_date = new_records1[i]
                        new_records1[i] = new_records1[i+1]
                        new_records1[i+1] = temp_date
                        temp_time = new_records2[i]
                        new_records2[i] = new_records2[i+1]
                        new_records2[i+1] = temp_time
                        temp_cust = new_records3[i]
                        new_records3[i] = new_records3[i+1]
                        new_records3[i+1] = temp_cust
                        scambi = True
        for i in range(0, len(new_records1)):
            c.execute('INSERT INTO cust_damiano VALUES (:id, :date, :time, :customer)',
                    {'id':str(i+1), 'date':new_records1[i], 'time':new_records2[i], 'customer':new_records3[i]})
        conn.commit()
        conn.close()

        # Salvo
        conn = sqlite3.connect(p_key)
        c = conn.cursor()
        c.execute("SELECT *,oid FROM cust_salvo")
        records = c.fetchall()
        day0 = dt.datetime.now()
        for i in range(1, len(records)+1):
                c.execute("SELECT Data FROM cust_salvo WHERE oid=" + str(i))
                date_str = c.fetchone()[0]
                date = dt.datetime.strptime(date_str, '%Y-%m-%d').date()
                if day0.date() > date:
                        c.execute("SELECT Ora FROM cust_salvo WHERE oid=" + str(i))
                        time_str = c.fetchone()[0]
                        time = dt.datetime.strptime(time_str, '%H:%M').time()
                        if day0.time() > time:
                                c.execute("""DELETE FROM cust_salvo WHERE oid=""" + str(i))
                                conn.commit()
        c.execute('SELECT *,oid FROM cust_salvo')
        records = c.fetchall()
        c.execute('DELETE FROM cust_salvo')
        new_records1 = []
        new_records2 = []
        new_records3 = []
        for i in range(0, len(records)):
                new_records1.append(records[i][1])
                new_records2.append(records[i][2])
                new_records3.append(records[i][3])
        scambi = True
        while scambi:
            scambi = False
            for i in range(0, len(records)-1):
                first_date = dt.datetime.strptime(new_records1[i], '%Y-%m-%d').date()
                second_date = dt.datetime.strptime(new_records1[i+1], '%Y-%m-%d').date()
                if first_date > second_date:
                    temp_date = new_records1[i]
                    new_records1[i] = new_records1[i+1]
                    new_records1[i+1] = temp_date
                    temp_time = new_records2[i]
                    new_records2[i] = new_records2[i+1]
                    new_records2[i+1] = temp_time
                    temp_cust = new_records3[i]
                    new_records3[i] = new_records3[i+1]
                    new_records3[i+1] = temp_cust
                    scambi = True
                elif first_date == second_date:
                    first_time = dt.datetime.strptime(new_records2[i], '%H:%M').time()
                    second_time = dt.datetime.strptime(new_records2[i+1], '%H:%M').time()
                    if first_time > second_time:
                        temp_date = new_records1[i]
                        new_records1[i] = new_records1[i+1]
                        new_records1[i+1] = temp_date
                        temp_time = new_records2[i]
                        new_records2[i] = new_records2[i+1]
                        new_records2[i+1] = temp_time
                        temp_cust = new_records3[i]
                        new_records3[i] = new_records3[i+1]
                        new_records3[i+1] = temp_cust
                        scambi = True
        for i in range(0, len(new_records1)):
            c.execute('INSERT INTO cust_salvo VALUES (:id, :date, :time, :customer)',
                    {'id':str(i+1), 'date':new_records1[i], 'time':new_records2[i], 'customer':new_records3[i]})
        conn.commit()
        conn.close()
        self.root.destroy()
        main()




    def change_background(self):
        filename = filedialog.askopenfilename(initialdir=home, title='Seleziona un file', filetypes=(('jpg files', '*.jpg'), ('png files', '*.png'), ('webp files', '*.webp'), ('All files', '*.*')))
        conn = sqlite3.connect(s_key)
        c = conn.cursor()
        c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=1""",
                {'imp':'Background', 'scelta':str(filename)})
        conn.commit()
        conn.close()
        self.root.destroy()
        main()


    def change_font(self):
        self.root.destroy()
        root = Tk()
        root.geometry('500x500')
        root.title('Automatic Management System - Font Settings')
        try:
            img = ImageTk.PhotoImage(Image.open(self.img_bg))
            l = Label(root, image=img)
            l.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            root.config(bg='#525355')

        # Create frames
        option_frame = Frame(root, bg=str(self.color_bg))
        option_frame.pack(pady=10)
        button_frame = Frame(root, bg=str(self.color_bg))
        button_frame.pack(pady=20)

        # Create OptionMenu
        options = ['Arial', 'Calibri', 'Colonna MT', 'Helvetica', 'Impact', 'Stencil', 'Times New Roman']
        clicked = StringVar()
        clicked.set(options[0])
        drop = OptionMenu(option_frame, clicked, *options)
        drop.pack()

        #Create buttons
        save_new_font_button = Button(button_frame, text='Salva', font=(str(self.font), 12), bg=str(self.color_bg), fg='white', command=lambda: self.save_font(clicked, root))
        save_new_font_button.grid(row=0, column=0)
        back_button = Button(button_frame, text='Indietro', font=(str(self.font), 12), bg=str(self.color_bg), fg='white', command=lambda: self.back(root))
        back_button.grid(row=0, column=1)

        root.mainloop()


    def save_font(self, clicked, master):
        conn = sqlite3.connect(s_key)
        c = conn.cursor()
        c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=2""",
                {'imp':'Font', 'scelta':str(clicked.get())})
        conn.commit()
        conn.close()
        master.destroy()
        main()


    def change_color_bg(self):
        my_color = colorchooser.askcolor()[1]
        conn = sqlite3.connect(s_key)
        c = conn.cursor()
        c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=3""",
                {'imp':'Color_bg', 'scelta':str(my_color)})
        conn.commit()
        conn.close()
        self.root.destroy()
        main()


    def change_color_fg_dami(self):
        my_color = colorchooser.askcolor()[1]
        conn = sqlite3.connect(s_key)
        c = conn.cursor()
        c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=4""",
                {'imp':'Color_fg_dami', 'scelta':str(my_color)})
        conn.commit()
        conn.close()
        self.root.destroy()
        main()

    
    def change_color_fg_salvo(self):
        my_color = colorchooser.askcolor()[1]
        conn = sqlite3.connect(s_key)
        c = conn.cursor()
        c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=5""",
                {'imp':'Color_fg_salvo', 'scelta':str(my_color)})
        conn.commit()
        conn.close()
        self.root.destroy()
        main()


    def default_settings(self):
        res = messagebox.askyesno('Attenzione!', 'Sei sicuro di voler tornare alle impostazioni di default?')
        if res == True:
            conn = sqlite3.connect(s_key)
            c = conn.cursor()
            c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=1""",
                {'imp':'Background', 'scelta':'#525355'})
            conn.commit()
            c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=2""",
                {'imp':'Font', 'scelta':'Helvetica'})
            conn.commit()
            c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=3""",
                {'imp':'Color_bg', 'scelta':'#525355'})
            conn.commit()
            c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=4""",
                {'imp':'Color_fg_dami', 'scelta':'white'})
            conn.commit()
            c.execute("""UPDATE settings
                SET Impostazione= :imp, Choice= :scelta
                WHERE oid=5""",
                {'imp':'Color_fg_salvo', 'scelta':'orange'})
            conn.commit()
            conn.close()
            self.root.destroy()
            main()


    def back(self, master):
        master.destroy()
        main()


##############################
# MAIN BODY
##############################
# Directories definition
home = os.getcwd()
out = home + '\OutFiles'

# Create directory
if not os.path.exists(out):
    os.mkdir(out)

# Create database
os.chdir(out)
p_key = 'Primary_Database.db'
s_key = 'Settings_Database.db'
if not os.path.isfile(p_key):
    conn = sqlite3.connect(p_key)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS cust_damiano
            ([ID] TEXT, [Data] TEXT, [Ora] TEXT, [Cliente] TEXT)""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS cust_salvo
            ([ID] TEXT, [Data] TEXT, [Ora] TEXT, [Cliente] TEXT)""")
    conn.commit()
    c.execute("INSERT INTO cust_damiano VALUES (:id, :d, :o, :c)",
            {'id':'1', 'd':'2022-08-31', 'o':'18:00', 'c':'Tumino'})
    conn.commit()
    c.execute("INSERT INTO cust_damiano VALUES (:id, :d, :o, :c)",
            {'id':'2', 'd':'2022-09-01', 'o':'10:00', 'c':'Cascone'})
    conn.commit()
    c.execute("INSERT INTO cust_damiano VALUES (:id, :d, :o, :c)",
            {'id':'3', 'd':'2022-09-01', 'o':'15:30', 'c':'Pannuzzo'})
    conn.commit()
    c.execute("INSERT INTO cust_damiano VALUES (:id, :d, :o, :c)",
            {'id':'4', 'd':'2022-09-02', 'o':'12:30', 'c':'Guastella'})
    conn.commit()
    c.execute("INSERT INTO cust_salvo VALUES (:id, :d, :o, :c)",
            {'id':'1', 'd':'2022-08-31', 'o':'14:00', 'c':'Nicola'})
    conn.commit()
    c.execute("INSERT INTO cust_salvo VALUES (:id, :d, :o, :c)",
            {'id':'2', 'd':'2022-09-01', 'o':'17:30', 'c':'Matteo'})
    conn.commit()
    c.execute("INSERT INTO cust_salvo VALUES (:id, :d, :o, :c)",
            {'id':'3', 'd':'2022-09-02', 'o':'9:00', 'c':'Francesco'})
    conn.commit()
    conn.close()

if not os.path.isfile(s_key):
    conn = sqlite3.connect(s_key)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS settings
            ([Impostazione] TEXT, [Choice] TEXT)""")
    conn.commit()
    c.execute("INSERT INTO settings VALUES (:imp, :scelta)",
            {'imp':'Background', 'scelta':'#525355'})
    conn.commit()
    c.execute("INSERT INTO settings VALUES (:imp, :scelta)",
            {'imp':'Font', 'scelta':'Helvetica'})
    conn.commit()
    c.execute("INSERT INTO settings VALUES (:imp, :scelta)",
            {'imp':'Color_bg', 'scelta':'#525355'})
    conn.commit()
    c.execute("INSERT INTO settings VALUES (:imp, :scelta)",
            {'imp':'Color_fg_dami', 'scelta':'white'})
    conn.commit()
    c.execute("INSERT INTO settings VALUES (:imp, :scelta)",
            {'imp':'Color_fg_salvo', 'scelta':'orange'})
    conn.commit()
    conn.close()

# Running app
main()