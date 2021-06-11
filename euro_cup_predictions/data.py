import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from euro_cup_predictions.params import EA_COUNTRY_CODES


def import_from_ea():
    """Grab individual player ranking from the Electronic Arts Fifa21 database

    Returns:
        pd.Dataframe: Raw DataFrame of player grades for players whose nationanity country is engaged in the Euro 2020
    """
    url = "https://ratings-api.ea.com/v2/entities/fifa-21?filter=&sort=ranking:ASC&limit=1000&offset=0"
    response = requests.get(url).json()
    all_players = pd.json_normalize(response["docs"])
    fifa_euro_players = all_players[
        all_players["nationality"].isin(list(EA_COUNTRY_CODES.keys()))
    ].copy()
    return fifa_euro_players
