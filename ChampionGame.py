# Alisa Arnold
# December 2, 2018
# CSC 119.201
# Creating the Champion Game for final project.
#

import random
import operator

dealerHand = []
nonDealerHand = []
player,nonPlayer = "nonDealer", "dealer"
# This was an idea that my tutor helped me out with using tuples to create
# the deck.
# After some research, I found the unicode characters for the card suits here:
# https://en.wikipedia.org/wiki/Playing_cards_in_Unicode#Card_suits
# How to put them into my tuple I used this: 
# https://stackoverflow.com/questions/17069413/how-can-i-output-unicode-symbols-in-python-3-0
deck = [(face, suit)  for face in range(2,15) for suit in ['\u2660','\u2665','\u2666','\u2663']]

def deal(deck):
    
    # The idea to to print out the play_pile card like this came from here:
    # https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
    card = """\n
        ┌─────────┐
        │{}        │
        │         │
        │         │
        │    {}    │
        │         │
        │         │
        │        {}│
        └─────────┘
        """.format(face_print(play_pile), play_pile[1], face_print(play_pile))
    print('The first card in the play pile is:' + card)
    # The idea to use the .shuffle method came from here:
    # https://stackoverflow.com/questions/19306976/python-shuffling-with-a-parameter-to-get-the-same-result    
    random.shuffle(deck)
    # This portion of code sorts the cards in each player's hand from lowest to higest.
    # The idea for this came from here: 
    # https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
    for i in range(5):
        dealerHand.append(deck.pop())
        dealerHand.sort(key = operator.itemgetter(0))
        nonDealerHand.append(deck.pop())
        nonDealerHand.sort(key = operator.itemgetter(0))


# This function puts a face card on those faces that have a J,Q,K,A instead of a number.
def face_print(card):
    face_name = card[0]
    if face_name == 11:
        face_name = 'J'
    elif face_name == 12:
        face_name = 'Q'
    elif face_name == 13:
        face_name ='K'
    elif face_name == 14:
        face_name = 'A'

    return '%s' % (face_name)

# This method creates a tuple that determines if a player is able to play or not and it was an idea from my
# tutor to aid in switching back and forth between players.
# The first value in the tuple is to show if the dealer can play and the second is for the player.
def playableHands(dealerHand, nonDealerHand):
    countDealer = 0
    countNonDealer = 0
    for i in dealerHand:
        if i[0] >= play_pile[0]:
            countDealer+=1
    for i in nonDealerHand:
        if i[0] >= play_pile[0]:
            countNonDealer+=1
    return (countDealer >=1,countNonDealer >=1)

