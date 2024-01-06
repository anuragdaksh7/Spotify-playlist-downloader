from trackLinks import getTrackLinks
from trackNames import getNamesFromTrack
from youtubeLinks import getYTlinksFromTrackNames
from YTdownloader import download_video

if __name__ == '__main__':
    playListLink = input("paste sportify playlist link: ")
    tracks = getTrackLinks(playListLink)
    songs = getNamesFromTrack(tracks)
    ytLinks = getYTlinksFromTrackNames(songs)
    for song, ytLink in zip(songs,ytLinks):
        print("Downloading ",song,"...")
        download_video(ytLink)
        
