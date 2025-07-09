import os
import datetime
import subprocess

# === CONFIGURATION ===
INPUT_FILE = "music_list.txt"     # Fichier contenant les noms des musiques
OUTPUT_ROOT = "output"            # Répertoire racine des téléchargements

# === FONCTIONS ===

def create_output_directory():
    """
    Crée un dossier daté dans le dossier output/ (ex : output/2025-07-09)
    """
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(OUTPUT_ROOT, today)
    os.makedirs(path, exist_ok=True)
    return path

def read_music_list(filepath):
    """
    Lit et retourne les lignes non vides du fichier TXT
    """
    if not os.path.exists(filepath):
        print(f"[ERREUR] Le fichier {filepath} est introuvable.")
        return []
    
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def download_mp3(track_title, output_dir):
    """
    Recherche et télécharge le 1er résultat YouTube correspondant au titre donné.
    """
    print(f"[+] Recherche et téléchargement : {track_title}")

    command = [
        "yt-dlp",
        "-x",                         # Extraire l'audio
        "--audio-format", "mp3",     # Format de sortie
        "--output", os.path.join(output_dir, "%(title)s.%(ext)s"),
        f"ytsearch1:{track_title}"   # Recherche YouTube (1er résultat)
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Échec du téléchargement pour : {track_title}")

def main():
    print("[*] Démarrage du script...")

    tracks = read_music_list(INPUT_FILE)
    if not tracks:
        print("[!] Aucun titre trouvé dans le fichier.")
        return

    output_dir = create_output_directory()
    print(f"[✓] Les fichiers seront enregistrés dans : {output_dir}\n")

    for title in tracks:
        download_mp3(title, output_dir)

    print("\n[✓] Tous les téléchargements sont terminés.")

if __name__ == "__main__":
    main()
