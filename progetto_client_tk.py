import tkinter as tk
from tkinter import ttk, messagebox
import socket
import pickle

# Dichiarazioni di variabili globali per i widget
password_entry = tk.Entry()
operation_choice = tk.StringVar()
delete_choice = tk.StringVar()
insert_choice = tk.StringVar()
update_choice = tk.StringVar()
input_update_mod = tk.StringVar()
input_update_id = tk.StringVar()
input_update_value = tk.StringVar()
input_name = tk.StringVar()
input_delete_id = tk.StringVar()
input_insert_nome = tk.StringVar()
input_insert_cognome = tk.StringVar()
input_insert_residenza = tk.StringVar()
input_insert_indirizzo = tk.StringVar()
input_insert_data_nascita = tk.StringVar()
input_insert_telefono = tk.StringVar()
input_insert_agente = tk.StringVar()
input_insert_citta = tk.StringVar()
input_insert_codd = tk.StringVar()

# Funzione per abilitare le schede dopo l'autenticazione
def enable_tabs():
    notebook.add(menu_frame, text="Menù Operazioni")
    notebook.add(execute_frame, text="Esecuzione Operazione")
    notebook.select(1)  # Passa alla scheda delle operazioni

# Funzione per autenticare il server
def authenticate_server():
    password = password_entry.get()
    s.send(password.encode())
    response = s.recv(1024).decode()
    if response == "Password corretta. Inizia la comunicazione":
        messagebox.showinfo("Autenticazione", "Autenticazione riuscita. Puoi iniziare a effettuare le operazioni.")
        notebook.select(1)  # Passa alla scheda delle operazioni
        notebook.add(menu_frame, text="Menù Operazioni")  # Aggiunge la scheda Menù Operazioni
        notebook.hide(0)  # Nasconde la scheda Autenticazione
    else:
        messagebox.showerror("Errore di autenticazione", response)

# Funzione per eseguire l'operazione scelta
def execute_operation():

    selected_operation = operation_choice.get()
 
    if selected_operation == "1" or selected_operation == "2":
        if selected_operation == "1" or selected_operation == "2":
            # Pulisce la frame di esecuzione e aggiunge un widget Entry per inserire il nome
        
            label = tk.Label(execute_frame, text="Inserisci il nome:")
            label.pack(pady=5)
            name_entry = tk.Entry(execute_frame)
            name_entry.pack(pady=5)

            def read_data():
                # Funzione interna per inviare il nome al server e visualizzare la risposta
                nome = name_entry.get()
                s.send(nome.encode())
                response = s.recv(1024).decode()
                if response == "[]":
                    result_label.config(text="Non è stato trovato il nome richiesto nel database")
                else:
                    result_label.config(text=response)

            # Aggiunge un pulsante per eseguire l'operazione
            execute_button = tk.Button(execute_frame, text="Esegui", command=read_data)
            execute_button.pack(pady=10)

    elif selected_operation == "3":
        scelta_elimina = delete_choice.get()
        s.send(scelta_elimina.encode())
        if scelta_elimina == "1":
            # Eliminazione da tabella dipendenti
            id_elimina = input_delete_id.get()
            s.send(id_elimina.encode())
        elif scelta_elimina == "2":
            # Eliminazione da tabella zone
            id_elimina = input_delete_id.get()
            s.send(id_elimina.encode())

    elif selected_operation == "4":
        scelta_inserisci = insert_choice.get()
        s.send(scelta_inserisci.encode())

        if scelta_inserisci == "1":
            parametri = {
                "nome": input_insert_nome.get(),
                "cognome": input_insert_cognome.get(),
                "residenza": input_insert_residenza.get(),
                "indirizzo": input_insert_indirizzo.get(),
                "data_nascita": input_insert_data_nascita.get(),
                "telefono": input_insert_telefono.get(),
                "agente":input_insert_agente.get()
            }
        elif scelta_inserisci == "2":
            
            parametri = {
                "nome_zona": input_insert_nome.get(),
                "numero_clienti": input_insert_cognome.get(),
                "citta": input_insert_citta.get(),
                "codd": input_insert_codd.get()
            }

        byte_parametri = pickle.dumps(list(parametri.values()))
        s.send(byte_parametri)

    elif selected_operation == "5":
    # Operazione di modifica
        scelta_modifica = update_choice.get()
        s.send(scelta_modifica.encode())

        st = s.recv(1024).decode()
        result_label.config(text=st)

        mod = input_update_mod.get()
        s.send(mod.encode())

        if scelta_modifica == "1":
            # Modifica in tabella dipendenti
            if mod == "1":
                parametri = {
                    "nome": input_update_value.get(),
                    "id": input_update_id.get(),
                }
            elif mod == "2":
                parametri = {
                    "cognome": input_update_value.get(),
                    "id": input_update_id.get(),
                }
            elif mod == "3":
                parametri = {
                    "residenza": input_update_value.get(),
                    "id": input_update_id.get(),
                }
            elif mod == "4":
                parametri = {
                    "indirizzo": input_update_value.get(),
                    "id": input_update_id.get(),
                }
            elif mod == "5":
                parametri = {
                    "data_nascita": input_update_value.get(),
                    "id": input_update_id.get(),
                }
            elif mod == "6":
                parametri = {
                    "telefono": input_update_value.get(),
                    "id": input_update_id.get(),
                }
            elif mod == "7":
                parametri = {
                    "agente": input_update_value.get(),
                    "id": input_update_id.get(),
                }

        elif scelta_modifica == "2":
            # Modifica in tabella zone
            if mod == "1":
                parametri = {
                    "nome_zona": input_update_value.get(),
                    "id_zona": input_update_id.get(),
                }
            elif mod == "2":
                parametri = {
                    "numero_clienti": input_update_value.get(),
                    "id_zona": input_update_id.get(),
                }
            elif mod == "3":
                parametri = {
                    "citta": input_update_value.get(),
                    "id_zona": input_update_id.get(),
                }
            elif mod == "4":
                parametri = {
                    "codd": input_update_value.get(),
                    "id_zona": input_update_id.get(),
                }

        byte_parametri = pickle.dumps(list(parametri.values()))
        s.send(byte_parametri)

