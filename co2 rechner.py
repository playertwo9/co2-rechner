
import webbrowser as web
import tkinter as tk
from tkinter import HIDDEN, ttk

root = tk.Tk()
root.geometry('800x300')
root.title('🌍CO²-Rechner🌍')

notebook = ttk.Notebook(root)
notebook.pack()

def werte_auslesen(wert):
    if wert == '':
        return 0

    else:
        return int(wert)

NORMALE_TEXTFELD_WIDTH = 9
co2_wert = 0


frame_start = ttk.Frame(notebook, width=800, height=300)
frame_heizung = ttk.Frame(notebook, width=800, height=300)
frame_mobilität = ttk.Frame(notebook, width=800, height=300)
frame_öfendliche_verkersmittel = ttk.Frame(notebook, width=800, height=300)
frame_essen = ttk.Frame(notebook, width=800, height=300)
frame_strom = ttk.Frame(notebook, width=800, height=300)
frame_ergebnis = ttk.Frame(notebook, width=800, height=300)

frame_start.place(x=400, y=500)
frame_heizung.place(x=400, y=500)
frame_mobilität.place(x=400, y=500)
frame_öfendliche_verkersmittel.place(x=400, y=500)
frame_essen.place(x=400, y=500)
frame_strom.place(x=400, y=500)
frame_ergebnis.place(x=400, y=500)


notebook.add(frame_start, text='Start')

def los_gehts_start():
    notebook.tab(frame_heizung, state='normal')
    notebook.tab(frame_mobilität, state='disabled')
    notebook.tab(frame_öfendliche_verkersmittel, state='disabled')
    notebook.tab(frame_strom, state='disabled')
    notebook.tab(frame_essen, state='disabled')

wilkommen_label = tk.Label(frame_start, text='Herzlich Wilkommen beim Co²-Rechner', font='Helvetica')

wichtig_label = tk.Label(frame_start, text='WICHTIG:', font='Verdan', fg='red')
kriterium_label1 = tk.Label(frame_start, text='- Punkt statt komma verwenden (Englische schreibweise)', fg='red')
kriterium_label2 = tk.Label(frame_start, text='- bitte keine Tausender Punkte benutzen', fg='red')

start_cancel = tk.Button(frame_start, text='Cancel', command=quit, bg='red')
start_weiter = tk.Button(frame_start, text="Los geht's", command=los_gehts_start, bg='green')

wilkommen_label.place(x=200, y=30)

wichtig_label.place(x=50, y=70)
kriterium_label1.place(x=50, y=100)
kriterium_label2.place(x=50, y=120)

start_weiter.place(x=300, y=200)
start_cancel.place(x=406, y=200)


notebook.add(frame_heizung, text='Heizung', state=HIDDEN)

holz_v = tk.StringVar(None)
heizöl_v = tk.StringVar(None)
erdgas1_v = tk.StringVar(None)
erdgas2_v = tk.StringVar(None)
fernwärme_v = tk.StringVar(None)

def felder_leeren_heizung():
    for variable in inputs_heizung:
        variable.delete(0,  'end')

def next_tab_heizung():
    notebook.tab(frame_mobilität, state='normal')


einheit_holz_label = tk.Label(frame_heizung, text='kWh')
holz_label = tk.Label(frame_heizung, text='Holz:')
holz_textfeld = tk.Entry(frame_heizung, textvariable=holz_v, width=NORMALE_TEXTFELD_WIDTH, )

einheit_heizöl_label = tk.Label(frame_heizung, text='Liter')
heizöl_label = tk.Label(frame_heizung, text='Heizöl:')
heizöl_textfeld = tk.Entry(frame_heizung, textvariable=heizöl_v, width=NORMALE_TEXTFELD_WIDTH)

erdgas_label = tk.Label(frame_heizung, text='Erdgas:')
erdgas_textfeld = tk.Entry(frame_heizung, textvariable=erdgas1_v, width=NORMALE_TEXTFELD_WIDTH)
erdgas_label_oder = tk.Label(frame_heizung, text='m³ oder')
erdgas_textfeld2 = tk.Entry(frame_heizung, textvariable=erdgas2_v, width=NORMALE_TEXTFELD_WIDTH)
einheit_erdgas_label = tk.Label(frame_heizung, text='kWh')

