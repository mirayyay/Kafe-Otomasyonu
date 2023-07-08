import time
import datetime
import random
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("1280x700")
root.title("Penta Coffee Self Kasa")
root.configure(background="#876445")
Tops = Frame(root, bg="#876445", bd=20, pady=5, relief=FLAT, )
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=("times", 60, "italic"), text="Penta Coffee Self Kasa",
                 bd=20, bg="#876445", fg="white", justify=CENTER)
lblTitle.grid(row=0, column=0)
ReceiptCal_F = Frame(root, bg="#876445", bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=LEFT)
Buttons_F = Frame(ReceiptCal_F, bg="#876445", bd=2, relief=RIDGE)
Buttons_F.pack(side=TOP)
Cal_F = Frame(ReceiptCal_F, bg="#876445", bd=4, relief=RIDGE)
Cal_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg="#876445", bd=10, relief=RIDGE)
MenuFrame.pack(side=RIGHT)
siparistutari = Frame(MenuFrame, bg="#876445", bd=4)
siparistutari.pack(side=BOTTOM)
sicakicecekler = Frame(MenuFrame, bg="#876445", bd=10, relief=RIDGE)
sicakicecekler.pack(side=LEFT)
icecekler = Frame(MenuFrame, bg="#876445", bd=10, relief=RIDGE)
icecekler.pack(side=LEFT)

#değişkenlerimiz
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()


toplamtutar = StringVar()
soguktumicecekler = StringVar()
sicaktumicecekler = StringVar()
text_Input = StringVar()
operator = ""
E_frappe = StringVar()
E_ice_mocha = StringVar()
E_cold_brew = StringVar()
E_Dalgona = StringVar()
E_Limonata = StringVar()
E_Meyveli_soda = StringVar()
E_İce_espresso = StringVar()
E_İce_latte = StringVar()
E_Salep = StringVar()
E_Latte = StringVar()
E_İced_latte = StringVar()
E_Americano = StringVar()
E_Filtre_kahve = StringVar()
E_Macchiato = StringVar()
E_Espresso = StringVar()
E_Mocha = StringVar()

#İLK DEĞERLERİ
E_frappe.set("0")
E_ice_mocha.set("0")
E_cold_brew.set("0")
E_Dalgona.set("0")
E_Limonata.set("0")
E_Meyveli_soda.set("0")
E_İce_espresso.set("0")
E_İce_latte.set("0")
E_Salep.set("0")
E_Latte.set("0")
E_İced_latte.set("0")
E_Americano.set("0")
E_Filtre_kahve.set("0")
E_Macchiato.set("0")
E_Espresso.set("0")
E_Mocha.set("0")


#ÇIKIŞ BUTONU
def iExit():
    iExit = messagebox.askyesno(
        "Penta Coffee Kasa", "Çıkmak istediğinizden emin misiniz?")
    if iExit > 0:
        root.destroy()
        return


def Reset():
    #İÇLERİNİ BOŞALTIYORUZ
    toplamtutar.set("")
    soguktumicecekler.set("")
    sicaktumicecekler.set("")
    E_frappe.set("0")
    E_ice_mocha.set("0")
    E_cold_brew.set("0")
    E_Dalgona.set("0")
    E_Limonata.set("0")
    E_Meyveli_soda.set("0")
    E_İce_espresso.set("0")
    E_İce_latte.set("0")
    E_Salep.set("0")
    E_Latte.set("0")
    E_İced_latte.set("0")
    E_Americano.set("0")
    E_Filtre_kahve.set("0")
    E_Macchiato.set("0")
    E_Espresso.set("0")
    E_Mocha.set("0")
   
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
   
    
   #RESET TUŞUNA BASINCA ÖNCEDEN GİRİLEN DEĞERLERİMİZ TAMAMEN SIFIRLANIYOR ADET KISMINDA SEÇİLMEMİŞ DURUMUNA GERİ DÖNÜYOR
    txtfrappe.configure(state=DISABLED)
    txtice_mocha.configure(state=DISABLED)
    txtcold_brew.configure(state=DISABLED)
    txtDalgona.configure(state=DISABLED)
    txtLimonata.configure(state=DISABLED)
    txtMeyveli_soda.configure(state=DISABLED)
    txtOrangeJuice.configure(state=DISABLED)
    txtİce_latte.configure(state=DISABLED)
    txtSalep.configure(state=DISABLED)
    txtLatte.configure(state=DISABLED)
    txtİced_latte.configure(state=DISABLED)
    txtAmericano.configure(state=DISABLED)
    txtFiltre_kahve.configure(state=DISABLED)
    txtMacchiato.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtMocha.configure(state=DISABLED)
   

