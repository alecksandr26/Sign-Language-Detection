import argparse

# Import the modules
from .dataset import Collector

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices = ["collect-data", "train", "demo"],
                        help = "The command to execute. Choose from 'collect-data', 'train', or 'demo'.")
    parser.add_argument("-pd", "--path-data", help = "To set an specific path where to collect the data")
    
    # Parse the arguments
    args = parser.parse_args()
    
    if args.command == "collect-data":
        if args.path_data:
            print(f"Collecting the data at {args.path_data}")
        else:
            print("Colleting the data")
            collector = Collector()
            collector.start()
    elif args.command == "train":
        print("Training the model")
    elif args.command == "demo":
        print("Running the demo")
    else:
        return -1
    
    return 0                    # As success

if __name__ == "__main__":
    exit(main())
