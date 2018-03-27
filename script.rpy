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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    p "Well, its been a long week. A lot of interesting things happened..."
    p "First there was that man"
    scene bg room lit
    p "He asked if I could kill for him...and that if i did..."
    p "I mean...with"

    # This ends the game.

    return
