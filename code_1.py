
def generate_random_data():
    random_string = 'Maintain history ago they they cold.'
    random_number = 56

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Maintain history ago they they cold.")
        print(f"Random Number: 56")

if __name__ == "__main__":
    main()