#ıtem olarak tanımlıyorum float türünde
def CostofItem():
    Item1 = float(E_frappe.get())
    Item2 = float(E_ice_mocha.get())
    Item3 = float(E_cold_brew.get())
    Item4 = float(E_Dalgona.get())
    Item5 = float(E_Limonata.get())
    Item6 = float(E_Meyveli_soda.get())
    Item7 = float(E_İce_espresso.get())
    Item8 = float(E_İce_latte.get())
    Item9 = float(E_Salep.get())
    Item10 = float(E_Latte.get())
    Item11 = float(E_İced_latte.get())
    Item12 = float(E_Americano.get())
    Item13 = float(E_Filtre_kahve.get())
    Item14 = float(E_Macchiato.get())
    Item15 = float(E_Espresso.get())
    Item16 = float(E_Mocha.get())
   
    
# burada ürün fiyatlarını belirledim.
    sogukicecekler = (Item1*14.00)+(Item2*7)+(Item3*3) + \
        (Item4*4)+(Item5*17)+(Item6*4)+(Item7*9)+(Item8*10)
    sicakicecekler = (Item9*6)+(Item10*10)+(Item11*12)+(Item12*15) + \
        (Item13*10)+(Item14*17)+(Item15*5)+(Item16*7)
   
    soguktotal = str("%.2f" % (sogukicecekler)), "TL"
    sicaktotal = str("%.2f" % (sicakicecekler)), "TL"
   
    soguktumicecekler.set(soguktotal)
    sicaktumicecekler.set(sicaktotal)
   
    TT = ((sogukicecekler+sicakicecekler))
    TC = str("%.2f" % (sogukicecekler+sicakicecekler)), "TL"
    toplamtutar.set(TC)


def chkfrappe():
    if(var1.get() == 1):
        txtfrappe.configure(state=NORMAL)
        txtfrappe.focus()
        txtfrappe.delete("0", END)
        E_frappe.set("")
    elif(var1.get() == 0):
        txtfrappe.configure(state=DISABLED)
        E_frappe.set("0")


def chkice_mocha():
    if (var2.get() == 1):
        txtice_mocha.configure(state=NORMAL)
        txtice_mocha.focus()
        txtice_mocha.delete("0", END)
        E_ice_mocha.set("")
    elif (var2.get() == 0):
        txtice_mocha.configure(state=DISABLED)
        E_ice_mocha.set("0")


def chkcold_brew():
    if (var3.get() == 1):
        txtcold_brew.configure(state=NORMAL)
        txtcold_brew.focus()
        txtcold_brew.delete("0", END)
        E_cold_brew.set("")
    elif (var3.get() == 0):
        txtcold_brew.configure(state=DISABLED)
        E_cold_brew.set("0")


def chkDalgona():
    if (var4.get() == 1):
        txtDalgona.configure(state=NORMAL)
        txtDalgona.focus()
        txtDalgona.delete("0", END)
        E_Dalgona.set("")
    elif (var4.get() == 0):
        txtDalgona.configure(state=DISABLED)
        E_Dalgona.set("0")


def chkLimonata():
    if (var5.get() == 1):
        txtLimonata.configure(state=NORMAL)
        txtLimonata.focus()
        txtLimonata.delete("0", END)
        E_Limonata.set("")
    elif (var5.get() == 0):
        txtLimonata.configure(state=DISABLED)
        E_Limonata.set("0")


def chkMeyveli_soda():
    if (var6.get() == 1):
        txtMeyveli_soda.configure(state=NORMAL)
        txtMeyveli_soda.focus()
        txtMeyveli_soda.delete("0", END)
        E_Meyveli_soda.set("")
    elif (var6.get() == 0):
        txtMeyveli_soda.configure(state=DISABLED)
        E_Meyveli_soda.set("0")


def chkİce_espresso():
    if (var7.get() == 1):
        txtİce_espresso.configure(state=NORMAL)
        txtİce_espresso.focus()
        txtİce_espresso.delete("0", END)
        E_İce_espresso.set("")
    elif (var7.get() == 0):
        txtİce_espresso.configure(state=DISABLED)
        E_İce_espresso.set("0")


