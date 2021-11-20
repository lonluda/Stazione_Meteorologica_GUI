import configparser, tkinter, serial, csv, sys, os
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path

# Crea un oggetto "finestra"
window = Tk()
window.title("Stazione meteorologica")
window.resizable(False, False)
window.geometry("320x270")

# Setup Variabili Globali
csv_cnt = 0
global_temp = StringVar()
global_hum = StringVar()
global_press = StringVar()
ini_config = {}

# Recupera le informazioni dal file di configurazione
def retrieve_ini():
    try:
        Config = configparser.ConfigParser()
        Config.read("config.ini")

        # [MAIN config.ini section]
        ini_config.update({"com_port" : Config.get('MAIN', 'porta')})
        ini_config.update({"csv_cycle_print" : Config.getint('MAIN', 'csv_cycle')})
        ini_config.update({"csv_enable" : Config.getint('MAIN', 'csv_enable')})
        # [TECHNICAL config.ini section]
        ini_config.update({"offset_enable" : Config.getint('TECHNICAL', 'offset_enable')})
        ini_config.update({"temp_offset" : Config.getfloat('TECHNICAL', 'temp_offset')})
        ini_config.update({"hum_offset" : Config.getfloat('TECHNICAL', 'hum_offset')})
        ini_config.update({"press_offset" : Config.getint('TECHNICAL', 'press_offset')})
    except:
        messagebox.showerror("File non trovato", 'Nessun file di configurazione "config.ini" trovato.')
        window.destroy()
        sys.exit()

# Inizializza la comunicazione attraverso la porta COM
def connect():
    while True:
        try:
            # Prova a stabilire la comunicazione tramite porta COM scelta
            arduino = serial.Serial(ini_config["com_port"], 9600)
            break
        except:
            # In caso di mancanza di comunicazione tramite porta COM scelta
            if messagebox.askretrycancel("Errore di comunicazione COM", 'Nessun dispositivo trovato sulla porta ' + ini_config["com_port"]) == True:
                continue
            else:
                exit()
    return arduino

# Ricezione messaggi tramite porta COM
def obt_messages():

    # Recupera il primo valore
    temp_temperatura = arduino.readline().decode('utf-8')
    # Recupera il secondo valore
    temp_umidita = arduino.readline().decode('utf-8')
    # Recupera il terzo valore
    temp_pressione = arduino.readline().decode('utf-8')

    # Esegue la correzione del valore trasmesso ( misura - offset )
    global_temp.set(float(temp_temperatura[:4]) - ini_config["temp_offset"])
    # Esegue la correzione del valore trasmesso ( misura - offset )
    global_hum.set(float(temp_umidita[:4]) - ini_config["hum_offset"])
    # Esegue la correzione del valore trasmesso ( misura - offset )
    global_press.set(int(temp_pressione[:4]) - ini_config["press_offset"])

    # Invia alla funzione csv_write i tre parametri da stampare a video
    csv_write(global_temp.get(), global_hum.get(), global_press.get())
    # Attendi 2 secondi ed esegue di nuovo la funzione per aggiornare i valori
    window.after(2000, obt_messages)

