#!/usr/bin/python
def doILikePie(ans):
    if ans:
        return "I like pie!"
    else:
        return "I hate pie!"

def main():
    msg = doILikePie(False)
    print(msg)

if __name__ == "__main__":
    main()
