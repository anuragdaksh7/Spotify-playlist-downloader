import requests

def getNamesFromTrack(trackLinks: list[str])->list[str]:
    trackNames = []
    for trackLink in trackLinks:
        RAW_HTML_DATA = requests.get(trackLink)
        HTML_CONTENT = RAW_HTML_DATA.text
        nameLocation = HTML_CONTENT.find("<title>")
        nameOffset = 7
        nameSize = 50
        trackName = HTML_CONTENT[nameLocation+nameOffset:nameLocation+nameOffset+nameSize].split("-")[0]
        if trackName!="Too Many Requests</title>\n</head>\n<body>\n<h1>429</":
            trackNames.append(trackName)
            print("Track Fetched: ",trackName,end="\n\n")

    print("All Track Fetched")
    return trackNames

