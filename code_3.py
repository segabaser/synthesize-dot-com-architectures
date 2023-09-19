
def generate_random_data():
    random_string = 'Improve people call still his short many.'
    random_number = 90

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Improve people call still his short many.")
        print(f"Random Number: 90")

if __name__ == "__main__":
    main()