# This method runs the turn for the active player.
def do_turn(playable,active,play_pile):
    turn_player = active
    play_pile = play_pile
    playable = playableHands(dealerHand,nonDealerHand)
    counter = 0
    strNonDealerHand = []
    if turn_player == 'nonDealer':
        # The idea for this came about from a lot of research to make the cards print as a card and all on one line.
        # Some of the inspiration for this code came from here: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
        # Really struggled with this one and ended up asking a question on Stackover flow: https://stackoverflow.com/questions/53578015/need-ascii-playing-cards-to-print-on-one-line
        # After asking this question and getting some responses, I ended up modifying the code from the first link to 
        # finally get the result that I have been wanting.  
        lines = [[] for i in range(9)]
        for index, card in enumerate(nonDealerHand):
        # This adds the individual card on a line by line basis.
            if card[0] != 10:
                lines[0].append(str(index + 1) +') '+'┌─────────┐ ')
                lines[1].append('   │{}        │ '.format(face_print(card))) 
                lines[2].append('   │         │ ')
                lines[3].append('   │         │ ')
                lines[4].append('   │    {}    │ '.format(card[1]))
                lines[5].append('   │         │ ')
                lines[6].append('   │         │ ')
                lines[7].append('   │        {}│ '.format(face_print(card)))
                lines[8].append('   └─────────┘ ')
            else: 
                lines[0].append(str(index + 1) +') '+'┌─────────┐ ')
                lines[1].append('   │{}       │ '.format(face_print(card))) 
                lines[2].append('   │         │ ')
                lines[3].append('   │         │ ')
                lines[4].append('   │    {}    │ '.format(card[1]))
                lines[5].append('   │         │ ')
                lines[6].append('   │         │ ')
                lines[7].append('   │       {}│ '.format(face_print(card)))
                lines[8].append('   └─────────┘ ')
        
        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))
        
        print('The cards in your hand are:')
        for card in result:
            print(card) 
        print()       
        if playable[1]:  #This is if the player can play a card from their hand.
            print('Which card would you like to play? Pick a number between 1 and ' + str(len(nonDealerHand)) + ".")
            cardNum = int(input())-1
            card = nonDealerHand[cardNum][0]
            # This make sure that the player plays a playable card.
            while card < play_pile[0]:
                print('Your card is not greater than or equal to the card on the play pile. Please choose another card.')
                print('Your hand: ' + ', '.join(strNonDealerHand))
                print('Which card would you like to play? Pick a number between 1 and ' + str(len(nonDealerHand)) + ".")
                cardNum = int(input())-1 
                card = nonDealerHand[cardNum][0]
            if card >= play_pile[0]:
                play_pile = nonDealerHand[cardNum]
                if(play_pile[0] != 10):
                    card = """\n
            ┌─────────┐
            │{}        │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │        {}│
            └─────────┘
                        """.format(face_print(play_pile), play_pile[1], face_print(play_pile))
                else:
                    card = """\n
            ┌─────────┐
            │{}       │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │       {}│
            └─────────┘
                        """.format(face_print(play_pile), play_pile[1], face_print(play_pile)) 
                print('You have played: ' + card)
                nonDealerHand.pop(cardNum) 
                turn_player = 'dealer'              
    elif(turn_player == 'dealer'):
        if playable[0]:
            for card in dealerHand:
                #This plays the lowest playable card in the dealer's hand.
                if card[0] >= play_pile[0]:
                    play_pile = dealerHand[counter]
                    if(play_pile[0] != 10):
                        card = """\n
            ┌─────────┐
            │{}        │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │        {}│
            └─────────┘
                        """.format(face_print(play_pile), play_pile[1], face_print(play_pile))
                    else:
                        card = """\n
            ┌─────────┐
            │{}       │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │       {}│
            └─────────┘
                        """.format(face_print(play_pile), play_pile[1], face_print(play_pile))                    
                    print('The Dealer plays: ' + card)      
                    dealerHand.pop(counter) 
                    break
                else:
                    counter +=1 
        turn_player = 'nonDealer' 
    print()
    return (turn_player,play_pile)

