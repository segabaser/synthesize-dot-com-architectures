
def generate_random_data():
    random_string = 'Choose floor long paper month.'
    random_number = 93

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Choose floor long paper month.")
        print(f"Random Number: 93")

if __name__ == "__main__":
    main()
