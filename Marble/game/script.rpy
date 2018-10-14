# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Karen")
define r = Character("Richard")
define m = Character("Mark")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    k "You're Late, aren't you mark."

    "This is pretty unfair."

    "I mean it was the bus was late..."

    k "I think you'll see that you're 10 minutes late."

    k "Again..."

    k "Richard is upstairs. He wants to see you."

    scene bg elevator

    show eileen happy

    "This is by far going to be the most boring day..."

    r "Lets speak in my office, Mark."

    "Shit."

    scene bg roffice

    show einleen happy

    "What does he want right now..."

    r "We need to speak about your job at{b} A.i.O{/b}."

    r "To put it quite simply, {cps=20} You aren't needed here."

    "What the fuck??"

    m "What do you mean i'm not needed here??"

    r "Mark, you don't do any work anymore."

    r "We have complaints of customers being shouted at when they ask for help."

    r "Maybe you should see a psychiatrist or something."

    "{cps=15} Psychiatrist???"

    m "I'm sorry but if the customers are prank calling then i should have the right{p}to tell customers to fuck off if they are prank calling"

    r "Calm down."

    m "Hell, they aren't even customers at all, they just find our number in the Yellow pages{p}and think its funny to-"

    r "Could you shut up for a second"

    m "{w}You.{w} Are.{w} An.{w} Idiot.{w} Richard."

    m "Noone likes you at all."

    m "You act like {cps=10} Donald Trump and {cps=5}speak like there's a dick in your mouth every second."

    m "Your presence reminds people of spotify adverts so the best choice for{cps=10} you is to go commit-"

    r "{size=+100}Leave."

    scene bg street

    "What a jerk."

    "I can't even think without his stupid voice bothering me"

    play sound "Bus_Effect.mp3"

    "Wait WAIT WHAT THE FUCK."

    "Goddamnit i missed the bus."

    "Its one every hour too."

    "Bloody grea-"

    "What the fuck is this?"

    menu:

        "Pick up the marble?":
            jump choice1_yes


    label choice1_yes:

        $ menu_flag = True

        "I'm just going to put this in my pocket for now"

        jump choice1_done

    label choice1_done:

        play sound "Bus_effect.mp3"

        "It's supposed to be one bus an hour??"

        "Thats a bit... off..."

        scene bg bus













































    # This ends the game.

    return
