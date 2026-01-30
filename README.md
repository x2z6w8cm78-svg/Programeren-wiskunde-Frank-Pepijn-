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
Laatste ding wat op kan vallen is dat bitwise in strings werkt en hamming door middel van classes dit hadden we zo gedaan omdat het werken met classes en stuk overzichtelijker gaat alleen voor de snelheid van bitwise is het beter om met strings te werken.
Als laatst wordt de data verzekerd met pariteitsbits, bij bitwise door middel van de xor-functie en bij hamming door middel van de matrixmultiplicatie verborgen in de class om overzichtelijkheid te bewaren.

Dan begint het verzenden in het bestand "Verzender_controlepost.py" waar eerst met een bepaalde factor "Omschakel_kans" de data wordt verstoord om de bitfouten te representeren in het echt. Daarna is het "verzonden" en is het de taak de originele data terug te krijgen dit wordt gedaan door wanneer het niet klopt (de pariteitsbits komen niet overeen met wat het hoort te zijn als je het weer narekend) de data opnieuw op te vragen en democratisch dan te besluiten wat de vector aan data zou moeten wezen (twee enen en een nul betekent dat er waarschijnlijk wel een een had moeten staan) en zo de fouten eruit te filteren door middel van kansrekening.

Als de data eenmaal weer klopt kan het weer terug omgezet worden en dir wordt in het bestand "Reverse_bit_converter.py" gedaan waar binair weer wordt omgezet in het corresponderende karakter. Om het process erachter iets meer te laten leven wordt tussen de nieuwe stukjes tekst een tussentijdse tekst uitegeprint met een getal erbij (erboven) wat staat voor hoe vaak het nodig was de tekst te moeten sturen voordat het klopte.

# Voorbeeld met opmerkingen
Nu gaat de tekst "Zo werken de volgende codes nou echt!" door de codes heen met een omschakelkans van 20, met andere woorden 5% van de bits krijgt een bitfout.
Main.py (Hamming-(37,24)):
