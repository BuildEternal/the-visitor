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
