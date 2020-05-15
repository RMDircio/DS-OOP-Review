'''Player class to record stats for individual players
'''


class Player:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay

    Class to represent a player on a American football team.

    ...

        Attributes:
        ----------
        name : string
            First name of the player

        yards : integer
            Number of yards the player has completed

        touchdowns : integer
            Number of touchdowns the player has completed
            
        safety : integer
            Number of times safety call has been issued to player

        interceptions : integer
            Number of interceptions of the football the player has completed

        field_goals : integer
            Number of field goals the player has completed
        
        Methods:
        -------
        get_points 
            Gathers points player completed via stats
    '''
    def __init__(self,
                name=None,
                yards=120, 
                touchdowns=5, 
                safety=1,
                interceptions=0, 
                field_goals=3
                ):
        '''
        Creates attributes for player object

            Parameters:
            ----------
            name : string
                First name of the player

            yards : integer (default: 120)
                Number of yards the player has completed

            touchdowns : integer (default: 5)
                Number of touchdowns the player has completed
            
            safety : integer (default: 1)
                Number of times safety call has been issued to player

            interceptions : integer (default: 0)
                Number of interceptions of the football the player has completed

            field_goals : integer (default: 3)
                Number of field goals the player has completed

        '''
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
                
                td_points : integer (default: 6)
                    Touchdown points player completed multipled by the default
                
                saftey_points : integer (default: 2)
                    Safety points issued to player multiplied by the default
                
                total_points : interger
                    Sum of td_points and saftey_points
            
            Returns:
            -------
                total_points : interger
                    Sum of td_points and saftey_points
        '''

        td_points = 6 * self.stats['td']
        safety_points = 2 * self.stats['safety']
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks

    Subclass to Player

    Attributes:
    ----------
        name : string
            First name of the quaterback

        yards : integer (default: 130)
            Number of yards the quaterback has completed

        touchdowns : integer (default: 5)
            Number of touchdowns the quaterback has completed
            
        safety : integer
            Number of times safety call has been issued to quaterback

        interceptions : integer (default: 4)
            Number of interceptions of the football the quaterback has completed

        field_goals : integer
            Number of field goals the quaterback has completed
        
        completed_passes : integer (default: 20)
            Number of passes of the football the quaterback has completed

    Methods:
    -------
        passing_score
            A randomized formula

    '''
    def __init__(self,
                name=None,
                yards=130,
                touchdowns=5,
                completed_passes=20,
                interceptions=4,
                safety=None,
                field_goals=None
                ):
        '''
        Creates attributes for the Quarterback subclass
        
            Parameters:
            ----------
                name : string
                    First name of the quaterback

                yards : integer (default: 130)
                    Number of yards the quaterback has completed

                touchdowns : integer (default: 5)
                    Number of touchdowns the quaterback has completed
            
                safety : integer
                    Number of times safety call has been issued to quaterback

                interceptions : integer (default: 4)
                    Number of interceptions of the football the quaterback has completed

                field_goals : integer
                    Number of field goals the quaterback has completed
        
                completed_passes : integer (default: 20)
                    Number of passes of the football the quaterback has completed


        '''

        super().__init__(name=name,
                        yards=yards,
                        touchdowns=touchdowns,
                        safety=safety,
                        interceptions=interceptions
                        )
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI

        score : integer 
            Number attained by Quaterback completed_passes minus the 
            product of the Quaterback interceptions times 2
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.

class Defense(Player):


    def __init__(self,
                name=None,
                yards=220,
                touchdowns=0,
                safety=1,
                interceptions=2, 
                field_goals=0,
                tackles=5,
                sacks=3
                ):
        super().__init__(name=name,
                        yards=yards,
                        touchdowns=touchdowns,
                        safety=safety,
                        interceptions=interceptions,
                        field_goals=field_goals)
        
        self.tackles = tackles
        self.sacks = sacks
    
    def defense_play(self):
        total = self.interceptions + self.tackles + self.sacks
        return total


