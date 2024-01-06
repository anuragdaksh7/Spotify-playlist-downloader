"""
extracts names from track links
"""
import requests

def get_names_from_track(track_links: list[str])->list[str]:
    """
    Retrieves track names from a list of track links.

    Args:
        track_links (list[str]): A list of track links.

    Returns:
        list[str]: A list of track names extracted from the track links.

    Examples:
        >>> track_links = ["https://open.spotify.com/track/abc123", ...]
        >>> get_names_from_track(track_links)
        ['Track 1', 'Track 2', ...]
    """
    track_names = []
    for track_link in track_links:
        raw_html_data = requests.get(track_link)
        html_content = raw_html_data.text
        name_location = html_content.find("<title>")
        name_offset = 7
        name_size = 50
        track_name = html_content[
            name_location+name_offset:name_location+name_offset+name_size
        ].split("-")[0]
        if track_name!="Too Many Requests</title>\n</head>\n<body>\n<h1>429</":
            track_names.append(track_name)
            print("Track Fetched: ",track_name,end="\n\n")

    print("All Track Fetched")
    return track_names
