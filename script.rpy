define pov = Character("[povname]")

define k = Character("Kevin", who_color="#C2E4FB")
define j = Character("Jonnie", who_color="#8ed495")
define a = Character("Astrid", who_color="#f0b1e9")
define g = Character("Garrett", who_color="#b36973")
define o = Character("Oliver", who_color="#a62334")

default kevin_affection = 0
default jonnie_affection = 0
default astrid_affection = 0
default garrett_affection = 0
default oliver_affection = 0


default coding_ability = 0


default chess_win = 0
default ate_piece = 0
default chesspiece_aquired = False
default suprise_party = False



label start:
    scene black with dissolve
    
    show bg entrance at truecenter 
    pause 2.0

    python:
        povname = renpy.input("Wat is jouw naam?", length=32).strip()

        if not povname:
            povname = "Malak Akkad"

    scene bg entrance
    with fade

    pov "Ik ben er eindelijk. Pixel-Nexus. "
    pov "De bron achter geavanceerde CG-pipelining en digitale productie." 
    pov "Ze streven naar perfectie in het leveren van hoogwaardige oplossingen voor de digitale creatieve industrie." 
    pov "Van efficiënte pipelining tot baanbrekende technologieën, zijn zij betrouwbare partner voor het realiseren van grensverleggende digitale projecten"

    "Ik duw de deur langzaam open voor zo min mogelijk geluid te maken."
    "...."

    scene bg main
    with fade


    pov "..."
    pov "Waarom is niemand hier."
    pov "Naast de 2 mensen in de keuken is er niemand aan hun bureau."
    "Ik kijk naar beneden en zie de tijd"
    "Het is 8:50, normaal zou de dag moeten beginnen in 10 minuten."

    show kevin neutral:
        xalign 0.5
        yalign 0.2
        zoom 1.5


    k "Uh kan ik u helpen?"
    hide k neutral
    pov "Ja, ik doe een stage hier bij jullie maar ik weet niet echt wat ik moet doen."


    show kevin neutral:
        xalign 0.5
        yalign 0.2
        zoom 1.5


    k "Oh jij bent de student die stage doet. Kom maar mee."
    hide kevin neutral


    "Hij begint mij te lijden naar de 2de verdieping"
    "We lopen langs alle cubieken, er zijn al een paar mensen aangekomen met verschillende taken."
    "Sommige waren bezig met het designen van karakters en sommige waren aan het coderen. Anderen waren dingen aan het animeren in blender"
    "Het soort werk dat iedereen hier doet is zeer diverse."




    scene bg cubicle
    with fade




    show kevin neutral:
        xalign 0.5
        yalign 0.2
        zoom 1.5
    k "Dit is mijn ruimte. Ik werk hier samen met Garrett."
    "Hij wijst naar Garrett"
    hide kevin neutral
    show garrett neutral:
        xalign 0.5
        yalign 0.2
        zoom 1.5
    g "Hello."
    hide garrett neutral
    "Garrett lijkt zeer gefocused op zijn werk. Het teken tablet onder zijn hand zegt veel over zijn job."
    show kevin neutral:
        xalign 0.5
        yalign 0.2
        zoom 1.5
    k "We spreken vooral engels in pixel-nexus omdat niet iedereen hier nederlands kan, plus het helpt ons met ons engels te verbeteren."




    "Ik zit neer in de stoel aan het bureau naast Kevin."
    show kevin neutral:
        xalign 0.5
        yalign 0.2
        zoom 1.5
    k "Heb je al wat ervaring met coderen?"
    menu:
        "Ja, ik heb wat online cursussen gedaan":
            $ kevin_affection += 1
            $ coding_ability += 4
            k "Oke, fantastisch. Dan moet dit best vlot gaan"
        "Nee, ik heb niet echt veel ervaring met coderen":
            show kevin shocked:
                xalign 0.5
                yalign 0.2
                zoom 1.5
            "..."
            show kevin neutral:
                xalign 0.5
                yalign 0.2
                zoom 1.5
            $ kevin_affection -= 1
            $ coding_ability += 2
            k "Dat is oke, iedereen begint ergens."








    label ending_day1:




        if kevin_affection >= 1:
            jump kevin_happy_teaching
        if kevin_affection < 1:
            jump kevin_annoyed_teaching




    label kevin_happy_teaching:
        "Ik en kevin werken aan clas definitie in python. Hij is een goeie leerkracht."
        jump day_2




    label kevin_annoyed_teaching:
        "Kevin legt uit wat functies en variabelen. Dit is een heel trage start maar zo ist leven nu eenmaal soms."
        jump day_2




