import socket
import pickle

def authenticate_server(s, max_attempts=3):
    for _ in range(max_attempts):
        password = input("Inserisci la password: ")
        s.send(password.encode())
        response = s.recv(1024).decode()
        if response == "Password corretta. Inizia la comunicazione":
            return True
        else:
            print(response)
    return False

def main():
    HOST = 'localhost'
    PORT = 50007

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    if authenticate_server(s):
        print("Autenticazione riuscita. Puoi iniziare a effettuare le operazioni.")
        s.send("ok".encode())
        while True:
            
            me = s.recv(1024).decode()
            print(me)

            scelta = "0"
            while( scelta < "1" or scelta > "6"):
                scelta = input("Operazione: ")
            s.send(scelta.encode())

            if scelta == "6":
                s.send("6".encode())
                print("Uscito")
                s.close()   
                break

            if scelta == "1" or scelta == "2":
                nome = input("Inserisci il nome: ")
                s.send(nome.encode())
                response = s.recv(1024).decode()
                if response == "[]":

                    print("non è stato trovato il nome rischiesto nel database")
                
                else:

                    print(response)

            if scelta == "3":

                mex = s.recv(1024).decode()
                print(mex)
                
                scelta1 = input("1 o 2? ")
                s.send(scelta1.encode())

                if scelta1 == "1" :
                    id_elimina = input("Inserisci l'id del dipendente per eliminare la sua istanza dalla tabella del database: ")
                    

                else:
                    id_elimina = input("Inserisci l'id della zona per eliminare la sua istanza dalla tabella del database: ")
                    
                s.send(id_elimina.encode())

            if scelta == "4":

                mex = s.recv(1024).decode()
                print(mex)
                
                scelta1 = input("1 o 2? ")
                s.send(scelta1.encode())

                if scelta1 == "1":
                    parametri = {
                        "nome": input("Inserisci il nome del dipendente da inserire: "),
                        "cognome": input("Inserisci il cognome del dipendente da inserire: "),
                        "residenza": input("Inserisci dove abita il dipendente da inserire: "),
                        "indirizzo": input("Inserisci l'indirizzo' del dipendente da inserire: "),
                        "data_nascita": input("Inserisci la data di nascita del dipendente da inserire: "),
                        "telefono": input("Inserisci numero di telefono del dipendente da inserire: "),
                        "agente": input("inserisci l'agente del dipendente da inserire: "),
                    }
                    #for value in parametri.values():
                        #s.send(value.encode())
                else:
                    
                    parametri = {
                        "nome_zona": input("Inserisci il nome della zona da inserire: "),
                        "numero_clienti": input("Inserisci il numero dei clienti da inserire: "),
                        "citta": input("Inserisci in che citta si trova la zona da inserire: "),
                        "codd": input("Inserisci a quale id dei dipendenti si riferisce la zona da inserire: "),
                    }
                byte_parametri = pickle.dumps(list(parametri.values()))
                s.send(byte_parametri)

            if scelta == "5":

                mex = s.recv(1024).decode()
                print(mex)
                
                scelta1 = input("1 o 2? ")
                s.send(scelta1.encode())

                if scelta1 == "1":
                    st = s.recv(1024).decode()
                    print(st)
                   
                    mod = (input("Scegli: "))

                    s.send(mod.encode())

                    if mod == "1":

                        parametri = {

                            "nome" : input("Inserisci il nuovo nome: "),
                            "id" : input("Inserisci l'id del quale vuoi modificare il nome: "),
                        }
                    
                    elif mod == "2":
                        
                        parametri = {

                            "cognome" : input("Inserisci il nuovo cognome: "),
                            "id" : input("Inserisci l'id del quale vuoi modificare il cognome: "),

                        }
                    
                    elif mod == "3":

                        parametri = {

                            "residenza" : input("Inserisci la nuova residenza: "),
                            "id" : input("Inserisci l'id del quale vuoi modificare la residenza: "),

                        }    

                    elif mod == "4":

                        parametri = {

                            "indirizzo" : input("Inserisci il nuovo indirizzo: "),
                            "id" : input("Inserisci l'id del quale vuoi modificare l'indirizzo: "),

                        }      

                    elif mod == "5":

                        parametri = {

                            "data_nascita" : input("Inserisci la nuova data di nascita: "),
                            "id" : input("Inserisci l'id del quale vuoi modificare la data di nascita: "),

                        }  

                    elif mod == "6":

                        parametri = {

                            "telefono" : input("Inserisci il nuovo numero di telefono: "),
                            "id" : input("Inserisci l'id del quale vuoi modificare il numero di telefono: "),

                        } 

                    elif mod == "7":

                        parametri = {

                            "agente" : input("Inserisci il nuovo agente: "),
                            "id" : input("Inserisci l'id del quale vuoi modificare l'agente: "),

                        }

                    #parametri = {
                    #    "id": input("Inserisci l'id del dipendente di cui vuoi modificare i dati: "),
                    #    "nome": input("Inserisci il nome del dipendente da inserire: "),
                    #    "cognome": input("Inserisci il cognome del dipendente da inserire: "),
                    #    "residenza": input("Inserisci dove abita il dipendente da inserire: "),
                    #    "indirizzo": input("Inserisci l'indirizzo' del dipendente da inserire: "),
                    #    "data_nascita": input("Inserisci la data di nascita del dipendente da inserire: "),
                    #    "telefono": input("Inserisci numero di telefono del dipendente da inserire: "),
                    #    "agente": input("inserisci l'agente del dipendente da inserire: "),
                    #}
                    #for value in parametri.values():
                        #s.send(value.encode())
                else:

                    st = s.recv(1024).decode()
                    print(st)
                
                    mod = (input("Scegli: "))

                    s.send(mod.encode())

                    if mod == "1":

                        parametri = {

                            "nome_zona" : input("Inserisci il nuovo nome: "),
                            "id_zona" : input("Inserisci l'id del quale vuoi modificare il nome: "),
                        }
                    
                    elif mod == "2":
                        
                        parametri = {

                            "numero_clienti" : input("Inserisci il nuovo numero dei clienti: "),
                            "id_zona" : input("Inserisci l'id del quale vuoi modificare il numero dei clienti: "),

                        }
                    
                    elif mod == "3":

                        parametri = {

                            "citta" : input("Inserisci la nuova citta: "),
                            "id_zona" : input("Inserisci l'id del quale vuoi modificare la citta: "),

                        }    

                    elif mod == "4":

                        parametri = {

                            "codd" : input("Inserisci il nuovo codice: "),
                            "id_zona" : input("Inserisci l'id del quale vuoi modificare il codice: "),

                        }      

                byte_parametri = pickle.dumps(list(parametri.values()))
                s.send(byte_parametri)


    else:
        print("Tentativi massimi raggiunti. Chiudo la connessione.")

    s.close()

if __name__ == "__main__":
    main()