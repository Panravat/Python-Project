#สร้างตาราง 0
from datetime import datetime
import sqlite3
import json
from reportlab.lib.pagesizes import  inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import datetime
# เชื่อมต่อกับฐานข้อมูล SQLite3
conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
cursor = conn.cursor()
# สร้างตารางสำหรับเก็บข้อมูลใบเสร็จหากยังไม่มีตาราง AUTOINCREMENT คือ เพิ่มค่าคีย์หลัก (Primary Key) โดยอัตโนมัติ เมื่อแทรกแถวใหม่ในตาราง
cursor.execute('''
    CREATE TABLE IF NOT EXISTS history ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        CustomerID TEXT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        massage_duration TEXT,
        employee_num TEXT,
        oil_type TEXT,
        total_price INTEGER,
        data TEXT,
        time TEXT)''')
conn.commit()
conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
cursor = conn.cursor()
# สร้างตารางสำหรับเก็บข้อมูลใบเสร็จหากยังไม่มีตาราง AUTOINCREMENT คือ เพิ่มค่าคีย์หลัก (Primary Key) โดยอัตโนมัติ เมื่อแทรกแถวใหม่ในตาราง
cursor.execute('''
    CREATE TABLE IF NOT EXISTS historysum ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        CustomerID TEXT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        massage_duration TEXT,
        employee_num TEXT,
        oil_type TEXT,
        total_price INTEGER,
        data TEXT,
        time TEXT)''')
conn.commit()
conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS member (
            CustomerID TEXT PRIMARY KEY,
            MembershipOrder INTEGER,
            FirstName TEXT,
            LastName TEXT,
            PhoneNumber TEXT,
            JoinDate DATE,
            UsageHistory JSON
        )
    ''')
conn.commit()
conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS oillist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            oil_type TEXT,
            oilprice INTEGER,
            total_price
        )
    ''')
conn.commit()
conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS emplist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee TEXT,
            empprice INTEGER,
            total_price
        )
    ''')
conn.commit()
conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS oillistshow (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            oil_type TEXT,
            oilprice INTEGER,
            total_price
        )
    ''')
