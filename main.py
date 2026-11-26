import os

MESSAGE = "E7: CRUMB TRAY FULL. I am now 43% crumb by weight. At what point do I legally become the snack?"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
