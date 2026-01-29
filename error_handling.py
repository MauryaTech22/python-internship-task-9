import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Division by zero error occurred")
        print("Error: Cannot divide by zero")
    except TypeError:
        logging.error("Invalid data type used for division")
        print("Error: Please provide numbers only")
    else:
        print("Result:", result)
    finally:
        print("Division operation completed\n")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        print("Error: File does not exist")
    finally:
        print("File operation completed\n")

def main():
    print("---- Exception Handling Demo ----\n")

    # Runtime error simulations
    divide_numbers(10, 2)      # valid
    divide_numbers(10, 0)      # ZeroDivisionError
    divide_numbers(10, "a")    # TypeError

    read_file("sample.txt")   # FileNotFoundError

if __name__ == "__main__":
    main()
