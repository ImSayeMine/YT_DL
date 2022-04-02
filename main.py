from os import system as sys 
from pytube import YouTube 

sys('clear'and'cls')
url = input("Please enter a link: ")
video = YouTube(url)

print("Title: ", video.title)
print("views: ", video.views)
print("lenght: ", video.length, "s")
print("Description: ", video.description)
print("Ratings: ", video.rating)

video_stream = video.streams.get_highest_resolution()

print("download started ...")
video_stream.download()

print("download completed")