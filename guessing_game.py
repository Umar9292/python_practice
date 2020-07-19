secret_word = 'Stranger'
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = input('Guess: ')
    guess_count += 1
    if guess == secret_word:
        print('You Won!')
        break
else:
    print('Sorry, You Lost!')
