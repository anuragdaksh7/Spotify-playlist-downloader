"""
returns yt links
"""
import requests
BASE_URL = "https://www.youtube.com/results?search_query="


def get_yt_links_from_track_names(track_names: list[str]) -> list[str]:
    """
    Retrieves YouTube links for a list of track names.

    Args:
        track_names (list[str]): A list of track names.

    Returns:
        list[str]: A list of YouTube links corresponding to the track names.

    Examples:
        >>> track_names = ["song 1", "song 2", "song 3"]
        >>> get_yt_links_from_track_names(track_names)
        ['youtu.be/link1', 'youtu.be/link2', 'youtu.be/link3']
    """
    yt_links = []
    approx_link_length = 20
    for track_name in track_names:
        raw_page_data = requests.get(BASE_URL+"%20".join(track_name.split(" ")))
        raw_html = raw_page_data.text
        flag = len('videoId": ')
        link_loc = raw_html.find('videoId')
        print(
            (
                f"{track_name} youtu.be/"
                + raw_html[
                    link_loc + flag : link_loc + flag + approx_link_length
                ].split('"')[0]
            )
        )
        yt_links.append("youtu.be/"+
                        raw_html[link_loc+flag:link_loc+flag+approx_link_length].split('"')[0])
    return yt_links

