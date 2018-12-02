# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# There are a lot of grammar errors here, im just pretty tired
# I'm  sure any scripters will find them and fix them for me <3


define k = Character("Karen")
define r = Character("Richard")
define m = Character("Mark")
define i = Character("Irratated lady")
define f = Character("Flight Assistant")
define jf = Character("Japanese Flight Assistant")
define jt = Character("Japanese Taxi Man")
define jhc = Character("Japanese Hotel Clerk")
define sp = Character("Loud Speaker")
define af = Character("On Board Flight Assistant")
define hk = Character("Hazel Kate")




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

                m "Fuck. I'm late."

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

            m "Rumerya Hoteru, Gomen. {p=0.5}{alpha=.5} Rumerya Hotel, Sorry.{/alpha}"

            jt "Hai. {p=0.5}{alpha=.5} Okay/Yes/Yeah.{/alpha}"

            scene bg hotelfront

            "This looks great... 4 stars in the review"

            "I've wanted to go here for my whole life. Feels worth it."

            scene bg insideofhotel

            "Looks pretty good..."

            "We'll see if the rooms are as good, though"

            scene hotelclerk

            jhc "Konbanwa. English? {p=0.5}{alpha=.5} Evening. English?{/alpha}"

            m "Evening. English please."

            jhc "Do you have a reservation number?"

            m "Yeah, I do."

            m "It's 13012018"

            jhc "Ah, Mark, Do you have a passport?"

            m "Yes, i do."

            m "Here"

            scene Marks passport

            jhc "Looks like you're all set to go."

            scene hotelclerk

            jhc "Here is the keys for going to the bar, for your unlimited drinks, for your room and for your garage"

            jhc "To get a replacement, it will cost you 10 yen."

            m "Alright."

            jhc "You are in room 444."

            m "Thanks."

            scene bg hotel_room

            "Looks awesome in here. It's 10 times as clean as it was in my apartment, too."

            "I feel pretty tired..."

            menu:

                "Sleep?":
                    jump choices_yes

                "Look around?":
                    jump choices_no

            label choices_no:

                "Alright, lets have an explore"

                scene hotel_bathroom

                "Looks pretty normal here..."

                scene sink

                "Just a toothbush... And some overpriced toothpaste.."

                scene bathtub

                "I think if i recall, this bathroom is made of marble."

                "Pretty cool, I hope it's worth it later."

                scene bed

                "It's huge."

                "I love it already"

                "Looks pretty luxery..."

                scene drawers

                "I wonder what's in here..."

                scene drawer_open

                "{b}A gun??{/b}"

                menu:

                    "Report to hotel manager":
                        jump subchoice_s_yes

                    "Don't report.":
                        jump subchoice_s_no

                label subchoice_s_yes:

                    "Alright, I'll do that when i'm going down to the grill."

                    jump subchoice_s_done

                label subchoice_s_no:

                    "..."

                    jump subchoice_s_done

            label subchoice_s_done:

                "I wonder what that was doing there..."

                jump choices_done

            label choices_yes:

                "That was a great sleep"

                "Wait..."

                "What's that sticking out of the drawer?"

                scene drawer_butitshalfopenwow

                "Uh"

                scene drawer_open

                "{b} A gun?{/b}"

                "..."

                jump choices_done

        label choices_done:

            "..."

            "I think i'll just go to the grill."

            "It'll improve my mood... Hopefully at least."

            scene stairs

            "..."

            "Why was that there, anyway."

            "Stupid things ruining my mood."

            "First she dies then..."

            "Ugh. That's not the point."

            "I just want to stop thinking."

            scene hotel_inside

            m "Arigatou. {p=0.5}{alpha=.5} Thanks/Thank you.{/alpha}"

            scene outside hotel

            "I don't feel like getting a taxi, so i'll walk it."

            "I wonder what the hell that was anyway"

            "Who on earth leaves a gun right there in a hotel.."

            "It's fucking mad.."

            "Where is this place anyway..."

            "I don't even need to get there on time. I came alone."

            "Fucking..."

            "Nevermind..."

            "..."

            "Fuck it."

            "I'll have the best time ever."

            "Fuck Richard."

            "Fuck Karen."

            "Fuck all of them."

            "I'll have a great day today."

            scene bg boi_da_stripclub

            "Here we are..."

            "Finally..."

            "It's loud as fuck and I can't hear my thoughts."

            "So calming."

            "So fun."

            "I'll drink the pain away."

            "Alcohol."

            "My Best friend."

            "The hand that keeps lending."

            "It's loud."

            "Better find a good reason to dr-"

            hk "Sorry! I wasn't looking where I was going!"

            m "No, no It's oka-"

            hk "You're from england?"

            m "Y-yeah? I am."

            hk "Wellllllll lets settle this in a drinking battle!"

            "I can't say no to this..."

            m "Wha- Why?"

            hk "Come on, ya can't tell me you don't want to drink too?"

            "Damn it she read my mind."

            m "Yeah but, when did this become a battle?"

            hk "As soon as you told me you were from england"

            "I'll just cave in."

            m "Alright."

            m "I'll win though"

            m "You'll watch me win"
