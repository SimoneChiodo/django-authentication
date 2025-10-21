# Progetto Django: Django Authentication

## 📖 Descrizione
**Django Authentication** è il proseguimento del progetto 
<a href="https://github.com/SimoneChiodo/django-database-model.git">***Django Database Model***</a>.  
In questo esercizio si approfondiscono i **form**, l’**inserimento dei dati da parte dell’utente** e la **gestione dell’autenticazione** tramite il modulo integrato `django.contrib.auth`.

L’obiettivo è comprendere come Django gestisce l’interazione tra **frontend e backend**, dai form ai messaggi di conferma fino al sistema di login/logout.


## 🌍 Funzionalità principali
- **Creazione di un form per i post**  
  Implementazione di un `ModelForm` per consentire agli utenti di aggiungere nuovi post tramite un’interfaccia web.  

- **Salvataggio nel database**  
  I dati inviati dal form vengono validati e salvati automaticamente nel database collegato al modello `Post`.  

- **Messaggi di conferma**  
  Utilizzo del sistema `messages` di Django per mostrare notifiche di successo o errore dopo l’invio del form.  

- **Autenticazione utente**  
  Implementazione delle pagine di **login** e **logout** sfruttando le view e i template forniti da `django.contrib.auth`.  


## 🎯 Obiettivo
Capire in modo pratico:
- come Django gestisce gli **input utenti** tramite form,  
- come collegare i form ai modelli con **ModelForm**,  
- come funziona il **sistema di autenticazione integrato** per login e logout.  


## 🛠️ Tecnologie utilizzate
- **Python** → linguaggio principale del progetto.  
- **Django** → framework principale, con moduli `forms`, `auth` e `messages`.  
- **SQLite** → database predefinito per la gestione dei dati dei post e degli utenti.  
- **HTML** → per creare le pagine di form, login e feedback.  
