"""
returns track links from playlist
"""
import re
import requests
def get_track_links(playlist_url:str) -> list[str]:
    """
    Retrieves track links from a Spotify playlist URL.

    Args:
        playlist_url (str): The URL of the Spotify playlist.

    Returns:
        list[str]: A list of track links extracted from the playlist.

    Examples:
        >>> playlist_url = "https://open.spotify.com/playlist/abc123"
        >>> get_track_links(playlist_url)
        ['https://open.spotify.com/track/02xwA3Ej9NPetftp9V7VZ3', ...]
    """
    playlist_content = requests.get(playlist_url)
    playlist_html_raw = playlist_content.text
    base_url = "https://open.spotify.com/track/"
    track_codes_zeroth_indexs = [m.start() for m in re.finditer(base_url, playlist_html_raw)]
    url_length = len("https://open.spotify.com/track/02xwA3Ej9NPetftp9V7VZ3")
    return [
        playlist_html_raw[zeroth_idx : zeroth_idx + url_length]
        for zeroth_idx in track_codes_zeroth_indexs
    ]
