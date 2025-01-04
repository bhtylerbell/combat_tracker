class Player:
        
    def __init__(self, name, role, max_hp, armor_class, initiative):
        self.name = name                #
        self.role = role                #
        self.maxhp = max_hp             #
        self.ac = armor_class           #
        self.initiative = initiative    # 
        death_sucesses = 0              # Number of death sucesses, if player HP < 0 default value is 0
        death_failures = 0              # Number of death failures, if player HP < 0 default value is 0
        condition = ""                  # Players condition if any (blinded, confused, etc)
        alive = 1                       # 1 == Alive, 0 == Dead, if HP < 0 AND death failures != 3 can't be dead
        
        