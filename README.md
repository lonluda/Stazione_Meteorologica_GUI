# Stazione Meteorologica
 Progetto per la misurazione di temperatura, umidità e pressione ambiente.
 
 ![Cattura](https://github.com/user-attachments/assets/968ab01d-92b8-460b-a23e-c0fb62df28c6)
![Cattura4](https://github.com/user-attachments/assets/f14a8350-dd38-4b23-845a-592ff615b657)

Progetto per la rilevazione dei seguenti parametri ambientali:

Temperatura - Espressa in Graci Centigradi
Umidità - Esepressa in percentuale relativa
Pressione - Espressa in hPa

![Cattura2](https://github.com/user-attachments/assets/98bcabf6-9326-4e8b-85e7-26d9ea42bab4)

Il software produce ad intervalli scelti dall'utente, un output in formato csv 
con le misurazioni effettuate della temperatura, umidità e pressione. 

![Cattura3](https://github.com/user-attachments/assets/d906052a-7dd1-45c9-91fb-84f14df6a650)
![Cattura6](https://github.com/user-attachments/assets/6fac910e-cb9d-44ea-b1d6-f60357bd7776)

## IMPORTANTE 
Accertarsi sempre che i file config.ini e la cartella /img/settings.png 
siano presenti nella stessa cartella dell'applicazione "Stazione_meteorologica.exe",
pena il mancato funzionamento della stessa. 

![Cattura5](https://github.com/user-attachments/assets/1b96ec71-066c-4672-97da-8d2330d46861)

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



