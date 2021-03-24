## Instrukcja użytkowania skryptu remove-in-directory

# Co robi skrypt
Skrypt porównuje zawartość pliku .xls z dostarczonymi indeksami z aktualnej oferty, z zawartością folderu w którym znajdują się zdjęcia. Usuwa zdjęcia produktów z folderu których nie ma w nowej ofercie. Po tym działaniu, w folderze ze zdjęciami pojawiają się pliki „usunięte-pliki.xls” z listą plików, które usunął oraz „brak-w-folderze.xls” z listą indeksów, które znajdują się w nowej ofercie, ale których zdjęcia nie znajdują się w folderze. 

# Wstępne wymagania i instalacja
Do użytku skryptu trzeba mieć zainstalowanego Pythona 3.7+ oraz biblioteki zewnętrzne xlrd i xlwt. Biblioteki możemy zainstalować automatycznie* uruchamiając plik pack-install.bat, który znajduje się w folderze installer (folder posiadasz jeśli dostałeś całą paczkę z instalatorem oraz plikiem wykonawczym) 
* aby móc zainstalować biblioteki automatycznie, wcześniej musi być zainstalowany Python w domyślnej ścieżce Windowsa

# Jak używać
Po zainstalowaniu wymaganych bibliotek, do użytku skryptu potrzebujemy plików run.bat oraz script.py.
1.	Wrzucamy pliki*1  run.bat oraz script.py do folderu w którym znajdują się zdjęcia produktów. 
2.	Wrzucamy arkusz kalkulacyjny*2 w formacie .xls (zapisujemy jako Excel 1997-2003) do folderu w którym znajdują się zdjęcia produktów oraz wcześniej wrzucone pliki skryptu. *3
3.	Uruchamiamy plik run.bat.
4.	Jeśli wszystko zadziałało poprawnie, w otwartym wierszu poleceń możemy ujrzeć informację o zapisaniu dwóch plików Excela. Jeśli coś nie działa i wierszu poleceń pojawia się coś dziwnego, robimy screena i wysyłamy do Kacpra W. 
5.	Wiersz poleceń możemy zamknąć.
6.	W folderze powinny pojawić się dwa pliki Excel: „usunięte-pliki.xls” oraz „brak-w-folderze.xls”, a nieaktualne zdjęcia powinny być usunięte. 

*1 Pliki dostarczane są w folderze executor, który posiadasz jeśli dostałeś całą paczkę z instalatorem oraz plikiem wykonawczym.
*2 Nazwa dostarczonego pliku nie ma znaczenia
*3 Należy pamiętać, aby przed uruchomieniem skryptu w folderze w którym działamy znajdował się tylko jeden plik Excela. W przypadku jeśli plików nie będzie lub będzie więcej niż jeden w konsoli pojawi się błąd, a skrypt się nie uruchomi. 
