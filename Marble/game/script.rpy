# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Karen")
define r = Character("Richard")
define m = Character("Mark")
define i = Character("Irratated lady")




label start:

    scene bg room

    show eileen happy


    k "You're Late."

    "Damn it."

    menu:


        "Lie about it.":
            jump choicea_yes


        "Tell the truth.":
            jump choicea_no

    label choicea_yes:

        $ menu_flag = True

        m "Well... The bus was late"

        k "Not good enough."

        "Does she think i'm god or something? I can't control the buses."

        jump choicea_done

    label choicea_no:

        m "I hurt my ankle while coming out of the house."

        m "It affected my ability to get here on time."

        k "Don't hurt your ankle next time. Then you can get here on time."

        "What is her point?"

        jump choicea_done

    label choicea_done:

    k "Whatever."

    k "Richard is upstairs. He wants to see you."

    scene bg elevator

    show eileen happy

    "This is great. I'm too tired for this crap."

    r "Lets speak in my office, Mark."

    "Shit."

    scene bg roffice

    show einleen happy

    # This is just a placeholder right now. Will change when i receive the spites.

    "What does he want right now..."

    r "We need to speak about your job at{b} A.i.O{/b}."

    r "To put it quite simply, {cps=20} You aren't needed here."

    "What the fuck??"

    m "What do you mean i'm not needed here??"

    r "Mark, you aren't the ideal staff member."

    r "We have complaints of customers being shouted at when they ask for help."

    r "Maybe you should see a psychiatrist or something."

    "{cps=15} Psychiatrist???"

    m "I'm sorry but if the customers are prank calling then i should have the right{p}to tell customers to fuck off if they are prank calling"

    r "That's besides the point."

    m "Hell, they aren't even customers at all, they just find our number in the Yellow pages or some bullshi-"

    r "Listen to me, Mark."

    m "{w}You.{w} Are.{w} An.{w} Idiot.{w} Richard."

    m "No one really likes your presence and you're a suffocating whore."

    m "The best choice you have right now is to go commi-"

    r "{size=+100}Leave."

    scene bg street

    "What a jerk."

    "I can't even think with his huge forehead in the way."

    play sound "Bus_Effect.mp3"

    "Shit. Another addition to my day."

    "Its one every hour too."

    "Bloody great."

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

        "Empty??"

        scene bg seat

        "Uh? A lottery scatch card?"

        "This is..."

        scene bg handwithticket

        "A scatch card??"

        scene bg scatchcard

        "No way?? It's for 3 billion pounds..."

        menu:

            "Take the scatch card.":
                jump choice2_yes



            "Don't take the scatch card.":
                jump choice2_no

        label choice2_yes:

            "This is coming with me, I suppose."

            "I can finally go to japan with this."

            "Seems today is clearing up..."

            scene bg apartment

            "It's a mess in here."

            "Would be nice if it was cleaner... Too lazy though."

            "Another time."

            scene afewhourslater
            with Dissolve(.5)
            pause .5
            scene bg airport
            with Dissolve(.5)
            scene bg airport

            "Flight 392. I need to remember this."

            "So many people here...It's overwhelming."

            scene blackscreen
            with vpunch

            m "Crap, Sorry."

            m "I wasn't thinking straight."


            scene bg airport
            show Irratated lady

            i "Well look where you're going next time, It's a pisstake, I have things to do."

            "Damn... She's hot."

            m "Y-Yeah. Sorry."

            menu:

                "Flight 332":
                    jump question1_a

                "Flight 239":
                    jump question1_a

                "Flight 392":
                    jump question1_b

                "Flight 332":
                    jump question1_a

            label question1_a:

                m "I don't think that was my flight."

                jump question1_done

            label question1_b:

                m "Shit."

                jump question1_done


        label question1_done:

        "I'm late, Fuck."

        scene bg airport2

        plsdniind










































































    # This ends the game.

    return
