
def generate_random_data():
    random_string = 'Raise bit too expert board short choose.'
    random_number = 97

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Raise bit too expert board short choose.")
        print(f"Random Number: 97")

if __name__ == "__main__":
    main()
