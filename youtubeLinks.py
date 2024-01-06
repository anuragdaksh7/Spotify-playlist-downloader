import requests
BASE_URL = "https://www.youtube.com/results?search_query="
def getYTlinksFromTrackNames(TrackNames: list[str])->list[str]:
    YTlinks = []
    for trackName in TrackNames:
        RAW_PAGE_DATA = requests.get(BASE_URL+"%20".join(trackName.split(" ")))
        RAW_HTML = RAW_PAGE_DATA.text
        flag = len('videoId": ')
        linkLoc = RAW_HTML.find(flag)
        approxLinkLength = 20
        print(trackName+" youtu.be/"+RAW_HTML[linkLoc+flag:linkLoc+flag+approxLinkLength].split('"')[0])
        YTlinks.append("youtu.be/"+RAW_HTML[linkLoc+flag:linkLoc+flag+approxLinkLength].split('"')[0])
        
