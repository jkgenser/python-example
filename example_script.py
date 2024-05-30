import os

os.environ['PYTHONBREAKPOINT']="ipdb.set_trace"

def main():
    x = 1
    y = 2

    z = x + y
    breakpoint()

    print(f"z is :{z}")


if __name__ == "__main__":
    main()