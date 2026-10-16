
import turtle
import random
import math
import pygame
import os

# ---------------- SETTINGS ----------------

WIDTH = 600
HEIGHT = 800

BACKGROUND = "#DDF3FF"
CAKE_COLORS = ["#FFB6C1", "#F8C8DC", "#DDA0DD"]
CANDLE_COLORS = ["#FFD700", "#7DF9FF", "#FF69B4", "#98FB98"]

# ---------------- MUSIC ----------------


pygame.mixer.init()

music_path = r"C:\Users\Sima Dutta\OneDrive\Desktop\pyyython\birthday.mp3"

print("File exists:", os.path.exists(music_path))

pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# ---------------- TURTLE SETUP ----------------

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("A Birthday Surprise 🎂")
screen.bgcolor(BACKGROUND)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# ---------------- DRAWING HELPERS ----------------

def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()

    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

    pen.end_fill()
    pen.penup()
    
def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()

def write_center(text, x, y, size, color, font="Arial"):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(
        text,
        align="center",
        font=(font, size, "bold")
    )


# ---------------- CUTE PASTEL DOODLES ----------------


def draw_heart(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pensize(2)
    pen.pendown()

    pen.circle(size * 0.6, 180)
    pen.left(180)
    pen.circle(size * 0.6, 180)

    pen.penup()
    pen.pensize(1)

def draw_star(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pensize(2)
    pen.pendown()

    for _ in range(5):
        pen.forward(size)
        pen.right(144)

    pen.penup()
    pen.pensize(1)


def draw_flower(x, y, color):
    for angle in range(0, 360, 72):
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle)
        pen.forward(9)
        pen.dot(10, color)

    pen.penup()
    pen.goto(x, y)
    pen.dot(7, "#FFD966")
    pen.penup()

def draw_sparkle(x, y, size, color):
    pen.color(color)
    pen.pensize(2)

    pen.penup()
    pen.goto(x - size, y)
    pen.pendown()
    pen.goto(x + size, y)

    pen.penup()
    pen.goto(x, y - size)
    pen.pendown()
    pen.goto(x, y + size)

    pen.penup()
    pen.pensize(1)



def draw_all_doodles():
    # Top-left corner
    draw_heart(-250, 330, 18, "#F4A6C8")
    draw_star(-210, 350, 16, "#75BDEB")
    draw_flower(-260, 275, "#F6B8D0")
    draw_sparkle(-205, 285, 8, "#E9B8F5")

    # Top-right corner
    draw_heart(250, 330, 18, "#F4A6C8")
    draw_star(210, 350, 16, "#75BDEB")
    draw_flower(260, 275, "#F6B8D0")
    draw_sparkle(205, 285, 8, "#E9B8F5")

    # Bottom-left corner
    draw_heart(-250, -335, 18, "#F4A6C8")
    draw_star(-210, -350, 16, "#75BDEB")
    draw_flower(-260, -275, "#F6B8D0")
    draw_sparkle(-205, -285, 8, "#E9B8F5")

    # Bottom-right corner
    draw_heart(250, -335, 18, "#F4A6C8")
    draw_star(210, -350, 16, "#75BDEB")
    draw_flower(260, -275, "#F6B8D0")
    draw_sparkle(205, -285, 8, "#E9B8F5")



# ---------------- CONFETTI ----------------

confetti = []

for _ in range(90):
    confetti.append({
        "x": random.randint(-440, 440),
        "y": random.randint(-330, 330),
        "speed": random.uniform(1, 3),
        "color": random.choice([
            "#FF69B4", "#FFD700", "#7DF9FF",
            "#98FB98", "#DDA0DD", "#FFFFFF"
        ]),
        "size": random.randint(3, 6)
    })

def draw_confetti():
    for piece in confetti:
        piece["y"] -= piece["speed"]

        if piece["y"] < -340:
            piece["y"] = 350
            piece["x"] = random.randint(-440, 440)

        pen.goto(piece["x"], piece["y"])
        pen.dot(piece["size"], piece["color"])

# ---------------- CAKE ----------------

def draw_cake():
    # Plate
    draw_circle(0, -190, 125, "#C7D4E8")
    draw_circle(0, -185, 118, "#F4F4F4")

    # Bottom cake layer
    draw_rectangle(-130, -190, 260, 70, "#B56A4B")
    draw_rectangle(-130, -125, 260, 15, "#FFF0D9")

    # Top cake layer
    draw_rectangle(-100, -110, 200, 55, "#F3A6C8")
    draw_rectangle(-100, -65, 200, 12, "#FFF0D9")

    # Frosting drips
    for x in [-80, -40, 0, 40, 80]:
        draw_circle(x, -65, 8, "#FFF0D9")

    # Cake decorations
    for x in [-75, -35, 5, 45, 75]:
        draw_circle(x, -88, 5, "#FFFFFF")

    # Candles
    candle_x = [-60, -20, 20, 60]

    for i, x in enumerate(candle_x):
        draw_rectangle(x - 5, -53, 10, 40, CANDLE_COLORS[i])

        # Candle stripes
        pen.penup()
        pen.goto(x - 3, -35)
        pen.color("#FFFFFF")
        pen.pensize(2)
        pen.pendown()
        pen.goto(x + 3, -28)
        pen.penup()
        pen.pensize(1)

    return candle_x
candle_positions = [-60, -20, 20, 60]


# ---------------- FLICKERING FLAMES ----------------

def draw_flames():
    for x in candle_positions:
        flame_size = random.randint(7, 12)
        flame_color = random.choice([
            "#FFD700", "#FFA500", "#FFFF99"
        ])
        draw_circle(x, 18, flame_size, flame_color)
        draw_circle(x, 18, max(2, flame_size // 3), "#FFFFFF")

# ---------------- BIRTHDAY GREETING ----------------

greeting = "Happy Birthday Auntyjiii !!!!!!!!!"
typed_chars = 0
greeting_y = 100

def animate_greeting():
    global typed_chars

    pen.clear()

    draw_confetti()
    draw_all_doodles()
    draw_cake()
    draw_flames()

    
    visible_text = greeting[:typed_chars]
    write_center(
    visible_text, 0, greeting_y, 25, "#AD1457"
    )


    if typed_chars < len(greeting):
        typed_chars += 1

    screen.update()

    if typed_chars < len(greeting):
        screen.ontimer(animate_greeting, 180)
    else:
        screen.ontimer(show_note, 2500)

# ---------------- BIRTHDAY NOTE ----------------

birthday_note = """
Happiest Birthday to my dearest Auntyjiiii,
my Lady Boss, and a teacher who will always
occupy a very special place in my heart.

Some people leave an impression on us through
extraordinary gestures, while others become
unforgettable through the smallest moments.
You, Ma'am, have somehow managed to do both.
And perhaps the most beautiful thing about
knowing you is that you may never fully realise
how profoundly your kindness has touched
the heart of your student.

I still treasure those little names you gave me:
PA, bunu, your real treasure.
To you, they might have been simple words,
spoken in passing. To me, they became little
keepsakes of a chapter in my life I will always
look back upon with fondness.

You taught me lessons beyond textbooks, gave
me encouragement when I needed it, and created
memories whose significance has only grown
with time.

And now, a formal complaint from your
neglected PA. Madam, the gossip department
is overflowing! I have accumulated enough
tea for an entire documentary, yet its most
distinguished listener remains perpetually
occupied. Should I submit my reports in writing?
Appoint the walls as temporary management?
Please advise.

Jokes aside, sometimes something happens and
my immediate instinct is to share it with you.
Then reality reminds me that life has become
busier, and I quietly save the story for another
day.

I understand, Ma'am, that responsibilities grow
and circumstances change. Still, it is possible
to understand someone's absence and miss their
presence at the same time. And I suppose that
is what happens when ordinary conversations
become cherished parts of one's day.

As you begin another year of life, I hope
happiness finds you in the quietest corners,
peace accompanies you through every uncertainty,
and love surrounds you in ways that make you
feel truly cherished.

May this new chapter be as beautiful as the
kindness you have given to others.

Perhaps years from now, when these school days
have become distant memories, I will still
remember you with the same gratitude: the
teacher who made a difference without perhaps
ever knowing the full extent of it.

Happy Birthday, Auntyjiiii.

Thank you for being a memorable part of my story.
May life always be generous to you, and may
your beautiful smile never lose its light.

With immense respect, endless gratitude,
a tiny unresolved complaint, and approximately
seventeen pending gossip reports,

Your PA, forever grateful to have been your student.
"""

# ---------------- SCROLLING NOTE ----------------

note_lines = birthday_note.strip().splitlines()

# Wrap long lines so they fit inside the window.
wrapped_lines = []

for line in note_lines:
    if not line:
        wrapped_lines.append("")
        continue

    words = line.split()
    current_line = ""

    for word in words:
        test_line = (current_line + " " + word).strip()

        if len(test_line) > 65:
            wrapped_lines.append(current_line)
            current_line = word
        else:
            current_line = test_line

    if current_line:
        wrapped_lines.append(current_line)

note_lines = wrapped_lines

scroll_y = -300
LINE_SPACING = 25
SCROLL_STEP = 1
FRAME_DELAY = 16


def show_note():
    global scroll_y

    pen.clear()
    draw_confetti()
    draw_all_doodles()

    write_center(
        "A LITTLE BIRTHDAY NOTE",
        0, 290, 22, "#D96C9D"
    )

    for i, line in enumerate(note_lines):
        y = scroll_y - i * LINE_SPACING

        if -340 < y < 270 and line:
            note_color = "#D96C9D" if i % 2 == 0 else "#548BB8"

            write_center(
                line, 0, y, 13, note_color
            )

    screen.update()
    scroll_y += SCROLL_STEP

    last_line_y = (
        scroll_y - (len(note_lines) - 1) * LINE_SPACING
    )

    if last_line_y < 330:
        screen.ontimer(show_note, FRAME_DELAY)
    else:
        screen.ontimer(finish_surprise, 1000)


# ---------------- FINISH ----------------


def finish_surprise():
    pen.clear()
    draw_confetti()
    draw_all_doodles()

    # Main heading
    write_center(
        "HAPPY BIRTHDAY",
        0, 220, 30, "#880E4F"
    )

    write_center(
        "AUNTYJIIII ♡",
        0, 175, 34, "#AD1457"
    )

    
    # Personal message
    ending_lines = [
        "Some teachers become",
        "beautiful memories,",
        "but you became someone",
        "I will always cherish.",
        "",
        "Thank you for every lesson,",
        "every little laugh,",
        "and every memory",
        "I still carry in my heart.",
    ]

    y = 95

    for line in ending_lines:
        write_center(
            line, 0, y, 17, "#548BB8"
        )
        y -= 29

    # Final signature
    write_center(
        "With love, respect & endless gratitude",
        0, -205, 13, "#880E4F"
    )

    write_center(
        "Your PA ♡",
        0, -245, 22, "#AD1457"
    )

    screen.update()


# ---------------- START ----------------


screen.ontimer(animate_greeting, 500)
turtle.done()
