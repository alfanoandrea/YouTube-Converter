import subprocess
import sys
import os    
try:
    import yt_dlp
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"])
    import yt_dlp


destination = "Music/"
if not os.path.exists(destination):
    os.makedirs(destination)


def convert(link):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        }   
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"{link} has been successfully downloaded")
    except Exception as e:
        print(f"Error downloading {link}: {e}")


def music():
    try:
        with open("music-links.txt", 'r') as file:
            urls = file.readlines()
        for url in urls:
            url = url.strip()
            if url:
                convert(url)
        with open("music-links.txt", 'w') as file:
            pass
    except FileNotFoundError:
        print("The file music-links.txt was not found. Please check the file path.")


if __name__ == "__main__":
    music()
