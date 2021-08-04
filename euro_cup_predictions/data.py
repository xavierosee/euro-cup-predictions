import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from euro_cup_predictions.params import EA_COUNTRY_CODES


def import_from_ea():
    """Grab individual player ranking from the Electronic Arts Fifa21 database

    Returns:
        pd.Dataframe: Raw DataFrame of player grades for players whose nationality country is engaged in the Euro 2020
    """

    url = "https://ratings-api.ea.com/v2/entities/fifa-21?filter=&sort=ranking:ASC&limit=1000&offset=0"
    response = requests.get(url).json()
    all_players = pd.json_normalize(response["docs"])
    fifa_euro_players = all_players[
        all_players["nationality"].isin(list(EA_COUNTRY_CODES.keys()))
    ].copy()

    return fifa_euro_players


def import_from_uefa():
    """Grab individual player ranking from the UEFA.com Database

    Returns:
        pd.DataFrame: raw Datagrame of player rankings for players whose nationality country is engaged in the Euro 2020
    """

    url = "https://performancezone.uefa.com/api/v3/rankings?competitionId=NTC&languageSet=EN&offset=0&seasonYear=current&statisticSet=FIELD_POSITION_SET&limit=1000"
    response = requests.get(url).json()
    uefa_players = pd.json_normalize(response["data"])
    uefa_euro_players = uefa_players[
        uefa_players["player.team.shortNames.EN"].isin(list(EA_COUNTRY_CODES.values()))
    ].copy()

    return uefa_euro_players


def import_from_fifa():
    """Grab official country rankings from FIFA.com for all countries involved in Euro 2020

    Returns:
        pd.DataFrame: DataFrame of shape (24,4) with all the countries involved in Euro 2020 and their official FIFA Rankings and scores.
    """

    url = "https://www.fifa.com/fifa-world-ranking/ranking-table/men/#UEFA"

    response = requests.get(url)
    soup = bs(response.content, "html.parser")

    teams = soup.find_all("tr", attrs={"data-team-id": True})

    fifa_rankings = []

    for team in teams:
        rank = team.td.span.text
        country = team.select_one(".fi-t__nText").text
        country_short = team.select_one(".fi-t__nTri").text
        score = float(team.select_one(".fi-table__points").span.text)
        fifa_rankings.append(
            {
                "rank": rank,
                "country": country,
                "country_shortcode": country_short,
                "score": score,
            }
        )

    return pd.DataFrame(fifa_rankings)
