from random import choice
from util import WORDS
from util import STATUS

def get_secret_word(words: list) -> str:
    """Devolve uma palavra aleatória de uma lista."""
    
    return choice(words)


def print_game_board() -> None:
    """Imprime a situação atual do jogo."""
    encoded_word = ''

    for letter in secret_word:
        if letter not in correct_letters:
            encoded_word += '_'
        else: 
            encoded_word += letter

    if error <= attempts:
        print(STATUS[error])

        print(encoded_word)
    
    print(f"\nCorrect letters: {' '.join(correct_letters)}")
    print(f"\nWrong letters: {' '.join(missed_letters)}")
    
    return None

def read_input_player():
    """Lê uma letra do usuário."""
    
    input_char = input('Choose a letter:')

    while len(input_char) != 1:
        input_char = input('Type only one letter: ')

    return input_char


def guess_letter():
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""
    
    if input_char not in correct_letters and input_char in secret_word:
        correct_letters.append(input_char)
        return True
    elif input_char not in correct_letters and input_char not in missed_letters:
        missed_letters.append(input_char)
        return False
    else: 
        print('This letter has already been played, please choose another one!')
        return True        


def game_continue():
    """Função que decide se jogo já encerrou ou não.""" 

    if set(correct_letters) == set(secret_word):
        print("\nYou win!")
        return False

    elif error >= attempts:
        print(STATUS[error])
        print(f'The word secret is {secret_word}')
        return False

    return True

secret_word = get_secret_word(WORDS) # variável para palavra secreta
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

while game_continue():
    print_game_board()
    input_char = read_input_player()
    if guess_letter() == False:
        error += 1
