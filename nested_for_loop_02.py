teams = ["India", "Australia", "Sri_Lanka", "New_Zealand", "South_Africa"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " Vs " + away_team)