import os
import eyed3

# Replace these with your actual values
folder_path = "path_to_your_folder"
album_name = "Your Album Name"

# Function to set album name for all MP3 files in the folder
def set_album_name_in_folder(folder_path, album_name):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            set_album_name_in_mp3(file_path, album_name)

# Function to set album name in an individual MP3 file
def set_album_name_in_mp3(file_path, album_name):
    audio_file = eyed3.load(file_path)

    if audio_file.tag is None:
        audio_file.initTag()

    audio_file.tag.album = album_name
    audio_file.tag.save()

# Call the function to set album name in all MP3 files in the folder
set_album_name_in_folder(folder_path, album_name)
