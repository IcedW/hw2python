from dataclasses import dataclass

@dataclass
class OneSlipper:
    color: str
    size: int
    location: str
    mood: str

    def complain(self):
        print(f"slipper {self.color} color, lost its pair")

    def move(self):
        print(f"slipper with the size {self.size} is: {self.location}.")

    def talk(self):
        print(f"I am {self.mood}.")

    def dream(self):
        print(f"slipper {self.color} dreams about its second pair")


def main():
    slipper1 = OneSlipper("blue", 42, "there", "sad")
    slipper2 = OneSlipper("red", 38, "over there", "angry")
    slipper3 = OneSlipper("green", 40, "there2", "happy")

    slipper1.complain()
    slipper1.move()
    slipper1.talk()
    slipper1.dream()

    print()

    slipper2.complain()
    slipper2.move()
    slipper2.talk()
    slipper2.dream()

    print()

    slipper3.complain()
    slipper3.move()
    slipper3.talk()
    slipper3.dream()


if __name__ == "__main__":
    main()