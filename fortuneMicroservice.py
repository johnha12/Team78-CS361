import random
import time

fortunes = [
    "Good things come to those who wait.",
    "You will soon meet someone special.",
    "A smile is your passport into the hearts of others.",
    "Your hard work will pay off in the end.",
    "Fortune favors the bold.",
    "You are destined for greatness.",
    "Believe in yourself and you can accomplish anything.",
    "Your kindness will be rewarded.",
    "The best way to predict the future is to create it.",
    "Success is just around the corner.",
    "Your dreams will come true if you keep working hard.",
    "You will find happiness in unexpected places.",
    "You have a heart of gold.",
    "You will be surrounded by love and laughter.",
    "Your talents will take you far in life.",
    "Opportunities are all around you.",
    "The world is full of endless possibilities.",
    "Your future is bright.",
    "Luck is on your side today.",
    "You are capable of achieving anything you set your mind to."
]


def request():
    with open('fortunePipe.txt', 'w') as f3:
        f3.write(str(3))
    with open('fortunePipe.txt', 'r') as f4:
        contents = f4.read().strip()
        while contents.isdigit():   # wait for a string
            time.sleep(1)
            with open('fortunePipe.txt', 'r') as f5:
                contents = f5.read().strip()
    return contents


def main():

    while True:
        with open('fortunePipe.txt', 'r') as f:
            contents = f.read().strip()  # read file contents and remove leading/trailing whitespaces
            if not contents.isdigit():
                continue  # contents is not a valid integer, so skip this iteration
            random_number = random.randint(0, 19)  # generate number for fortune
            output = fortunes[random_number]  # write generated fortune
            with open('fortunePipe.txt', 'w') as f2:
                f2.write(output)

    # random_number = random.randint(0, 19)
    # output = fortunes[random_number]

    return output


if __name__ == '__main__':
    print(main())
