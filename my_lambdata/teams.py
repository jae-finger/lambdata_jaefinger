# example teams.py (Object-Oriented-Programming inheritance approach)

class Team():
    def __init__(self, name, city):
        self.name = name
        self.city = city

if __name__ == "__main__":
    # teams = [
    #     {"city": "New York", "name": "Yankees", "pitcher": "John"},
    #     {"city": "New York", "name": "Mets", "pitcher": "Jane"},
    #     {"city": "Boston", "name": "Red Sox",  "pitcher": "Ames"},
    #     {"city": "New Haven", "name": "Ravens",  "pitcher": "Vishal"},
    #     {"city": "Washington", "name": "Nationals",  "pitcher": "Cody"}
    # ]
    # for team in teams:
    #     print("-------")
    #     #print(full_name(team))
        #advertise(team)
    team = Team(city="Washington", name="Wizards") #initialize / create an instance of the object
    print(team)
    print(type(team))
    print(team.name) #invoking attributes
    print(team.city) #invoking attributes

    team2 = Team("Cubs", "Chicago") #initialize / create an instance of the object
    print(team2)
    print(type(team2))
    print(team2.name) #invoking attributes
    print(team2.city) #invoking attributes


    # df1 = DataFrame({"x": [1,2,3], "y": [4,5,6]})
    # df1.head()
    # df1.columns
    # df2 = DataFrame({"x": [7,7,7], "y": [4,4,4]})
    # df2.head()
    #team = Team(city="Washington", name="Wizards") # initialize / create an instance of the object
    #print(team)
    #print(type(team))
    #print(team.name) # invoking attributes
    #print(team.city) # invoking attributes
#
    #team2 = Team("Giants", "New York") # initialize / create an instance of the object
    #print(team2)
    #print(type(team2))
    #print(team2.name) # invoking attributes
    #print(team2.city) # invoking attributes