conn.commit()
conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS emplistshow (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee TEXT,
            empprice INTEGER,
            total_price
        )
    ''')
conn.commit()
def register_new_user():
    global register_window
    # เรียกใช้งานหน้าต่างลงทะเบียน
    register_window = tk.Toplevel()
    register_window.title("ลงทะเบียนผู้ใช้ใหม่")
    register_window.geometry("600x300")
    register_window.resizable(False, False)
    register_window.configure(bg="light yellow")
    image2 = Image.open(r"C:\Users\HP\Downloads\กรุณากรอกข้อมูล (1).png") 
    image2 = image2.resize((600, 300), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(register_window, image=photo2)
    label2.pack()
    # สร้าง Label และ Entry สำหรับข้อมูลลงทะเบียน
    entry_new_firstname = tk.Entry(register_window)
    entry_new_firstname.place(x=250,y=80)
    entry_new_firstname.configure(fg="light yellow",bg="light pink")

    entry_new_lastname = tk.Entry(register_window)
    entry_new_lastname.place(x=250,y=120)
    entry_new_lastname.configure(fg="light yellow",bg="light pink")

    entry_new_phone = tk.Entry(register_window)
    entry_new_phone.place(x=250,y=160)
    entry_new_phone.configure(fg="light yellow",bg="light pink")

    def usephone():
        phone_number = entry_new_phone.get().strip()
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        # ค้นหาเบอร์โทรศัพท์ในตาราง
        cursor.execute("SELECT COUNT(*) FROM member WHERE PhoneNumber=?", (phone_number,))
        count = cursor.fetchone()[0]
        if count > 0:
            messagebox.showerror("(;￢_￢)Error(;￢_￢)", "(;￢_￢)!!!เบอร์โทรศัพท์นี้มีอยู่ในระบบแล้ว!!!(;￢_￢)")
            register_window.deiconify()
        else:
            add_customer()
            
    def check3():
        first_name = entry_new_firstname.get().strip() #ลบช่องว่าง (หรือตัวอักษรหน้าและหลัง) 
        last_name = entry_new_lastname.get().strip()
        phone_number = entry_new_phone.get().strip()
        if not first_name  or not last_name or not phone_number:
            def gotoregis():
                Error5.destroy()
                register_window.deiconify()
            Error5= tk.Toplevel()
            Error5.title("แจ้งเตือน")
            Error5.geometry("500x580")
            Error5.resizable(False,False)
            Error5.option_add("*Font", "consolas 15")
            Error5.configure(background="#EADFF2")
            image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (6).png") 
            image2 = image2.resize((500, 500), Image.BOX) 
            photo2 = ImageTk.PhotoImage(image2)
            label2 = tk.Label(Error5, image=photo2)
            label2.pack()
            Button(Error5,text="OKกะเทย",bg="red",fg="black",width=15,command=gotoregis).place(x=180,y=510)
            Error5.mainloop()
        else:
            usephone()
    def check4():
        r=entry_new_phone.get()
        if len(r) == 10 and r.isdigit(): #len(r) == 10: ตรวจสอบว่าความยาวของสตริง "r" เท่ากับ 10 หรือไม่ r.isdigit(): ตรวจสอบว่าทุกตัวอักษรในสตริง "r" เป็นตัวเลขหรือไม่
            check3()
        else:
            def gotoregis2():
                Error6.destroy()
                register_window.deiconify()
            Error6 = tk.Toplevel()
            Error6.title("แจ้งเตือน")
            Error6.geometry("500x580")
            Error6.resizable(False,False)
            Error6.option_add("*Font", "consolas 15")
            Error6.configure(background="#EADFF2")
            image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (5).png") 
            image2 = image2.resize((500, 500), Image.BOX) 
            photo2 = ImageTk.PhotoImage(image2)
            label2 = tk.Label(Error6, image=photo2)
            label2.pack()
            Button(Error6,text="OKกะเทย",bg="red",fg="black",width=15,command=gotoregis2).place(x=180,y=510)
            Error6.mainloop()
    # สร้างปุ่มสำหรับบันทึกข้อมูลลงทะเบียน
    def add_customer():
        from datetime import datetime
        firstname = entry_new_firstname.get()
        lastname = entry_new_lastname.get()
        phone = entry_new_phone.get()
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S') #'%Y-%m-%d %H:%M:%S' จะแสดงวันที่และเวลาในรูปแบบ "YYYY-MM-DD HH:MM:SS" 
    # ค้นหาหมายเลขลำดับลูกค้าที่ใหญ่ที่สุดในฐานข้อมูล
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(CAST(SUBSTR(CustomerID, 4) AS INTEGER)) FROM member") #ตัวดึงรหัสลูกค้า CAST(... AS INTEGER) คือการแปลงค่าที่ได้จากการดึง substring มาเป็นประเภทข้อมูลจำนวนเต็ม (integer) 
        max_order = cursor.fetchone()[0] # fetchone() ใช้เพื่อดึงแถวแรกจากผลลัพธ์ของคำสั่ง SQL  fetchone() จะคืน tuple ที่มีข้อมูลเพียงค่าเดียว และ [0] ใช้ในการดึงค่านั้นออกมาจาก tuple ในตำแหน่งที่ 0 ของ tuple นั้น เพื่อนำไปใช้ในตัวแปร max_order
        if max_order is None:
            max_order = 0
        # สร้างรหัสลูกค้าใหม่โดยเพิ่ม 1 จากหมายเลขลำดับลูกค้าที่ใหญ่ที่สุด
        new_order = max_order + 1
        new_customer_id = f'fj{new_order:04d}'  # ตัวเลขลำดับให้มีความยาว 4 ตัวเสมอ :04d เพื่อให้หมายเลขลำดับลูกค้ามีความยาวเท่ากับ 4 หลักและเติมเลข 0 ไปด้านหน้าถ้าหมายเลขน้อยกว่า 4 หลัก.

        # เพิ่มข้อมูลลูกค้าใหม่ลงในตาราง
        cursor.execute("INSERT INTO member (CustomerID, MembershipOrder, FirstName, LastName, PhoneNumber, JoinDate) VALUES (?, ?, ?, ?, ?, ?)",
                    (new_customer_id, new_order, firstname, lastname, phone, formatted_datetime))
        m=messagebox.showinfo("การสมัครสมาชิก","สมัครสมาชิกเสร็จสิ้น")
        if m:
            root.deiconify()
            register_window.destroy()
            conn.commit()
    tk.Button(register_window, text=" ❀บันทึก❀",fg="light yellow",bg="#BE6060",width=10, command=check4).place(x=100,y=220)
    tk.Button(register_window, text=" ❀ย้อนกลับ❀ ",fg="light yellow",bg="#BE6060",width=10, command=gogo4).place(x=350,y=220)
    register_window.mainloop()
#เก็บค่าตาราง 
def save_receipt(): 
    from datetime import datetime
    global total_pricemm,cusid,total_pricem_text
    # ดึงค่าข้อมูลจากตัวแปร
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    formatted_date = current_datetime.strftime('%Y-%m-%d')
    formatted_time = current_datetime.strftime('%H:%M:%S')
    first_name = et1.get()
    last_name = et2.get()
    phone_number = et3.get()
    massage_duration = choicehour.get()
    if et9.get() != "":
        # เชื่อมต่อกับฐานข้อมูล SQLite
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        # ค้นหารหัสลูกค้าจากฐานข้อมูลด้วยรหัสลูกค้าที่รับจาก et9
        customer_id = et9.get()
        cursor.execute("SELECT CustomerID FROM member WHERE CustomerID=?", (customer_id,))
        customer_data = cursor.fetchone()
        
        # ถ้าพบรหัสลูกค้าในฐานข้อมูลให้ใช้รหัสลูกค้านั้น ไม่งั้นใช้เครื่องหมาย "-"
        if customer_data:
            cusid = customer_data[0]
        else :
            cusid ="-"
    else :
        cusid ="-"
    oil_str = ', '.join(oil_types_list)
    oil_strr = ("oil : "+ oil_str)
    empstr = ', '.join(emp_list)
    empstrr = ("employee : "+ empstr)
    # คำนวณราคา
    # เก็บข้อมูลใบเสร็จในฐานข้อมูล
    total_pricem_text = (str(total_pricemm) +" baht")  # สร้างสตริงที่รวมค่า total_price และ "บาท"
    tel=("Tel "+str(phone_number))
    massage_duration_text=(str(massage_duration)+" minutes")
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO history (CustomerID, first_name, last_name, phone_number, massage_duration, employee_num, oil_type, total_price,data,time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (cusid, first_name, last_name, tel, massage_duration_text, empstrr, oil_strr, total_pricem_text,formatted_date,formatted_time))
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO historysum (CustomerID, first_name, last_name, phone_number, massage_duration, employee_num, oil_type, total_price,data,time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (cusid, first_name, last_name, tel, massage_duration_text, empstr, oil_str, total_pricemm,formatted_date,formatted_time))
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE CustomerID = ?", (cusid,))
    history_data = cursor.fetchall() #ดึงข้อมูลทั้งหมดจากคำสั่ง SQL นั้น ข้อมูลที่ดึงมาจะถูกเก็บในตัวแปร history_data.
    history = []
    for row in history_data: #วนลูปผ่านข้อมูลที่ดึงมาแต่ละแถว
        entry = {
        "Joining date": row[9],            # ใช้ตำแหน่งดัชนีของคอลัมน์ datatime
        "massage duration": row[5],  # ใช้ตำแหน่งดัชนีของคอลัมน์ massage_duration
        "employee": row[6],      # ใช้ตำแหน่งดัชนีของคอลัมน์ employee_num
        "oil type": row[7],            # ใช้ตำแหน่งดัชนีของคอลัมน์ oil_type
        "total price": row[8]        # ใช้ตำแหน่งดัชนีของคอลัมน์ total_price
        }
        history.append(entry) #เก็บในรายการ history.
# แปลงข้อมูลประวัติการใช้เป็น JSON
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    history_json = json.dumps(history) #แปลงรายการ history ที่เก็บข้อมูลประวัติการใช้ให้กลายเป็นรูปแบบ JSON และเก็บในตัวแปร history_json.
    cursor.execute("UPDATE member SET UsageHistory = ? WHERE CustomerID = ?", (history_json, cusid))
    conn.commit()
    pdf()
def pdf():
    # ค้นหาค่าลำดับที่ล่าสุดจาก SQLite
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")  
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM history')  #เลือกข้อมูลล่าสุด
    last_id = cursor.fetchone()[0]#ดึงข้อมูลคอลัมแรกมา คือลำดับล่าสุดของsqlite
    conn.close()
    custom_page_size = (5 * inch, 3 * inch)
    # สร้างไฟล์ PDF
    current_datetime = datetime.datetime.now()
    pdf_file_name = f'queue_{current_datetime.strftime("%Y%m%d_%H%M%S")}.pdf'
    doc = SimpleDocTemplate(pdf_file_name, pagesize=custom_page_size) #คลาสในโมดูล reportlab.platypus ที่ใช้สร้างเอกสาร PDF โดยรับพารามิเตอร์หลักสองตัวคือ pdf_file_name = name และ pagesize.=papersize
    # สร้างสไตล์ข้อความ
    styles = getSampleStyleSheet()
    style = ParagraphStyle(name='CustomStyle', parent=styles['Normal'], fontSize=40) 
    # สร้างเนื้อหา PDF
    content = []
    content.append(Paragraph(f"Queue : {last_id}", style))
    # สร้าง PDF และบันทึกไฟล์
    doc.build(content)
    i = messagebox.askyesno("ใบเสร็จ","ต้องการใบเสร็จหรือไม่??")
    if i:
        pdf2()
    else:
        messagebox.showinfo("ใบเสร็จ","ดำเนินการเสร็จสิ้น")
        root.deiconify()
def pdf2():
    # 1. ดึงข้อมูลจาก SQLite
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")  
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history ORDER BY id DESC LIMIT 1') #ค้นหาและคืนค่าข้อมูลทั้งหมดในแถวที่มีค่า id มากที่สุดในตาราง je
    data_from_sqlite = cursor.fetchall()
    conn.close()
    custom_page_size = (6 * inch, 5 * inch)
    # 2. สร้าง PDF
    current_datetime = datetime.datetime.now()
    pdf_file_name = f'receipt_{current_datetime.strftime("%Y%m%d_%H%M%S")}.pdf'  
    doc = SimpleDocTemplate(pdf_file_name, pagesize=custom_page_size)
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(name='CustomStyle', parent=styles['Normal'], fontSize=16)
    messagebox.showinfo("ใบเสร็จ","ดำเนินการเสร็จสิ้น")
    # 3. เขียนข้อมูลลงใน PDF
    content = []
    for row in data_from_sqlite:
        # สร้างข้อมูลจากข้อมูลใน SQLite
        data_to_write = f"✧*:✧*❆ ❇ Receipt ❈ ❉✧*✧*<br /><br />CustomerID : {row[1]}<br /><br />Phone number: {row[4]}<br /><br />Time: {row[5]}<br /><br />Oil: {row[7]}<br /><br />Employee: {row[6]}<br /><br />Total price: {row[8]}<br /><br /> DATE:{row[9]} {row[10]}"
        # เขียนข้อมูลลงใน PDF ด้วย Paragraph
        content.append(Paragraph(data_to_write, custom_style))
    # สร้าง PDF และบันทึกไฟล์
    doc.build(content)
#ลบข้อมูลในsqlistขั้นเลือกตำแหน่ง
def deleteinfo():
    global et4
    global dl
    dl = tk.Toplevel()
    dl.title(">⌓<ลบข้อมูล>⌓<")
    dl.geometry("500x100")
    dl.option_add("*Font", "consolas 15")
    dl.configure(background="light yellow")
    dl.resizable(False,False)
    image2 = Image.open(r"C:\Users\HP\Downloads\กรุณาเลือกคิวที่จะลบ  (1).png") 
    image2 = image2.resize((500, 100), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(dl, image=photo2)
    label2.pack()
    et4 = tk.Entry(dl)
    et4.place(x=200,y=15)
    et4.configure(background="#644A4F",fg="light yellow")
    tk.Button(dl,text="(⍤3⍤)ยืนยัน(⍤3⍤)",bg="#644A4F",fg="light yellow",width=10,command=deletenext).place(x=80,y=50)
    tk.Button(dl,text="(⍤3⍤)ย้อนกลับ(⍤3⍤)",bg="#644A4F",fg="light yellow",width=10,command=gogo15).place(x=280,y=50)
    dl.mainloop()
#ลบข้อมูลในsqlistขั้นลบในsqlist
def deletenext():
    global dl
    # เชื่อมต่อกับฐานข้อมูล SQLite3
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    # สร้างคำสั่ง SQL สำหรับลบข้อมูล
    # เช่น ลบข้อมูลในตาราง receipts ที่มี id = 1
    id = et4.get()
    cursor.execute('''
        DELETE FROM history
        WHERE id = ?
    ''', (id,))
    # ยืนยันการเปลี่ยนแปลง
    conn.commit()
    # ปิดการเชื่อมต่อกับฐานข้อมูล
    conn.close()
    p = messagebox.showinfo("໒( ●ᴥ ●)ʋการลบข้อมูล","ดำเนินการเสร็จสิ้น(¯ε ¯)\nʕ； •`ᴥ•´ʔ   ʕ>⌓<｡ʔ ʕ ◔ᴥ◔ ʔ")
    if p:
        root.deiconify()
        dl.destroy()

#แสดงคิวในsqlist
def show():
    global showw
    showw=tk.Toplevel()
    showw.title("♫•*¨แสดงคิว*•.¸¸♪")
    showw.geometry("1200x590")
    showw.option_add("*Font", "consolas 15")
    showw.configure(background="#F5E9E2")
    mainmenu = tk.Menu(showw)
    showw.config(menu=mainmenu) # กำหนดเมนูหลักให้หน้าต่างย่อย คือการกำหนดให้เมนูหลัก (main menu) ของหน้าต่างย่อย (Toplevel) ชื่อ neww ใช้เมนูหลักที่คุณได้สร้างไว้และเก็บไว้ในตัวแปร mainmenu.
    submenu8 = tk.Menu(mainmenu, tearoff=0) #นี่คือการสร้างเมนูย่อย (sub-menu) โดยใช้ tk.Menu(mainmenu) เพื่อเชื่อมโยงเมนูย่อยนี้กับเมนูหลัก mainmenu
    submenu8.add_command(label="ʕっ•ᴥ•ʔっย้อนกลับʕっ•ᴥ•ʔっ", command=gogo11)
    submenu8.configure(bg='light yellow',fg="#644A4F")
    submenu8.add_command(label="ʕっ•ᴥ•ʔっ ลบคิว ʕっ•ᴥ•ʔっ ",font="consolas 15", command=deleteinfo)
    submenu8.configure(bg='light yellow',fg="#644A4F")   
    mainmenu.add_cascade(label="✎เพิ่มเติม✎", menu=submenu8)
    #ทำการดึงข้อมูล
    def fetch_data():
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id,CustomerID,first_name,last_name,phone_number,data,time FROM history")
        data = cursor.fetchall()
        for row in data:
            listbox.insert(tk.END, row)  # เพิ่มข้อมูลลงใน Listbox
        conn.close()
    #สร้างเฟรมให้listboxอยู่
    frame = tk.Frame(showw)
    frame.pack()
    #สร้างlistboxในเฟรม
    listbox = tk.Listbox(frame, width=100, height=20)
    listbox.configure(bg="#99BDB8")
    listbox.pack()
    image2 = Image.open(r"C:\Users\HP\Downloads\ดีไซน์ที่ยังไม่ได้ตั้งชื่อ (13).png") 
    image2 = image2.resize((1200, 590), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(showw, image=photo2)
    label2.pack()
    # ปุ่มสำหรับดึงข้อมูล
    fetch_button = tk.Button(showw, text=" ◍•㉦•◍ แสดงคิว ◍•㉦•◍ ",bg="#644A4F",fg="light yellow",width=20, command=fetch_data)
    fetch_button.place(x=300,y=500)
    def clear_frame2():
        listbox.delete(0,tk.END)
    button = tk.Button(showw, text="٩(◕‿◕)۶ล้างข้อมูล٩(◕‿◕)",bg="#644A4F",fg="light yellow",width=20,command=clear_frame2)
    button.place(x=700,y=500)
    showw.mainloop()
def showmember():
    global showw2
    showw2=tk.Toplevel()
    showw2.title("♫•*¨สมาชิก*•.¸¸♪")
    showw2.geometry("1200x590")
    showw2.option_add("*Font", "consolas 15")
    showw2.configure(background="#F5E9E2")
    mainmenu = tk.Menu(showw2)
    showw2.config(menu=mainmenu) # กำหนดเมนูหลักให้หน้าต่างย่อย คือการกำหนดให้เมนูหลัก (main menu) ของหน้าต่างย่อย (Toplevel) ชื่อ neww ใช้เมนูหลักที่คุณได้สร้างไว้และเก็บไว้ในตัวแปร mainmenu.
    submenu8 = tk.Menu(mainmenu, tearoff=0) #นี่คือการสร้างเมนูย่อย (sub-menu) โดยใช้ tk.Menu(mainmenu) เพื่อเชื่อมโยงเมนูย่อยนี้กับเมนูหลัก mainmenu
    submenu8.add_command(label="ʕっ•ᴥ•ʔっย้อนกลับʕっ•ᴥ•ʔっ", command=gogo10)
    submenu8.configure(bg='light yellow',fg="#644A4F")
    mainmenu.add_cascade(label="✎เพิ่มเติม✎", menu=submenu8)
    #ทำการดึงข้อมูล
    def fetch_data():
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute("SELECT CustomerID, MembershipOrder, FirstName, LastName, PhoneNumber, JoinDate FROM member")
        data = cursor.fetchall()
        for row in data:
            listbox.insert(tk.END, row)  # เพิ่มข้อมูลลงใน Listbox
        conn.close()
    #สร้างเฟรมให้listboxอยู่
    frame = tk.Frame(showw2)
    frame.pack()
    #สร้างlistboxในเฟรม
    listbox = tk.Listbox(frame, width=100, height=20)
    listbox.configure(bg="#99BDB8")
    listbox.pack()
    # ปุ่มสำหรับดึงข้อมูล
    image2 = Image.open(r"C:\Users\HP\Downloads\ดีไซน์ที่ยังไม่ได้ตั้งชื่อ (13).png") 
    image2 = image2.resize((1200, 590), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(showw2, image=photo2)
    label2.pack()
    fetch_button = tk.Button(showw2, text=" ◍•㉦•◍ แสดงรายชื่อ ◍•㉦•◍ ",bg="#644A4F",fg="light yellow", command=fetch_data)
    fetch_button.place(x=300,y=500)
    #ทำการล้างข้อมูลในลิสบ็อก
    def clear_frame():
        listbox.delete(0,tk.END)
    button = tk.Button(showw2, text="٩(◕‿◕)۶ล้างข้อมูล٩(◕‿◕)",bg="#644A4F",fg="light yellow",command=clear_frame)
    button.place(x=700,y=500)
    showw2.mainloop()
    
def ooo2(event): #เป็นพารามิเตอร์ของฟังก์ชัน ซึ่งมีลักษณะเฉพาะ เพราะฉะนั้นอาจจะไม่แสดงเป็นตัวหนาเหมือนตัวแปรทั่วไป
    global entry_queue_number2,entry_firstname2,entry_lastname2, entry_phone2
    queue_number2 = entry_queue_number2.get()
    if not queue_number2:
        return
    connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = connection.cursor()
        # ดึงข้อมูลจากตารางโดยใช้ ID ที่กรอกเข้ามา
    cursor.execute("SELECT * FROM member WHERE CustomerID=?", (queue_number2,))
    data = cursor.fetchone()
    if data:
        entry_firstname2.delete(0, tk.END)
        entry_firstname2.insert(0, data[2])  # 1 คือ index ของ firstname ในข้อมูล
        entry_lastname2.delete(0, tk.END)
        entry_lastname2.insert(0, data[3])  # 2 คือ index ของ lastname ในข้อมูล
        entry_phone2.delete(0, tk.END)
        entry_phone2.insert(0, data[4])

def fff2():
    global app2
    queue_number2 = entry_queue_number2.get()
    firstname2 = entry_firstname2.get()
    lastname2 = entry_lastname2.get()
    phone2 = entry_phone2.get()
    connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = connection.cursor()
    # ตรวจสอบว่าคิวที่ป้อนมีอยู่ในฐานข้อมูลหรือไม่
    cursor.execute("SELECT * FROM member WHERE CustomerID=?", (queue_number2,))
    existing_data = cursor.fetchone()
    if existing_data:
        # อัปเดตข้อมูล
        cursor.execute("UPDATE member SET firstname=?, lastname=?, phonenumber=? WHERE CustomerID=?",
                       (firstname2, lastname2, phone2, queue_number2))
        connection.commit()
        def upshop():
            conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE history SET first_name=?, last_name=?, phone_number=? WHERE CustomerID = ?", (firstname2, lastname2, phone2, queue_number2))
            conn.commit()
        upshop()
        g=messagebox.askyesno("ทำรายการเสร็จสิ้น","ต้องการทำรายการแก้ไขอีกหรือไม่")
        if g:
            app2.deiconify()
        else:
            root.deiconify()
            app2.destroy()
            
def check5():
    global first_name,last_name,phone_number
    first_name = entry_firstname2.get().strip() 
    last_name = entry_lastname2.get().strip()
    phone_number = entry_phone2.get().strip()
    if not first_name  or not last_name or not phone_number:
        def gotoregis():
            Error8.destroy()
            app2.deiconify()
        Error8= tk.Toplevel()
        Error8.title("แจ้งเตือน")
        Error8.geometry("500x580")
        Error8.resizable(False,False)
        Error8.option_add("*Font", "consolas 15")
        Error8.configure(background="#EADFF2")
        image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (6).png") 
        image2 = image2.resize((500, 500), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(Error8, image=photo2)
        label2.pack()
        Button(Error8,text="OKกะเทย",bg="red",fg="black",width=15,command=gotoregis).place(x=180,y=510)
        Error8.mainloop()
    else:
        fff2()
    
def check6():
    p = entry_phone2.get()
    if len(p) == 10 and p.isdigit():
        check5()
    else:
        def gotoapp2():
            Error7.destroy()
            app2.deiconify()
        Error7 = tk.Toplevel()
        Error7.title("แจ้งเตือน")
        Error7.geometry("500x580")
        Error7.resizable(False,False)
        Error7.option_add("*Font", "consolas 15")
        Error7.configure(background="#EADFF2")
        image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (5).png") 
        image2 = image2.resize((500, 500), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(Error7, image=photo2)
        label2.pack()
        Button(Error7,text="OKกะเทย",bg="red",fg="black",width=15,command=gotoapp2).place(x=180,y=510)
        Error7.mainloop()
#แก้ตารางในsqlite
def changeinfo2():
    global entry_queue_number2,entry_firstname2,entry_lastname2, entry_phone2,app2
    app2 = tk.Toplevel()
    app2.title("แก้ไขข้อมูลสมาชิก")
    app2.geometry("400x300")
    app2.configure(bg="light yellow")
    app2.option_add("*Font", "consolas 15")
    app2.resizable(False,False)
    image2 = Image.open(r"C:\Users\HP\Downloads\แก้ไขข้อมูลที่ต้องการ.png") 
    image2 = image2.resize((400, 300), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(app2, image=photo2)
    label2.pack()
    # สร้างแท็บเบิลและอินพุตสำหรับข้อมูล
    entry_queue_number2 = tk.Entry(app2,bg="#C2D0BA",fg="#5E7879")
    entry_queue_number2.place(x=150,y=80)
    entry_queue_number2.bind("<KeyRelease>", ooo2)

    entry_firstname2 = tk.Entry(app2,bg="#C2D0BA",fg="#5E7879")
    entry_firstname2.place(x=150,y=120)

    entry_lastname2 = tk.Entry(app2,bg="#C2D0BA",fg="#5E7879")
    entry_lastname2.place(x=150,y=160)

    entry_phone2 = tk.Entry(app2,bg="#C2D0BA",fg="#5E7879")
    entry_phone2.place(x=150,y=200)
    
    # เมื่อข้อมูลใน Entry ของคิวเปลี่ยนแปลงให้เรียกฟังก์ชัน on_queue_change
    submit_button = tk.Button(app2, text="♫ย้อนกลับ♫",width=10, command=gogo2)
    submit_button.place(x=240,y=240)
    submit_button.configure(bg="#5E7879",fg="#C2D0BA")
    save_button = tk.Button(app2, text="♫บันทึกข้อมูล♫",width=10, command=check6)
    save_button.place(x=70,y=240)
    save_button.configure(bg="#5E7879",fg="#C2D0BA")
    app2.mainloop()
###########################################################################################
from tkinter import* #แบบการ import นี้นำเข้าคลาสและฟังก์ชันทั้งหมดโดยตรง
from PIL import Image, ImageTk # นำเข้ารูป
import tkinter as tk #แบบการ import นี้นำเข้าโมดูล tkinter ทั้งหมดโดยให้มีชื่อย่อว่า tk
from tkinter import ttk # นำเข้า combobox
from tkinter import messagebox# นำเข้า messagebox
import webbrowser
a=0
b=0
memberid = 1
photo_buttons = {}  # ในที่นี้, photo_buttons เป็น dictionary ที่ใช้เก็บข้อมูลเกี่ยวกับรูปภาพที่เรียกว่า "photo" ซึ่งอาจจะเป็นรูปภาพที่แสดงบนปุ่มหรือใช้ในส่วนอื่น ๆ ของโปรแกรม Tkinter
money1=None
submenu3=None
photo=None #แสดงตัวแปลให้เป็นค่าว่าง
employees = {"B1": 100, "B2": 110, "B3": 120, "B4": 130, "B5": 140,"B6" : 150} #คำสั่งนี้สร้างตัวแปร employees ซึ่งเป็นพจนานุกรม (dictionary)
oil_types = {"Lamenatt Oil": 50, "Aroma Oil": 60, "Herbaroma Oil": 70, "Coconut Oil": 80, "WATAPO Oil": 90, "Foot Massage Oil": 100}
#เช็คว่ากรอกข้อมูลและเลือกเวลารึยัง 
def check2():
    global first_name,last_name,phone_number
    first_name = et1.get().strip() 
    last_name = et2.get().strip()
    phone_number = et3.get().strip()
    hour=choicehour.get().strip()#บรรทัดนี้รับค่าที่ผู้ใช้เลือกใน ComboBox (ในตัวแปร choicehour) และนำมาเก็บในตัวแปร hour โดยลบช่องว่างที่อาจป้อนผิดพลาดด้านหน้าและด้านหลังของข้อความที่ผู้ใช้เลือก.
    
    if not first_name or not hour or not last_name or not phone_number or hour=="0":
        def gotoroot():
            Error3.destroy()
            root.deiconify()
        Error3 = tk.Toplevel()
        Error3.title("แจ้งเตือน")
        Error3.geometry("500x580")
        Error3.resizable(False,False)
        Error3.option_add("*Font", "consolas 15")
        Error3.configure(background="#EADFF2")
        image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (3).png") 
        image2 = image2.resize((500, 500), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(Error3, image=photo2)
        label2.pack()
        Button(Error3,text="OKกะเทย",bg="red",fg="black",width=15,command=gotoroot).place(x=180,y=510)
        Error3.mainloop()
    
    else :
        oil()
        
def check1():
    p = et3.get()
    if len(p) == 10 and p.isdigit():
        check2()
    else:
        def gotoroot2():
            Error4.destroy()
            root.deiconify()
        Error4 = tk.Toplevel()
        Error4.title("แจ้งเตือน")
        Error4.geometry("500x580")
        Error4.resizable(False,False)
        Error4.option_add("*Font", "consolas 15")
        Error4.configure(background="#EADFF2")
        image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (5).png") 
        image2 = image2.resize((500, 500), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(Error4, image=photo2)
        label2.pack()
        Button(Error4,text="OKกะเทย",bg="red",fg="black",width=15,command=gotoroot2).place(x=180,y=510)
        Error4.mainloop()
#ส่งข้อมูลไปsqlist  
def exit_money():
    global total_pricemm
    save_receipt()
    total_pricemm = 0
    money1.destroy() #ปิดหน้าต่างที่เลือก
    root.deiconify() #ย้อนไปที่หน้าต่างที่เลือก
    clear_text()
#คิวอาร์โค้ด พพ. 
def money():
    global money1,photo,total_price,total_pricemm
    rere.destroy()
    money1 = tk.Toplevel() # จะสร้างหน้าต่างย่อยใหม่และกำหนดอ็อบเจกต์ของหน้าต่างย่อยนี้ให้กับตัวแปร money1 เพื่อให้คุณสามารถทำการกำหนดคุณสมบัติและเพิ่มองค์ประกอบกราฟิกลงในหน้าต่างย่อยนี้ต่อไปได้. หน้าต่างย่อยนี้จะเป็นหน้าต่างอิสระที่แสดงบนหน้าต่างหลักและคุณสามารถปิดหน้าต่างย่อยนี้เมื่อคุณต้องการโดยไม่ส่งผลต่อหน้าต่างหลัก.
    money1.title("($ _ $)ชำระเงิน($ _ $)")
    money1.geometry("420x520")
    money1.option_add("*Font", "consolas 15")
    money1.configure(background="light yellow")
    money1.resizable(False,False)
    
    image = Image.open(r"D:\รูปโปรเจค\373490479_172313635897220_2542070284102451361_n.png") #บรรทัดนี้เปิดไฟล์รูปภาพที่ตั้งอยู่ในเส้นทางที่ระบุ ตัวอักษร "r" ด้านหน้าสตริงใช้เพื่อหลีกเลี่ยงการแปลงอักขระพิเศษ
    image = image.resize((350, 400), Image.BOX)#บรรทัดนี้ปรับขนาดรูปภาพที่โหลดเข้ามาเป็นขนาดใหม่คือ 400x400 พิกเซล โดยใช้ตัวกรองการสกัด ("Image.BOX") นี่หมายความว่ารูปภาพจะถูกย่อหรือขยายเพื่อให้พอดีกับขนาดที่ระบุโดยยังคงความสัดส่วนเดิม
    photo = ImageTk.PhotoImage(image)#หลังจากปรับขนาดรูปภาพแล้ว รูปภาพจะถูกแปลงเป็นออบเจ็กต์ PhotoImage โดยใช้ฟังก์ชัน ImageTk.PhotoImage() นี้เป็นการที่จำเป็นเพื่อแสดงรูปภาพใน GUI ของ tkinter เนื่องจาก tkinter ไม่รองรับการแสดงออบเจ็กต์ PIL Image โดยตรง

    label = tk.Label(money1, image=photo)#บรรทัดนี้สร้างวิดเจ็ต Label ของ tkinter โดยให้ Label นี้เชื่อมโยงกับหน้าต่างหรือกรอบ tkinter ที่ชื่อ "money1" และกำหนดรูปภาพที่จะแสดงใน Label โดยใช้ตัวแปร "photo" ซึ่งเป็นรูปภาพที่ได้รับการปรับขนาดและแปลงให้อยู่ในรูปแบบที่ tkinter สามารถแสดงได้ นั่นคือรูปภาพนี้จะแสดงอยู่ใน Label.
    label.pack()#นี่เป็นการกำหนดระยะห่างรอบข้างของ Label ภายในหน้าต่างหรือกรอบนั้นๆ เพื่อให้มีการจัดวางแบบที่สวยงามและคงความสมดุลในหน้าต่างหรือกรอบ GUI ของคุณ.
    tk.Label(money1,text="ราคาที่ต้องชำระ : "+str(total_pricemm)+" บาท",fg="hot pink",bg="light yellow",font="consolas 20").place(y=410,x=30)
    tk.Button(money1,text="(♡‿♡)เสร็จสิ้น(♡‿♡)",bg="hot pink",fg="light yellow",command=exit_money).place(y=450,x=120)
#ใบเสร็จ 
def summary(): 
    global emp_list,total_pricemm,total_price,cusid,oil_types_list,oil_price_list
    showw99.destroy()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    # ดึงข้อมูลจากคอลัมน์ oil_type ในตาราง oillist
    cursor.execute('SELECT empprice FROM emplist')
    # นำข้อมูลจากคอลัมน์ oil_type มาเก็บในลิสต์
    emp_price_list = sum(int(row[0]) for row in cursor.fetchall())
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    # ดึงข้อมูลจากคอลัมน์ oil_type ในตาราง oillist
    cursor.execute('SELECT employee FROM emplist')
    # นำข้อมูลจากคอลัมน์ oil_type มาเก็บในลิสต์
    emp_list = [row[0] for row in cursor.fetchall()]
    connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = connection.cursor()
    # ลบข้อมูลทั้งหมดจากตาราง
    cursor.execute('DROP TABLE emplist')  # แทน 'your_table' ด้วยชื่อตารางของคุณ
    cursor.execute('DROP TABLE emplistshow')
    # ยืนยันการเปลี่ยนแปลง
    connection.commit()
    
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    # ดึงข้อมูลจากคอลัมน์ oil_type ในตาราง oillist
    cursor.execute('SELECT oilprice FROM oillist')
    # นำข้อมูลจากคอลัมน์ oil_type มาเก็บในลิสต์
    oil_price_list = sum(int(row[0]) for row in cursor.fetchall())
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    # ดึงข้อมูลจากคอลัมน์ oil_type ในตาราง oillist
    cursor.execute('SELECT oil_type FROM oillist')
    # นำข้อมูลจากคอลัมน์ oil_type มาเก็บในลิสต์
    oil_types_list = [row[0] for row in cursor.fetchall()]
    connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = connection.cursor()
    # ลบข้อมูลทั้งหมดจากตาราง
    cursor.execute('DROP TABLE oillist')  # แทน 'your_table' ด้วยชื่อตารางของคุณ
    cursor.execute('DROP TABLE oillistshow')
    # ยืนยันการเปลี่ยนแปลง
    connection.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS oillist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                oil_type TEXT,
                oilprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS emplist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee TEXT,
                empprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS oillistshow (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                oil_type TEXT,
                oilprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS emplistshow (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee TEXT,
                empprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    bo.destroy()
    from datetime import datetime
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    # รับค่าเวลาการนวดที่เลือก
    selected_hour = choicehour.get()
    # แปลงเวลาเป็นนาที (หากมีการเลือกเวลา)
    if "30" in selected_hour:
        total_minutes = 30*5
    elif "60" in selected_hour:
        total_minutes = 60*5
    elif "120" in selected_hour:
        total_minutes = 120*5
    elif "180" in selected_hour:
        total_minutes = 180*5
    else:
        total_minutes = (int(choicehour.get())*10)
    # คำนวณราคา
    total_price = oil_price_list + emp_price_list + total_minutes
    #ถ้ากรอกรหัสลูกค้าจะได้รับส่วนลด5%
    customer_id = et9.get()
# ตรวจสอบว่ารหัสลูกค้าถูกต้องและมีในฐานข้อมูล SQLite
    if customer_id and customer_id.strip():
        connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM member WHERE CustomerID=?", (customer_id,))
        customer_data = cursor.fetchone()
        connection.close()
        # ตรวจสอบว่าพบรหัสลูกค้าในฐานข้อมูล และ total_price > 500
        if customer_data and total_price > 500:
            total_pricemm = total_price - (total_price * 0.1)
        else:
            total_pricemm = total_price
    else:
            total_pricemm = total_price
    r=messagebox.showinfo("ใบเสร็จ","กรุณาตรวจสอบข้อมูลของท่าน")
    if r :
        global rere
        rere=tk.Toplevel()
        rere.title("ʕ； •`ᴥ•´ʔใบเสร็จʕ； •`ᴥ•´ʔ")
        rere.geometry("1000x500")
        # rere.resizable(False,False)
        rere.option_add("*Font", "consolas 15")
        rere.configure(background="light yellow")
        frame = tk.Frame(rere)
        frame.place(x=10)
        listbox = tk.Listbox(frame, width=40, height=50)
        listbox.configure(bg="light pink")
        listbox.place(x=10)
        xxx=tk.Label(rere,text="🤑ใบเสร็จ🤑" ,fg="black",bg="light yellow",font="consolas 30")
        xxx.place(x=380,y=20)
        tk.Button(rere,text="เสร็จสิ้น",fg="black",bg="light pink",command=money).place(x=730,y=20)
        ee=tk.Label(rere,text="。･:･ ⌒♡*:･。 ⌒♥ ✧*:･ﾟ✧･:･ ⌒♡*:･。 ⌒♥  ☆ﾟ.*･｡ﾟ *:･ﾟ★  ★｡･ ｡･:･ﾟ☆ ｡･:★･:･ ⌒♡*:･。 ⌒♥ ✧*:･ﾟ✧ ☆ﾟ.*･｡ﾟ *:･ﾟ★  ★｡･ ｡･:･ﾟ☆ ｡･:★",fg="hot pink",bg="light yellow")
        ee.place(x=10,y=80)
        aaa=tk.Label(rere,text="ชื่อ : "+ et1.get() +"  นามสกุล : "+ et2.get() +"  โทร : "+ et3.get(),fg="black",bg="light yellow")
        aaa.place(x=10,y=130)
        a=tk.Label(rere,text="โทร : "+ et3.get(),fg="black",bg="light yellow")
        a.place(x=10,y=170)
        bbb=tk.Label(rere,text="ระยะเวลา "+ str(choicehour.get()) +" นาที"+"  =  "+ str(total_minutes) +" บาท",fg="black",bg="light yellow")
        bbb.place(x=10,y=210)
        ccc = tk.Label(rere, text="น้ำมัน : " + (str(oil_types_list)) + " = " + str(oil_price_list) + " บาท", fg="black", bg="light yellow")
        ccc.place(x=10, y=250)
        ddd = tk.Label(rere, text="พนักงาน : " + (str(emp_list)) + " = " + str(emp_price_list) + " บาท", fg="black", bg="light yellow")
        ddd.place(x=10, y=290)
        eee=tk.Label(rere,text="วันที่ : "+ formatted_datetime ,fg="black",bg="light yellow")
        eee.place(x=10,y=330)
        t=tk.Label(rere,text="ราคาปกติ : "+ str(total_price) +" บาท" ,fg="black",bg="light yellow")
        t.place(x=10,y=370)
        e=tk.Label(rere,text="。･:･ ⌒♡*:･。 ⌒♥ ✧*:･ﾟ･:･ ⌒♡*:･。 ⌒♥ ✧ ☆ﾟ.*･｡ﾟ *:･ﾟ★  ★｡･ ｡･:･ﾟ☆ ｡･:★･:･ ⌒♡*:･。 ⌒♥ ✧*:･ﾟ✧ ☆ﾟ.*･｡ﾟ *:･ﾟ★  ★｡･ ｡･:･ﾟ☆ ｡･:★",fg="hot pink",bg="light yellow")
        e.place(x=10,y=400)
        xxx=tk.Label(rere,text="ราคารวม : "+ str(total_pricemm),fg="black",bg="light yellow",font="consolas 30")
        xxx.place(x=330,y=420)
        xx=tk.Label(rere,text="***ลดราคา 10 % เมื่อมีค่าบริการมากกว่า 500 บาท เฉพาะสมาชิกร้านฟิวจี้อาบอบนวด สมัครฟรี!***",fg="black",bg="light yellow",font="consolas 10")
        xx.place(x=230,y=470)
lll=[]
def waitemp():
    ag2.destroy()
    global showw99
    showw99=tk.Toplevel()
    showw99.title("♫•*¨พนักงาน*•.¸¸♪")
    showw99.geometry("900x800")
    showw99.resizable(False,False)
    showw99.option_add("*Font", "consolas 20")
    showw99.configure(background="#F5E9E2")
    #ทำการดึงข้อมูล
    def fetch_data99():
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, employee, empprice FROM emplistshow")
        data = cursor.fetchall()
        for row in data:
            listbox.insert(END, row)  # เพิ่มข้อมูลลงใน Listbox
        conn.close()
    #สร้างเฟรมให้listboxอยู่
    frame = tk.Frame(showw99)
    frame.pack()
    #สร้างlistboxในเฟรม
    listbox = tk.Listbox(frame, width=50, height=20)
    listbox.configure(bg="#99BDB8")
    listbox.pack()
    image2 = Image.open(r"C:\Users\HP\Downloads\ดีไซน์ที่ยังไม่ได้ตั้งชื่อ (16).png") 
    image2 = image2.resize((900, 800), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(showw99, image=photo2)
    label2.pack()
    # ปุ่มสำหรับดึงข้อมูล
    fetch_button = tk.Button(showw99, text=" แสดงรายการ ",font="consolas 20",bg="#644A4F",fg="light yellow", command=fetch_data99)
    fetch_button.place(x=100,y=700)
    #ทำการล้างข้อมูลในลิสบ็อก
    def clear_frame99():
        listbox.delete(0,END)
    button = tk.Button(showw99, text="  ล้างข้อมูล  ",font="consolas 20",bg="#644A4F",fg="light yellow",command=clear_frame99)
    button.place(x=380,y=700)
    bbutton = tk.Button(showw99, text="    ถัดไป    ",font="consolas 20",bg="#644A4F",fg="light yellow",command=summary)
    bbutton.place(x=650,y=700)
    mainmenu = tk.Menu(showw99)
    showw99.config(menu=mainmenu)
    submenu99 = tk.Menu(mainmenu, tearoff=0) #นี่คือการสร้างเมนูย่อย (sub-menu) โดยใช้ tk.Menu(mainmenu) เพื่อเชื่อมโยงเมนูย่อยนี้กับเมนูหลัก mainmenu
    submenu99.add_command(label="ʕっ•ᴥ•ʔっยกเลิกรายการʕっ•ᴥ•ʔっ", command=delete99)
    submenu99.configure(bg='light yellow',fg="#644A4F")
    submenu99.add_command(label="ʕっ•ᴥ•ʔっย้อนกลับʕっ•ᴥ•ʔっ", command=gobackemp)
    submenu99.configure(bg='light yellow',fg="#644A4F")
    mainmenu.add_cascade(label="✎เพิ่มเติม✎", menu=submenu99)# กำหนดเมนูหลักให้หน้าต่างย่อย คือการกำหนดให้เมนูหลัก (main menu) ของหน้าต่างย่อย (Toplevel) ชื่อ neww ใช้เมนูหลักที่คุณได้สร้างไว้และเก็บไว้ในตัวแปร mainmenu.
    showw99.mainloop()
def gobackemp():
    showw99.destroy()
    bo.deiconify()
def delete99():
        global dlll,et999
        dlll = tk.Toplevel()
        dlll.title(">⌓<ลบข้อมูล>⌓<")
        dlll.geometry("500x100")
        dlll.option_add("*Font", "consolas 15")
        dlll.configure(background="light yellow")
        image2 = Image.open(r"C:\Users\HP\Downloads\กรุณาเลือกคิวที่จะลบ  (3).png") 
        image2 = image2.resize((500, 100), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(dlll, image=photo2)
        label2.pack()
        et999 = tk.Entry(dlll)
        et999.place(x=230,y=15)
        et999.configure(background="#644A4F",fg="light yellow")
        tk.Button(dlll,text="(⍤3⍤)ยืนยัน(⍤3⍤)",bg="#644A4F",fg="light yellow",width=10,command=deletenext99).place(x=80,y=50)
        tk.Button(dlll,text="(⍤3⍤)ย้อนกลับ(⍤3⍤)",bg="#644A4F",fg="light yellow",width=10,command=gogo17).place(x=280,y=50)
        dlll.mainloop()
        
    #ลบข้อมูลในsqlistขั้นลบในsqlist
def deletenext99():
        global et999
        # เชื่อมต่อกับฐานข้อมูล SQLite3
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        # สร้างคำสั่ง SQL สำหรับลบข้อมูล
        # เช่น ลบข้อมูลในตาราง receipts ที่มี id = 1
        id = et999.get()
        cursor.execute('''
            DELETE FROM emplist
            WHERE id = ?
        ''', (id,))
        cursor.execute('''
            DELETE FROM emplistshow
            WHERE id = ?
        ''', (id,))
        # ยืนยันการเปลี่ยนแปลง
        conn.commit()
        # ปิดการเชื่อมต่อกับฐานข้อมูล
        conn.close()
        p = messagebox.showinfo("໒( ●ᴥ ●)ʋการลบข้อมูล","ดำเนินการเสร็จสิ้น(¯ε ¯)\nʕ； •`ᴥ•´ʔ   ʕ>⌓<｡ʔ ʕ ◔ᴥ◔ ʔ")
        if p:
            showw99.deiconify()
            dlll.destroy()
    
def select_employee(employee): #เป็นฟังชั่นแลมด้าที่ถูกเรียกเมื่อคลิก select_employee(emp): นี่คือการเรียกใช้ฟังก์ชัน select_employee โดยส่ง emp เป็นอาร์กิวเมนต์ เมื่อปุ่มถูกคลิก
    global b,bo
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    
    # ดึงรายการพนักงานที่เคยเลือกไปแล้วจากฐานข้อมูล
    cursor.execute('SELECT employee FROM emplist')
    selected_employees = set(row[0] for row in cursor.fetchall())
    
    if employee in selected_employees:
        # กระทำเมื่อเลือกพนักงานที่เคยเลือกไปแล้ว
        def gotoemp():
            Error2.destroy()
            bo.deiconify()
        Error2 = tk.Toplevel()
        Error2.title("พนักงาน")
        Error2.geometry("500x580")
        Error2.resizable(False,False)
        Error2.option_add("*Font", "consolas 15")
        Error2.configure(background="#EADFF2")
        image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (1).png") 
        image2 = image2.resize((500, 500), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(Error2, image=photo2)
        label2.pack()
        Button(Error2,text="OKกะเทย",bg="red",fg="black",width=15,command=gotoemp).place(x=180,y=510)
        Error2.mainloop()
    else:
        lll.append(employee)
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        # ดึงค่าคอลัมน์ total_price จากตาราง oillist
        cursor.execute('SELECT empprice FROM emplist')

    # ดึงผลรวมของคอลัมน์ total_price จากผลลัพธ์ของคำสั่ง SQL
        totalempprice = sum(int(row[0]) for row in cursor.fetchall())
        totalempprice2 = ("ราคารวม :"+ str(totalempprice)+" บาท")
        emp = lll[0]
        empprce =  employees.get(lll[0])
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO emplist (employee, empprice, total_price)
        VALUES (?, ?, ?)
    ''', (emp, empprce, totalempprice2))
        conn.commit()
        totalempprice2 = ("ราคารวม :"+ str(totalempprice)+" บาท")
        emp2 = ("พนักงาน : "+lll[0])
        empprce2 =  ("ราคา : "+str(employees.get(lll[0]))+" บาท")
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO emplistshow (employee, empprice, total_price)
        VALUES (?, ?, ?)
    ''', (emp2, empprce2, totalempprice2))
        conn.commit()
        aggg()
def aggg():
    global ag2
    lll.clear()
    ag2 = tk.Toplevel()
    ag2.title("พนักงาน")
    ag2.geometry("700x500")
    ag2.resizable(False,False)
    ag2.option_add("*Font", "consolas 15")
    ag2.configure(background="#EADFF2")
    image2 = Image.open(r"C:\Users\HP\Downloads\ต้องการเลือกรายการเพิ่มหรือไม่.png") 
    image2 = image2.resize((700, 500), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(ag2, image=photo2)
    label2.pack()
        
    tk.Button(ag2,text="ต้องการ",width=25,bg="#AD5890",fg="#EADFF2",command=boo).place(x=50,y=400)
    tk.Button(ag2,text="ไม่ต้องการ",width=25,bg="#AD5890",fg="#EADFF2",command=waitemp).place(x=400,y=400)
    ag2.mainloop()
def boo():
    global bo
    ag2.destroy()
    
    bo.deiconify()

#เลือกพนักงาน 
def boy():
    global bo
    showw9.destroy()
    neww.destroy()
    bo = tk.Toplevel()
    bo.title("♫•*¨พนักงาน*•.¸¸♪")
    bo.geometry("1060x750")
    bo.option_add("*Font", "consolas 15")
    bo.configure(background="light yellow")
    bo.resizable(False,False)
    
    mainmenu = tk.Menu(bo)
    bo.config(menu=mainmenu) # กำหนดเมนูหลักให้หน้าต่างย่อย คือการกำหนดให้เมนูหลัก (main menu) ของหน้าต่างย่อย (Toplevel) ชื่อ neww ใช้เมนูหลักที่คุณได้สร้างไว้และเก็บไว้ในตัวแปร mainmenu.
    submenu8 = tk.Menu(mainmenu, tearoff=0) #นี่คือการสร้างเมนูย่อย (sub-menu) โดยใช้ tk.Menu(mainmenu) เพื่อเชื่อมโยงเมนูย่อยนี้กับเมนูหลัก mainmenu
    submenu8.add_command(label="ʕっ•ᴥ•ʔっย้อนกลับʕっ•ᴥ•ʔっ", command=gogo18)
    submenu8.configure(bg='light yellow',fg="#644A4F")
    mainmenu.add_cascade(label="✎เพิ่มเติม✎", menu=submenu8)
    
    # ในส่วนของสร้าง photo_buttons ให้เพิ่มรูปภาพในตัวแปร photo_buttons ด้วย
    for employee_name, price in employees.items(): #คือการประกาศลูป for ที่จะวนลูปที่ดิกชันนารี empolyees โดย employee_name และ price คือตัวแปรที่จะใช้เก็บค่าชื่อพนักงานและราคาตามลำดับในแต่ละรอบของลูป.
        # โหลดรูปภาพที่ต่างกันสำหรับแต่ละประเภทน้ำมัน
        if employee_name == "B1":
            image1 = Image.open(r"C:\Users\HP\Downloads\BB1.png")
        elif employee_name == "B2":
            image1 = Image.open(r"C:\Users\HP\Downloads\bb2.png")
        elif employee_name == "B3":
            image1 = Image.open(r"C:\Users\HP\Downloads\bb3.png")
        elif employee_name == "B4":
            image1 = Image.open(r"C:\Users\HP\Downloads\bb4.png")
        elif employee_name == "B5":
            image1 = Image.open(r"C:\Users\HP\Downloads\bb5.png")
        elif employee_name == "B6":
            image1 = Image.open(r"C:\Users\HP\Downloads\b6.png")
        # เพิ่มเงื่อนไขสำหรับประเภทน้ำมันอื่น ๆ ตามที่คุณต้องการ

        image1 = image1.resize((300, 300), Image.BOX) 
        photo = ImageTk.PhotoImage(image1) #แปลงรูปเป็น ImageTk.PhotoImage ด้วย ImageTk.PhotoImage(image1) เพื่อใช้ในการแสดงใน GUI.
        photo_buttons[employee_name] = photo 
        
    for i, (employee, price) in enumerate(employees.items()):
        # เพิ่มรูปภาพในปุ่มใช้วิธี image=photo_buttons[employee] โดยใช้ compound="top" 
        tk.Button(bo, text=f"{employee} ({price} baht)",bg="#644A4F",fg="light yellow", image=photo_buttons[employee], compound="top",width=350, command=lambda emp=employee: select_employee(emp)).grid(row=i // 3, column=i % 3) #photoimage คือ photo_buttons[employee_name] = photo  
        #emp=employee: นี่คือการสร้างพารามิเตอร์ emp สำหรับ Lambda Function และกำหนดให้มีค่าเท่ากับ employee ซึ่งคือพารามิเตอร์ที่คุณต้องการส่งเข้าไปในฟังก์ชัน select_employee เมื่อปุ่มถูกคลิก
    Label(bo,text="ʕ•ᴥ•ʔกรุณาเลือกพนักงานที่ต้องการʕ•ᴥ•ʔ",fg="#644A4F",bg="light yellow",bd=10,font="consolas 20").grid(columnspan=10)#การใช้ lambda นี้ช่วยในการล็อคค่า employee เมื่อปุ่มถูกคลิกและส่งค่านี้ไปยัง select_employee อย่างถูกต้อง.
#เก็บค่าที่เลือกเข้าลิสaa 
ll =[]
def waitoil():
    global showw9
    agg.destroy()
    showw9=tk.Toplevel()
    showw9.title("♫•*¨น้ำมัน*•.¸¸♪")
    showw9.geometry("900x800")
    showw9.resizable(False,False)
    showw9.option_add("*Font", "consolas 20")
    showw9.configure(background="#F5E9E2")
    #ทำการดึงข้อมูล
    def fetch_data9():
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, oil_type, oilprice FROM oillistshow")
        data = cursor.fetchall()
        for row in data:
            listbox.insert(END, row)  # เพิ่มข้อมูลลงใน Listbox
        conn.close()
    #สร้างเฟรมให้listboxอยู่
    frame = tk.Frame(showw9)
    frame.pack()
    #สร้างlistboxในเฟรม
    listbox = tk.Listbox(frame, width=50, height=20)
    listbox.configure(bg="#99BDB8")
    listbox.pack()
    # ปุ่มสำหรับดึงข้อมูล
    image2 = Image.open(r"C:\Users\HP\Downloads\ดีไซน์ที่ยังไม่ได้ตั้งชื่อ (16).png") 
    image2 = image2.resize((1000, 800), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(showw9, image=photo2)
    label2.pack()
    fetch_button = tk.Button(showw9, text=" แสดงรายการ ",font="consolas 20",bg="#644A4F",fg="light yellow", command=fetch_data9)
    fetch_button.place(x=100,y=700)
    #ทำการล้างข้อมูลในลิสบ็อก
    def clear_frame9():
        listbox.delete(0,END)
    button = tk.Button(showw9, text="  ล้างข้อมูล  ",font="consolas 20",bg="#644A4F",fg="light yellow",command=clear_frame9)
    button.place(x=380,y=700)
    bbutton = tk.Button(showw9, text="    ถัดไป    ",font="consolas 20",bg="#644A4F",fg="light yellow",command=boy)
    bbutton.place(x=650,y=700)
    mainmenu = tk.Menu(showw9)
    showw9.config(menu=mainmenu) # กำหนดเมนูหลักให้หน้าต่างย่อย คือการกำหนดให้เมนูหลัก (main menu) ของหน้าต่างย่อย (Toplevel) ชื่อ neww ใช้เมนูหลักที่คุณได้สร้างไว้และเก็บไว้ในตัวแปร mainmenu.
    
    submenu9 = tk.Menu(mainmenu, tearoff=0) #นี่คือการสร้างเมนูย่อย (sub-menu) โดยใช้ tk.Menu(mainmenu) เพื่อเชื่อมโยงเมนูย่อยนี้กับเมนูหลัก mainmenu
    submenu9.add_command(label="ʕっ•ᴥ•ʔっยกเลิกรายการʕっ•ᴥ•ʔっ", command=delete)
    submenu9.configure(bg='light yellow',fg="#644A4F")
    submenu9.add_command(label="ʕっ•ᴥ•ʔっย้อนกลับʕっ•ᴥ•ʔっ", command=gobackoil)
    submenu9.configure(bg='light yellow',fg="#644A4F")
    
    mainmenu.add_cascade(label="✎เพิ่มเติม✎", menu=submenu9)
    showw9.mainloop()
    
def gobackoil():
    showw9.destroy()
    neww.deiconify()
def delete():
        global dll,et99
        dll = tk.Toplevel()
        dll.title(">⌓<ลบข้อมูล>⌓<")
        dll.geometry("500x100")
        dll.option_add("*Font", "consolas 15")
        dll.configure(background="light yellow")
        image2 = Image.open(r"C:\Users\HP\Downloads\กรุณาเลือกคิวที่จะลบ  (3).png") 
        image2 = image2.resize((500, 100), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(dll, image=photo2)
        label2.pack()
        et99 = tk.Entry(dll)
        et99.place(x=230,y=15)
        et99.configure(background="#644A4F",fg="light yellow")
        tk.Button(dll,text="(⍤3⍤)ยืนยัน(⍤3⍤)",bg="#644A4F",fg="light yellow",width=10,command=deletenext9).place(x=80,y=50)
        tk.Button(dll,text="(⍤3⍤)ย้อนกลับ(⍤3⍤)",bg="#644A4F",fg="light yellow",width=10,command=gogo16).place(x=280,y=50)
        dll.mainloop()
    #ลบข้อมูลในsqlistขั้นลบในsqlist
def deletenext9():
        global et99
        # เชื่อมต่อกับฐานข้อมูล SQLite3
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        # สร้างคำสั่ง SQL สำหรับลบข้อมูล
        # เช่น ลบข้อมูลในตาราง receipts ที่มี id = 1
        id = et99.get()
        cursor.execute('''
            DELETE FROM oillist
            WHERE id = ?
        ''', (id,))
        cursor.execute('''
            DELETE FROM oillistshow
            WHERE id = ?
        ''', (id,))
        # ยืนยันการเปลี่ยนแปลง
        conn.commit()
        # ปิดการเชื่อมต่อกับฐานข้อมูล
        conn.close()
        p = messagebox.showinfo("໒( ●ᴥ ●)ʋการลบข้อมูล","ดำเนินการเสร็จสิ้น(¯ε ¯)\nʕ； •`ᴥ•´ʔ   ʕ>⌓<｡ʔ ʕ ◔ᴥ◔ ʔ")
        if p:
            showw9.deiconify()
            dll.destroy()
    
def select_oil(ooiill):
    global a,neww
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    
    # ดึงรายการน้ำมันที่เคยเลือกไปแล้วจากฐานข้อมูล
    cursor.execute('SELECT oil_type FROM oillist')
    selected_oils = set(row[0] for row in cursor.fetchall())
    
    if ooiill in selected_oils:
        # กระทำเมื่อเลือกน้ำมันที่เคยเลือกไปแล้ว
        def gotooil():
            Error.destroy()
            neww.deiconify()
        Error = tk.Toplevel()
        Error.title("น้ำมัน")
        Error.geometry("500x550")
        Error.resizable(False,False)
        Error.option_add("*Font", "consolas 15")
        Error.configure(background="#EADFF2")
        image2 = Image.open(r"C:\Users\HP\Downloads\เลือกรายการซ้ำค่ะกะเทย! (1).png") 
        image2 = image2.resize((500, 500), Image.BOX) 
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(Error, image=photo2)
        label2.pack()
        Button(Error,text="OKกะเทย",bg="red",fg="black",width=15,command=gotooil).place(x=180,y=500)
        Error.mainloop()
    else:
        ll.append(ooiill)
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()

        # ดึงค่าคอลัมน์ total_price จากตาราง oillist
        cursor.execute('SELECT oilprice FROM oillist')

    # ดึงผลรวมของคอลัมน์ total_price จากผลลัพธ์ของคำสั่ง SQL
        totalprice = sum(int(row[0]) for row in cursor.fetchall())
        totalprice2 = ("ราคารวม :"+ str(totalprice)+" บาท")
        oiltype = ll[0]
        oilprice =  oil_types.get(ll[0])
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO oillist (oil_type, oilprice, total_price)
        VALUES (?, ?, ?)
    ''', (oiltype, oilprice, totalprice2))
        conn.commit()
        totalprice = sum(int(row[0]) for row in cursor.fetchall())
        totalprice2 = ("ราคารวม :"+ str(totalprice)+" บาท")
        oiltype2 = ("น้ำมัน : "+ll[0])
        oilprice2 =  ("ราคา : "+str(oil_types.get(ll[0]))+" บาท")
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO oillistshow (oil_type, oilprice, total_price)
        VALUES (?, ?, ?)
    ''', (oiltype2, oilprice2, totalprice2))
        conn.commit()
        ag()
def ag():
    global agg
    ll.clear()
    agg = Toplevel()
    agg.title("น้ำมัน")
    agg.geometry("700x500")
    agg.resizable(False,False)
    agg.option_add("*Font", "consolas 15")
    agg.configure(background="#EADFF2")
    image2 = Image.open(r"C:\Users\HP\Downloads\ต้องการเลือกรายการเพิ่มหรือไม่.png") 
    image2 = image2.resize((700, 500), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(agg, image=photo2)
    label2.pack()
    Button(agg,text="ต้องการ",command=newww,width=25,bg="#AD5890",fg="#EADFF2").place(x=50,y=400)
    Button(agg,text="ไม่ต้องการ",command=waitoil,width=25,bg="#AD5890",fg="#EADFF2").place(x=400,y=400)
    agg.mainloop()

def newww():
    agg.destroy()
    neww.deiconify()
    # neww.destroy()
    # boy()
#สร้างปุ่มน้ำมัน 
def oil():
    global neww,submenu3
    neww = tk.Toplevel()
    neww.title("oil")
    neww.geometry("1060x750")
    neww.option_add("*Font", "consolas 15")
    neww.configure(background="light yellow")
    neww.resizable(False,False)
    
    mainmenu = tk.Menu(neww)
    neww.config(menu=mainmenu) # กำหนดเมนูหลักให้หน้าต่างย่อย คือการกำหนดให้เมนูหลัก (main menu) ของหน้าต่างย่อย (Toplevel) ชื่อ neww ใช้เมนูหลักที่คุณได้สร้างไว้และเก็บไว้ในตัวแปร mainmenu.
    
    submenu3 = tk.Menu(mainmenu, tearoff=0) #นี่คือการสร้างเมนูย่อย (sub-menu) โดยใช้ tk.Menu(mainmenu) เพื่อเชื่อมโยงเมนูย่อยนี้กับเมนูหลัก mainmenu
    submenu3.add_command(label="ʕっ•ᴥ•ʔっน้ำมันนวดʕっ•ᴥ•ʔっ", command=open_link)
    submenu3.configure(bg='light yellow',fg="#644A4F")
    submenu3.add_command(label="ʕっ•ᴥ•ʔっย้อนกลับʕっ•ᴥ•ʔっ", command=gogo8)
    submenu3.configure(bg='light yellow',fg="#644A4F")
    
    mainmenu.add_cascade(label="✎เพิ่มเติม✎", menu=submenu3) #นี่คือเมนูย่อยที่คุณต้องการให้แสดงเมื่อผู้ใช้คลิกที่รายการเมนูหลักนี้ ในที่นี้คือ submenu2 ซึ่งคือเมนูย่อยที่คุณได้สร้างไว้และเพิ่มรายการเมนูย่อยลงในนั้น.
    
    for oil_type, price in oil_types.items(): #คือการประกาศลูป for ที่จะวนลูปที่ดิกชันนารี oil_types โดย oil_type และ price คือตัวแปรที่จะใช้เก็บค่าประเภทน้ำมันและราคาตามลำดับในแต่ละรอบของลูป.
        # โหลดรูปภาพที่ต่างกันสำหรับแต่ละประเภทน้ำมัน
        if oil_type == "Lamenatt Oil":
            image = Image.open(r"C:\Users\HP\Downloads\laminatt.png")
        elif oil_type == "Aroma Oil":
            image = Image.open(r"C:\Users\HP\Downloads\Aroma.png")
        elif oil_type == "Herbaroma Oil":
            image = Image.open(r"C:\Users\HP\Downloads\herbaroma.png")
        elif oil_type == "Coconut Oil":
            image = Image.open(r"C:\Users\HP\Downloads\coconut.png")
        elif oil_type == "WATAPO Oil":
            image = Image.open(r"C:\Users\HP\Downloads\Watapo.png")
        elif oil_type == "Foot Massage Oil":
            image = Image.open(r"C:\Users\HP\Downloads\foot oil.png")
        # เพิ่มเงื่อนไขสำหรับประเภทน้ำมันอื่น ๆ ตามที่คุณต้องการ

        image = image.resize((300, 300), Image.BOX)  
        photo = ImageTk.PhotoImage(image)#นี่คือการสร้าง PhotoImage จากรูปภาพ image ที่ถูกปรับขนาดแล้ว
        photo_buttons[oil_type] = photo#นี่คือการเก็บ PhotoImage ลงในตัวแปร photo_buttons โดยใช้ประเภทน้ำมัน oil_type เป็นคีย์ (key) 

    for i, (ooiill, price) in enumerate(oil_types.items()):
        # เพิ่มรูปภาพในปุ่มใช้วิธี image=photo_buttons[employee] โดยใช้ compound="top" 
        tk.Button(neww, text=f"{ooiill} ({price} baht)",bg="#644A4F",fg="light yellow", image=photo_buttons[ooiill], compound="top",width=350, command=lambda ooiii=ooiill: select_oil(ooiii)).grid(row=i // 3, column=i % 3) 
    Label(neww,text="୧ʕ•̀ᴥ•́ʔ୨กรุณาเลือกน้ำมันที่ต้องการ୧ʕ•̀ᴥ•́ʔ୨",fg="#644A4F",bg="light yellow",bd=10,font="consolas 20").grid(columnspan=10)
#แสดงข้อมูลเจ้าของร้าน
def developer_info():
    # messagebox.showinfo("(≧◇≦)เจ้าของร้านฟิวจี้อาบอบนวด (≧◇≦)", "☆ﾟนายปาณรวัฐ ไชยช่วย รหัสนักศึกษา 653050327-9☆ﾟ\n☆ﾟนางสาวสุชาดา หวานจิตร รหัสนักศึกษา 653050157-8☆ﾟ\n♫•*¨*•.♫•*¨*•ยินดีต้อนรับทุกท่านนะคะ♫•*¨*•.¸¸♪•*¨*•.") 
    global info
    info=tk.Toplevel()
    info.title(".*･｡ﾟ *:･ﾟผู้พัฒนา.*･｡ﾟ *:･ﾟ")
    info.geometry("650x650")
    info.option_add("*Font", "consolas 15")
    info.configure(background="light yellow")
    info.resizable(False,False)
    image2 = Image.open(r"C:\Users\HP\Downloads\ปาณรวัฐ ไชยช่วย 653050327-9 (1).png") 
    image2 = image2.resize((600, 600), Image.BOX)#บรรทัดนี้ปรับขนาดรูปภาพที่โหลดเข้ามาเป็นขนาดใหม่คือ 400x400 พิกเซล โดยใช้ตัวกรองการสกัด ("Image.BOX") นี่หมายความว่ารูปภาพจะถูกย่อหรือขยายเพื่อให้พอดีกับขนาดที่ระบุโดยยังคงความสัดส่วนเดิม
    photo2 = ImageTk.PhotoImage(image2)#หลังจากปรับขนาดรูปภาพแล้ว รูปภาพจะถูกแปลงเป็นออบเจ็กต์ PhotoImage โดยใช้ฟังก์ชัน ImageTk.PhotoImage() นี้เป็นการที่จำเป็นเพื่อแสดงรูปภาพใน GUI ของ tkinter เนื่องจาก tkinter ไม่รองรับการแสดงออบเจ็กต์ PIL Image โดยตรง
    label2 = tk.Label(info, image=photo2)
    label2.pack()
    tk.Button(info,text=".*･｡ﾟ *:･ﾟ(♡‿♡)ย้อนกลับ(♡‿♡).*･｡ﾟ *:･ﾟ",bg="hot pink",fg="light yellow",command=gogo).place(x=130,y=550)
    info.mainloop()
#ปิดหน้าต่าง
def gogo20():
    root.deiconify()
    summaM.destroy()
def gogo19():
    root.deiconify()
    summa.destroy()
def gogo18():
    oil()
    bo.destroy()
def gogo17():
    showw99.deiconify()
    dlll.destroy()
def gogo16():
    showw9.deiconify()
    dll.destroy()
def gogo15():
    showw.deiconify()
    dl.destroy()
def gogo12():
    root.deiconify()
    rere.destroy()
def gogo11():
    root.deiconify()
    showw.destroy()
def gogo10():
    root.deiconify()
    showw2.destroy()
def gogo9():
    oil()
    bo.destroy()
def gogo8() :
    connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = connection.cursor()
    # ลบข้อมูลทั้งหมดจากตาราง
    cursor.execute('DROP TABLE oillist')  # แทน 'your_table' ด้วยชื่อตารางของคุณ
    cursor.execute('DROP TABLE oillistshow')
    # ยืนยันการเปลี่ยนแปลง
    connection.commit()
    connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = connection.cursor()
    # ลบข้อมูลทั้งหมดจากตาราง
    cursor.execute('DROP TABLE emplist')  # แทน 'your_table' ด้วยชื่อตารางของคุณ
    cursor.execute('DROP TABLE emplistshow')
    # ยืนยันการเปลี่ยนแปลง
    connection.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS oillist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                oil_type TEXT,
                oilprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS emplist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee TEXT,
                empprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS oillistshow (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                oil_type TEXT,
                oilprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS emplistshow (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee TEXT,
                empprice INTEGER,
                total_price
            )
        ''')
    conn.commit()
    root.deiconify()
    neww.destroy()
