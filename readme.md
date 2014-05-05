#PostBot
Vi har gjort ett program som anv�nder sig av Reddits API. Denna s� kallade bots m�l �r att kommentera p� tr�dar som har skrivits p� ett specifikt subreddit. 
Programmet arbetar i flera olika steg varje g�ng den ska h�mta information.

* H�mta de 25 senaste tr�darna i given subreddit och l�gga dem i en lista.
* Loopar igenom denna lista och filtrera bort de tr�dar som redan har kommenterats p� med hj�lp av en fil som h�ller koll p� kommenterade tr�dar.
* Kommentera det givna medelandet p� given okommenterad tr�d.
* L�gga till den nya kommenterade tr�den filen f�r kommenterade tr�dar.

Programmet anv�nder sig av en s� kallad �Throttler� f�r att begr�nsa hur m�nga antal �requests� som f�r skickas. Den �r standard inst�lld p� reddits rekommenderade inst�llningar som �r 30 requests per minut.
Programmet anv�nder sig av dessa �requests� f�r att kommunicera med reddit.com och h�mta information. Dem requestsen som v�r bot f�r tillf�llet kan g�ra �r f�ljande:

* Logga in.
* H�mta tr�dar i en given subreddit.
* H�mta kommentarer i en given tr�d.
* Skriva en kommentar i en given tr�d.

Det �r v�ldigt simpelt att l�gga till ytterligare requestsorter d� dessa �rver fr�n en standard request klass. Av dessa requests f�r man oftast tillbaka en json med information som man sedan f�r anv�nda hur man vill.

Programmet �r f�r n�rvarande inst�llt att om en request misslyckats eller man har �verstigit max requests s� v�ntar den p� att man kan g�ra det igen. Detta kan dock �ndras ganska l�tt till ett annat system men vi tyckte att detta var mest l�mpligt f�r v�r bots syfte.
##F�rb�ttringar
Det vi skulle kunna l�gga till och �ndra i programmet �r att ha ett b�ttre system f�r att l�gga till requests som ska k�ras. Detta kan antingen l�sas med att skicka dem till en k� eller anv�nda sig av events. Det man ocks� skulle kunna g�ra �r att anv�nda sig av multithreading f�r att kunna k�ra flera requests samtidigt. Vi skulle ocks� kunna g�ra v�rt program mera anv�ndarv�nligt s� att andra personer bara med n�gra rader kan skriva sin egen bot med standardfunktioner utan att beh�va filtrera ut svaret ur jsonlistor.

