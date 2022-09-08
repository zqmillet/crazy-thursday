from random import choice

from .articles import articles

def main():
    print(choice(articles))

if __name__ == '__main__':
    main()