# This method is triggered when either there are no more cards in the deck or if either player runs out of 
# cards and wins the game.
def gameOver(dealerHand, nonDealerHand, deck):
    # All of the ASCII text artwork came from here: http://http://patorjk.com/software/taag/
    if len(deck) == 0:
        print(''' 
        
 _____ _                                         _                   _                    _ 
|_   _| |                                       (_)                 | |                  | |
  | | | |__   ___    __ _  __ _ _ __ ___   ___   _ ___    __ _    __| |_ __ __ ___      _| |
  | | | '_ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \ | / __|  / _` |  / _` | '__/ _` \ \ /\ / / |
  | | | | | |  __/ | (_| | (_| | | | | | |  __/ | \__ \ | (_| | | (_| | | | (_| |\ V  V /|_|
  \_/ |_| |_|\___|  \__, |\__,_|_| |_| |_|\___| |_|___/  \__,_|  \__,_|_|  \__,_| \_/\_/ (_)
                     __/ |                                                                  
                    |___/                                                                   

        
        ''')
        print('There are no more cards in the deck.')
        return True
    # Minotaur courtesy of https://www.asciiart.eu/mythology/fantasy by Shanaka Dias
    elif len(dealerHand) == 0:
        print('''

 _______ _                _            _                   _                      _   _   _          _        _           _                       _   
 |__   __| |              | |          | |                 | |                    | | | | | |        (_)      | |         | |                     | |  
    | |  | |__   ___    __| | ___  __ _| | ___ _ __   _ __ | | __ _ _   _  ___  __| | | |_| |__   ___ _ _ __  | | __ _ ___| |_    ___ __ _ _ __ __| |  
    | |  | '_ \ / _ \  / _` |/ _ \/ _` | |/ _ \ '__| | '_ \| |/ _` | | | |/ _ \/ _` | | __| '_ \ / _ \ | '__| | |/ _` / __| __|  / __/ _` | '__/ _` |  
    | |  | | | |  __/ | (_| |  __/ (_| | |  __/ |    | |_) | | (_| | |_| |  __/ (_| | | |_| | | |  __/ | |    | | (_| \__ \ |_  | (_| (_| | | | (_| |_ 
    |_|  |_| |_|\___|  \__,_|\___|\__,_|_|\___|_|    | .__/|_|\__,_|\__, |\___|\__,_|  \__|_| |_|\___|_|_|    |_|\__,_|___/\__|  \___\__,_|_|  \__,_(_)
                                                     | |             __/ |                                                                             
                                                     |_|            |___/                                                                              


                                             ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\

               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\

               -,-..\  _  \  `  /  ,  / `._) _,-\`       \

                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \

              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\ V   V, /`     /
   ,--\(        ,     <_/`\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`        
        
                                                                                                                    _____   
 ______   _____        ____   ______   _____            _____                   ____                 _____     _____\    \  
|\     \ |     |   ____\_  \__\     \  \    \          |\    \              ____\_  \__         _____\    \   /    / |    | 
\ \     \|     |  /     /     \\    |  |    |           \\    \            /     /     \       /    / \    | /    /  /___/| 
 \ \           | /     /\      ||   |  |    |            \\    \          /     /\      |     |    |  /___/||    |__ |___|/ 
  \ \____      ||     |  |     ||    \_/   /|             \|    | ______ |     |  |     |  ____\    \ |   |||       \       
   \|___/     /||     |  |     ||\         \|              |    |/      \|     |  |     | /    /\    \|___|/|     __/ __    
       /     / ||     | /     /|| \         \__            /            ||     | /     /||    |/ \    \     |\    \  /  \   
      /_____/  /|\     \_____/ | \ \_____/\    \          /_____/\_____/||\     \_____/ ||\____\ /____/|    | \____\/    |  
      |     | / | \_____\   | /   \ |    |/___/|         |      | |    ||| \_____\   | / | |   ||    | |    | |    |____/|  
      |_____|/   \ |    |___|/     \|____|   | |         |______|/|____|/ \ |    |___|/   \|___||____|/      \|____|   | |  
                  \|____|                |___|/                            \|____|                                 |___|/   


        
        ''')
        return True
    # This Harpy is courtsey of https://www.asciiart.eu/mythology/fantasy by Joan Stark
    elif len(nonDealerHand) == 0:
        print('''

   ___     ___    _  _     ___     ___     ___    _____   _   _    _       ___    _____    ___     ___    _  _     ___      _    
  / __|   / _ \  | \| |   / __|   | _ \   /   \  |_   _| | | | |  | |     /   \  |_   _|  |_ _|   / _ \  | \| |   / __|    | |   
 | (__   | (_) | | .` |  | (_ |   |   /   | - |    | |   | |_| |  | |__   | - |    | |     | |   | (_) | | .` |   \__ \    |_|   
  \___|   \___/  |_|\_|   \___|   |_|_\   |_|_|    |_|    \___/   |____|  |_|_|    |_|    |___|   \___/  |_|\_|   |___/    (_)         
        
                            ,                                        ,
                            |\                                      /|
                        ,   \'._ ,                           ,  _.'/   ,
                        |\  {'. '-`\,      ,-._**_.-,      ,/`-' .'}  /|
                        \`'-'-.  '.`\       \*____*/      /`.'  .-'-'`/
                        ,'-'-._  '.  ) )    /`    `\     ( (  .'  _.-'-',
                        |\'- _ '.   , /     /  /""\  \     \ ,  .'  _ -'/|
                         \'-.   .  ; (      \_|^  ^|_/      ) ;   .  .-'/
                         `'--, . ;  {`-.      \__/      .-'}  ; . ,--'`
                          '--`_. ;  { ^  \   _|  |_    /  ^ }  ; ._`--'
                         `,_.--  ;  { ^  `-'`      `'-`  ^ }  ;  --._,`
                            ,_.-    ; {^    /        \    ^} ;    -._, 
                             ,_.-`), /\{^,/\\_'_/\_'_//\,^}/\ ,(`-._,
                               _.'.-` /.'   \        /   `.\ `-.'._
                            `    _.' `       \      /       ` '._   `
                                            .-'.  .'-.
                                          .'    `` ^  '.
                                         /  ^ ^   ^  ^  \

                                          | ^    ^   ^   |
                                        /^   ^/    \  ^  \

                                        \,_^_/    ^ \_,^./
                                        /=/  \^   /  \=\

                                    __ /=/_   | ^|   _\=\ __
                                <(=,'=(==,) |  | (,==)=',=)>
                                    /_/|_\    /  \    /_|\_\

                                    `V (=|  .'    '.  |=) V`
                                        V  / _/  \_ \  V
                                        `"` \  / `"`
                                                \(        


 __   __   ___    _   _          __      __ ___    _  _      _    
 \ \ / /  / _ \  | | | |         \ \    / // _ \  | \| |    | |   
  \ V /  | (_) | | |_| |          \ \/\/ /| (_) | | .` |    |_|   
   |_|    \___/   \___/            \_/\_/  \___/  |_|\_|    (_)  

        
        ''')
        return True
    else:
        return False

