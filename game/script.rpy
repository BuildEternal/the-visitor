# Characters

define character.sirena = Character("Sirena", color="#ffa64d")

define character.me = Character("Me", color="#4d4dff")

# Scenes

# You, [Player Character], wake up to find yourself wandering a foggy street, with no memory of how you got there.
# Almost immediately, you encounter a strange girl with with black hair [Sirena], who almost seems—disappointed. It
# seems she was looking to "summon" somebody else here, but it didn't work; and now, here you are.

# Still, she doesn't know how to banish you immediately—so to kill time while the two of you wait for the "dream" to
# kick you out, she decides to ask you a couple odd, philosophical questions…

label start:
    with dissolve

    "There is a question we all learn to ask ourselves, eventually."

    "Anyone who's made it through the first decade and a half of their life knows the question, more or less:"

    "Who am I?{w=.5} What am I doing here?"

    "And, why?"

    "Some will argue that this makes no sense. That those are three questions, not one."

    "Still, it's possible to argue the contrary—insisting that all three questions are, in reality, one and the same…"

    scene bg marina fog
    with dissolve

    me "…"

    me "…"

    me "…"

    me "What…"

    "An unfamiliar scene. The fog hangs thick and heavy over a street I don't recognize—shrouding everything in a humid, gloomy {i}white{/i}."

    me "(Palm trees…)"

    me "(I didn't know we had palm trees in my city.)"

    pause 3.0

    "A silhouette manifests out of the darkness, approaching me with measured steps."

    "(Her footsteps are cold, and silent—like a tomb that's lost its echo.)"

    show sirena solemn:
        zoom 0.95
        xalign 0.25 yalign 1.0
    with dissolve

    me "…?!"

    sirena "…Darn. Looks like I got the wrong person again." (name = "???")

    show sirena wry

    sirena "…Ahaha." (name = "???")

    menu: 
        "What's so funny?":
            show sirena solemn

            sirena "Oh, nothing. I just…" (name = "???")

            show sirena wry
            
            sirena "…Well, it's not all that funny, really." (name = "???")

            sirena "I suppose I'm just tired." (name = "???")
        "{i}Say nothing.{/i}":
            show sirena solemn

            sirena "…" (name = "???")

            me "…"

            sirena "…Sorry." (name = "???")
    
    "We lapse into an awkward silence."

    sirena "…" (name = "???")

    sirena "Actually, if it isn't too much trouble…" (name = "???")

    show sirena:
        ease 0.5:
            xalign 0.5
            yalign 1.0
            zoom 1
    
    pause 0.5

    sirena "…could I have your name?" (name = "???")

    $ player_name = renpy.input("{i}Enter your name:{/i}", length=20)

    sirena "Thanks. Nice to meet you, [player_name]. Although we won't meet for long." (name = "???")

    menu:
        "And, your name?":
            pass

    show sirena solemn # TODO: Sirena looks somewhat antsy here

    sirena "Oh." (name = "???")

    sirena "It's Sirena.{w} Sirena Agaforth."

    me "…"

    sirena "…"

    me "So… why {i}are{/i} you here, anyway?{w} And, where am I?"

    sirena "Huh? This is a dream.{w} Yours, specifically."

    sirena "So, I don't know where we are…"

    me "Uh-huh. I'll take your word for it."

    me "(This whole place has a surreal-like quality, anyway. And I don't feel cold at all.)"

    "{cps=*0.5}Sirena hasn't answered your other question.{/cps}"

    "Pry a little?"

    menu:
        "{i}Ask her—again—why she's here.{/i}":
            sirena "I was looking for…someone else.{w} Took a wrong turn, I suppose."

            me "That's all?"

            sirena "That's all."

            me "(Somebody else, huh…)"

            me "(I wonder who?)"
        "{i}Say nothing.{/i}":
            pause 2.0

            sirena "Mhm…{w} Well, I suppose that's my cue to go."

            me "Cue?{w} What cue?"

            sirena "My apologies for interrupting your sleep."

            sirena "But, don't worry. You won't remember me in the morning…{w} I promise."

            me "Shit, wait! Don't go yet.{w} I'm still confused—{w=0.5}{nw}"

            hide sirena

            "{w=1.0}{cps=*0.3}{sc}Sirena takes out a knife.{/sc}{/cps}{w=2.0}{nw}" (
                advance = False, slow_abortable = False
            )

            me "…!"

            window hide

            $ renpy.pause(2.0, hard=True)

            show sirena wry: # TODO: Smiley sprite :)
                xalign 0.5
                zoom 2

            $ renpy.pause(2.0, hard=True)

            sirena "{cps=*0.5}Goodnight, [player_name].{/cps}"

            call ending pass (end="BAD ENDING 1") from _call_ending
            
            return
        "{i}Change the subject.{/i}":
            pass

    scene black
    with Dissolve(1)

    return

image ending_text = ParameterizedText(
    xalign = 0.5,
    yalign = 0.5,
    slow_cps=True,
    slow_cps_multiplier=0.5,
    slow_abortable=False
)

label ending(end="GAME OVER"):
    show black

    pause 2.0

    show ending_text "{color=#f00}" + end + "{/color}"

    $ renpy.pause(5.0, hard=True)

    hide ending_text
    with Dissolve(1)

    return