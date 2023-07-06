import os

# Pobieranie ścieżki do folderu
folder_path = input("Podaj ścieżkę do folderu, w którym chcesz pracować: ")

# Pobieranie słów kluczowych
keywords = input("Podaj słowa kluczowe, oddzielone spacją: ")
keywords = keywords.split()

# Zmienna do przechowywania liczby usuniętych plików
deleted_files_count = 0

# Rekurencyjne przeszukiwanie folderu i usuwanie plików
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        for keyword in keywords:
            if keyword in filename:
                os.remove(file_path)
                deleted_files_count += 1
                break  # Przerywamy pętlę w przypadku znalezienia słowa kluczowego w nazwie pliku

# Wyświetlanie informacji o zakończeniu pracy
print("Zakończono pracę.")
print("Liczba usuniętych plików:", deleted_files_count)
