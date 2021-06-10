scores = {}
competitions = [['HTML','C#'],
                ['C#','Python'],
                ['Python','HTML']]
results = [0,0,1]
#0 - away team won - right team
#1 = home team won - left team
for i in range(len(competitions)):
    for j in range(len(competitions[i])):

        #Away team wins
        if results[i]==0:
            if competitions[i][1] in scores:
                scores[competitions[i][1]] += 3
                if competitions[i][0] in scores:
                    scores[competitions[i][0]] +=0
                else:
                    scores[competitions[i][0]]=0
            else:
                scores[competitions[i][1]]=3

        #Home team wins
        if results[i]==1:
            if competitions[i][0] in scores:
                scores[competitions[i][0]] +=3
                if competitions[i][1] in scores:
                    scores[competitions[i][1]] +=0
                else:
                    scores[competitions[i][1]]=0

            else:
                scores[competitions[i][0]]=3

        
max_key = max(scores, key=scores.get)
print(max_key)


#Using Functions like a pro
def tournamentWinner(competitions, results):
    # Write your code here.
	currentBestTeam = ""
	scores = {currentBestTeam:0}
	HOME_TEAM_WON = 1
	
	for idx,competition in enumerate(competitions):
		result = results[idx]
		homeTeam,awayTeam = competition
		winningTeam = homeTeam if result==HOME_TEAM_WON else awayTeam
		updateScores(winningTeam,3,scores)
		if scores[currentBestTeam] < scores[winningTeam]:
			currentBestTeam = winningTeam
	return currentBestTeam

def updateScores(team,points,scores):
	if team not in scores:
		scores[team]=0
	scores[team] +=points

