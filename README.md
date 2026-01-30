# Programeren-wiskunde-Frank-Pepijn
# Eind project over Hamming-code en bitwise
# Introductie
Een hamming code is een code die extra informatie toevoegt aan een streng met data van enen en nullen zodat dit extra verzekerd wordt. Als namelijk een bitfout optreedt (dus van 1 naar 0 of vic versa) kan dit gedetecteerd worden en opgelost op diverse manieren.
Hammingcodes werken meer intuïtief door middel van matrixen waarbij de pariteitsbits worden uitgerekend door middel van een matrixvermenigvuldiging werkt biwise door gebruik te maken van bolean-operaties wat wel minder overzichtelijker is maar (in ons geval) gemiddeld gezien tot vier maal zo snel is.
In ons geval is de Hamming-code een (37,24) wat inhoud dat er 24 databits aanwezig zijn en die verzekerd worden door 13 pariteitsbits. De bitwise code is een standaard (7,4) dus 4 databits en 3 pariteitsbits.

# Uitleg 
Dit project bestaat dus uit twee losse codes war verschillende python-bestanden interacties hebben met elkaar, vandaar ook de twee Main.py-bestandjes. 
Alles wat te maken heeft met de Bitwise code staat ook op die manier aangeduid in de naam van het bestand, de andere zijn onderdeel van de hamming-(37,24) code.
Als je wilt testen hoe de code werkt ga je naar een van beide main.py-bestandjes en runt hem. Als je dat doet wordt er aan je gevraagt welke tekst je wilt "overzetten" wat gaat simuleren hoe de hamming/bitwise in zijn werking gaat en stuurt het eerst door naar de "Bit_converter".
Hier wordt tekst omgezet in binair. Voor bitwise was dit op een simpele manier gedaan door middel van ASCII wat al een unieke combinatie van enen en nullen heeft voor elk karakter, deze bestaat uit 8 nieuwe karakters dus is het opgesplitst in twee stukken van 4 zodat de (7,4) het hendellen kan. Bij de hamming gaat het nog niet zo gemakkelijk omdat het iets efficiënter te werk te gaan. Door wat karakters uit te sluiten waren er maar 6 bits nodig een karakter te coderen dus gaan er vier karakters per vector.