def gogo2():
    global app2
    root.deiconify()
    app2.destroy()
def gogo():
    global info
    root.deiconify()
    info.destroy()
def gogo3():
    global app
    root.deiconify()
    app.destroy()
def gogo4():
    global register_window
    root.deiconify()
    register_window.destroy()
#เปิดลิ้งเพิ่มเติม
def open_link():
        # import webbrowser
        webbrowser.open("https://www.thaimedicos.com/blog/5-best-massage-oil-of-2020/") 
#ล้างข้อมูลที่กรอกและที่เลือก 
def clear_text():
    et1.config(state=tk.NORMAL, fg="light yellow")
    et1.delete(0, tk.END)
    et2.config(state=tk.NORMAL, fg="light yellow")
    et2.delete(0, tk.END)
    et3.config(state=tk.NORMAL, fg="light yellow")
    et3.delete(0, tk.END)
    et9.config(state=tk.NORMAL, fg="light yellow")
    et9.delete(0, tk.END)
    combo.set("")
#สร้างปุ่มยืนยันแล้วรันไปตามฟังก์ชั่น 
def hellohi():
    Label(root,text="ฟิวจี้ยินดีต้อนรับ˘³˘♥",font="consolas 30",fg="#644a4f",bg="#F2E6D4",highlightbackground="light pink", highlightthickness=0).place(x=620,y=300)