# This function draws the Champion Card when neither player can play.
def Champion(playable,dealerHand,nonDealerHand):
    indexDealer = 0
    indexNonDealer = 0
    strNonDealerHand = []

    lines = [[] for i in range(9)]

    for index, card in enumerate(nonDealerHand):
        # This adds the individual card on a line by line basis.
        if card[0] != 10:
            lines[0].append(str(index + 1) +') '+'┌─────────┐ ')
            lines[1].append('   │{}        │ '.format(face_print(card))) 
            lines[2].append('   │         │ ')
            lines[3].append('   │         │ ')
            lines[4].append('   │    {}    │ '.format(card[1]))
            lines[5].append('   │         │ ')
            lines[6].append('   │         │ ')
            lines[7].append('   │        {}│ '.format(face_print(card)))
            lines[8].append('   └─────────┘ ')
        else: 
            lines[0].append(str(index + 1) +') '+'┌─────────┐ ')
            lines[1].append('   │{}       │ '.format(face_print(card))) 
            lines[2].append('   │         │ ')
            lines[3].append('   │         │ ')
            lines[4].append('   │    {}    │ '.format(card[1]))
            lines[5].append('   │         │ ')
            lines[6].append('   │         │ ')
            lines[7].append('   │       {}│ '.format(face_print(card)))
            lines[8].append('   └─────────┘ ')
    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    print('The cards in your hand are:')
    for card in result:
        print(card)
    print()

    # This checks that both players cannot play, they both have 5 cards in their deck, and there are still cards remaining in the deck.
    while playable[0] == 0 and playable[1] == 0 and len(dealerHand) == 5 and len(nonDealerHand) == 5 and len(deck) > 0:

        print('''
     __     _ _   _                       _                                                 _               _ 
  /\ \ \___(_) |_| |__   ___ _ __   _ __ | | __ _ _   _  ___ _ __    ___ __ _ _ __    _ __ | | __ _ _   _  / \
 
 /  \/ / _ \ | __| '_ \ / _ \ '__| | '_ \| |/ _` | | | |/ _ \ '__|  / __/ _` | '_ \  | '_ \| |/ _` | | | |/  /
/ /\  /  __/ | |_| | | |  __/ |    | |_) | | (_| | |_| |  __/ |    | (_| (_| | | | | | |_) | | (_| | |_| /\_/ 
\_\ \/ \___|_|\__|_| |_|\___|_|    | .__/|_|\__,_|\__, |\___|_|     \___\__,_|_| |_| | .__/|_|\__,_|\__, \/   
                                   |_|            |___/                              |_|            |___/     
    ___                    _               _   _                                     ___              _   _  _ 
   /   \_ __ __ ___      _(_)_ __   __ _  | |_| |__   ___    /\  /\___ _ __ ___     / __\__ _ _ __ __| | / \/ \

  / /\ / '__/ _` \ \ /\ / / | '_ \ / _` | | __| '_ \ / _ \  / /_/ / _ \ '__/ _ \   / /  / _` | '__/ _` |/  /  /
 / /_//| | | (_| |\ V  V /| | | | | (_| | | |_| | | |  __/ / __  /  __/ | | (_) | / /__| (_| | | | (_| /\_/\_/ 
/___,' |_|  \__,_| \_/\_/ |_|_| |_|\__, |  \__|_| |_|\___| \/ /_/ \___|_|  \___/  \____/\__,_|_|  \__,_\/ \/   
                                   |___/                                                               
        
        
        ''')

        # This artwork is courtsey of https://www.asciiart.eu/mythology/fantasy by Tua Xiong
        print(''' 
                                      /|
                                     |\|
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                  ~-[{o}]-~
                                     |/|
                                     |/|
             ///~`     |\\_          `0'         =\\\\         . .
            ,  |='  ,))\_| ~-_                    _)  \      _/_/|
           / ,' ,;((((((    ~ \                  `~~~\-~-_ /~ (_/\

         /' -~/~)))))))'\_   _/'                      \_  /'  D   |
        (       (((((( ~-/ ~-/                          ~-;  /    \--_
         ~~--|   ))''    ')  `                            `~~\_    \   )
             :        (_  ~\           ,                    /~~-     ./
              \        \_   )--__  /(_/)                   |    )    )|
    ___       |_     \__/~-__    ~~   ,'      /,_;,   __--(   _/      |
  //~~\`\    /' ~~~----|     ~~~~~~~~'        \-  ((~~    __-~        |
((()   `\`\_(_     _-~~-\                      ``~~ ~~~~~~   \_      /
 )))     ~----'   /      \                                   )       )
  (         ;`~--'        :                                _-    ,;;(
            |    `\       |                             _-~    ,;;;;)
            |    /'`\     ;                          _-~          _/
           /~   /    |    )                         /;;;''  ,;;:-~
          |    /     / | /                         |;;'   ,''
          /   /     |  \\|                         |   ,;(    
        _/  /'       \  \_)                   .---__\_    \,--._______
       ( )|'         (~-_|                   (;;'  ;;;~~~/' `;;|  `;;;\

        ) `\_         |-_;;--__               ~~~----__/'    /'_______/
        `----'       (   `~--_ ~~~;;------------~~~~~ ;;;'_/'
                     `~~~~~~~~'~~~-----....___;;;____---~~
        
        
        ''')
        indexDealer = 0
        indexNonDealer = 0
        play_pile = deck.pop(0)
        if(play_pile[0] != 10):
            card = """\n
            ┌─────────┐
            │{}        │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │        {}│
            └─────────┘
            """.format(face_print(play_pile), play_pile[1], face_print(play_pile))
        else:
            card = """\n
            ┌─────────┐
            │{}       │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │       {}│
            └─────────┘
            """.format(face_print(play_pile), play_pile[1], face_print(play_pile))
        print('The Champion Card!: ' + card)
        # The idea to use the enumerate came from here:
        # https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
        for index, card in enumerate(dealerHand):
            if card[0] >= play_pile[0]:
                break
            else:
                indexDealer +=1
        for index, card in enumerate(nonDealerHand):
            if card[0] >= play_pile[0]:
                break   
            else:
                indexNonDealer +=1
        # This portion of my code is here because if my for loop went through all of the cards in a player's
        # hand, then the index would end up as 5 instead of 4 causing an out of bounds issue. 
        # Tried to work on this issue with my tutor, and he was unable to come up with a solution either.        
        if indexDealer == 5:
            indexDealer = 4
        if indexNonDealer == 5:
            indexNonDealer = 4

        if nonDealerHand[indexNonDealer][0] != 10:
            nonDealerCard = """\n
            ┌─────────┐
            │{}        │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │        {}│
            └─────────┘
            """.format(face_print(nonDealerHand[indexNonDealer]), nonDealerHand[indexNonDealer][1], face_print(nonDealerHand[indexNonDealer]))
        else: 
            nonDealerCard = """\n
            ┌─────────┐
            │{}       │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │       {}│
            └─────────┘
            """.format(face_print(nonDealerHand[indexNonDealer]), nonDealerHand[indexNonDealer][1], face_print(nonDealerHand[indexNonDealer]))
        print('The playable card in your hand is: ' + nonDealerCard)

        if dealerHand[indexDealer][0] != 10:
            dealerCard = """\n
            ┌─────────┐
            │{}        │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │        {}│
            └─────────┘""".format(face_print(dealerHand[indexDealer]), dealerHand[indexDealer][1], face_print(dealerHand[indexDealer]))
        else:
            dealerCard = """\n
            ┌─────────┐
            │{}       │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │       {}│
            └─────────┘""".format(face_print(dealerHand[indexDealer]), dealerHand[indexDealer][1], face_print(dealerHand[indexDealer]))

        print('The playable card in Dealer hand is: ' + dealerCard)

        # This determines which player gets to play from the card that is drawn for the Champion card.
        if nonDealerHand[indexNonDealer][0] >= play_pile[0] and dealerHand[indexDealer][0] < play_pile[0]: 
            print('You get to play the next card!')
            player,nonPlayer = "nonDealer", "dealer"
            break       
        elif (nonDealerHand[indexNonDealer][0] < dealerHand[indexDealer][0]) and nonDealerHand[indexNonDealer][0] >= play_pile[0]:
            print('You get to play the next card!')
            player,nonPlayer = "nonDealer", "dealer"
            break
        elif nonDealerHand[indexNonDealer][0] < play_pile[0] and dealerHand[indexDealer][0] >= play_pile[0]: 
            print('The Dealer gets to play the next card.')
            player,nonPlayer = "dealer", "nonDealer"
            break                
        elif (dealerHand[indexDealer][0] < nonDealerHand[indexNonDealer][0]) and dealerHand[indexDealer][0] >= play_pile[0]:
            print('The Dealer gets to play the next card.')
            player,nonPlayer = "dealer", "nonDealer"
            break
        # This will trigger the loop again if both of the players have the same card value.
        elif dealerHand[indexDealer][0] == nonDealerHand[indexDealer][0]:
            print('Neither player can play. Need a new Champion!')
            indexDealer = 0
            indexNonDealer = 0
        print()
        print()
    # This resets the playable variable if the loop runs again.
    playable = playableHands(dealerHand,nonDealerHand)
    # This resets the indexes for the dealer and the player.
    indexDealer = 0
    indexNonDealer = 0
    # This activates the gameOver method in case the cards in the deck run out.
    if len(deck) == 0:
        return('',play_pile)
    return(player,play_pile)



