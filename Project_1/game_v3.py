"""Game 'Guess a number'
Robot makes and guesses a number by its self
"""

import numpy as np


def recursive_predict(number: int = 1) -> int:
    """Randomly-recursively guess a number

    Args:
        number (int, optional): maked number. Defaults to 1.

    Returns:
        int: attempt's number
    """
    count = 0
    
    def find_numb(low, high): 
        """Recursive function reduses array's demands of possible numbers"""
        
        nonlocal count
        
        count += 1
        predict_number = np.random.randint(low, high)  # guessed number
        
        if  predict_number == number:
            return count  # exit from recursive
        else: #updating useful rest of array
            if predict_number < number:
                low = predict_number+1 # '+1' used to avoid duplication of lower bound
                return find_numb (low, high)
            else:
                high = predict_number
                return find_numb (low, high)
            
    return find_numb(1, 101)

def score_game(recursive_predict) -> int:
    """What avarege number of attempts by 1000 tries algorithm resolves problem 

    Args:
        recursive_predict ([type]): guess function

    Returns:
        int: avarege number of attempts  
    """
    count_ls = []
    np.random.seed(1)  # seed fixing 
    random_array = np.random.randint(1, 101, size=(1000))  # array of random guessed numbers

    for number in random_array:
        count_ls.append(recursive_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

score_game(recursive_predict)