fernwärme_label = tk.Label(frame_heizung, text='Fernwärme:')
fernwärme_textfeld = tk.Entry(frame_heizung, textvariable=fernwärme_v, width=NORMALE_TEXTFELD_WIDTH)
einheit_fernwärme_label = tk.Label(frame_heizung, text='kWh')

inputs_heizung = [holz_textfeld, heizöl_textfeld, erdgas_textfeld, erdgas_textfeld2, fernwärme_textfeld]

heizung_cancel = tk.Button(frame_heizung, text='Cancel', command=quit, bg='red')
heizung_next_tab = tk.Button(frame_heizung, text='-->', command=next_tab_heizung, bg='green')
heizung_delete = tk.Button(frame_heizung, text='alle Felder leeren', command=felder_leeren_heizung, bg='blue')


holz_label.place(x=50, y=35)
holz_textfeld.place(x=100, y=35)
einheit_holz_label.place(x=160, y=35)

heizöl_label.place(x=50, y=65)
heizöl_textfeld.place(x=100, y=65)
einheit_heizöl_label.place(x=160, y=65)

erdgas_label.place(x=50, y=95)
erdgas_textfeld.place(x=100, y=95)
erdgas_label_oder.place(x=160, y=95)
erdgas_textfeld2.place(x=210, y=95)
einheit_erdgas_label.place(x=250, y=95)

fernwärme_label.place(x=50, y=125)
fernwärme_textfeld.place(x=120, y=125)
einheit_fernwärme_label.place(x=170, y=125)

heizung_next_tab.place(x=265, y=200)
heizung_delete.place(x=300, y=200)
heizung_cancel.place(x=406, y=200)


notebook.add(frame_mobilität, text='Mobilität', state=HIDDEN)

elektroantrieb_v1 = tk.StringVar(None)
elektroantrieb_v2 = tk.StringVar(None)
benzin_v1 = tk.StringVar(None)
benzin_v2 = tk.StringVar(None)
benzin_v3 = tk.StringVar(None)
diesel_v1 = tk.StringVar(None)
diesel_v2 = tk.StringVar(None)
diesel_v3 = tk.StringVar(None)

def felder_leeren_mobilität():
    for variable in inputs_mobilität:
        variable.delete(0, 'end')

def next_tab_mobilität():
    notebook.tab(frame_öfendliche_verkersmittel, state='normal')

elektroantrieb_label = tk.Label(frame_mobilität, text='PKW Elektroantroantrieb')
elektroantrieb_texfeld = tk.Entry(frame_mobilität, textvariable=elektroantrieb_v1, width=NORMALE_TEXTFELD_WIDTH)
einheit_elektroantrieb = tk.Label(frame_mobilität, text='km x')
elektroantrieb_texfeld2 = tk.Entry(frame_mobilität, textvariable=elektroantrieb_v2,  width=5)
einheit_elektroantrieb2 = tk.Label(frame_mobilität, text='kWh/100')

benzin_label = tk.Label(frame_mobilität, text='PKW Verbrenner')
benzin_textfeld = tk.Entry(frame_mobilität, textvariable=benzin_v1, width=NORMALE_TEXTFELD_WIDTH)
einheit_benzin = tk.Label(frame_mobilität, text='Liter Benzin oder Gesamtstrecke')
benzin_textfeld2 = tk.Entry(frame_mobilität, textvariable=benzin_v2, width=NORMALE_TEXTFELD_WIDTH)
einheit_benzin2 = tk.Label(frame_mobilität, text='km x')
benzin_textfeld3 = tk.Entry(frame_mobilität, textvariable=benzin_v3, width=5)
einheit_benzin3 = tk.Label(frame_mobilität, text='Liter/100')

diesel_label = tk.Label(frame_mobilität, text='PKW/LKW Verbrenner')
diesel_textfeld = tk.Entry(frame_mobilität, textvariable=diesel_v1, width=NORMALE_TEXTFELD_WIDTH)
einheit_diesel1 = tk.Label(frame_mobilität, text='Liter Diesel oder Gesamtstrecke')
diesel_textfeld2 = tk.Entry(frame_mobilität, textvariable=diesel_v2, width=NORMALE_TEXTFELD_WIDTH)
einheit_diesel2 = tk.Label(frame_mobilität, text='km x')
diesel_textfeld3 = tk.Entry(frame_mobilität, textvariable=diesel_v3, width=5)
einheit_diesel3 = tk.Label(frame_mobilität, text='Liter/100')