# This runs all of the methods. Tried to work with my tutor to get this into a __main__ function, but 
# we couldn't get it to work without it breaking, so I decided to scrap it for now.
# Got the artwork generated from this website: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=The%20Champion%20Game!%0A
print('___________.__               ___ ___                          ________                            ._.')
print('\__    ___/|  |__   ____    /   |   \   ___________  ____    /  _____/_____    _____   ____       | |')
print('  |    |   |  |  \_/ __ \  /    ~    \_/ __ \_  __ \/  _ \  /   \  ___\__  \  /     \_/ __ \      | |')
print('  |    |   |   Y  \  ___/  \    Y    /\  ___/|  | \(  <_> ) \    \_\  \/ __ \|  Y Y  \  ___/\     | |')
print('  |____|   |___|  /\___  >  \___|_  /  \___  >__|   \____/   \______  (____  /__|_|  /\___  >     |_|')
print('                \/     \/         \/       \/                       \/     \/      \/     \/\/    ***')
print('')
print('')
print("The rules are simple!")
print("Five cards are dealt to both players.")
print("Play a card from your hand that has a higher or equal value to the card in the play pile.")
print("The suits do not matter.")
print("If either player cannot play their hand, they have to draw cards from the deck until they have five cards again and loses their turn.")
print("If neither player can play, a Champion Card will be drawn so the play can continue.")
print("When a Champion Card is drawn, whoever has the lowest playable card will get to play.")
print("If neither player has a card to play on the Champion Card or if both players have the same card to play, then a Champion Card is drawn until a player can play.")
print("The game is over when either the deck has no more cards in it or if either player has no more cards in their hand.")
print("Let's play!")

