from pytube import YouTube

link = input("provide your link which you wanna download: ")

youtube1  = YouTube(link)

print(youtube1.title)

videos = youtube1.streams.filter(progressive = True)
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Please provide your index you want to download :"))
videos[strm].download()
print("Successfully Downloaded")