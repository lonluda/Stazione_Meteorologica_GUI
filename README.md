# Stazione Meteorologica
 Progetto per la misurazione di temperatura, umidità e pressione ambiente.
 
![Cattura4](https://github.com/user-attachments/assets/34cc2fba-4653-4141-a305-638d1e1a8195)

Progetto per la rilevazione dei seguenti parametri ambientali:

• Temperatura - Espressa in Graci Centigradi <br>
• Umidità - Esepressa in percentuale relativa <br>
• Pressione - Espressa in hPa


![Cattura2](https://github.com/user-attachments/assets/ec6c2e40-fa82-4509-ae49-a6a8d4e01c2a)


Il software produce ad intervalli scelti dall'utente, un output in formato csv 
con le misurazioni effettuate della temperatura, umidità e pressione. 

![Cattura3](https://github.com/user-attachments/assets/4198b7cb-6e7d-489f-a324-3adddec41664)
![Cattura6](https://github.com/user-attachments/assets/07c968e7-5aed-4a5b-9bc5-12270b9a0813)


## IMPORTANTE 
Accertarsi sempre che i file config.ini e la cartella /img/settings.png 
siano presenti nella stessa cartella dell'applicazione "Stazione_meteorologica.exe",
pena il mancato funzionamento della stessa. 

Inoltre bisogna rilevare la porta di comunicazione seriale COM assegnata da Windows
alla periferica di rilevazione ( Arduino ) e scrivere il numero della porta COM assegnata
nella relativa sezione dedicata del file config.ini :

<img src="https://github.com/user-attachments/assets/2da7285a-a4c1-4f64-9e4a-78852fe90b45" width="300px"/>

### Arduino
La cartella 'Arduino' contiene il file sketch e relative librerie da inserire
nelle cartelle del software Arduino per poterci lavorare correttamente.

![WhatsApp Image 2025-08-21 at 11 32 26](https://github.com/user-attachments/assets/43e1aa7e-4412-4416-ab2a-80c45bb8dde4)


### Build
Contiene le versioni beta compilate a scopo di test.

### Release
Contiene le versioni ufficiali rilasciate a scopo di utilizzo.

### Source
La cartella 'Source' contiene i file sorgenti scritti in Python per eventuali modifiche 
e implementazioni future al software.