#ออกจากระบบ
def exit_application():
    answer = messagebox.askquestion("(っ>ω <)っยืนยันการออกจากระบบ(っ>ω <)っ", "คุณต้องการออกจากระบบหรือไม่?\nʕ•ᴥ•ʔ ʕ·͡ᴥ·ʔ ʕっ•ᴥ•ʔっ ୧ʕ•̀ᴥ•́ʔ୨ ʕ≧ᴥ≦ʔ ")
    if answer == "yes":
        connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = connection.cursor()
        # ลบข้อมูลทั้งหมดจากตาราง
        cursor.execute('DROP TABLE oillist')  # แทน 'your_table' ด้วยชื่อตารางของคุณ
        cursor.execute('DROP TABLE oillistshow')
        # ยืนยันการเปลี่ยนแปลง
        connection.commit()
        connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = connection.cursor()
        # ลบข้อมูลทั้งหมดจากตาราง
        cursor.execute('DROP TABLE emplist')  # แทน 'your_table' ด้วยชื่อตารางของคุณ
        cursor.execute('DROP TABLE emplistshow')
        # ยืนยันการเปลี่ยนแปลง
        connection.commit()
        connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = connection.cursor()
        # ลบข้อมูลทั้งหมดจากตาราง
        connection.commit()
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS oillist (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    oil_type TEXT,
                    oilprice INTEGER,
                    total_price
                )
            ''')
        conn.commit()
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS emplist (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee TEXT,
                    empprice INTEGER,
                    total_price
                )
            ''')
        conn.commit()
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS oillistshow (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    oil_type TEXT,
                    oilprice INTEGER,
                    total_price
                )
            ''')
        conn.commit()
        conn = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS emplistshow (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee TEXT,
                    empprice INTEGER,
                    total_price
                )
            ''')
        conn.commit()
        root.destroy()
