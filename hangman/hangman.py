import glob, os


guessed_char = set()
wrong_guessed = set()
score = 0
chance = 0
category = []
store = dict()
def process(word):
    remain = 0
    word2 = ""
    for e in word:
        t = e.lower()
        if not t.isalpha():
            word2 += e
        elif t in guessed_char:
            word2 += e+" "
        else :
            word2+=("_ ")
            remain += 1
    
    return word2, remain
def guess(word, g):
    g = g.lower()
    if g in guessed_char or g in wrong_guessed:
        return
    if g not in word.lower():
        wrong_guessed.add(g)
        global chance
        chance -= 1
        return
    global score
    guessed_char.add(g)
    for e in word :
        if e == g:
            score += 10

def play(word, hint):
    print("Hint :", hint)
    global score, chance
    # print(chance)
    wrong_guessed.clear()
    guessed_char.clear()
    while True:
        w , rem = process(word)
        if( rem == 0 ):
            break
        if chance == 0 :
            return 
        print(w, end = "  ")
        print("Score :", score, end = ", ")
        print("Remaining wrong guess :", chance, end=", ")
        print("wrong guess :", (" ").join(wrong_guessed))
        g = input(">>")
        if(len(g)!=1) or g.isalpha()==False:
            print("Invalid input")
            continue
        guess(word, g)
        # print("Guess :", guessed_char)
        # print("Wrong Guess :", wrong_guessed)
    print("Yayyyyy! the word is", word, ".\n")


def load():
    for file in glob.glob("res/*.txt"):
        # print(file)
        cat = file[4:-4]
        # print(cat)
        category.append(cat)
        store[cat] = []
        f = open(file, 'r')
        for line in f:
            word = line.strip()
            hint = f.readline().strip()
            if not hint:
                 return
            # print(word, hint)
            store[cat].append((word,hint))
        f.close()

def show_category():
    print("Please select category.")
    for i in range(len(category)):
        print(""+str(i+1)+". " + str(category[i]))

def main():
    load()
    show_category()
    
    while(True): 
        cat = int(input("> "))
        if cat  in range(1, len(category)+1):
            break
        print("Invalid input.")
    
    global score, chance
    score = 0
    chance = 10
    for (word, hint) in store[category[cat-1]]:
        # print("Word", word, "Hint", hint)
        if(chance == 0 ):
            break

        play(word, hint)
    print("Game Over, Score :", score)

main()
