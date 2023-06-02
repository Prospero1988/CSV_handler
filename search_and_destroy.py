import os

# Pobieranie ścieżki do folderu
folder_path = input("Podaj ścieżkę do folderu, w którym chcesz pracować: ")

# Pobieranie słów kluczowych
keywords = input("Podaj słowa kluczowe, oddzielone spacją: ")
keywords = keywords.split()

# Zmienna do przechowywania liczby usuniętych plików
deleted_files_count = 0

# Przeszukiwanie folderu i usuwanie plików
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        for keyword in keywords:
            if keyword in filename:
                os.remove(file_path)
                deleted_files_count += 1
                break  # Przerywamy pętlę w przypadku znalezienia słowa kluczowego w nazwie pliku

# Wyświetlanie informacji o zakończeniu pracy
print("Zakończono pracę.")
print("Liczba usuniętych plików:", deleted_files_count)
