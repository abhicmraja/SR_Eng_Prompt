import json
import pandas as pd
import matplotlib.pyplot as plt

matrix = []
with open("data.json", "r") as f:
    data = json.load(f)

team_names = list(data.keys())

for team_1 in data:
    scores = []
    a = team_names.index(team_1)
    if a == 0:  # the first team, hence, adding "-"
        scores.append("-")

    d = data[team_1]
    for team_2 in d:
        b = team_names.index(team_2)
        team_2 = d[team_2]
        score = team_2["W"]
        scores.append(score)
        if b == a - 1:
            # the next 'team_2' from the list 'team_names' will be 'team_1', hence adding a hyphen, since the dictionary does not contain record of the W/L of the team against itself
            scores.append("-")

    matrix.append(scores)


df = pd.DataFrame(matrix, index=team_names, columns=team_names)
print(df)
# print(df.to_string(index=False, header=False))

fig, ax = plt.subplots()
ax.set_axis_off()
tab = ax.table(cellText=matrix, rowLabels=team_names, colLabels=team_names, rowColours=["orange"]*len(team_names), colColours=["orange"]*len(team_names), cellLoc="center", loc="upper left")
plt.show()