inputs_mobilität = [elektroantrieb_texfeld, elektroantrieb_texfeld2, benzin_textfeld, benzin_textfeld2, benzin_textfeld3, diesel_textfeld, diesel_textfeld2, diesel_textfeld3]

mobilität_cancel = tk.Button(frame_mobilität, text='Cancel', command=quit, bg='red')
mobilität_next_tab = tk.Button(frame_mobilität, text='-->', command=next_tab_mobilität, bg='green')
mobilität_delete = tk.Button(frame_mobilität, text='alle Felder leeren', command=felder_leeren_mobilität, bg='blue')


elektroantrieb_label.place(x=50, y=35)
elektroantrieb_texfeld.place(x=190, y=35)
einheit_elektroantrieb.place(x=253,  y=35)
elektroantrieb_texfeld2.place(x=290, y=35)
einheit_elektroantrieb2.place(x=332, y=35)

benzin_label.place(x=50, y=65)
benzin_textfeld.place(x=150,  y=65)
einheit_benzin.place(x=210, y=65)
benzin_textfeld2.place(x=388, y=65)
einheit_benzin2.place(x=450, y=65)
benzin_textfeld3.place(x=485, y=65)
einheit_benzin3.place(x=525, y=65)

diesel_label.place(x=50, y=95)
diesel_textfeld.place(x=175, y=95)
einheit_diesel1.place(x=235, y=95)
diesel_textfeld2.place(x=410, y=95)
einheit_diesel2.place(x=470, y=95)
diesel_textfeld3.place(x=506, y=95)
einheit_diesel3.place(x=540, y=95)

mobilität_next_tab.place(x=265, y=200)
mobilität_delete.place(x=300, y=200)
mobilität_cancel.place(x=406, y=200)


notebook.add(frame_öfendliche_verkersmittel, text='öffentliche Verkehrsmittel', state=HIDDEN)

nahverkehr_spin_v = tk.StringVar()
nahverkehr_v= tk.StringVar()
reisebus_spin_v  = tk.StringVar()
reisebus_v = tk.StringVar()
bahnfahrt_spin_v  = tk.StringVar()
bahnfahrt_v = tk.StringVar()
flugreise_spin_v  = tk.StringVar()
flugreise_v = tk.StringVar()
kreutsfahrt_spin_v  = tk.StringVar()
kreutsfahrt_v = tk.StringVar()
kreutsfahrt2_spin_v  = tk.StringVar()
kreutsfahrt2_v = tk.StringVar()


def felder_leeren_öffendliche_verkersmittel():
    for variable in imputs_öffendliche_verkersmittel:
        variable.delete(0, 'end')

    for spin_variable in spin_imputs_öffendliche_verkersmittel:
        spin_variable.set(0)

def next_tab_öffendliche_verkersmittel():
    notebook.tab(frame_essen, state='normal')

nahverker_label = tk.Label(frame_öfendliche_verkersmittel, text='Nahverkehr')
nahverkehr_spinbox = tk.Spinbox(frame_öfendliche_verkersmittel, textvariable=nahverkehr_spin_v, width=NORMALE_TEXTFELD_WIDTH, from_=0, to=999999)
einheit_nahverkehr = tk.Label(frame_öfendliche_verkersmittel, text='Personen')
nahverkehr_texfeld = tk.Entry(frame_öfendliche_verkersmittel, textvariable=nahverkehr_v,  width=NORMALE_TEXTFELD_WIDTH)
einheit_nahverkehr2 = tk.Label(frame_öfendliche_verkersmittel, text='km')

reisebus_label = tk.Label(frame_öfendliche_verkersmittel, text='Reisebus')
reisebus_spinbox = tk.Spinbox(frame_öfendliche_verkersmittel, textvariable=reisebus_spin_v, width=NORMALE_TEXTFELD_WIDTH, from_=0, to=999999)
einheit_reisebus = tk.Label(frame_öfendliche_verkersmittel, text='Personen')
reisebus_texfeld = tk.Entry(frame_öfendliche_verkersmittel, textvariable=reisebus_v,  width=NORMALE_TEXTFELD_WIDTH)
einheit_reisebus2 = tk.Label(frame_öfendliche_verkersmittel, text='km')

