
class Pacman:
    points = 5000
    lives = 3
    v_ghost = 200

    def oof():
        Pacman.lives -= 1
    
    def exlife():
        Pacman.lives += 1
    def eat(things):
        Pacman.points += things
        return Pacman.points
    def eat_ghosts():
        Pacman.points += Pacman.v_ghost
        Pacman.v_ghost *= 2
        if Pacman.v_ghost == 1600:
            Pacman.v_ghost = 200
new_life = 10000

things = {
    'dot' : 10,
    'cherry' : 100,
    'strawberry' : 300,
    'orange' : 500,
    'apple' : 700,
    'melon' : 1000,
    'galaxian' : 2000,
    'bell' : 3000,
    'key' : 5000,
    }



path = open('pac.txt', 'r')
pathing = path.read().split(',')

for paths in pathing:
    score= paths.lower()

    if score == 'vulnerableghost':
        Pacman.eat_ghosts()
    elif score == 'invincibleghost':
        Pacman.oof()
    
    else:
        for key, value in things.items():
            if score == key:
                Pacman.eat(value)
    if Pacman.points >= new_life:
        Pacman.exlife()
        new_life += 10000
    if Pacman.lives == 0:
        break
    print(f"Lives: {Pacman.lives}\n"
        f"Points: {Pacman.points}")



