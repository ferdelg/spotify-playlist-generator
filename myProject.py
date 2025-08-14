# File: myProject.py
# Purpose: A program that gives users information on their favorite and least favorite popular artists, 
# favorite popular song, and a playlist based on their popular artist interests.
# Author: Maria Fernanda del Granado
#
# Colaboration statement:
# -Went to prefect sesssions for help.
# -Went to office hours for help.
# -Maria Jose del Granado: consulted on how to use functions of a class within that same class and how to make f strings.

import random
class ArtistLib:
    def __init__(self, artistfile, songfile): 
        self.artistfile = artistfile
        self.songfile = songfile
        self.artistNames = []                #list of artist names 
        self.artistNamesOfSongs = ['Artist'] #list of artists of songs
        self.songs = ['Song']                #list of songs
        self.artistObjects = []              #list of artist objects
        self.songObjects = []                #list of song objects
    
    def makeArtists(self): 
        """
    Given the artists.csv file, function makes a list of all the artist names and a list of artist objects for every artist.
        """
        #parses through file, creates list of artist names and artist objects
        with open(self.artistfile, 'r') as f:
            for line in f:
                vals = line.strip().split(',') 
                self.artistNames.append(vals[0])
                artistObj = Artist(vals[0])
                self.artistObjects.append(artistObj)

    def makeSongs(self): 
        """
    Given the songs.csv file, function makes a list of all the song names, a list of the names of the artists of those songs
    and a list of song objects for every song. 
        """
        #parses through file
        with open(self.songfile, 'r') as f:
            for line in f:
                vals = line.strip().split(',') 
                if vals[0] != 'Artist and Title':
                    SongDashArtist = vals[0]
                    songsAndArtists = SongDashArtist.split(" - ")

                    #splits artist and title from csv, appends artist to list and corresponding song to another list
                    song, artist = songsAndArtists[-1], songsAndArtists[0]
                    self.artistNamesOfSongs.append(artist)
                    self.songs.append(song)

                    #creating songs objects
                    songObj = Song(songsAndArtists[-1], songsAndArtists[0])
                    self.songObjects.append(songObj)
        
    def askUser(self): 
        """
    Asks the user for their favorite artist, least favorite artist, favorite song
    second favorite artist and other artists they are interested in.

    Returns: 
        tuple containing:
         -favArtist: string
         -leastFavArtist: string
         -favRanking: an int
         -leastFavArtistRank: an int
         -favArtistString: string
         -favSong: string
         -secondFavArtist: string 
         -artistInterests: string
        """
        #asking users for input

        favArtist = ''
        favArtistTries = 0

        #while loop that asks the user up to five times about their favorite artist (if they input somone not in csv list or with lowercase)
        while(((favArtist == '') or (favArtist not in self.artistNames)) and (favArtistTries <= 4)):
            favArtist = input("Who is your favorite popular artist? ")
            if ((favArtist == '') or (favArtist not in self.artistNames)) and (favArtistTries <= 4):
                print('You need to give me a popular artist (make sure you spell the name right and capatalization is correct)!')
                favArtistTries += 1
        

        leastFavArtist = ''
        leastFavArtistTries = 0
        #while loop that asks the user up to five times about their least favorite artist (if they input somone not in csv list or with lowercase)
        while(((leastFavArtist == '') or (leastFavArtist not in self.artistNames)) and (leastFavArtistTries <= 4)):
            leastFavArtist = (input("Who is your least favorite popular artist? "))
            if ((leastFavArtist == '') or (leastFavArtist not in self.artistNames)) and (leastFavArtistTries <= 4):
                print('You need to give me a popular artist (make sure you spell the name right and capatalization is correct)!')
                leastFavArtistTries += 1

        favSong = input("What is your favorite popular song? ")
        secondFavArtist = input("Who is your second favorite popular artist? ")

        print("For the next question: give a list of full artist names separated by commas.")
        artistInterests = input("What are some other popular artists you are interested in? ")

        favArtistString, favRanking  = self.getFavArtistRank(favArtist)
        leastFavArtistRank = self.getLeastFavArtistRank(leastFavArtist)

        if favRanking == None:
            print(favArtistString)
        return favArtist, leastFavArtist, favRanking, leastFavArtistRank, favArtistString, favSong, secondFavArtist, artistInterests
    
                       
    def artistRanks(self):
        """
    For every artist in the list of artist objects (self.artistObjects) it
    uses the Artist class .addRank function to add the corresponding rank 
    to each artist object.
        """
        #adding artist ranking to each artist object
        for artist in self.artistObjects:
            rank = self.artistNames.index(artist.getName())
            artist.addRank(rank)

    def getFavArtistRank(self, favArtist): 
        """
    Given an artist's name (that is in artists.csv), function returns a string containing a message
    about their ranking and a value representing the artist's ranking
    Param:
        favArtist: string representing name of fave artist
    Returns:
        tuple with f string and value representing the ranking
    """
        #checks if user fav artist is in list of artist names from csv
        # and gets their rank
        if favArtist in self.artistNames:
            for artist in self.artistObjects:
                if favArtist == artist.getName():
                    favArtistRank = artist.getRank()  

        #creating f strings with result that will later be printed out to user and 
            favArtistRanked = f"{favArtist} is ranked #{str(favArtistRank)} on the list of most streamed artists on spotify of all time!"
            return favArtistRanked, favArtistRank
        else:
            favArtistRanked = f"Sorry, it seems like {favArtist} is not in the list of most streamed artists on spotify. :("
            return favArtistRanked, None
        
    def getLeastFavArtistRank(self, leastFavArtist): 
        """
    Given an artist's name (that is in artists.csv), function returns a value representing the artist's ranking.
    Param:
        leastFavArtist: string representing name of favorite artist
    Returns:
        an int (value representing the ranking)
        """
        #checks that the least fav artist is in the list of artist names from csv and gets rank
        if leastFavArtist in self.artistNamesOfSongs:

            for artist in self.artistObjects:
                if leastFavArtist == artist.getName():
                    leastFavArtistRank = artist.getRank()  
                    return leastFavArtistRank
                
    def compareArtists(self, favArtist, leastFavArtist, favArtistRank, leastFavArtistRank): 
        """
    Given two artist's names (that are in artists.csv), function returns a string comparing the artists rankings.
    Param:
        -favArtist: string representing name of favorite artist
        -leastFavArtist: string representing name of least favorite artist
        -favArtistRank: an int (value representing the ranking of that artist)
        -leastFavArtistRank: an int (value representing the ranking of that artist)
    Returns:
        an f string or an empty string
        """
        #checks that both fav and least fav artist are in the list of artist names from csv

        #makes f string of comparison if fav artist is ranked higher than least fav
        if favArtist in self.artistNames and leastFavArtist in self.artistNames:
            if favArtistRank < leastFavArtistRank:

                rankAbove = leastFavArtistRank - favArtistRank
                comparison = f"{favArtist} is ranked {rankAbove} spots above {leastFavArtist}!"
                return comparison 
            
        #makes f string of comparison if fav artist is ranked lower than least fav
            elif favArtistRank > leastFavArtistRank: 

                rankBelow = favArtistRank - leastFavArtistRank
                comparison = f"{favArtist} is ranked {rankBelow} spots below {leastFavArtist} :("
                return comparison
        else:
            return ""

    def topSongs(self, favArtist): 
        """
    Given an artist name (that is in artists.csv), function returns a string that says the amount of songs
    that artist has in the list of most streamed songs on spotify.
    Param:
        favArtist: string representing name of favorite artist
    Returns:
        an f string or an empty string
        """
        #if the favorite artist is in the list of artist names from csv, makes f string of how many top songs they have

        if favArtist in self.artistNames:
            numTopSongs = 0

            for i in range(len(self.artistNamesOfSongs)):
                if favArtist == self.artistNamesOfSongs[i]:
                    numTopSongs +=1
                    favArtistTopSongs = f"{favArtist} has {numTopSongs} songs in the list of most streamed songs on spotify!"

            return favArtistTopSongs
        else:
            favArtistTopSongs = f"Sorry it seems like {favArtist} has no top songs :("
            return favArtistTopSongs
        
    def checkArtistInterests(self, artistInterests):  
        """
    Given the string of other popular artists interests that the user inputs, function separates this into a list of 
    those artists.
    Param:
        artistInterests: string of artists the user is interested in separated by commas
    Returns:
        a list of strings
        """
        #grabs the user's artist interest input, splits at commas, and strips every element in the list created previously

        artistInterestsSplitted = artistInterests.strip().split(',')
        artistInterestsList = []

        if len(artistInterestsSplitted) > 1:
            for artist in artistInterestsSplitted:
                artistInterestsList.append(artist.strip()) 
            return artistInterestsList
        
        else:
            return artistInterestsList
    
    def checkSong(self, favSong): 
        """
    Given the users favorite song, function checks if the song is in the list of most streamed songs on spotify and 
    returns an f string that gives that songs ranking.
    Param:
        favSong: string 
    Returns:
        an f string
        """
        #checks if the song is in the list of song names from csv
        if favSong in self.songs:
            for i in range(len(self.songObjects)):
    
        #gets song ranking and crated f string
                if favSong == self.songObjects[i].getSong():

                    songRank = self.songObjects.index(self.songObjects[i])
                    favSongRank = f"{favSong} was ranked #{songRank + 1} in the list of most streamed songs on spotify!"
                    return favSongRank
        else:
                favSongRank = f"Sorry, it seems like your favorite popular song {favSong} is not in the list of most streamed songs on spotify :("
                return favSongRank
        
    def makeListArtists(self, favArtist, secondFavArtist, artistInterestsList):
        """
    Given the users favorite artist, second favorite artist and other artists they are interested in, function creates a list
    of all those artists.
    Param:
        -favArtist: string
        -secondFavArtist: string
        -artistInterestsList: list of strings
    Returns:
        list of strings
        """
        #appends user's fav artist and second fav artist to new list
        songArtistList = []
        songArtistList.append(favArtist)
        songArtistList.append(secondFavArtist)

        #also appends artist interests to list
        for artist in artistInterestsList:
            if artist not in songArtistList:
                artist.strip() #making sure there are no whitespaces before or after artist name
                songArtistList.append(artist)
        return songArtistList
    
    def makeListSongs(self, songArtistList):
        """
    Given the list of all artists the user is interested in, function gets the songs each artist has 
    in the list of most streamed songs on spotify and adds all those songs to a new list.
    Param:
        songArtistList: list of strings
    Returns:
        list of strings
        """
        #adds all songs in csv associated with artists user is interested in to new list (playlist)
        songsForUserPlaylist = []
        for artist in songArtistList:
            for i in range(len(self.songObjects)):
                if artist == self.songObjects[i].getArtist():
                    songsForUserPlaylist.append(self.songObjects[i].getSong())
        
        #checks that the songs in the playlist actually belong to one of the artists the user is interested in
        checkedSongsForUserPlaylist = []
        for i in range(len(self.songObjects)):
            for song in songsForUserPlaylist: 
                if song == self.songObjects[i].getSong() and self.songObjects[i].getArtist() in songArtistList: 
                    checkedSongsForUserPlaylist.append(song)

        return checkedSongsForUserPlaylist

    def getSongsInPlaylist(self, checkedSongsForUserPlaylist): 
        """
    Given the list of songs of all the artists the user is interested in, function checks if that list is 
    longer than 10, if it is then it randomly chooses 10 songs from that list and adds it to a new list, if the
    given list is not longer than 10 then it adds the songs in that list to the playlist and randomly adds the 
    missing songs from the songs in songs.csv. 
    Param:
        songsForUserPlaylist: list of strings
    Returns:
        list of strings or an empty string
        """
        #if the length of list of songs from user inputs (checkedSongsForUserPlaylist) is 
        # longer than 10, randomly appends 10 songs from that list to new list
        playlist = []
        if len(checkedSongsForUserPlaylist) > 10:
            while len(playlist) <= 9:
                randomSongFromList = random.choice(checkedSongsForUserPlaylist)

                #making sure we don't append same song twice
                if randomSongFromList not in playlist:
                    playlist.append(randomSongFromList)
            return playlist
        
        #if there is less than 10 songs in the list, appends songs from how many there is in previous list
        elif len(checkedSongsForUserPlaylist) < 10 and len(checkedSongsForUserPlaylist) >= 0:
            while len(playlist) <= 9:
                otherRandomSongs = 10 - len(checkedSongsForUserPlaylist)
                for song in checkedSongsForUserPlaylist:

                    #making sure we dont append song twice
                    if song not in playlist:
                        playlist.append(song)

                    #appends random songs for there to be 10 songs in playlist
                    for i in range(otherRandomSongs):
                        randomSong = random.choice(self.songs)
                        if randomSong not in playlist:
                            playlist.append(randomSong)
            return playlist
        
    def makeUserPlaylist(self, playlist, songArtistList):
        """
    Given the playlist list of 10 songs, function makes new list with the song and artist in each string,
    Param:
        playlist: list of strings
    Returns:
        list of strings
        """
        #for every song in the playlist created in last function, gets artist name of song 
        playlistWithSongsAndArtists = []
        for song in playlist:
            for songObj in self.songObjects:
                if song == songObj.getSong() and songObj.getArtist() in songArtistList:

                    #creates f string with song and artist, appends this to new list
                    songAndArtist = f"-'{song}' by {songObj.getArtist()}"
                    playlistWithSongsAndArtists.append(songAndArtist)

        return playlistWithSongsAndArtists

    def printResults(self): #add comments on chunks of code and number of chunks 3 or 4 
        """
    Given all the functions defined in ArtisLib class, function prints result to user. 
        """
        #user input
        favArtist,leastFavArtist, favRanking, leastFavArtistRank, favArtistString, favSong, secondFavArtist, artistInterests  = self.askUser()

        #creating rankings and comparisons
        comparison = self.compareArtists(favArtist,leastFavArtist, favRanking, leastFavArtistRank)
        favArtistTopSongs = self.topSongs(favArtist)
        favSongRank = self.checkSong(favSong)

        #creating list of artist interests, list of all artists the user is interested in,
        #list of songs, list of all songs of those artists in the csv, 
        #list of 10 randomly picked songs and final playlist list of songs and artists 
        artistInterestsList = self.checkArtistInterests(artistInterests)
        songArtistList = self.makeListArtists(favArtist, secondFavArtist, artistInterestsList)
        checkedSongsForUserPlaylist = self.makeListSongs(songArtistList)
        playlist = self.getSongsInPlaylist(checkedSongsForUserPlaylist)
        playlistWithSongsAndArtists = self.makeUserPlaylist(playlist, songArtistList)

        #printing results from comparison and rankings of artists inputed and fav song
        print("")
        print("Here are your results:")
        print(favArtistString)
        print(favArtistTopSongs)
        print(comparison)
        print(favSongRank)

        #printing generated playlist to user (by itterating through list of f strings)
        print("")
        print("Here is a playlist just for you!")
        for songAndArtist in playlistWithSongsAndArtists:
            print(songAndArtist)

    
class Artist: 
    #class made to store rank and names of every artist in artists.csv
    def __init__(self, name): 
        self.name = name
        self.rank = 0

    def getName(self):
        """
    Returns: 
        string (of artist name)
        """
        return self.name
    
    def addRank(self, rank):
        """ 
    Param:
        int (value representing rank)
        """
        self.rank += rank
    
    def getRank(self):
        """
    Returns: 
        int (of artist ranking)  
        """
        return self.rank
    
class Song: 
    #class made to store song name and artist of every song in songs.csv
    def __init__(self, songName, Artist):
        self.song = songName
        self.songartist = Artist

    def getArtist(self):
        """
    Returns: 
        string (of song artist)
        """
        return self.songartist
    
    def getSong(self):
        """
    Returns: 
        string (of song)
        """
        return self.song

if __name__ == "__main__":
    mylib = ArtistLib('artists.csv', 'songs.csv')
    mylib.makeArtists() 
    mylib.makeSongs()
    mylib.artistRanks()
    mylib.printResults()
