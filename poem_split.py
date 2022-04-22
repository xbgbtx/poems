class PoemReader:
    def __init__(self):
        with open("all.txt", "r") as f:
            self.lines = f.readlines()

    def dump(self):
        for l in self.lines:
            print(l)


def main():

    pr = PoemReader()
    pr.dump()

if __name__ == "__main__":
    main()
