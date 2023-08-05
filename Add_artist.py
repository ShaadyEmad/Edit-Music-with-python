import os
import eyed3

# Replace these with your actual values
folder_path = r"C:\Users\Shady Emad\Desktop\Music\cairokee"
artist_name = "Cairokee"

# Function to set the artist name for all MP3 files in the folder
def set_artist_name_in_folder(folder_path, artist_name):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            set_artist_name_in_mp3(file_path, artist_name)

# Function to set the artist name in an individual MP3 file
def set_artist_name_in_mp3(file_path, artist_name):
    audio_file = eyed3.load(file_path)

    if audio_file.tag is None:
        audio_file.initTag()

    audio_file.tag.artist = artist_name
    audio_file.tag.save()

# Call the function to set the artist name in all MP3 files in the folder
set_artist_name_in_folder(folder_path, artist_name)
