import csv

# Team Names and Practice Schedules
team_names = ["Sharks", "Dragons", "Raptors"]
practice = {'Sharks':'March 17, 3PM', 'Dragons':'March 17, 1PM', 'Raptors': 'March 18, 1PM'}
 #import players and distribute players to teams based on experience
 #3 teams, so the counters cycle through 0,1,2
def get_players():
    teams = [[],[],[]]
    experienced = 0
    rookies = 0
    with open('soccer_players.csv') as playerfile:
        player_reader = csv.DictReader(playerfile, delimiter=",")
        for rows in player_reader:
            if rows['Soccer Experience'] == "YES":
                rows['team'] = team_names[experienced]
                teams[experienced].append(rows)
                if experienced != 2:
                    experienced +=1
                else:
                    experienced = 0
            else:
                rows['team'] = team_names[rookies]
                teams[rookies].append(rows)
                if rookies != 2:
                    rookies += 1
                else:
                    rookies = 0
    # Export teams data to the other functions for building team rosters and parent letters
    team_rosters(teams)
    parent_letters(teams)

# Build team roster file with only the information needed in the file, name, experience and guardian name
# List all three teams 
def team_rosters(teams):
    x = 0
    for team in teams:
        with open("teams.txt", "a") as team_file:
            team_file.write(team_names[x] + '\n')
            team_file.write("=" * 10 + '\n')
            for player in team:
                team_file.write("{}, {}, {} \n".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))
            team_file.write("\n" * 2)
        x += 1

# Build parent letter files with information needed from teams
# use practice schedule dict to fill in each teams practice schedule
def parent_letters(teams):
    for team in teams:
        for player in team:
            squad = player['team']
            new_file = "_".join(player['Name'].split()).lower()
            with open(new_file+'.txt', 'w') as file:
                file.write("Dear {}, \n\n".format(player['Guardian Name(s)']))
                file.write("Your little child, {}, is on the greatest team in the world, THE {}! \n".format(player['Name'], player['team'].upper()))
                file.write("Our first practice will be held on {}.\n\n".format(practice[squad]))
                file.write("Sincerely,\n\nYour Coach\n\n")

# Make sure it doesn't execute when imported
if __name__ == "__main__":
    get_players()