def chkİce_latte():
    if (var8.get() == 1):
        txtİce_latte.configure(state=NORMAL)
        txtİce_latte.focus()
        txtİce_latte.delete("0", END)
        E_İce_latte.set("")
    elif (var8.get() == 0):
        txtİce_latte.configure(state=DISABLED)
        E_İce_latte.set("0")


def chkSalep():
    if(var9.get() == 1):
        txtSalep.configure(state=NORMAL)
        txtSalep.focus()
        txtSalep.delete("0", END)
        E_Salep.set("")
    elif(var9.get() == 0):
        txtSalep.configure(state=DISABLED)
        E_Salep.set("0")


def chkLatte():
    if (var10.get() == 1):
        txtLatte.configure(state=NORMAL)
        txtLatte.focus()
        txtLatte.delete("0", END)
        E_Latte.set("")
    elif (var10.get() == 0):
        txtLatte.configure(state=DISABLED)
        E_Latte.set("0")


def chkİced_latte():
    if (var11.get() == 1):
        txtİced_latte.configure(state=NORMAL)
        txtİced_latte.focus()
        txtİced_latte.delete("0", END)
        E_İced_latte.set("")
    elif (var11.get() == 0):
        txtİced_latte.configure(state=DISABLED)
        E_İced_latte.set("0")


def chkAmericano():
    if (var12.get() == 1):
        txtAmericano.configure(state=NORMAL)
        txtAmericano.focus()
        txtAmericano.delete("0", END)
        E_Americano.set("")
    elif (var12.get() == 0):
        txtAmericano.configure(state=DISABLED)
        E_Americano.set("0")


def chkFiltre_kahve():
    if (var13.get() == 1):
        txtFiltre_kahve.configure(state=NORMAL)
        txtFiltre_kahve.focus()
        txtFiltre_kahve.delete("0", END)
        E_Filtre_kahve.set("")
    elif (var13.get() == 0):
        txtFiltre_kahve.configure(state=DISABLED)
        E_Filtre_kahve.set("0")


def chkMacchiato():
    if (var14.get() == 1):
        txtMacchiato.configure(state=NORMAL)
        txtMacchiato.focus()
        txtMacchiato.delete("0", END)
        E_Macchiato.set("")
    elif (var14.get() == 0):
        txtMacchiato.configure(state=DISABLED)
        E_Macchiato.set("0")


def chkEspresso():
    if (var15.get() == 1):
        txtEspresso.configure(state=NORMAL)
        txtEspresso.focus()
        txtEspresso.delete("0", END)
        E_Espresso.set("")
    elif (var15.get() == 0):
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")


def chkMocha():
    if (var16.get() == 1):
        txtMocha.configure(state=NORMAL)
        txtMocha.focus()
        txtMocha.delete("0", END)
        E_Mocha.set("")
    elif (var16.get() == 0):
        txtMocha.configure(state=DISABLED)
        E_Mocha.set("0")






# Ürünler ve fiyatlarının yazdığı tablo kısmı 
frappe = Checkbutton(sicakicecekler, text="Frappe   14 TL", variable=var1, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F4DFBA", command=chkfrappe).grid(row=0, sticky=W) #TEA 14TL OLARAK DEGİSTİ
ice_mocha = Checkbutton(sicakicecekler, text="İce Mocha   7 TL", variable=var2, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkice_mocha).grid(row=1, sticky=W)#COKE 7TL OLARAK DEGİSTİ
cold_brew = Checkbutton(sicakicecekler, text="Cold Brew   3 TL", variable=var3, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkcold_brew).grid(row=2, sticky=W)#WATER 3TL OLARAK DEGİSTİ
Dalgona = Checkbutton(sicakicecekler, text="Dalgona   4TL", variable=var4, onvalue=1, offvalue=0, font=(
    "times", 20,"italic"), bg="#876445", fg="#F6D7A7", command=chkDalgona).grid(row=3, sticky=W)#AYRAN 4TL OLARAK DEGİSTİ
Limonata = Checkbutton(sicakicecekler, text="Limonata   17 TL", variable=var5, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkLimonata).grid(row=4, sticky=W)#LİMONATA 17TL OLARAK DEGİSTİ
Meyveli_soda = Checkbutton(sicakicecekler, text="Meyveli Soda   4 TL", variable=var6, onvalue=1, offvalue=0, font=(
    "times", 20,"italic"), bg="#876445", fg="#F6D7A7", command=chkMeyveli_soda).grid(row=5, sticky=W)#SODA WATER 4TL OLARAK DEGİSTİ
İce_espresso = Checkbutton(sicakicecekler, text="İce Espresso   9 TL", variable=var7, onvalue=1, offvalue=0, font=(
    "times", 20,"italic"), bg="#876445", fg="#F6D7A7", command=chkİce_espresso).grid(row=6, sticky=W)#ORANGE JUİCE 9TL OLARAK DEGİSTİ
İce_latte = Checkbutton(sicakicecekler, text="İce Latte   10 TL", variable=var8, onvalue=1, offvalue=0, font=(
    "times", 20,"italic"), bg="#876445", fg="#F6D7A7", command=chkİce_latte).grid(row=7, sticky=W)#TURKISH COFFEE 10TL OLARAK DEGİSTİ
"""Entry Box for Drinks"""
txtfrappe = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
               width=7, justify=LEFT, state=DISABLED, textvariable=E_frappe)
