
# Zusammenfassung 
Diese Zusammenfassung dient als Orientierung zur Vorbereitung und nicht als die offiziellen Lernmaterial für die Prüfungsvorbereitung. 

Das offizielle Lernmaterial ist WBS Python Buch (Python3), Kapitel Netzwerkkommunikation

# OSI-Layer
- besteht aus 7 Layers
- Software Programmierer arbeiten meistens mit den höheren Layers (Ab layer 4)


# Sockets
bieten die grundlegende Funktionalität zur Netzwerkkommunikation an.


# Ports
- 16xbit Zahl . D.h. 65535 unterschiedliche Ports

Standard Port List die freigegeben ist bis 1024. Aber heute gibt es noch viel mehr bis ca. 10000 reserviert unter Validation von internationalen Organisation.
z.B:
- 21: FTP
- 22: SSH, sFTP
- 25: SMTP
- 80: HTTP
- 110: POP3
- 443: HTTPS

  
# UDP (User Datagram Protocol)
- schnellet als TCP
- Nicht zuverlässig
- Für Steams, VoIP (Voice over ip)

# HTTP (Hyper Text Transfer Protocol)
- Standard Port für HTTP ist : 80
- Port 80: reserviert für Webservers (Webseiten) als Standard Port. 


# TCP ( Transmission Control Protocol)
- langsamer als UDP
- Für z.B. Chat, EMails und Datei Austausch
- Zuverlässig und man kann damit sicherstellen dass die Infos ans Ziel angekommen sind
  

# FTP (File Transfer Protocol)
- ist ein TCP Protocl
- ermöglichst Datein hoch- oder runterzuladen von einem FTP Server
- Standard Port : 21
- Standard sFTP (Secured FTP) port : 22
- 

# EMails
python 'email' module bietet die Möglichkeit an, sonderzeichen, binärformatte wie Anwendungen, Audiodatein, Grafikdateien zu handeln (via was sogenannte MiMe Encoding)

## SMTP (Simple Mail Transfer Protocol)
- E-Mails zu senden
- Durch MiMe Encoding kann mann onderzeichen, binärformatte wie Anwendungen, Audiodatein, Grafikdateien zu senden
-  


## IMAP4 (Internet Message Access Protocol)
- E-Mails abzuholen
- Erlaubt Unterordner
- Serverbasierte Speicher

## POP3 (Post Office Protocol)
- erlaubt kein Unterordner in der E-Mail Struktur
- Clientbasietre Speicher was für Multi-Device schlecht ist
- 

# XML-RPC (Remote Proceduce call)
- Ermöglicht den entfernten Funktions- und Methodenaufruf über eine Nrtzwerkschnittstelle.
- Moderne Methoden : Webservices, Rest APIs , SOAP, etc. um entfernten Funktionen aufzurufen

# Telnet
Es ist ein Client-Server Protocol. (Command Line basierte Kommunikation) 
Ermöglicht die Kommunikation zwischen Geräte (Routers, Switches, etc.) oder Netzwerk-Knoten wie Software Servers (IMAP Server, FTP Server, etc.). Aber leider unverschlüsselt. Die alternative ist SSH (Secure Shell Protocol), was verschlüsselt ist.