bahnfahrt_label = tk.Label(frame_öfendliche_verkersmittel, text='Bahnfahrt')
bahnfahrt_spinbox = tk.Spinbox(frame_öfendliche_verkersmittel, textvariable=bahnfahrt_spin_v, width=NORMALE_TEXTFELD_WIDTH, from_=0, to=999999)
einheit_bahnfahrt = tk.Label(frame_öfendliche_verkersmittel, text='Personen')
bahnfahrt_texfeld = tk.Entry(frame_öfendliche_verkersmittel, textvariable=bahnfahrt_v,  width=NORMALE_TEXTFELD_WIDTH)
einheit_bahnfahrt2 = tk.Label(frame_öfendliche_verkersmittel, text='km')

flugreise_label = tk.Label(frame_öfendliche_verkersmittel, text='Flugreise')
flugreise_spinbox = tk.Spinbox(frame_öfendliche_verkersmittel, textvariable=flugreise_spin_v, width=NORMALE_TEXTFELD_WIDTH, from_=0, to=999999)
einheit_flugreise = tk.Label(frame_öfendliche_verkersmittel, text='Personen')
flugreise_texfeld = tk.Entry(frame_öfendliche_verkersmittel, textvariable=flugreise_v,  width=NORMALE_TEXTFELD_WIDTH)
einheit_flugreise2 = tk.Label(frame_öfendliche_verkersmittel, text='km')

kreutsfahrt_label = tk.Label(frame_öfendliche_verkersmittel, text='Kreutsfahrt')
kreutsfahrt_spinbox = tk.Spinbox(frame_öfendliche_verkersmittel, textvariable=kreutsfahrt_spin_v, width=NORMALE_TEXTFELD_WIDTH, from_=0, to=999999)
einheit_kreutsfahrt = tk.Label(frame_öfendliche_verkersmittel, text='Personen')
kreutsfahrt_texfeld = tk.Entry(frame_öfendliche_verkersmittel, textvariable=kreutsfahrt_v,  width=NORMALE_TEXTFELD_WIDTH)
einheit2_kreutsfahrt = tk.Label(frame_öfendliche_verkersmittel, text='Tage auf See')

kreutsfahrt2_label = tk.Label(frame_öfendliche_verkersmittel, text='Kreutsfahrt')
kreutsfahrt2_spinbox = tk.Spinbox(frame_öfendliche_verkersmittel, textvariable=kreutsfahrt2_spin_v, width=NORMALE_TEXTFELD_WIDTH, from_=0, to=999999)
einheit_kreutsfahrt2 = tk.Label(frame_öfendliche_verkersmittel, text='Personen')
kreutsfahrt2_texfeld = tk.Entry(frame_öfendliche_verkersmittel, textvariable=kreutsfahrt2_v,  width=NORMALE_TEXTFELD_WIDTH)
einheit2_kreutsfahrt2 = tk.Label(frame_öfendliche_verkersmittel, text='Tage an Land')

spin_imputs_öffendliche_verkersmittel = [nahverkehr_spin_v, reisebus_spin_v, bahnfahrt_spin_v, flugreise_spin_v, kreutsfahrt_spin_v, kreutsfahrt2_spin_v]
imputs_öffendliche_verkersmittel= [nahverkehr_texfeld, reisebus_texfeld, bahnfahrt_texfeld, flugreise_texfeld, kreutsfahrt2_texfeld, kreutsfahrt_texfeld]

öffendliche_verkersmittel_cancel = tk.Button(frame_öfendliche_verkersmittel, text='Cancel', command=quit, bg='red')
öffendliche_verkersmittel_next_tab = tk.Button(frame_öfendliche_verkersmittel, text='-->', command=next_tab_öffendliche_verkersmittel, bg='green')
öffendliche_verkersmittel_delete = tk.Button(frame_öfendliche_verkersmittel, text='alle Felder leeren', command=felder_leeren_öffendliche_verkersmittel, bg='blue')


kreutsfahrt2_label.place(x=50,  y=185)
kreutsfahrt2_spinbox.place(x=120, y=185)
einheit_kreutsfahrt2.place(x=189, y=185)
kreutsfahrt2_texfeld.place(x=250, y=185)
einheit2_kreutsfahrt2.place(x=300, y=185)

kreutsfahrt_label.place(x=50,  y=155)
kreutsfahrt_spinbox.place(x=120, y=155)
einheit_kreutsfahrt.place(x=189, y=155)
kreutsfahrt_texfeld.place(x=250, y=155)
einheit2_kreutsfahrt.place(x=300, y=155)

flugreise_label.place(x=50,  y=125)
flugreise_spinbox.place(x=120, y=125)
einheit_flugreise.place(x=189, y=125)
flugreise_texfeld.place(x=250, y=125)
einheit_flugreise2.place(x=300, y=125)

