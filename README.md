# SR_Eng_Prompt
My submission to the Engineering Internship Prompt for Sports Reference 2024 Summer Internship

**Note:** I'm very comfortable coding in python, hence the submission is a python script.

**General Outiline of the Code:**
1. To read the json file, I use the json package in python (lines 6-7) -- assuming json filename is "data.json"
2. The data in the json file is returned as a dictionary, with team names as the key
3. I'm keeping a list 'team_names', to keep track of the teams (line 9), which will be useful for adding headers to the table (line 29, 36)
4. "matrix" holds all the data of the head to head records
5. Iterating through the keys of the json data (which is the team_1 name), I get the dictionary of the W/L record against other teams
6. Keeping a list, 'scores' to store the head to head records of the team against other teams (line 12)
7. I am appending only the records under the Win column to the list 'scores' (line 22)
8. When team_1 == team_2, I'm appending a hyphen to the list (line 24)
9. Converting the data to a pandas dataframe, and printing the data on the terminal screen, without any UI/colors (lines 30-31)
10. Showing the same data on a table (with color) using matplotlib (lines 34 - 37)
11. Can see the results of 10 and 11 in the png file named "Table - Terminal and UI.png"

**Explanation for Adding "-" using index:**
I'm iterating through the names of the team twice, (loop inside a loop), with team_1 being the row and team_2 representing the column of the table. The dictionary stored under the 'team_1' key does not contain the same team, as record does not exist for head to head. Hence, by using the indices of the two teams from list 'team_names', we can append a hyphen to the list 'scores'. When 'team_2' index is one less than index of 'team_1', appending a hyphen will add a hyphen for the head to head record for 'team_1' vs 'team_1'


**Explanation for Adding only Win records:**
By noticing the table provided, we can see that the head to head record, when read horizontally (reading left to right for a particular row), only stores the win record of the team in the row heading. When read vertically, the cell stores the loss record of the team in the column heading. Since, I'm using a list of list type representation, I'm reading data from the json file horizontally, and also storing it in the same manner. Hence, only storing the win records.

  
