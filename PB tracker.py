import sys
import pickle
import os.path
class game(object):
    
    def __init__(self, name):
        self.name = name
        self.categories = {}

def listGames():
    for i in games:
        f = str((games.index(i) + 1))
        print (f + '. ' + i.name)

def listPBs():
    p = ('')
    for i in games:
        p = p + '\n' + ('====' + i.name + '====')
        cats = list(i.categories.items())
        cats.sort()
        for k, v in cats:
            p = p + '\n{} {}'.format(k, v)
    return p

def quitProgram():
    print ('Are you sure you would like to quit? Y/N')
    while 1:
        confirm = input ('')
        if confirm.title() == ('Y'):
            sys.exit()
        else:
            break

def addGame():
    while 1:
        gamename = input ('')
        if not gamename:
            print (intro)
            return
        
        
        k = dupeCheck('1', gamename)
        if k:
            print ('You already have a game named that.')
        else:
            games.append(game(gamename))
            s = addCat(gamename)
        if s:
            print ('Game succesfully added. Continue to add more if you wish. Enter to return.')

def addCat(gamename, itself=0):
    if not games:
        return 1
    print ('Please add a category to {}. Enter to return'.format(gamename))
    while 1:
        name = input ('')
        if not name.strip():
            return 1
        for p, f in enumerate(games):
            if gamename == f.name:
                break
        k = dupeCheck('2', name, p)
        if k:
            print ('You already have a category named that.')
            return 0
        print ('What is your PB in {}?'.format(name))
        while 1:
            time = input ('')
            if not time:
                print ('I\'m sure you\'re fast, but not that fast')
            else:
                for p, f in enumerate(games):
                    if gamename == f.name:
                        break
                games[p].categories[name] = (time)
                if itself:
                    print ('PB succesfully recorded.')
                    return 0
                else:
                    return 1
            
       
        
    
    

def dupeCheck(kind, name, selgame=None):
    if kind == ('1'):
        for o in games:
            if name == o.name:
                return 1
            
    elif kind == ('2'):
        for o in games[selgame].categories.keys():
            if name == o:
                return 1


k = 0
m = 0
games = []
if os.path.isfile('PBs.p'):
    games = pickle.load( open( "PBs.p", "rb") )
intro = ('Hello and welcome to the PB tracker. Available commands:\n1. Add a new game.\n2. Add a new category to an existing game.\n3. Update an older PB.\n4. Remove a game or category\n5. View a list of PBs\nQ. Quit')

print (intro)
while 1:
    menu = input ('')

    if menu == ('1'):
        print ('You have selected 1. Please enter the name of the game. Enter to return.')
<<<<<<< HEAD
        addGame()           
=======
        addGame()
                
            
>>>>>>> FETCH_HEAD
            
                    
                
    elif menu == ('2'):
        if not games:
            print ('You have no games to add categories to')
        else:
            print ('You have selected 2. Please select a game to add the category to. Enter to return.')
            for i in games:
                f = str((games.index(i) + 1))
                print (f + '. ' + i.name)
            
            while 1:
                selgame = input('')
                if not selgame:
                    print (intro)
                    break
                
                n = int(selgame)
                if n > len(games):
                    print ('That\'s not a selectable value')
                else:
                    n -= 1
                    gamename = games[n].name
                    break
            while 1:
                Catadd = addCat(gamename, 1)
                if Catadd:
                    print (intro)
                    break       
            

                
                                        
    elif menu == ('3'):
        print ('You have selected 3. Please select a game to update. Enter to return')
        for i in games:
            f = str((games.index(i) + 1))
            print (f + '. ' + i.name)
        while 1:
            selgame = input ('')
            if not selgame:
                break
            n = int(selgame)
            if n > len(games):
                print ('That\'s not a selectable value')
            else:
                n -= 1
                gamename = games[n].name
                break
        print ('Please select a category to update')
        for t in games[n].categories.keys():
            print (t)
        while 1:
            selcat = input ('')
            if not selcat in games[n].categories.keys():
                print ('That\'s not a category.')
            else:
                break
        print ('What time did you get?')
        while 1:
            peebee = input ('')
            if not peebee:
                print ('I\'m sure you\'re fast, but not that fast')
            else:
                break
        games[n].categories[selcat] = (peebee)
        print ('PB succesfully updated\n')
        print (intro)
            
            
            
        
    elif menu == ('4'):
        print ('Would you like to remove a game, or category? 1/2. Enter to return.')
        while 1:
            deletion = input ('')
            if not deletion:
                break

            elif deletion == ('1'):
                print ('Please select a game to remove. Enter to return.')
                for i in games:
                    f = str((games.index(i) + 1))
                    print (f + '. ' + i.name)
                while 1:
                    delthing = input ('')
                    if not delthing:
                        break
                    n = int(delthing)-1
                    if n+1 > len(games):
                        print ('That is not a selectable value')
                    else:
                        print ('Are you sure you would like to delete ' + games[n].name + '? Y/N')
                        while 1:
                            confirm = input ('')
                            if confirm.title() == ('Y'):
                                del games[n]
                            break
                        break
                    break
                print (intro)
                break
            
                

        
                    
            elif deletion == ('2'):
                if not games:
                    break
                print ('Please select a game to remove from. Enter to return.')
                for i in games:
                    f = str((games.index(i) + 1))
                    print (f + '. ' + i.name)
                while 1:
                    delthing = input ('')
                    if not delthing:
                        break
                    n = int(delthing) - 1
                    if n+1 > len(games):
                        print ('That is not a selectable value')
                    else:
                        break
                print ('Please select a category to delete')
                catlist = list(games[n].categories.keys())
                for l, b in enumerate(catlist):
                    print (str(l+1) + '. ' + b)
                while 1:
                    delcat = input ('')
                    c = int(delcat)-1
                    if c+1 > len(catlist):
                        print ('That is not a selectable value')
                    else:
                        break
                print ('Are you sure you would like to delete ' + list(catlist)[c] + '? Y/N')
                while 1:
                    confirm = input ('')
                    if confirm.title() == ('Y'):
                        del games[n].categories[catlist[c]]
                        break
                    else:
                        break
                print (intro)
                break
                

            else:
                print ('That is not a selectable value')
    elif menu == ('5'):
        print (listPBs())
        print ('\n' + intro)
        
          
    elif menu.title() == ('Q'):
        pickle.dump( games, open( "PBs.p", "wb" ) )
        quitProgram()
        
    else:
        print ('That is not one of the available commands')
