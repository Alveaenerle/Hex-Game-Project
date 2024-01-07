# Dane Autora
    Imię i nazwisko: Dominik Śledziewski
    Nr Indeksu: 331447

# Cel i opis projektu
    Projektem jest gra planszowa Hex, w której 2 graczy ma za zadanie połączyc
    jednym ciągiem swoje strony planszy (górną i dolną lub lewą i prawą)
    Wygrywa ten gracz który zrobi to jako pierwszy
    Gra została oparta o framework two_player_games i została zrealizowana w terminalu

# Podział na klasy
### Hex
    Główna klasa w grze, która odpowiada za obsługę reszty klas
    Za jej pośrednictwem następuje komunikacja z całą grą
    Przechowuje one obecny stan gry typu HexState
    Dziedziczy ona po klasie Game z frameworku
### HexState
    Klasa przedstawiająca stan gry
    Przechowuje one aktualną planszę wraz z informacją, który gracz wykonuje ruch
    Odpowiada ona w głównej mierze za logikę gry
    Dziedziczy ona po klasie State z frameworku
### HexMove
    Klasa przedstawiająca ruch na planszy
    Posiada ona koordynaty Hexa jako krotkę [linia, kolumna]
    Dziedziczy ona po klasie Move z frameworku
### HexPlayer
    Klasa przedstawiająca gracza
    Gracz posiada swój unikalny symbol (stringa o długości 1)
    oraz atrybut up_down wskazujący na strony planszy które
    gracz posiada (jeśli up_down jest prawdą to gracz posiada górną i dolną część planszy)
    Klasa ta dziedziczy po klasie Player z frameworku
# Instrukcja
### Instalacja
    Należy pobrać repozytorium z 'https://gitlab-stud.elka.pw.edu.pl/dsledzie/Hex'
### Uruchamianie
    Aby włączyc grę należy uruchomić plik "main.py"
    Windows: 'python main.py'
    Linux: 'python3 main.py'
    Należy pamiętać aby znajdować się w pobranym folderze 'Hex'
### Obsługa
    Na początku należy unikalny napis o długości 1 dla każdego gracza
    Następnie gra poprosi o podanie wielkości planszy (od 1 do 26)
    W następnych krokach każdy z graczy będzię musiał podać koordynaty hexa, na którym chce postawić pionka
    koordynaty należy podać w kolejności: kolumna (litera), linia (liczba)
# Część refleksyjna
    Gra została oparta o framework, co znacznie usprawniło tworzenie gry
    Dwoma największymi trudnościami było efektywne przechowywanie planszy
    oraz algorytm do znajdowania zwycięzcy
    W pierwszy przypadku zdecydowałem się na stworzenie listy list
    pierwsza lista zawiera w sobię liste pól w danej kolumnie
    plansza składa się z sześciokątów, więc możliwe jest podzielenie jej na kolumny linie
    Jeśli jakieś pole jest zajęte przez gracza oznacza się je jego symbolem
    Za implementację znajdowania zwycięzcy odpowiada algorytm BFS, ponieważ jest on efektywny
    i prosty do zrozumienia
### Elementy niezrealizowane
    Graficzny interfejs użytkownika - ze względu na zmienną wielkość planszy,
    implementacja jest czasochłonna oraz framework stawia na implementacje w terminalu
    Tryb gry dla jednego gracza - implementacja AI która miałaby szanse wygrać z człowiekiem
    jest bardzo wymagający