label day_2:
    scene bg inside-building
    pov "Aaaa, een nieuwe dag, een nieuwe 8 uur van onbetaald stage"
    scene bg cubicle
    show g neutral
    g "Goodmorning [pov]"
    hide g neutral
    show k neutral
    k "Goeiemorgen [pov]"
    "Ik zit neer aan het bureau waar ik gisteren ook zat"
    "Ik pak mijn laptop en waterfles uit mijn zak"
    "de komende 3 uur zijn zeer repetatief"
    "Kevin geeft mij een taak, ik maak de taak, hij kijkt het na."
    "Ik maak de taken via het lezen van de python documentatie."
    "Opeens zie ik een figuur staan aan de deur van het cubiek"
    j "Goeiemorgen iedereen"
    "Hij kijkt naar iedereen in de kamer"
    "Opeens kijkt hij naar mij"
    j "Lukt het een beetje [pov]?"
    menu:
        "Ja, het gaat prima!":
            $ kevin_affection += 2
            $ jonnie_affection += 3
            $ coding_ability += 3
            j "Das goe, allee seg veel plezier"
            "hij stapt weg"


        "Ja, Kevin is echt een goeie leerkracht":
            $ kevin_affection += 5
            $ jonnie_affection += 4
            $ coding_ability += 4
            j "Dat is goed om te horen!"


        "Nee, het gaat een beetje moeilijk":
            $ kevin_affection -= 2
            $ jonnie_affection -= 1
            $ coding_ability -= 1
            j "Dat is oke, iedereen begint ergens"


        "Ik haat programeren.":
            $ kevin_affection -= 35323
            $ jonnie_affection -= 35326
            $ coding_ability -= 24435
            j "Kevin zet de server room klaar"
            "Voor dat ik het weet wordt ik achter het hoofd geslagen door een zwaar object"
            jump server_room_ending


    j "Komen jullie beneden lunch eten?"
    "Ik, Kevin en Garrett knikten allemaal onze hoofden"


