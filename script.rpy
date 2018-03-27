# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Goku")

# get_target_resolution(source_x, source_y)
#   Function for retrieving scaling data for the images.
#
# Parameters:
#   - horizontal size of the source images
#   - vertical size of the source images
#
# Returns:
#   - horizontal resolution
#   - vertical resolution
#   - scale factor
#   - aspect ratio of the original system resolution
#       if the system resolution cannot be found, the ratio of the source
#       image is used

init:
    #Backgrounds
    image bg room = im.FactorScale("images/room1.png", 1.5)
    image bg room lit = im.FactorScale("images/room2.png", 1.5)
    #Characters
    image goku lean = "images/phoenix.gif"
    image goku happy = "images/goku-happy.png"
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    p "Welcome! This is a project made by the Rutgers Creation of Games society."
    p "The premise of the game is about a man whose brother went MIA overseas years ago"
    p "Over the years, he served in the army to follow in his brothers footsteps before being discharged."
    p "One day, after coming home, he receives a letter from an anonymous sender asking him to become a bounty hunter."
    p "This is where our story takes place."

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    p "Well, its been a long week. A lot of interesting things happened..."
    p "First there was that man."
    scene bg room lit
    p "He asked if I could kill for him...and that if I did..."
    #Pull up image of the letter and its contents
    p "I mean...if I can see him again..."
    #WHAT IS HIS BROTHER'S NAME??????
    p "But I don't know who sent this."
    p "Can I trust him?"
    p "..."
    #His desire to see his brother again overpowers his suspicion and he accepts
    #How he accepts, I don't know, maybe throw a paper airplane towards the direction of the sender
    #Transition into next scene where he starts killing

    # This ends the game.

    return