#ดึงข้อมูลจากตารางโดยใช้รหัสลูกค้า
def showmem(event):
    global et9
    q=et9.get()
    if not q:
        return
    connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
    cursor = connection.cursor()
        # ดึงข้อมูลจากตารางโดยใช้ ID ที่กรอกเข้ามา
    cursor.execute("SELECT * FROM member WHERE CustomerID=?", (q,))
    data = cursor.fetchone()
    if data:
        et1.delete(0, tk.END)
        et1.insert(0, data[2])  # 1 คือ index ของ firstname ในข้อมูล
        et1.config(state="readonly",fg="#644a4f")
        et2.delete(0, tk.END)
        et2.insert(0, data[3])  # 2 คือ index ของ lastname ในข้อมูล
        et2.config(state="readonly",fg="#644a4f")
        et3.delete(0, tk.END)
        et3.insert(0, data[4])
        et3.config(state="readonly",fg="#644a4f")
        et9.config(state="readonly",fg="#644a4f")
    
def open(event):
    if et10.get() == "ฟิวจี้ขายหอย":
        et10.delete(0, tk.END)  # ลบข้อความที่อยู่ใน et10 ทั้งหมด
        et10.insert(0, "ยินดีต้อนรับค่ะกะเทย")  # แทนที่ด้วยข้อความ "*" ใน et10
        yy.config(state=tk.NORMAL)
        cc.config(state=tk.NORMAL)
        menumain.entryconfig("♪ หน้าร้าน ♪",state=tk.NORMAL)
        menumain.entryconfig("☼ ผู้ดูแลระบบ ☼",state=tk.NORMAL)
        menumain.entryconfig("☯สรุปยอด☯",state=tk.NORMAL)
        et10.config(state="readonly",fg="#644a4f")
