# DjangoAPI
## Lavoro di tesi per visualizzazione e quering delle informazioni su sequenze geniche
### Prima modalità di utilizzo - DB su Virtual Machine - Allinearsi all'ultimo rilascio del branch main
#### Per poter avviare il progetto occorre:
1. Possedere connessione al DB;
1. Installare *Visual Studio Code* per poter modificare e lanciare il progetto;
1. Installare una *Virtual Local Einvorment PYTHON* per installare le librerie necessarie al corretto funzionamento;
1. Lanciare le APIs del backend eseguendo, nella cartella principale del progetto, il comando *python manage.py runserver*
1. Installare la cli di Angular;
1. Nella cartella della ui eseguire prima *npm install* e successivamente *npm start* 

### Seconda modalità di utilizzo - Docker - Allinearsi all'ultimissimo rilascio sul branch dockerizzazione
#### Per poter avviare il progetto occorre:
1. Scaricare ed installare docker-desktop
1. Aprire una shell/prompt di comando nella cartella principale del progetto in cui vi è il file docker-compose.yml
1. Avviare docker-desktop e verificare che la virtualizzazione sia disponibile
1. Eseguire i comandi: *docker-compose build* e *docker-compose up -d*