# Esegue la scrittura dei parametri sul file .csv
def csv_write(temperatura, umidita, pressione):
    global csv_cnt
    
    # Ottiene data e ora correnti
    local = datetime.now()
    # Separa la data dall'Ora
    data = local.strftime("%d/%m/%Y")
    # Separa l'ora dalla Data
    ora = local.strftime("%H:%M:%S")

    # Colonne che verranno create nel file csv
    header = ["Data", "Ora", "Temperatura - °C", "Umidità - %", "Pressione - mBar"]
    # Riga che sarà creata ad ogni print sul file csv
    data = [data, ora, temperatura, umidita, pressione]

    # Se la variabile csv_enable è settata su 1 esegui:
    if ini_config["csv_enable"]:
        # Se il contatore impostato per il print del csv è uguale alla soglia desiderata
        if csv_cnt == ini_config["csv_cycle_print"]:
            try:
                if os.path.exists('report.csv') == True:
                    with open('report.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        # Scrivi i dati
                        writer.writerow(data)
                        # Porta il contatore a 0 per un nuovo ciclo
                        csv_cnt = 0
                else:
                    with open('report.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        # Scrivi il nome alle colonne
                        writer.writerow(header)
                        # Scrivi i dati
                        writer.writerow(data)
                        # Porta il contatore a 0 per un nuovo ciclo
                        csv_cnt = 0
            except:
                messagebox.showinfo("File report.csv in uso.", 'File report.csv in uso oppure non accessibile.\nChiudere il file e riprovare.')
                csv_cnt = 0
        csv_cnt += 1

# Esegue il salvataggio delle modifiche al file config.ini
def savesettings(csv_state, offset_state):

    Config = configparser.ConfigParser()
    
    myfile = Path('config.ini')
    Config.read(myfile)

    Config.set('MAIN', 'csv_enable', str(csv_state))
    Config.set('TECHNICAL', 'offset_enable', str(offset_state))
    Config.write(myfile.open("w"))

# Genera il form delle impostazioni
def set_form():

    # Crea un oggetto "finestra"
    set_form = Toplevel()
    set_form.title("Impostazioni")
    set_form.resizable(False, False)
    set_form.geometry("250x105")

    csv_state = tkinter.IntVar()
    offset_state = tkinter.IntVar()

    # Aggiorna i valori scritti nel file config.ini
    retrieve_ini()

    # Creazione Widget
    button_1 = Checkbutton(set_form, text="ATTIVA OUTPUT FILE CSV", onvalue=1, variable=csv_state)
    button_2 = Checkbutton(set_form, text="APPLICA CORREZIONE VALORI", onvalue=1, variable=offset_state)
    save_button = ttk.Button(set_form, text="Salva", command=lambda: savesettings(csv_state.get(), offset_state.get()))
    build = ttk.Label(set_form, text="Build 0.2")

    # Posizionamento Widget
    button_1.grid(column=1, row=1, sticky="W", padx=25, pady=(10, 0))
    # Se csv_enable è impostato su 1, contrassegna la checkbox come spuntata
    if ini_config["csv_enable"]:
        button_1.select()
    button_2.grid(column=1, row=2, sticky="W", padx=25, pady=(5, 0))
    # Se offset_enable è impostato su 1, contrassegna la checkbox come spuntata
    if ini_config["offset_enable"]:
        button_2.select()
    save_button.grid(column=1, row=3, sticky="W", padx=25, pady=(5, 0))
    build.grid(column=1, row=3, sticky="E", padx=10, pady=(15, 0))
    
    # SET_FORM Main Loop
    set_form.mainloop()

# Genera il form principale
def main_form():

    # Creazione Widget
    welcome = Label(window, text="Stazione meteorologica\n Laboratorio analisi", font=('TkDefaultFont', 18))

    temperature = Label(window, text="Temperatura:", font=('TkDefaultFont', 12))
    umidita = Label(window, text="Umidità:", font=('TkDefaultFont', 12))
    pressione = Label(window, text="Pressione:", font=('TkDefaultFont', 12))

    val_temp = ttk.Label(window, textvariable=global_temp, font=('TkDefaultFont', 12))
    val_umid = ttk.Label(window, textvariable=global_hum, font=('TkDefaultFont', 12))
    val_press = ttk.Label(window, textvariable=global_press, font=('TkDefaultFont', 12))

    photo = PhotoImage(file=r"img\\settings.png")
    sett_btn = ttk.Button(window, text="Impostazioni", image=photo, command=set_form)

    # Posizionamento Widget sulla grid
    welcome.grid(column=1, columnspan=6, row=1, ipadx=25, ipady=10, pady=10, padx=5)

    temperature.grid(column=2, columnspan=2, row=3, pady=10, padx=(20, 0), sticky="W")
    umidita.grid(column=2, columnspan=2, row=4, pady=10, padx=(20, 0), sticky="W")
    pressione.grid(column=2, columnspan=2, row=5, pady=10, padx=(20, 0), sticky="W")

    val_temp.grid(column=5, columnspan=2, row=3, sticky="W")
    val_umid.grid(column=5, columnspan=2, row=4, sticky="W")
    val_press.grid(column=5, columnspan=2, row=5, sticky="W")

    sett_btn.grid(column=5, columnspan=2, row=6, sticky="NE")

    window.after(2000, obt_messages())
    window.mainloop()

if __name__ == "__main__":
    retrieve_ini()
    arduino = connect()
    main_form()
