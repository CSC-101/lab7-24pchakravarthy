from convert import str_to_float

def gather_numbers() -> list[float]:
    numbers = []
    while True:
        given = str(input("Give me a number or type 'done' if you are done: "))
        if given.lower() == "done":
            break
        number = str_to_float(given)
        if number is not None:
            numbers.append(number)
        else:
            print("This is not a valid number. Please try again.")
    return numbers

if __name__ == "__main__":
    print(gather_numbers())
