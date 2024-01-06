from pytube import YouTube


def download_video(url, output_path="."):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()

        video_stream.download(output_path)
        print("Download completed.")
    except Exception as e:
        print(f"Error: {e}")