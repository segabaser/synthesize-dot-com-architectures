
def generate_random_data():
    random_string = 'Mention inside training offer.'
    random_number = 9

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Mention inside training offer.")
        print(f"Random Number: 9")

if __name__ == "__main__":
    main()
