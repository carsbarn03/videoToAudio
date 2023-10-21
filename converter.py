import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
output_audio_file = asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
audio = video.audio

audio.write_audiofile(output_audio_file)
print("Completed")