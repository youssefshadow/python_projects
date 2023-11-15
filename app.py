# Importer le module turtle
import turtle

# Créer une fenêtre pour le jeu
wind = turtle.Screen()
wind.title("Ping Pong By Youssef")  # Titre de la fenêtre
wind.bgcolor("black")  # Couleur de fond de la fenêtre
wind.setup(width=800, height=600)  # Dimensions de la fenêtre
wind.tracer(0)  # Désactiver les mises à jour automatiques de la fenêtre

# Joueur 1 (madrab1)
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")  # Forme du joueur 1 (rectangle)
madrab1.color("blue")  # Couleur du joueur 1
madrab1.shapesize(stretch_wid=5, stretch_len=1)  # Taille du joueur 1
madrab1.penup()
madrab1.goto(-350, 0)  # Position initiale du joueur 1

# Joueur 2 (madrab2)
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")  # Forme du joueur 2 (rectangle)
madrab2.color("red")  # Couleur du joueur 2
madrab2.shapesize(stretch_wid=5, stretch_len=1)  # Taille du joueur 2
madrab2.penup()
madrab2.goto(350, 0)  # Position initiale du joueur 2

# Balle (ball)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")  # Forme de la balle (cercle)
ball.color("yellow")  # Couleur de la balle
ball.penup()
ball.goto(0, 0)  # Position initiale de la balle

# Fonctions de mouvement pour les joueurs
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

# Liaison des touches du clavier aux fonctions de mouvement
wind.listen()
wind.onkeypress(madrab1_up, "s")
wind.onkeypress(madrab1_down, "w")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# La boucle principale du jeu
while True:
    wind.update()  # Mettre à jour la fenêtre