# Funzione per inviare la scelta dell'operazione al server
def send_operation_choice():
    selected_operation = operation_choice.get()
    if selected_operation == "1" or selected_operation == "2":
        # Se l'operazione è 1 o 2, seleziona direttamente la scheda di esecuzione
        notebook.select(2)
    else:
        # Altrimenti, procedi con l'invio dell'operazione al server
        s.send(selected_operation.encode())
        notebook.select(2)

# Creazione della finestra principale
root = tk.Tk()
root.title("Client App")

# Variabili per la comunicazione
HOST = "localhost"
PORT = 50007
PASSWORD = "tepsit"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

# Schede
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Scheda di autenticazione
auth_frame = tk.Frame(notebook)
notebook.add(auth_frame, text="Autenticazione")

password_entry_label = tk.Label(auth_frame, text="Password:")
password_entry_label.pack(pady=10)

password_entry = tk.Entry(auth_frame, show="*")
password_entry.pack(pady=10)

auth_button = tk.Button(auth_frame, text="Autentica", command=authenticate_server)
auth_button.pack(pady=10)

# Scheda di scelta operazione
menu_frame = tk.Frame(notebook)
notebook.add(menu_frame, text="Menù Operazioni")

operation_choice_label = tk.Label(menu_frame, text="Scegli un'operazione:")
operation_choice_label.pack(pady=10)

operation_choice = tk.StringVar()
operation_choice.set("1")  # Imposto il valore predefinito a 1

operation_radio1 = tk.Radiobutton(menu_frame, text="Leggi dati di un dipendente", variable=operation_choice, value="1")
operation_radio1.pack(pady=5)

operation_radio2 = tk.Radiobutton(menu_frame, text="Leggi dati di una zona di lavoro", variable=operation_choice, value="2")
operation_radio2.pack(pady=5)

operation_radio3 = tk.Radiobutton(menu_frame, text="Elimina un'istanza da una tabella", variable=operation_choice, value="3")
operation_radio3.pack(pady=5)

operation_radio4 = tk.Radiobutton(menu_frame, text="Inserisci un'istanza da una tabella", variable=operation_choice, value="4")
operation_radio4.pack(pady=5)

operation_radio5 = tk.Radiobutton(menu_frame, text="Modifica un dato da una tabella", variable=operation_choice, value="5")
operation_radio5.pack(pady=5)

execute_button = tk.Button(menu_frame, text="Esegui Operazione", command=send_operation_choice)
execute_button.pack(pady=10)

# Scheda di esecuzione operazione
execute_frame = tk.Frame(notebook)
notebook.add(execute_frame, text="Esecuzione Operazione")

# Altre variabili per input

# Aggiungi altre variabili se necessario

# Aggiungi altri widget e input necessari per l'esecuzione dell'operazione
result_label = tk.Label(execute_frame, text="")
result_label.pack(pady=10)

notebook.hide(1)
notebook.hide(2)

# Connessione al server
try:
    s.connect((HOST, PORT))
except Exception as e:
    messagebox.showerror("Errore di connessione", f"Impossibile connettersi al server: {e}")
    root.destroy()
    
# Avvio dell'applicazione
root.mainloop()
