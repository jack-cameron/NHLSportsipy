from sportsipy.nhl.boxscore import Boxscore
from sportsipy.nhl.teams import Teams
from sportsipy.nhl.schedule import Schedule

from geopy.geocoders import Nominatim
from geopy import distance

import pandas as pd

currrent_teams = ['ANA', 'ARI', 'BOS', 'BUF', 'CGY', 'CAR', 'CHI', 'COL', 'CBJ', 'DAL', 'DET', 'EDM', 'FLA', 'LAK', 'MIN', 'MTL', 'NSH', 'NJD', 'NYI', 'NYR', 'OTT', 'PHI', 'PIT', 'SJS', 'SEA', 'STL', 'TBL', 'TOR', 'VAN', 'VEG', 'WSH', 'WPG']

def kms_travelled(abrv, year):
    distance_travelled = 0
    team_schedule = Schedule(abrv, year)
    current_coordinates = (0, 0)
    count = 0
    for game in team_schedule:
        #set current coordinates for first game
        if count == 0:
            game_data = Boxscore(game.date[0:4] + game.date[5:7] + game.date[8:10] + "0"+ abrv)
            if(game_data.duration):
                arena = game_data.arena
                if(arena == "Madison Square Garden (IV)"):
                    arena = "Madison Square Garden"
                if(arena == "BB&T Center"):
                    arena = "FLA Live Arena"
                if(arena == "Bell Centre"):
                    arena = "Centre Bell"
                geolocator = Nominatim(user_agent="jack")
                location = geolocator.geocode(arena)
                current_coordinates = (location.latitude, location.longitude)
            else:
                home_team = game._opponent_abbr
                game_data = Boxscore(game.date[0:4] + game.date[5:7] + game.date[8:10] + "0"+ home_team)
                arena = game_data.arena
                if(arena == "Madison Square Garden (IV)"):
                    arena = "Madison Square Garden"
                if(arena == "BB&T Center"):
                    arena = "FLA Live Arena"
                if(arena == "Bell Centre"):
                    arena = "Centre Bell"
                if(arena == "Tim Horton's Field"):
                    arena = "Tim Hortons Field"
            #   print(arena)
                geolocator = Nominatim(user_agent="jack")
                location = geolocator.geocode(arena)
                #address = location.address
                current_coordinates = (location.latitude, location.longitude)
        game_data = Boxscore(game.date[0:4] + game.date[5:7] + game.date[8:10] + "0"+ abrv)
        if(game_data.duration):
            arena = game_data.arena
            if(arena == "Madison Square Garden (IV)"):
                arena = "Madison Square Garden"
            if(arena == "BB&T Center"):
                arena = "FLA Live Arena"
            if(arena == "Bell Centre"):
                arena = "Centre Bell"
            geolocator = Nominatim(user_agent="jack")
            location = geolocator.geocode(arena)
            destination_coordinates = (location.latitude, location.longitude)
            distance_travelled += float(distance.distance(current_coordinates, destination_coordinates).km)
            print(distance_travelled)
            current_coordinates = destination_coordinates
        else:
            home_team = game._opponent_abbr
            game_data = Boxscore(game.date[0:4] + game.date[5:7] + game.date[8:10] + "0"+ home_team)
            arena = game_data.arena
            if(arena == "Madison Square Garden (IV)"):
                arena = "Madison Square Garden"
            if(arena == "BB&T Center"):
                arena = "FLA Live Arena"
            if(arena == "Bell Centre"):
                arena = "Centre Bell"
            if(arena == "Tim Horton's Field"):
                arena = "Tim Hortons Field"
            #print(arena)
            geolocator = Nominatim(user_agent="jack")
            location = geolocator.geocode(arena)
            address = location.address
            destination_coordinates = (location.latitude, location.longitude)
            distance_travelled += float(distance.distance(current_coordinates, destination_coordinates).km)
            print(distance_travelled)
            current_coordinates = destination_coordinates
        count += 1

    print(abrv + "'s total distance travelled: " + str("%.2f" % distance_travelled))


#print(distance.distance(san_jose, toronto).km)
def all_teams_kms_travelled(year):
    kms_data = {}
    for team in currrent_teams:
        total_kms = kms_travelled(team, year)
        kms_data[team] = total_kms