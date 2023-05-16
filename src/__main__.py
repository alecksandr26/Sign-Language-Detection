import argparse

# Import the modules
from .dataset import Collector

def main():
    parser = argparse.ArgumentParser()

    # Add the command argument
    parser.add_argument(
        "command",
        choices=["collect-data", "build-dataset", "train", "transcript"],
        help="The command to execute. Choose from 'collect-data', 'build-dataset', 'train', or 'transcript'."
    )
    


    # For the collection of the data
    parser.add_argument(
        "-c", "--amount-classes",
        nargs = '?',
        type = int,
        metavar = "N",
        help = "The number of classes or signs to classify."
    )
    parser.add_argument(
        "-n", "--amount-pictures",
        nargs = '?',
        type = int,
        metavar = "N",
        help = "The number of pictures to generate per class."
    )
    
    parser.add_argument(
        "-f", "--folder",
        nargs = '?',
        metavar="PATH",
        help="The path to store the collected data."
    )


    # Arguments for 'collect-data' command
    args = parser.parse_args()
    
    print(args)
    
    # Parse the arguments
    if args.command == "collect-data":
        config = {}
        if args.amount_classes:
            config["amount_classes"] = args.amount_classes
        if args.amount_pictures:
            config["amount_pics"] = args.amount_pictures
        if args.folder:
            config["folder"] = args.path_data

        # unpack the configuration 
        collector = Collector(**config)
        collector.start()       # Start collecting the data
        print("Data collection completed.")
        
    elif args.command == "train":
        print("Training the model")
    elif args.command == "demo":
        print("Running the demo")
    else:
        return -1
    
    return 0                    # As success

if __name__ == "__main__":
    exit(main())
