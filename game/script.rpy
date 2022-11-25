# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define character.sirena = Character("Sirena", color = "#ffa64d")

define character.me = Character("Me", color = "#4d4dff")


# The game starts here.

label start:

    "There is a question we all learn to ask ourselves, eventually."

    "Anyone who's made it through the first decade and a half of their life knows the question, more or less:"

    "Who am I? What am I doing here?"

    "And, why?"

    "Some will argue that this makes no sense. That those are three questions, not one."

    "Still, it's possible to argue the contrary—insisting that all three questions are, in reality, one and the same…"

    scene bg marina fog
    with dissolve

    me "..."

    me "..."

    me "..."

    me "What..."

    "An unfamiliar scene. The fog hangs thick and heavy over a street I don't recognize—shrouding everything in a humid, gloomy {i}white{/i}."

    me "(Palm trees...)"

    me "(I didn't know we had palm trees in my city.)"

    pause 3.0

    "A silhouette manifests out of the darkness, approaching me with measured steps."

    "(Her footsteps are cold, and silent—like a tomb that's lost its echo.)"

    #TODO: Have the sprite resized to not need to be scaled up.
    show sirena solemn:
        zoom 1.5
        xalign 0.25 yalign 1.0
    with dissolve

    me "…?!"

    sirena "…Darn. Looks like I got the wrong person again." (name = "???")

    show sirena wry

    sirena "…Ahaha." (name = "???")

    scene black
    with dissolve

    return
