"""
download videos from yt url
"""
from pytube import YouTube


def download_video(url: str, output_path="."):
    """
    Downloads a video from the given URL and saves it to the specified output path.

    Args:
        url (str): The URL of the video to download.
        output_path (str, optional):
            The path where the downloaded video will be saved. Defaults to the current directory.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the download process.

    Examples:
        >>> url = "https://www.youtube.com/watch?v=abc123"
        >>> download_video(url, output_path="/path/to/save/video")
        Download completed.
    """
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()

        video_stream.download(output_path)
        print("Download completed.")
    except Exception as e:
        print(f"Error: {e}")
