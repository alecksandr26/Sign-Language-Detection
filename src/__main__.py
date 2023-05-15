import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['collect-data'],
                        help = 'collect-data: Collects data generate by your wepcam')

    # Parse the arguments
    args = parser.parse_args()
    if args.command == "collect-data":
        print("Collecting the data")

    else:
        return -1

    return 0                    # As success

if __name__ == "__main__":
    exit(main())
