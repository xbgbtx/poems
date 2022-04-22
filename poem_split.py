class Poem:
    def __init__(self, title):
        self.title = title
        self.lines = []

        self.lines.append(title+"\n\n")

    def add_line(self, l):
        self.lines.append(l+"\n")

    def dump(self):
        print("> %s" % self.title)

        for l in self.lines:
            print(l)

class PoemReader:
    def __init__(self):
        with open("all.txt", "r") as f:
            self.lines = f.readlines()

        self.current_line = 0

    def dump(self):
        for l in self.lines:
            print(l)

    def read_next(self):

        poem = None

        while self.current_line < len(self.lines):
            line = self.lines[self.current_line].strip()
            self.current_line += 1

            if len(line) == 0:
                continue

            if line[0:2:1] == "##":
                title = line[2:].strip()
                if poem is None:
                    poem = Poem(title)
                    continue
                else:
                    self.current_line -= 1
                    break

            if poem is None:
                raise Exception("No Poem Title - line %s" % (self.current_line-1))

            poem.add_line(line)

        return poem


def save_poems(poems):

    file_count = 0

    for p in poems:
        file_count += 1
        fname = "poems/%03d - %s" % (file_count, p.title)
        print(fname)
        
        with open(fname, 'w') as f:
            f.writelines(p.lines)



def main():

    pr = PoemReader()
    poems = []
        
    while (poem := pr.read_next()) is not None:
        poems.append(poem)

    save_poems(poems)

if __name__ == "__main__":
    main()

