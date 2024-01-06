"""
download video from a spotify playlist
"""
from track_links import get_track_links
from track_names import get_names_from_track
from youtube_links import get_yt_links_from_track_names
from YTdownloader import download_video

if __name__ == '__main__':
    playListLink = input("paste sportify playlist link: ")
    tracks = get_track_links(playListLink)
    songs = get_names_from_track(tracks)
    ytLinks = get_yt_links_from_track_names(songs)
    for song, ytLink in zip(songs,ytLinks):
        print("Downloading ",song,"...")
        download_video(ytLink)
