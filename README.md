# Stazione Meteorologica
 Progetto per la misurazione di temperatura, umidità e pressione ambiente.
 
![Cattura4](https://github.com/user-attachments/assets/34cc2fba-4653-4141-a305-638d1e1a8195)

<p>Progetto per la rilevazione dei seguenti parametri ambientali:

Temperatura - Espressa in Graci Centigradi
Umidità - Esepressa in percentuale relativa
Pressione - Espressa in hPa</p>

Il software produce ad intervalli scelti dall'utente, un output in formato csv 
con le misurazioni effettuate della temperatura, umidità e pressione. 

## IMPORTANTE 
Accertarsi sempre che i file config.ini e la cartella /img/settings.png 
siano presenti nella stessa cartella dell'applicazione "Stazione_meteorologica.exe",
pena il mancato funzionamento della stessa. 

Inoltre bisogna rilevare la porta di comunicazione seriale COM assegnata da Windows
alla periferica di rilevazione ( Arduino ) e scrivere il numero della porta COM assegnata
nella relativa sezione dedicata del file config.ini :

### Arduino
La cartella 'Arduino' contiene il file sketch e relative librerie da inserire
nelle cartelle del software Arduino per poterci lavorare correttamente.

### Build
Contiene le versioni beta compilate a scopo di test.

### Release
Contiene le versioni ufficiali rilasciate a scopo di utilizzo.

### Source
La cartella 'Source' contiene i file sorgenti scritti in Python per eventuali modifiche 
e implementazioni future al software.