txtfrappe.grid(row=0, column=1)
txtice_mocha = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
                width=7, justify=LEFT, state=DISABLED, textvariable=E_ice_mocha)
txtice_mocha.grid(row=1, column=1)
txtcold_brew = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
                 width=7, justify=LEFT, state=DISABLED, textvariable=E_cold_brew)
txtcold_brew.grid(row=2, column=1)
txtDalgona = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
                 width=7, justify=LEFT, state=DISABLED, textvariable=E_Dalgona)
txtDalgona.grid(row=3, column=1)
txtLimonata = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
                    width=7, justify=LEFT, state=DISABLED, textvariable=E_Limonata)
txtLimonata.grid(row=4, column=1)
txtMeyveli_soda = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
                      width=7, justify=LEFT, state=DISABLED, textvariable=E_Meyveli_soda)
txtMeyveli_soda.grid(row=5, column=1)
txtOrangeJuice = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
                       width=7, justify=LEFT, state=DISABLED, textvariable=E_İce_espresso)
txtOrangeJuice.grid(row=6, column=1)
txtİce_latte = Entry(sicakicecekler, font=("times", 16, "bold"), bd=9,
                          width=7, justify=LEFT, state=DISABLED, textvariable=E_İce_latte)
txtİce_latte.grid(row=7, column=1)
#SICAK İÇECEKLER
Salep = Checkbutton(icecekler, text="Tarçınlı Salep   6 TL", variable=var9, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkSalep).grid(row=0, sticky=W)
Latte = Checkbutton(icecekler, text="Latte   10 TL", variable=var10, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkLatte).grid(row=1, sticky=W)
İced_latte = Checkbutton(icecekler, text="Sıcak Çikolata   12 TL", variable=var11, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkİced_latte).grid(row=2, sticky=W)
Americano = Checkbutton(icecekler, text="Americano   15 TL", variable=var12, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkAmericano).grid(row=3, sticky=W)
Filtre_kahve = Checkbutton(icecekler, text="Filtre kahve   10 TL", variable=var13, onvalue=1, offvalue=0, font=(
    "times", 20, "italic"), bg="#876445", fg="#F6D7A7", command=chkFiltre_kahve).grid(row=4, sticky=W)
Macchiato = Checkbutton(icecekler, text="Macchiato   17 TL", variable=var14, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkMacchiato).grid(row=5, sticky=W)
Espresso = Checkbutton(icecekler, text="Espresso   5 TL", variable=var15, onvalue=1, offvalue=0, font=(
    "times", 20,"italic" ), bg="#876445", fg="#F6D7A7", command=chkEspresso).grid(row=6, sticky=W)
Mocha = Checkbutton(icecekler, text="Mocha   7 TL", variable=var16, onvalue=1, offvalue=0, font=(
    "times", 20,"italic"), bg="#876445", fg="#F6D7A7", command=chkMocha).grid(row=7, sticky=W)

txtSalep = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                width=7, justify=LEFT, state=DISABLED, textvariable=E_Salep)
txtSalep.grid(row=0, column=1)
txtLatte = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                width=7, justify=LEFT, state=DISABLED, textvariable=E_Latte)
txtLatte.grid(row=1, column=1)
txtİced_latte = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                width=7, justify=LEFT, state=DISABLED, textvariable=E_İced_latte)
txtİced_latte.grid(row=2, column=1)
txtAmericano = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                 width=7, justify=LEFT, state=DISABLED, textvariable=E_Americano)
txtAmericano.grid(row=3, column=1)
txtFiltre_kahve = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                 width=7, justify=LEFT, state=DISABLED, textvariable=E_Filtre_kahve)
txtFiltre_kahve.grid(row=4, column=1)
txtMacchiato = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                  width=7, justify=LEFT, state=DISABLED, textvariable=E_Macchiato)
txtMacchiato.grid(row=5, column=1)
txtEspresso = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                  width=7, justify=LEFT, state=DISABLED, textvariable=E_Espresso)
txtEspresso.grid(row=6, column=1)
txtMocha = Entry(icecekler, font=("times", 16, "bold"), bd=9,
                        width=7, justify=LEFT, state=DISABLED, textvariable=E_Mocha)
