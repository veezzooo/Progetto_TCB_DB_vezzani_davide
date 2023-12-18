import socket
import mysql.connector
import pickle

PASSWORD = "tepsit"

def lettura_dipendenti(parametri):
    
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5Btepsit",
        port=3306
    )

    cursor = conn.cursor()
    
    query = f"SELECT * FROM dipendenti_davide_vezzani WHERE 1=1 {build_conditions(parametri)}"
    cursor.execute(query)
    dati = cursor.fetchall()
    conn.commit()
    return dati

def lettura_zone(parametri):

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5Btepsit",
        port=3306
    )

    cursor = conn.cursor()
    
    query = f"SELECT * FROM zone_di_lavoro_davide_vezzani WHERE 1=1 {build_conditions(parametri)}"
    cursor.execute(query)
    dati = cursor.fetchall()
    conn.commit()
    return dati

def elimina_istanza(parametri,sc):
    
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5Btepsit",
        port=3306
    )

    cursor = conn.cursor()

    if sc == "1":
        query = f"DELETE FROM dipendenti_davide_vezzani WHERE 1=1 {build_conditions(parametri)}"
    
    else:
        query = f"DELETE FROM zone_di_lavoro_davide_vezzani WHERE 1=1 {build_conditions(parametri)}"

    cursor.execute(query)
    conn.commit()

def inserisci_istanza(parametri,sc):
    
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5Btepsit",
        port=3306
    )

    cursor = conn.cursor()

    if sc == "1":

        query = f"INSERT INTO dipendenti_davide_vezzani (nome, cognome, residenza, indirizzo, data_nascita, telefono, agente) VALUES (%s, %s, %s, %s, %s, %s, %s)" #%s è un segnaposto che viene utilizzato nelle query SQL per rappresentare un valore di tipo stringa
    
    else:

        query = f"INSERT INTO zone_di_lavoro_davide_vezzani (nome_zona, numero_clienti, citta, codd) VALUES (%s, %s, %s, %s)" 

    cursor.execute(query, parametri)
    conn.commit()

def modifica_dato(parametri, mod,sc):
    
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5Btepsit",
        port=3306
    )

    cursor = conn.cursor()

    if sc == "1":
            
        if mod == "1":
            query = f"UPDATE dipendenti_davide_vezzani SET nome = '{parametri[0]}' WHERE id = {parametri[1]}"
        elif mod == "2":
            query = f"UPDATE dipendenti_davide_vezzani SET cognome = '{parametri[0]}' WHERE id = {parametri[1]}"
        elif mod == "3":
            query = f"UPDATE dipendenti_davide_vezzani SET residenza = '{parametri[0]}' WHERE id = {parametri[1]}"
        elif mod == "4":
            query = f"UPDATE dipendenti_davide_vezzani SET indirizzo = '{parametri[0]}' WHERE id = {parametri[1]}"
        elif mod == "5":
            query = f"UPDATE dipendenti_davide_vezzani SET data_nascita = '{parametri[0]}' WHERE id = {parametri[1]}"
        elif mod == "6":
            query = f"UPDATE dipendenti_davide_vezzani SET telefono = '{parametri[0]}' WHERE id = {parametri[1]}"
        elif mod == "7":
            query = f"UPDATE dipendenti_davide_vezzani SET agente = '{parametri[0]}' WHERE id = {parametri[1]}"
    
    else:

        if mod == "1":
            query = f"UPDATE zone_di_lavoro_davide_vezzani SET nome_zona = '{parametri[0]}' WHERE id_zona = {parametri[1]}"
        elif mod == "2":
            query = f"UPDATE dipendenti_davide_vezzani SET numero_clienti = '{parametri[0]}' WHERE id_zona = {parametri[1]}"
        elif mod == "3":
            query = f"UPDATE dipendenti_davide_vezzani SET citta = '{parametri[0]}' WHERE id_zona = {parametri[1]}"
        elif mod == "4":
            query = f"UPDATE dipendenti_davide_vezzani SET codd = '{parametri[0]}' WHERE id_zona = {parametri[1]}"

    cursor.execute(query)
    conn.commit()


def build_conditions(parametri):
    clausole = ""
    for key, value in parametri.items():
        clausole += f"AND {key} = '{value}' "
    return clausole

