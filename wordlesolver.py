import re
import random

class candidates():
    """
    path : string
    Path to the textfile with the possible wordle-words.

    File has to contain one word per line.
    
    The class generates a list with all the possible words.

    Depending on the methods, the list gets filtered more and more with every method, used on one certain candidates-object.

    To show the list of possible word-candidates in this object call the objects list:
    wordlesolver.candidates.list
    """

    def __init__(self, path="5-letter-words.txt"):
        with open(path) as file:
            words = file.readlines()
            words = [word.rstrip("\n") for word in words]
        self.list = words
        
    def candidate(self):
        """
        Prints a random word from the word-list of the candidates-object.
        """
        print(random.choice(self.list))

    def nope(self, string, candidate=False, inplace=False):
        """
        Excludes all words containing characters in 'string'.

        string : string
          All characters that are not in the searched word. Example: "acg"

        candidate : bool, default False
          If True, prints a new possible candidate from the new word list.

        inplace : bool, default False
          If True, change in-place.

        Treates lowercase as uppercase.

        Returns:
          candidates-object or None
        """      
        filtered_list = [word for word in self.list if re.search(f"[{string.upper()}]", word) == None]
        self.list = filtered_list
        if candidate:
            self.candidate()
        if not inplace:
            return self

    def somewhere(self, *args, candidate=False, inplace=False):
        """
        Keeps all words, containing the characters, but exludes words with the characters on given position.

        arg : string
          specify contained character and his false position together in a string like this: 
          "A2" = word contains letter A, but not on position 2.
          For more characters or one character on several wrong positions just list all hints as follows:
          wordlesolver.candidates.somewhere("A2", "A5", "G3")

        candidate : bool, default False
          If True, prints a new possible candidate from the new word list.

        inplace : bool, default False
          If True, change in-place.

        Treates lowercase as uppercase.

        Returns:
          candidates-object or None
        """
        for arg in args:
            filtered_list = [word for word in self.list if arg[0].upper() in word]
            filtered_list = [word for word in filtered_list if word[int(arg[1])-1] != arg[0].upper()]
            self.list = filtered_list
        if candidate:
            self.candidate()
        if not inplace:
            return self

    def nailedit(self, *args, candidate=False, inplace=False):
        """
        Keeps all words, containing certain characters at certain positions.

        arg : string
          specify contained character and his position together in a string like this: 
          "A2" = word contains letter A, but not on position 2.
          For more characters or one character on several position just list all hints as follows:
          wordlesolver.candidates.somewhere("A2", "A5", "G3")

        candidate : bool, default False
          If True, prints a new possible candidate from the new word list.

        inplace : bool, default False
          If True, change in-place.

        Treates lowercase as uppercase.

        Returns:
          candidates-object or None
        """
        for arg in args:
            filtered_list = [word for word in self.list if word[int(arg[1])-1] == arg[0].upper()]
            self.list = filtered_list
        if candidate:
            self.candidate()
        if not inplace:
            return self
