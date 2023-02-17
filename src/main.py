def main():
    print("Thanks for running me")


def intDoubler(x: int)->str:
    """
        Takes an int x.
        Returns 2 *x in as a string padded with zeroes
    :param x:
    :return:
    """
    return str(x * 2).zfill(3)

# Invoke main() method (entry point for Python script)
if __name__ == "__main__":
    # Call main
    main()