def start_server(host, port, password): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()

    print("In attesa di connessioni...")

    conn, addr = s.accept()
    print('Connected by', addr)

    i = 0
    while i < 3:    
        client_password = conn.recv(1024).decode()
        if client_password == password:
            conn.send("Password corretta. Inizia la comunicazione".encode())
            break
        else:
            i += 1
            tentativi_rimasti = 3 - i
            if i < 3:
                conn.send(f"Errore: Password sbagliata. Tentativi rimasti: {tentativi_rimasti}".encode())
            else:
                conn.send("Tentativi massimi raggiunti. Chiudo la connessione".encode())
                conn.close()
                exit()

    #db_conn = mysql.connector.connect(
    #    host="127.0.0.1",
    #    user="root",
    #    password="",
    #    database="5Btepsit",
    #    port=3306
    #)
    #cursor = db_conn.cursor(dictionary=True)  (dictionary=True) permette di ottenere i risultati delle query come dizionari e non come tuple

    conn.recv(1024).decode()
    while True:

        conn.send("Scegli un'operazione: \n1. Leggi dati di un dipendenti; \n2. Leggi dati di una zona di lavoro; \n3. Elimina un'istanza da una tabella; \n4. Inserisci un'istanza da una tabella; \n5. Modifica un dato da una tabella; \n6. Esci.".encode())
    
        data = conn.recv(1024).decode()
        if not data:
            conn.close()
            break
        if data == "6":  
            print("Uscita richiesta. Chiudo la connessione")
            conn.close() 
            s.close()      
            break       
    
        if data == "1":

            nome = conn.recv(1024).decode()
            par = {"nome": nome}
            result = lettura_dipendenti(par)
            conn.send(str(result).encode())

        elif data == "2":
            
            nome = conn.recv(1024).decode() 
            par = {"nome_zona": nome}
            result = lettura_zone(par)
            conn.send(str(result).encode())

        elif data == "3":
            
            conn.send("Scegli se eliminare dalla tabella dipendenti (premi 1) o zone (premi 2): ".encode())
            sc = conn.recv(1024).decode()

            if sc == "1":
                id_elimina = conn.recv(1024).decode()
                par = {"id": id_elimina}
                elimina_istanza(par,sc)

            else:
                id_elimina = conn.recv(1024).decode()
                par = {"id_zona": id_elimina}
                elimina_istanza(par,sc)

        elif data == "4":
            
            #parametri = {
            #    "nome": conn.recv(1024).decode(),
            #   "cognome": conn.recv(1024).decode(),
            #   "residenza": conn.recv(1024).decode(),
            #   "indirizzo": conn.recv(1024).decode(),
            #    "data_nascita": conn.recv(1024).decode(),
            #    "telefono": conn.recv(1024).decode(),
            #    "agente": conn.recv(1024).decode(),
            #}
            conn.send("Scegli se inserire un'istanza dalla tabella dipendenti (premi 1) o zone (premi 2): ".encode())
            sc = conn.recv(1024).decode()

            parametri = conn.recv(1024)
            parametri_lista = pickle.loads(parametri)
            inserisci_istanza(parametri_lista,sc)

        elif data == "5":
            
            #parametri = {
            #    "id": conn.recv(1024).decode(),
            #    "nome": conn.recv(1024).decode(),
            #    "cognome": conn.recv(1024).decode(),
            #    "residenza": conn.recv(1024).decode(),
            #    "indirizzo": conn.recv(1024).decode(),
            #    "data_nascita": conn.recv(1024).decode(),
            #    "telefono": conn.recv(1024).decode(),
            #    "agente": conn.recv(1024).decode(),
            #}

            conn.send("Scegli se inserire un'istanza dalla tabella dipendenti (premi 1) o zone (premi 2): ".encode())
            sc = conn.recv(1024).decode()

            if sc == "1":
            
                conn.send("Decidi che dato vuoi modificare, inserisci 1 per il nome, 2 per il cognome, 3 per la residenza, 4 per l'indirizzo, 5 per la data di nascita, 6 per il telefono, 7 per l'agente: ".encode())
            
            else:

                conn.send("Decidi che dato vuoi modificare, inserisci 1 per il nome, 2 per il numero dei clienti, 3 per la citta, 4 per il codice: ".encode())
            
            mod = conn.recv(1024).decode()   
            parametri = conn.recv(1024)
            parametri_lista = pickle.loads(parametri)
            modifica_dato(parametri_lista,mod,sc)

    #conn.close()
    #s.close()

HOST = "localhost"
PORT = 50007
PASSWORD = "tepsit"

start_server(HOST, PORT, PASSWORD)