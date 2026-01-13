# Projekt sterowania robotem UR5 w środowisku ROS2
Projekt zawiera skrypt, który obraca drugim przegubem robota UR5 w górę lub dół z komputera lokalnego w środowisku ROS2

# Instalacja i działanie
Aby poprawnie zainstalować projekt należy pobrać repozytorium na git huba na komputer lokalny
```bash
git clone git@github.com:Vinterion/ROS_project.git
```
A następnie wejść w projekt i uruchomić skrypt startowy
```bash
cd ROS_project/
sudo xhost +local:docker
bash start.sh
```
Po komendzie sudo xhost +local:docker wymagane jest wpisanie hasła użytkownika. Jest ona wymagana do poprawnego działania GUI dockera. Skrypt tworzy kontener w Dockerze, a następnie pobiera wszystkie wymagane biblioteki. Po ich pobraniu uruchamia symulację robota w środowisku Gazeboo, oraz tworzy okno z obrazem z kamery USB (w wypadku braku kamery widać tylko czarne okno). Wszystkie komendy na temat pobieranych bibliotek znajdują się w pliku Dockerfile a na temat uruchamianych paczek ROSa w pliku entrypoint.sh. 
Po uruchomieniu skryptu startowego oraz poprawnej inicjalizacji projektu powinnismy widzieć okno symulacji robota w Gazeboo oraz okno słuzące do sterowania robotem:
<img width="1015" height="630" alt="image" src="https://github.com/user-attachments/assets/43e7f178-c9a1-4fa2-a612-7280e88d7791" />
Po naciśnięciu w dolną część ekranu robot obróci swoim drugim przegubem w dół:
<img width="1015" height="630" alt="image" src="https://github.com/user-attachments/assets/5f6a4efe-1769-4dc0-a5a2-99901a2b10a7" />
Analogicznie po nacisnięciu w górną część okna robot obróci się w górę:
<img width="1015" height="630" alt="image" src="https://github.com/user-attachments/assets/19cc2218-1e94-452e-bd1f-8bafe9ae0d6c" />
