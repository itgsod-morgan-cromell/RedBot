#PostBot
Vi har gjort ett program som använder sig av Reddits API. Denna så kallade bots mål är att kommentera på trådar som har skrivits på ett specifikt subreddit. 
Programmet arbetar i flera olika steg varje gång den ska hämta information.

* Hämta de 25 senaste trådarna i given subreddit och lägga dem i en lista.
* Loopar igenom denna lista och filtrera bort de trådar som redan har kommenterats på med hjälp av en fil som håller koll på kommenterade trådar.
* Kommentera det givna medelandet på given okommenterad tråd.
* Lägga till den nya kommenterade tråden filen för kommenterade trådar.

Programmet använder sig av en så kallad ”Throttler” för att begränsa hur många antal ”requests” som får skickas. Den är standard inställd på reddits rekommenderade inställningar som är 30 requests per minut.
Programmet använder sig av dessa ”requests” för att kommunicera med reddit.com och hämta information. Dem requestsen som vår bot för tillfället kan göra är följande:

* Logga in.
* Hämta trådar i en given subreddit.
* Hämta kommentarer i en given tråd.
* Skriva en kommentar i en given tråd.

Det är väldigt simpelt att lägga till ytterligare requestsorter då dessa ärver från en standard request klass. Av dessa requests får man oftast tillbaka en json med information som man sedan får använda hur man vill.

Programmet är för närvarande inställt att om en request misslyckats eller man har överstigit max requests så väntar den på att man kan göra det igen. Detta kan dock ändras ganska lätt till ett annat system men vi tyckte att detta var mest lämpligt för vår bots syfte.
##Förbättringar
Det vi skulle kunna lägga till och ändra i programmet är att ha ett bättre system för att lägga till requests som ska köras. Detta kan antingen lösas med att skicka dem till en kö eller använda sig av events. Det man också skulle kunna göra är att använda sig av multithreading för att kunna köra flera requests samtidigt. Vi skulle också kunna göra vårt program mera användarvänligt så att andra personer bara med några rader kan skriva sin egen bot med standardfunktioner utan att behöva filtrera ut svaret ur jsonlistor.

