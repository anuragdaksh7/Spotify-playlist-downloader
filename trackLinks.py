import requests
import re
def getTrackLinks(playlistURL:str)->list[str]:
    playlistContent = requests.get(playlistURL)
    playlistHTML_RAW = playlistContent.text
    baseURL = "https://open.spotify.com/track/"
    trackCodesZerothIndexs = [m.start() for m in re.finditer(baseURL, playlistHTML_RAW)]
    urlLength = len("https://open.spotify.com/track/02xwA3Ej9NPetftp9V7VZ3")
    trackLinks = []
    for zerothIdx in trackCodesZerothIndexs:
        trackLinks.append(playlistHTML_RAW[zerothIdx:zerothIdx+urlLength])
    return trackLinks