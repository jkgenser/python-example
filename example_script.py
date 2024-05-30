import os

# This environment variable can be set elsewhere like in .bashrc, etc. By setting it here
# it means that breakpoint() uses ipdb instead of built-in pdb
os.environ['PYTHONBREAKPOINT']="ipdb.set_trace"

def main():
    x = 1
    y = 2

    z = x + y
    breakpoint()

    print(f"z is :{z}")


if __name__ == "__main__":
    main()