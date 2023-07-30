from data import loadH2SEvets, LoadGoogleEvent
from data import loadH2SEvets, LoadGoogleEvent


def allevent_len():
    google = LoadGoogleEvent()
    Hack2Skill = loadH2SEvets()

    all_Events = google + Hack2Skill
    all_Events_length = len(all_Events)
    return all_Events_length