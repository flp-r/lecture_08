

def is_correct(sudoku):
    sudoku = set(sudoku)
    if len(sudoku) != 9:
        return False
    return True




def main():
    assert is_correct([1, 2, 8, 9, 3, 5, 6, 7, 4]) == True
    assert is_correct([1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert is_correct([1, 1, 2, 8, 9, 3, 5, 7, 4]) == False
    assert is_correct([]) == False


if __name__ == "__main__":
    main()