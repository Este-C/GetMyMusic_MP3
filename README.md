
# 🎵 GetMyMusic-MP3 by 6sco

GetMyMusic-MP3 est une application en Python qui permet de télécharger automatiquement au format MP3 les musiques listées dans un fichier texte. Elle effectue une recherche YouTube sur chaque titre, récupère le premier résultat, et extrait l’audio au format `.mp3`.

---

## 🚀 Fonctionnalités

- Lecture d'un fichier `music_list.txt` contenant une liste de titres de musiques (un par ligne).
- Recherche automatique sur YouTube via `yt-dlp`.
- Extraction audio en format MP3.
- Classement des musiques téléchargées dans un dossier daté (`output/YYYY-MM-DD/`).
- Installation automatique via un script bash.

---

## 📁 Structure du projet

```

GetMyMusic-MP3/
├── GetMyMusic-MP3.py         # Script principal Python
├── music\_list.txt          # Liste des musiques à télécharger
├── install.sh              # Script d'installation (automatisation)
├── venv/                   # Environnement virtuel Python (généré)
└── output/                 # Dossier de sortie contenant les musiques (par date)

````

---

## ✅ Prérequis

- Linux (Debian/Ubuntu)
- `bash`
- Connexion Internet
- YouTube accessible

---

## ⚙️ Installation

1. Clone le dépôt ou copie les fichiers dans un dossier local.
2. Rends le script exécutable :
   ```bash
   chmod +x install.sh```

3. Lance l'installation :

   ```bash
   ./INSTALL.sh
   ```
4. Active l’environnement virtuel :

   ```bash
   source ./venv/bin/activate
   ```

---

## 📝 Utilisation

1. Ouvre le fichier `music_list.txt` et insère un titre de musique **par ligne** :

   ```
   One More Time
   Lose Yourself
   Time
   ```

2. Lance le script :

   ```bash
   python download_mp3.py
   ```

3. Les fichiers `.mp3` seront disponibles dans le dossier `output/YYYY-MM-DD/`.

---

## 📦 Dépendances

* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
* [`ffmpeg`](https://ffmpeg.org/)

Ces dépendances sont automatiquement installées par le script `INSTALL.sh`.

---


## 👨‍💻 Auteur

**6sco** — professionnel en cybersécurité et automatisation.