bahnfahrt_label.place(x=50,  y=95)
bahnfahrt_spinbox.place(x=120, y=95)
einheit_bahnfahrt.place(x=189, y=95)
bahnfahrt_texfeld.place(x=250, y=95)
einheit_bahnfahrt2.place(x=300, y=95)

reisebus_label.place(x=50,  y=65)
reisebus_spinbox.place(x=120, y=65)
einheit_reisebus.place(x=189, y=65)
reisebus_texfeld.place(x=250, y=65)
einheit_reisebus2.place(x=300, y=65)

nahverker_label.place(x=50,  y=35)
nahverkehr_spinbox.place(x=120, y=35)
einheit_nahverkehr.place(x=189, y=35)
nahverkehr_texfeld.place(x=250, y=35)
einheit_nahverkehr2.place(x=300, y=35)

öffendliche_verkersmittel_next_tab.place(x=265, y=215)
öffendliche_verkersmittel_delete.place(x=300, y=215)
öffendliche_verkersmittel_cancel.place(x=406, y=215)

notebook.add(frame_essen, text='Essen', state=HIDDEN)

essen_v = tk.StringVar()

def felder_leeren_essen():
    textfeld_essen.delete(0, 'end')

def next_tab_essen():
    notebook.tab(frame_strom, state='normal')

label_essen = tk.Label(frame_essen, text='Ernärung & Konsum (durchschnittlich 4,5t pro jahr & pro person)')
textfeld_essen = tk.Entry(frame_essen, textvariable=essen_v, width=NORMALE_TEXTFELD_WIDTH)
einheit_essen = tk.Label(frame_essen, text='Tonnen Co²')

essen_cancel = tk.Button(frame_essen, text='Cancel', command=quit, bg='red')
essen_next_tab = tk.Button(frame_essen, text='-->', command=next_tab_essen, bg='green')
essen_delete = tk.Button(frame_essen, text='alle Felder leeren', command=felder_leeren_essen, bg='blue')


label_essen.place(x=50, y=35)
textfeld_essen.place(x=400, y=35)
einheit_essen.place(x=455, y=35)

essen_next_tab.place(x=265, y=200)
essen_delete.place(x=300, y=200)
essen_cancel.place(x=406, y=200)


notebook.add(frame_strom, text='Strom', state=HIDDEN)

strom_v = tk.StringVar()

def felder_leeren_strom():
    strom_textfeld.delete(0, 'end')

def next_tab_strom_auswertung():
    notebook.tab(frame_ergebnis, state='normal')

    global co2_wert

    holz_co2 = float(werte_auslesen(holz_v.get())) * 0.39
    heizöl_co2 = float(werte_auslesen(heizöl_v.get())) * 2.92
    erdgas1_co2 = float(werte_auslesen(erdgas1_v.get())) * 2.0
    erdgas2_co2 = float(werte_auslesen(erdgas2_v.get())) * 0.20
    fernwärme_co2 = float(werte_auslesen(fernwärme_v.get())) * 0.16

    elektroantrieb_co2 = float(werte_auslesen(elektroantrieb_v1.get())) * float(werte_auslesen(elektroantrieb_v2.get())) * 0.341
    verbrennerPKW_co2 = float(werte_auslesen(benzin_v1.get())) * 3.14
    verbrennerPKW2_co2 = float(werte_auslesen(benzin_v2.get())) * float(werte_auslesen(benzin_v3.get())) * 3.14
    verbrennerLKW_co2 = float(werte_auslesen(diesel_v1.get())) * 3.31
    verbrennerLKW2_co2 = float(werte_auslesen(diesel_v2.get())) * float(werte_auslesen(diesel_v3.get())) * 3.31

    nahverker_co2 = float(werte_auslesen(nahverkehr_spin_v.get())) * float(werte_auslesen(nahverkehr_v.get())) * 0.08
    reisebus_co2 = float(werte_auslesen(reisebus_spin_v.get())) * float(werte_auslesen(reisebus_v.get())) * 0.03
    bahnfahrt_co2 = float(werte_auslesen(bahnfahrt_v.get())) * float(werte_auslesen(bahnfahrt_v.get())) * 0.05
    flugreise_co2 = float(werte_auslesen(flugreise_spin_v.get())) * float(werte_auslesen(flugreise_v.get())) * 0.27
    kreutsfahrtco2 = float(werte_auslesen(kreutsfahrt_spin_v.get())) * float(werte_auslesen(kreutsfahrt_v.get())) * 280
    kreutsfahrt2_co2 = float(werte_auslesen(kreutsfahrt2_spin_v.get())) * float(werte_auslesen(kreutsfahrt2_v.get())) * 190

    strom_co2 = float(werte_auslesen(strom_v.get())) * 0.420

    essen_co2 = float(werte_auslesen(essen_v.get())) * 1000000

    co2_wert = (holz_co2 + heizöl_co2 + erdgas1_co2 + erdgas2_co2 + fernwärme_co2 + elektroantrieb_co2 + verbrennerPKW_co2 + verbrennerPKW2_co2 + verbrennerLKW_co2 + verbrennerLKW2_co2 + nahverker_co2 + reisebus_co2 + bahnfahrt_co2 + flugreise_co2 + kreutsfahrtco2 + kreutsfahrt2_co2 + strom_co2 + essen_co2)
    ergebnis_label.config(text='Du hast einen geschätzen Co² wert von: ' + str(co2_wert) + ' pro Jahr')