txtMocha.grid(row=7, column=1)

#toplam tutar kısmı
lbltoplamtutar = Label(siparistutari, font=("times", 12, "italic"),
                        text="Kasa Toplam\t   ", bd=7, bg="#876445", fg="#F6D7A7")
lbltoplamtutar.grid(row=0, column=0, sticky=W)
lbltoplamtutar = Entry(siparistutari, font=("times", 14, "bold"),
                        textvariable=toplamtutar, bd=7, bg="#F6D7A7", insertwidth=2, justify=RIGHT)
lbltoplamtutar.grid(row=0, column=1)





lbltoplamtutar = Label(siparistutari, font=("times", 12,"italic"),
                     text=" \tToplam Tutar", bd=7, bg="#876445", fg="#F6D7A7")
lbltoplamtutar .grid(row=0, column=2, sticky=W)
txttoplamtutar = Entry(siparistutari, font=("times", 14, "bold"),
                     textvariable=toplamtutar, bd=7, bg="#F6D7A7", insertwidth=2, justify=RIGHT)
txttoplamtutar .grid(row=0, column=3)







#Buttonların olduğu yer burada 3 butonumuzun yaptığı görevler ve tasarımları
Toplam = Button(Buttons_F, padx=16, pady=4,  bd=7, fg="#F6D7A7",borderwidth=10, font=(
    "times", 16, ), width=8, text="Toplam", bg="#876445", command=CostofItem).grid(row=0, column=0)
Resetle = Button(Buttons_F, padx=16, pady=4, bd=7, fg="#F6D7A7",borderwidth=10, font=(
    "times", 16, ), width=8, text="Temizle", bg="#876445", command=Reset).grid(row=0, column=2)
Cikis = Button(Buttons_F, padx=16, pady=4, bd=7,  fg="#F6D7A7",borderwidth=10, font=(
    "times", 16,), width=8, text="Kapat", bg="#876445", command=iExit).grid(row=0, column=3)
"""Calculator Display"""


def btnClick(numbers):
    global operator
    operator = operator+str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_Input.set("")
   

#eşittir butonu
def btnEquals():
    global operator
    cold_brewmup = str(eval(operator))
    text_Input.set(cold_brewmup)
    operator = ""


txtDisplay = Entry(Cal_F, width=50, bg="#F6D7A7", bd=4, font=(
    "times", 12, "bold"), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")



#Hesap makinesi kodları hazır aldık programda bir hata belirirse hesap makinesi yardımıyla işlemlerin yapılması adına.
btn7 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="7", bg="#876445", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="8", bg="#876445", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="9", bg="#876445", command=lambda: btnClick(9)).grid(row=2, column=2)
btnAdd = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
                width=4, text="+", bg="#876445", command=lambda: btnClick("+")).grid(row=2, column=3)
btn4 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
               width=4, text="4", bg="#876445", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="5", bg="#876445", command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="6", bg="#876445", command=lambda: btnClick(6)).grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
                width=4, text="-", bg="#876445", command=lambda: btnClick("-")).grid(row=3, column=3)
btn1 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="1", bg="#876445", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="2", bg="#876445", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="3", bg="#876445", command=lambda: btnClick(3)).grid(row=4, column=2)
btnMult = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
                 width=4, text="*", bg="#876445", command=lambda: btnClick("*")).grid(row=4, column=3)
btn0 = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
              width=4, text="0", bg="#876445", command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=(
    "times", 16, "bold"), width=4, text="C", bg="#CA965C", command=btnClear).grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=(
    "times", 16, "bold"), width=4, text="=", bg="#876445", command=btnEquals).grid(row=5, column=2)
btnDivision = Button(Cal_F, padx=16, pady=1, bd=7, fg="#F6D7A7", font=("times", 16, "bold"),
                     width=4, text="/", bg="#876445", command=lambda: btnClick("/")).grid(row=5, column=3)

root.mainloop()