# Makes the first card the 2 of Spades.
play_pile = deck.pop(0)
deal(deck)
# Makes sure that both of the players can play.
playable = playableHands(dealerHand,nonDealerHand)
# Starts the player as the first person to play since the computer is the dealer.
player,nonPlayer = "nonDealer", "dealer"

while gameOver(dealerHand,nonDealerHand,deck) == False:
    strNonDealerHand = []
    playable = playableHands(dealerHand,nonDealerHand)
    # This checks to see if the Champion method needs to be activated.
    if not playable[0] and not playable[1] and len(dealerHand) == 5 and len(nonDealerHand) == 5 and len(deck) > 0: 
        ChampionOne = Champion(playable,dealerHand,nonDealerHand)
        play_pile = ChampionOne[1]
        doTurn = do_turn(playable,ChampionOne[0],play_pile)
        play_pile = doTurn[1]
        player = doTurn[0]
    # Activates the do_turn method for each of the active players.
    # The idea for switching between players came from thei Stackoverflow post:
    # https://stackoverflow.com/questions/21884119/how-to-alternate-between-two-players     
    elif player == "nonDealer":
        if playable[1]:
            doTurn = do_turn(playable,player,play_pile)
            player = doTurn[0]
            play_pile = doTurn[1]
            playable = playableHands(dealerHand,nonDealerHand)
        elif not playable[1]:
            if len(nonDealerHand) == 5:
                lines = [[] for i in range(9)]
                for index, card in enumerate(nonDealerHand):
                    # This adds the individual card on a line by line basis.
                    if card[0] != 10:
                        lines[0].append(str(index + 1) +') '+'┌─────────┐ ')
                        lines[1].append('   │{}        │ '.format(face_print(card))) 
                        lines[2].append('   │         │ ')
                        lines[3].append('   │         │ ')
                        lines[4].append('   │    {}    │ '.format(card[1]))
                        lines[5].append('   │         │ ')
                        lines[6].append('   │         │ ')
                        lines[7].append('   │        {}│ '.format(face_print(card)))
                        lines[8].append('   └─────────┘ ')
                    else: 
                        lines[0].append(str(index + 1) +') '+'┌─────────┐ ')
                        lines[1].append('   │{}       │ '.format(face_print(card))) 
                        lines[2].append('   │         │ ')
                        lines[3].append('   │         │ ')
                        lines[4].append('   │    {}    │ '.format(card[1]))
                        lines[5].append('   │         │ ')
                        lines[6].append('   │         │ ')
                        lines[7].append('   │       {}│ '.format(face_print(card)))
                        lines[8].append('   └─────────┘ ')
                result = []
                for index, line in enumerate(lines):
                    result.append(''.join(lines[index]))

                print('The cards in your hand are:')
                for card in result:
                    print(card)
               
                print("You do not have a playable card. It is the dealer's turn.")
                playable = playableHands(dealerHand,nonDealerHand)
            else:
                # If the player does not have a playable card and has less than 5 cards in their hand, then
                # the hand is refilled until 5 cards are reached.
                print("You do not have a playable card. Refilling your hand.")
                while(len(nonDealerHand) != 5 and len(deck) != 0):
                    nonDealerHand.append(deck.pop(0))
                    nonDealerHand.sort(key = operator.itemgetter(0)) 
            player,nonPlayer = "dealer", "nonDealer"
            playable = playableHands(dealerHand,nonDealerHand)
    elif player == "dealer":
        if playable[0]:
            doTurn = do_turn(playable,player,play_pile)
            player = doTurn[0]
            play_pile = doTurn[1]
            playable = playableHands(dealerHand,nonDealerHand)
        elif not playable[0]:
            if len(dealerHand) == 5:
                print("The dealer does not have a playable card. It is your turn.")
                playable = playableHands(dealerHand,nonDealerHand)
            else:
                # If the dealer does not have a playable card and has less than 5 cards in their hand, then
                # the hand is refilled until 5 cards are reached.
                print("Dealer does not have a playable card. Refilling their hand.")
                while(len(dealerHand) != 5 and len(deck) != 0):
                    dealerHand.append(deck.pop(0))
                    dealerHand.sort(key = operator.itemgetter(0))
        player,nonPlayer = "nonDealer", "dealer"
        playable = playableHands(dealerHand,nonDealerHand)
    if(play_pile[0] != 10):
        card = """\n
            ┌─────────┐
            │{}        │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │        {}│
            └─────────┘
        """.format(face_print(play_pile), play_pile[1], face_print(play_pile))
    else:
        card = """\n
            ┌─────────┐
            │{}       │
            │         │
            │         │
            │    {}    │
            │         │
            │         │
            │       {}│
            └─────────┘
        """.format(face_print(play_pile), play_pile[1], face_print(play_pile))
    print('Play pile: ' + card)