strom_label = tk.Label(frame_strom, text='Strom')
strom_textfeld = tk.Entry(frame_strom, textvariable=strom_v, width=NORMALE_TEXTFELD_WIDTH)
einheit_strom = tk.Label(frame_strom, text='kWh')

#WICHTIG dieses label ist nur hier weil es sonst nicht das ergebnis anzeigen kann und es wird im ergebnis tab angezeigt
ergebnis_label = tk.Label(frame_ergebnis, text='Du hast einen geschätzen Co² wert von:  pro Jahr', font=('Arial', 14))
ergebnis_label.place(x=130, y=70)


strom_cancel = tk.Button(frame_strom, text='Cancel', command=quit, bg='red')
strom_next_tab = tk.Button(frame_strom, text='berechnen', command=next_tab_strom_auswertung, bg='green')
strom_delete = tk.Button(frame_strom, text='alle Felder leeren', command=felder_leeren_strom, bg='blue')


strom_label.place(x=50, y=35)
strom_textfeld.place(x=90, y=35)
einheit_strom.place(x=150, y=35)

strom_next_tab.place(x=225, y=200)
strom_delete.place(x=300, y=200)
strom_cancel.place(x=406, y=200)


notebook.add(frame_ergebnis, text='Ergebnis', state=HIDDEN)

def reset():
    felder_leeren_heizung()
    felder_leeren_mobilität()
    felder_leeren_öffendliche_verkersmittel()
    felder_leeren_essen()
    felder_leeren_strom()
    notebook.tab(frame_start, state='normal')
    notebook.tab(frame_heizung, state='hidden')
    notebook.tab(frame_mobilität, state='hidden')
    notebook.tab(frame_öfendliche_verkersmittel, state='hidden')
    notebook.tab(frame_strom, state='hidden')
    notebook.tab(frame_essen, state='hidden')
    notebook.tab(frame_ergebnis, state='hidden')

def open_klimarechener_webside():
    web.open('https://www.wwf.de/themen-projekte/klima-energie/wwf-klimarechner', new=2)


begrüßung_ergebnis_label = tk.Label(frame_ergebnis, text='Herzlichen Glückwunsch', font=('Helvetica', 17))
achtung_label = tk.Label(frame_ergebnis, text='Achtung', font=('Verdan', 13), fg='red')
achtung_label2 = tk.Label(frame_ergebnis, text='Dieses ergebnis ist nur geschätzt \n wenn du deinen Co²-Wert genauer wissen willst:', font=('Arial', 10))
open_button_ergebnis = tk.Button(frame_ergebnis, text='dann klick hier', command=open_klimarechener_webside)
reset_button_ergebnis = tk.Button(frame_ergebnis, text='Reset', command=reset, bg='green')
cancel_button = tk.Button(frame_ergebnis, text='Cancel', command=quit, bg='red')

begrüßung_ergebnis_label.place(x=240, y=30)
#hier ist an position x=130 y=70 ist das ergebnis_label das ist jetzt bei den defenitionen von dem tab strom weil es sont den wert des ergebnises nicht annehmen kann
achtung_label.place(x=500, y=120)
achtung_label2.place(x=400, y=150)
open_button_ergebnis.place(x=500, y=195)
reset_button_ergebnis.place(x=100, y=200)
cancel_button.place(x=206, y=200)


root.mainloop()