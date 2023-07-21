import json

def LoadGoogleEvent():
    with open('./Events/Google.json') as f:
        google = json.load(f)
    return google["allEvents"]

def loadH2SEvets():
    with open('./Events/H2S.json') as f:
        H2s = json.load(f)
    return H2s["allEvents"]

