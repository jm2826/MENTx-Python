import argparse


def init_argparse():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [NUMBER]...",
        description="Add numbers together.",
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument("numbers", nargs="*")
    return parser

def main():
    parser = init_argparse()
    args = parser.parse_args()
    try:
        # using map() to 
        # perform conversion 
        sum_list = list(map(int, args.numbers)) 

        sum_out = sum(sum_list)
        print(sum_out)

    except ValueError:
        print('Invalid input. Please try again with only numbers.')

if __name__ == "__main__":
    main()