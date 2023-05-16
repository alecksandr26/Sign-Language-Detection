import argparse
import json

# Import the modules
from .dataset import Collector, DataSet, ALPHABET_DICT

sign_map_dict = ALPHABET_DICT

def main():
    parser = argparse.ArgumentParser()

    # Add the command argument
    parser.add_argument(
        "command",
        choices=["collect-data", "build-dataset", "train", "transcript"],
        help="The command to execute. Choose from 'collect-data', 'build-dataset', 'train', or 'transcript'."
    )
    
    # For the collector of the data
    parser.add_argument(
        "-n", "--amount-pictures",
        nargs = '?',
        type = int,
        metavar = "N",
        help = "The number of pictures to generate per class."
    )
    
    parser.add_argument(
        "-d", "--directory",
        nargs = '?',
        metavar="PATH",
        help="The directory to store the collected data."
    )

    parser.add_argument(
        "-s", "--signs",
        nargs = '?',
        metavar="PATH",
        help = "The json file with each sign to classify."
    )

    # Flags for build-dataset
    args = parser.parse_args(
        "-f", "--file-dataset",
        nargs = '?',
        metavar="PATH",
        help = "The output file where the dataset will be sotred."
    )
    
    print(args)
    
    config = {}
    # Parse the arguments
    if args.command == "collect-data":
        if args.signs:
            # Load the new signs
            sign_map_dict = json.load(open(args.signs))
            config["amount_classes"] = len(sign_map_dict)
        if args.amount_pictures:
            config["amount_pics"] = args.amount_pictures
        if args.directory:
            config["directory"] = args.directory

        # Unpack the configuration 
        collector = Collector(**config)
        collector.start()       # Start collecting the data
        print("Data collection completed.")
        
    elif args.command == "build-dataset":
        if args.file_dataset:
            config["filename"] = args.file_dataset
            
        if args.directory:
            config["directory"] = args.directory

        # Unpack the configuration
        dataset = DataSet(**config)
        dataset.build()
        print("Dataset builted")
        
    elif args.command == "train":
        print("Training the model")
    elif args.command == "demo":
        print("Running the demo")
    else:
        return -1
    
    return 0                    # As success

if __name__ == "__main__":
    exit(main())
