# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Karen")
define r = Character("Richard")
define m = Character("Mark")
define i = Character("Irratated lady")
define f = Character("Flight Assistant")
define jf = Character("Japanese Flight Assistant")
define jt = Character("Japanese Taxi man")



# The game starts here.

label start:

    scene bg room

    show eileen happy


    k "You're late."

    "Damn it."

    menu:


        "Lie about it.":
            jump choicea_yes


        "Tell the truth.":
            jump choicea_no

    label choicea_yes:

        $ menu_flag = True

        m "Hey, in my defense, the bus was late!"

        k "Not good enough."

        "Does she think I'm God or something? I can't control the buses."

        jump choicea_done

    label choicea_no:

        m "I hurt my ankle while coming out of the house."

        m "It affected my ability to get here on time."

        k "Right, don't hurt your ankle next time. Only then will you be able to arrive on sufficient note."

        "What is her point?"

        jump choicea_done

    label choicea_done:

    k "Whatever."

    k "Richard is upstairs. He would like to see you right now."

    scene bg elevator

    show eileen happy

    "This is great. I'm too tired for this crap."

    r "Let's speak in my office, Mark."

    "Shit."

    scene bg roffice

    show einleen happy

    # This is just a placeholder right now. Will change when i receive the spites.

    "What in God's name does he want right now...?"

    r "We need to speak about your job at{b} A.i.O{/b}."

    r "To put it quite simply, {cps=20} you aren't needed here."

    "Okay, okay. Hold the phone. What the actual fuck?"

    "I've always known him to be the kind of guy to be an absolute jackass, but this was on a whole other level!"

    m "...What do you mean that I'm not needed here?"

    r "Mark, you aren't the ideal staff member."

    r "We have complaints of customers being shouted at when they ask for services."

    r "I reckon you to see a psychiatrist or so. These angry outbursts are getting out of hand."

    "{cps=15} Psychiatrist...?"

    "I couldn't believe what I was hearing."

    m "I'm sorry, but if the customers are prank calling, then I should have the right{p}to tell them to fuck off!"

    r "That's besides the point."

    m "Hell, they aren't even customers at all! They just find our number in the Yellow pages or some bullshi-"

    r "Listen to me, Mark."

    m "{w}You.{w} Are.{w} An.{w} Idiot.{w} Richard."

    m "You know what? No one really likes your presence anyway, and you're a suffocating whore."

    m "The best choice you have right now is to go commi-"

    r "{size=+100}Leave."

    scene bg street

    "Goddamn, what a jerk."

    "I can't even think with his huge forehead in the way."

    play sound "Bus_Effect.mp3"

    "Shit. Another addition to my day."

    "It's one every hour, too."

    "Bloody great."

    "Absolutely fantastic."

    "Love it."

    "Hey, what's that?"

    "It's a marble!"

    "What's this little guy doing out here?"

    menu:

        "Pick up the marble?":
            jump choice1_yes


    label choice1_yes:

        $ menu_flag = True

        "I'm just gonna pocket this, for now."

        jump choice1_done

    label choice1_done:

        play sound "Bus_effect.mp3"

        "Uh, isn't it supposed to be one bus every hour...?"

        "That's a bit... off..."

        scene bg bus

        "Empty?"

        scene bg seat

        "What's this over here?"

        "This is..."

        scene bg handwithticket

        "A scratch card?"

        scene bg scatchcard

        "Holy shit, no way! It's for 3 billion pounds!"

        menu:

            "Take the scratch card.":
                jump choice2_yes



            "Don't take the scratch card.":
                jump choice2_no

        label choice2_yes:

            "This is coming with me, I suppose."

            "Hell, I can finally go to Japan with this."

            "Seems today is clearing up..."

            scene bg apartment

            "It's an absolute mess in here."

            "Would be nice if it was cleaner... too lazy though."

            "Another time."

            scene afewhourslater
            with Dissolve(.5)
            pause .5
            scene bg airport
            with Dissolve(.5)
            scene bg airport

            "After that conflicting day of countless turns of events, I find myself wounded up in the airport."

            "I'm stood infront of a machine, awaiting my pass to be printed out."

            "I have to say, I'm pretty ticked off at losing my job."

            "It was logical for me to yell at the customers. They were literally asking for it."

            "They all get on the last of my nerves. Freaking low-lives."

            "I'm just gonna have to face it, aren't I? Being fired..."

            "Fuckin' hated Richard anyway."

            "I can't wait to see the look on his ugly face when he finds out I went to Japan."

            "The machine successfully printed out my boarding pass."

            "The flight is at {b}1843{/b}. I need to remember this."

            "So many people here, it's overwhelming..."

            scene blackscreen
            with vpunch

            m "Crap, sorry."

            m "I wasn't thinking straight."


            scene bg airport
            show Irratated lady

            i "Well look where you're going next time, bonehead! It's a pisstake, I have things to do."

            "Damn... she's hot."

            m "Y-Yeah. Sorry."

            menu:

                "1834":
                    jump question1_a

                "1846":
                    jump question1_a

                "1843":
                    jump question1_b

                "1823":
                    jump question1_a

            label question1_a:

                m "I don't think that was the time of my flight..."

                jump question1_done

            label question1_b:

                m "Shit."

                jump question1_done


        label question1_done:

        "I'm late, Fuck."

        scene bg airport2

        m "Hey, my fligh-"

        f "Are you mark?"

        m "Yes, but my fligh-"

        f "Can I have your autograph??"

        "What??"

        m "I'm sorry but i need to b-"

        f "Please??"

        "Can she stop interrup-"

        f "Come here, give me a hug, Mark!"

        m "This makes me uncomfortabl-"

        scene blackscreen
        with vpunch

        "I can't breath?"

        "Mfmm"

        "Wait."

        "Am I?"

        "WHAT THE FUCK?"

        scene breastscloseup

        "S..."

        "SHIT"

        scene bg airport2

        f "How was that?"

        m " I'M SORRY, BUT YOU JUST BREACHED MY PERSONAL FUCKING SPAC-"

        f "Shhh..."

        "I'm leaving, Fuck no."

        scene bg airport3

        "I'm finally here."

        "On time."

        "..."

        "All this running is making me hungry."

        menu:

            "KFC":
                jump choiceb_a

            "Get on the flight":
                jump choiceb_b

        label choiceb_a:

            "{i}You can get food on the flight you hungry bastard{/i}"

            jump choiceb_done

        label choiceb_b:

            "Alright. Lets get going."

            jump choiceb_done

        label choiceb_done:

            scene bg plane

            "It's pretty crowded in here..."

            scene bg back_of_a_seat

            "I should probably listen to some music."

            # This is the end of section 1.
            # Here we start section 2.

        menu:

            "Track 1":
                jump choice_music_1

            "Track 2":
                jump choice_music_2

            "Track 3":
                jump choice_music_3

            "Track 4":
                jump choice_music_4

        label choice_music_1:
            # I haven't got the music for this yet, itll be provided by rxxx
            jump choice_music_done

        label choice_music_2:
            # Same here uwu
            jump choice_music_done

        label choice_music_3:
            # owo
            jump choice_music_done

        label choice_music_4:
            # hmmmmmmmm
            jump choice_music_done

        label choice_music_done:

            "Finally"

            "It's a good thing I decided to learn japanese."

            scene bg japanese_airport

            m "Konnichuwa.{p=0.5}{alpha=.5}Hello/Hi.{/alpha}"

            jf "Konbanwa. {p=0.5}{alpha=.5} Good evening/Afternoon{/alpha}"

            jf "Sumimasen, demo fukuro wa motte kimashita ka? {p=0.5}{alpha=.5}Excuse me/Sorry, did you bring any bags?{/alpha}"

            m "Iie. {p=0.5}{alpha=.5} No.{/alpha}"

            jf "Sore wa sukoshi kimyoudesu. {p=0.5}{alpha=.5} That's a bit weird/queer.{/alpha}"

            jf "Tonikaku, anata no taizai o o tanoshimi kudasai!. {p=0.5}{alpha=.5} Anyway, Enjoy your stay!{/alpha}"

            m "Arigatou. {p=0.5}{alpha=.5} Thanks/ Thank you.{/alpha}"

            scene bg japan_outside_airport

            jt "Konnichuwa, Doko ni ikitai? {p=0.5}{alpha=.5} Hello/Hi, Where would you like to go?{/alpha}"

            m "Rumerya Hotel"

            jt "Nani? {p=0.5}{alpha=.5} What?{/alpha}"

            m "Rumerya Hoteru, Gomen. {P=0.5}{alpha=.5} Rumerya Hotel, Sorry.{/alpha}"