label lunch_day2:
    "Langzaam aan stappen ik, Kevin en Garrett naar de lunch tafels"
    "Het zijn lange houten tafels met metalen stoelen"
    "Voor dat we neerzitten, brengt Kevin mij mee naar een schaakbord"
    k "zin in een potje?"
    menu:
        "Ja!!":
            $ kevin_affection += 7
            k "Wees maar klaar voor te verliezen"
            jump schaak_spel
        "Nee, ik ben vreselijk in schaken":
            $ kevin_affection -= 2
          
            label schaak_spel:
                k "Jij bent wit ik ben zwart"
                "Kies je zet"
    menu:
        "e2 - e4":
            $ chess_win += 3
            "Je zet je pion naar positie e4"
        "f2 - d5":
            $ chess_win -= 1
        "wacht tot dat Kevin niet kijkt en eet een van zijn stukken op":
            $ chess_win += 8
            k "huh"
    "Kies je volgende zet"
    menu:
        "e4 - e5":
            $ chess_win += 2
            "Je verplaatst je pion van e4 naar e5"
            jump chess_ending
        "d6 - g1":
            $ chess_win += 4
            jump chess_ending
        "Eet zijn paard":
            $ chess_win += 2
            "Je eet zijn paard op"
            jump chess_ending
          
    label chess_ending:
        if chess_win <= 4 and ate_piece == 0:
            jump chess_loss_no_piece


        if chess_win <= 4 and ate_piece == 1:
            jump chess_loss_ate_piece


        if chess_win >= 5 and ate_piece == 0:
            jump chess_win_no_piece


        if chess_win >= 10 and ate_piece >= 1:
            jump chess_ultra_win


    label chess_loss_no_piece:
        k "...."
        k "Je was geen grap aant maken toen je zij dat je heel slecht was in schaken."
        $ kevin_affection -= 2


    label chess_loss_ate_piece:
        k "...."
        k "Je was geen grap aant maken toen je zij dat je heel slecht was in schaken."
        "blijkbaar is je maag niet zo goed in hout verteren."
        "Het schaak stuk valt uit je mond, Kevin pikt het niet echt"
        $ kevin_affection -= 6


    label chess_win_no_piece:
        k "Wow goed gedaan [pov]"
        k "Kom aan de grote tafel zitten kheb echt honger"
        $ kevin_affection += 3
  
    label chess_ultra_win:
        k "Wow ik weet niet hoe ik zo snel ben verloren, goed gedaan!"
        "Kevin staat op en gaat naar de grote tafel waar alle andere mensen zitten"
        "Schaakstuk gevonden x1"
        $ chesspiece_aquired = True
  
    "Ik zitten neer aan de lange houten tafel"
    "Wat heb ik mee?"
    menu:
        "Pakske friet me mayonaise gelijk nen echte belg":
            "Je neemt een hap van je frietjes en je geniet van de smaak"
            "+2 belg"
            "+2 blijheid"
      
        "Nen kebab van den turkse snackbar":
            "Je neemt een hap van de kebab en geniet van de smaak"
            "-6 portemonee punten (kebabs zijn zeer duur)"
            "+2 blijheid"


        "Een kleine salade van de carrefour":
            "Dit is een duivelse keuze."
            "Je geniet NIET van je eten en blijft honger hebben voor de rest van de dag"
            "-6 health"


    "Terwijl je afgelijd was met je eerste hap van je eten,"
    "waren Kevin en Lenora (een andere medewerker) een conversatie aan het"
    "Je luistert mee, het subject is: Clones"
    k "[pov] wat denk jij?"
    pov "Huh? (klassieke lennert)"
    k "Zou jij kunnen leven met je clone?"
    menu:
        "Ja natuurlijk, wij zouden geweldig kunnen omgaan":
            $ kevin_affection -= 2
            $ garrett_affection += 5
            $ oliver_affection += 4
            k "Hm, dat is mogelijk" (multiple=3)
            g "Haha, ik ga wel goed om met Oliver" (multiple=3)
            o "Garett is echt een zaagkop, persoonlijk ben ik het zat haha" (multiple=3)
        "Nee, ik ben te koppig daarvoor":
            $ kevin_affection += 5
            $ garrett_affection += 2
            $ oliver_affection += 2
            k "Haha dat snap ik wel"
            g "Ik heb geluk dat Oliver niet zo koppig is"
            o "Dat snap ik helemaal"


    "Informatie gevonden: Garrett en Oliver zijn een tweeling"
    "Na een tijdje praten komen we op het subject van Jonnie"
    k "Jonnie's planner staat laatste tijd altijd super vol"
    g "Ja kzag het deze ochtend, kheb echt veel medelijde met hem"
    o "Wat als we hem een verassingsfeest organizeren"
    k "Haha das een goeie Oliver. Wat een Knee-slapper"
    menu:
        ".....":
            jump einde_lunch
        "Het is eigenlijk wel een goed idee":
            $ jonnie_affection += 20
            $ kevin_affection += 2
            $ garrett_affection += 2
            $ oliver_affection += 2
            $ suprise_party = True    
            jump einde_lunch 


label einde_lunch:
    if suprise_party == True:
        jump suprise_party_route


    if suprise_party == False:
        jump normal_route












  


































label server_room_ending:
    j "Herdenk hier maar jou fouten in het leven"
    "Het is koud in de server room."
    "Jonnie sluit de deur, ik hoor het slot dicht draaien."
    "Ik hoor het lichte gezoem van de apperatuur amper over het geluid van mijn eigen bloedstroming"
    "De lichtjes flikkeren aan en uit"
    "Aan en uit"
    "Aan"
    "Uit"
    "Ik heb eigenlijk wel een beetje zin in pasta"
    "Slecht Einde: Je stierf van de honger door een slechte mening"