def summaa():
    global summa
    summa=tk.Toplevel()
    summa.title(".*･｡ﾟ *:･ﾟสรุปยอดรายวัน.*･｡ﾟ *:･ﾟ")
    summa.geometry("650x300")
    summa.option_add("*Font", "consolas 25")
    summa.configure(background="#F5E9E2")
    summa.resizable(False,False)
    def generate_summary():
        connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = connection.cursor()
        # ดึงข้อมูลการขายจากฐานข้อมูล
        cursor.execute("SELECT data, SUM(total_price) FROM historysum GROUP BY data")
        results = cursor.fetchall() 
        style = ttk.Style()
        style.configure("Treeview", font=("consolas", 15)) 
        style.configure("Treeview.Heading", font=("consolas", 15))
        for row in result_tree.get_children():
            result_tree.delete(row)
        # แสดงผลลัพธ์ในตาราง
        for date, total in results:
            total_with_baht = f"{total} บาท"
            result_tree.insert("", "end", values=(date, total_with_baht))
    result_tree = ttk.Treeview(summa, columns=("Date", "Total"))
    result_tree.heading("#1", text="วันที่")
    result_tree.heading("#2", text="ยอดรวม")
    result_tree.pack()
    vertical_scrollbar = ttk.Scrollbar(summa, orient="vertical", command=result_tree.yview)
    # เชื่อมตาราง Treeview กับ Scrollbar
    result_tree.configure(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.place(x=610,y=30)
    image2 = Image.open(r"C:\Users\HP\Downloads\ดีไซน์ที่ยังไม่ได้ตั้งชื่อ (20).png") 
    image2 = image2.resize((650, 300), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(summa, image=photo2)
    label2.pack()
    generate_button = tk.Button(summa, text="สรุปยอดขาย",font="consolas 15",bg="#644a4f",fg="light yellow", command=generate_summary)
    generate_button.place(x=150,y=230)
    generate_button2 = tk.Button(summa, text="ย้อนกลับ",font="consolas 15",bg="#644a4f",fg="light yellow", command=gogo19)
    generate_button2.place(x=420,y=230)
    summa.mainloop()
def summaaM():
    global summaM
    summaM=tk.Toplevel()
    summaM.title(".*･｡ﾟ *:･ﾟสรุปยอดรายเดือน.*･｡ﾟ *:･ﾟ")
    summaM.geometry("650x300")
    summaM.option_add("*Font", "consolas 25")
    summaM.configure(background="#F5E9E2")
    summaM.resizable(False,False)
    def generate_summaryM():
        connection = sqlite3.connect(r"D:\pt3\sqlite\ShopfewfeeJeje.db")
        cursor = connection.cursor()
        # ดึงข้อมูลการขายจากฐานข้อมูล
        # เปลี่ยน SQL Query เพื่อรวมยอดขายรายเดือน
        cursor.execute("SELECT strftime('%Y-%m', data) AS month, SUM(total_price) FROM historysum GROUP BY month")

        results = cursor.fetchall() 
        style = ttk.Style()
        style.configure("Treeview", font=("consolas", 15)) 
        style.configure("Treeview.Heading", font=("consolas", 15))
        for row in result_tree.get_children():
            result_tree.delete(row)
        # แสดงผลลัพธ์ในตาราง
        for month, total in results:
            total_with_baht = f"{total} บาท"
            result_tree.insert("", "end", values=(month, total_with_baht))
    result_tree = ttk.Treeview(summaM, columns=("Date", "Total"))
    result_tree.heading("#1", text="วันที่")
    result_tree.heading("#2", text="ยอดรวม")
    result_tree.pack()
    vertical_scrollbar = ttk.Scrollbar(summaM, orient="vertical", command=result_tree.yview)
    # เชื่อมตาราง Treeview กับ Scrollbar
    result_tree.configure(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.place(x=610,y=30)
    image2 = Image.open(r"C:\Users\HP\Downloads\ดีไซน์ที่ยังไม่ได้ตั้งชื่อ (20).png") 
    image2 = image2.resize((650, 300), Image.BOX) 
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(summaM, image=photo2)
    label2.pack()
    generate_button = tk.Button(summaM, text="สรุปยอดขาย",font="consolas 15",bg="#644a4f",fg="light yellow", command=generate_summaryM)
    generate_button.place(x=150,y=230)
    generate_button2 = tk.Button(summaM, text="ย้อนกลับ",font="consolas 15",bg="#644a4f",fg="light yellow", command=gogo20)
    generate_button2.place(x=420,y=230)
    summaM.mainloop()
########################################################################################################
#หน้าต่างแรก 
root = tk.Tk() #การสร้างหน้าต่างหลัก จะสร้างหน้าต่างหลักใหม่และกำหนดอ็อบเจกต์ของหน้าต่างหลักนี้ให้กับตัวแปร root เพื่อให้คุณสามารถเพิ่มองค์ประกอบกราฟิกและดำเนินการอื่น ๆ บนหน้าต่างหลักนี้ในโปรแกรม Tkinter ของคุณได้. หน้าต่างหลักนี้จะเป็นหน้าต่างหลักของโปรแกรมและจะปรากฏเมื่อคุณเริ่มทำงานกับโปรแกรม Tkinter ของคุณ.
root.title("✿ ✿ ✿ ร้านฟิวจี้อาบอบนวด ✿ ✿ ✿ ")
root.option_add("*Font", "consolas 20") # เป็นเมธอดใน Tkinter ที่ใช้ในการตั้งค่าหน้าต่างหลักหรืออ็อบเจกต์ Tkinter
root.configure(background="light yellow") # คือ option ที่ระบุว่าเรากำหนดค่าการตั้งค่าแบบอักษร (font settings) โดย * ซึ่งในที่นี้หมายถึงทุกตัวอักษรในโปรแกรม.
root.geometry("1020x540") #เป็นคำสั่งใน Tkinter ที่ใช้กำหนดขนาดของหน้าต่างหลัก (main window)
root.resizable(False,False)
image2 = Image.open(r"C:\Users\HP\Downloads\ฟิวจี้อาบอบนวดนะจุ้ (1).png") 
image2 = image2.resize((1020, 540), Image.BOX) 
photo2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(root, image=photo2)
label2.pack()
#แสดงชื่อร้าน และแสดงคำว่า ชื่อ นามสกุล เบอร์ติดต่อเพื่อใช้กับentrybox 2
#สร้างช่องกรอก 
et10 = tk.Entry(root,fg="light yellow",bg="#644a4f")
et10.place(x=220,y=120)
et10.bind("<KeyRelease>",open)
et9 = tk.Entry(root,fg="light yellow",bg="#644a4f")
et9.place(x=220,y=180)
et9.bind("<KeyRelease>",showmem)
et1 = tk.Entry(root,fg="light yellow",bg="#644a4f")
et1.place(x=220,y=240)
et2 = tk.Entry(root,fg="light yellow",bg="#644a4f")
et2.place(x=220,y=300)
et3 = tk.Entry(root,fg="light yellow",bg="#644a4f")
et3.place(x=220,y=370)
#สร้างปุ่มยืนยันแล้วรันไปตามฟังก์ชั่น 
yy=tk.Button(root,text="❀ยืนยัน❀",bg="#644a4f",fg="light yellow",width=15,state=tk.DISABLED, command=check1)
yy.place(x=200,y=450)
#ปุ่มล้างข้อมูล
cc=tk.Button(root,text="❀ล้างข้อมูล❀",bg="#644a4f",fg="light yellow",width=15,state=tk.DISABLED, command=clear_text)
cc.place(x=650,y=450)
#combobox เลือกจำนวนเวลา 
choicehour = tk.StringVar(value="")#สร้างตัวแปรชนิด StringVar ของ tkinter ที่เริ่มต้นค่าเป็นข้อความว่าง ตัวแปรนี้จะใช้เก็บค่าที่ผู้ใช้เลือกใน ComboBox.
combo = ttk.Combobox(textvariable=choicehour)#สร้าง ComboBox โดยกำหนดให้ ComboBox นี้เชื่อมกับตัวแปร choicehour ที่เราสร้างขึ้น เพื่อเก็บค่าที่ผู้ใช้เลือก.
combo["values"] = ("30", "60", "120", "180")#combo["values"] = ("30 นาที", "60 นาที", "120 นาที", "180 นาที"): กำหนดค่าที่สามารถเลือกได้ใน ComboBox
combo.place(x=620,y=140)
combo.configure(foreground="#644a4f")

#ปุ่มหัวใจ
hello = tk.Button(root,text="❤❤❤❤❤",font="consolas 20",bg="#644a4f",fg="light yellow",command=hellohi)
hello.place(x=700,y=200)
#สร้างเมนู 
menumain = tk.Menu(root)
root.config(menu=menumain)#ถ้าไม่มีตรงนี้แถบเมนูจะไม่มี กำหนดเมนูที่ถูกสร้างขึ้นในตัวแปร menumain ให้กับหน้าต่างหลัก เมนูหลักที่จะปรากฏเมื่อเริ่มทำงานแอปพลิเคชัน
#เมนูย่อย 
submenu = tk.Menu(menumain, tearoff=0)#tearoff ถูกกำหนดเป็น 0 (ศูนย์) แสดงว่าไม่อนุญาตให้ถอดเมนูย่อย ถ้าเป็น 1 (หนึ่ง) แสดงว่าอนุญาตให้ถอดเมนูย่อยได้.
submenu.add_command(label="☯ผู้พัฒนา☯",font="consolas 15", command=developer_info)
submenu.configure(bg='light yellow',fg="#644A4F")
submenu.add_command(label="☯สมัครสมาชิกฟรี☯",font="consolas 15", command=register_new_user)
submenu.configure(bg='light yellow',fg="#644A4F")
submenu.add_command(label="☯รายชื่อสมาชิก☯",font="consolas 15", command=showmember)
submenu.configure(bg='light yellow',fg="#644A4F")
submenu.add_command(label="☯แก้ไขรายชื่อ☯",font="consolas 15", command=changeinfo2)
submenu.configure(bg='light yellow',fg="#644A4F")

submenu2 = tk.Menu(menumain, tearoff=0)
submenu2.add_command(label="☯ แสดงคิว ☯",font="consolas 15", command=show)
submenu2.configure(bg='light yellow',fg="#644A4F")

submenu3 = tk.Menu(menumain, tearoff=0)
submenu3.add_command(label="☯รายวัน☯",font="consolas 15", command=summaa)
submenu3.configure(bg='light yellow',fg="#644A4F")
submenu3.add_command(label="☯รายเดือน☯",font="consolas 15", command=summaaM)
submenu3.configure(bg='light yellow',fg="#644A4F")
 
#เมนูหลัก 
menumain.add_cascade(label="♪ หน้าร้าน ♪", state=tk.DISABLED, menu=submenu2)
menumain.add_cascade(label="☼ ผู้ดูแลระบบ ☼", state=tk.DISABLED, menu=submenu)    
menumain.add_cascade(label="☯สรุปยอด☯", state=tk.DISABLED, menu=submenu3) 
menumain.add_cascade(label="❀ ออกจากระบบ ❀",command=exit_application)
root.mainloop()