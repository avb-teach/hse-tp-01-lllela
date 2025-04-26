import os
import sys
import shutil
from argparse import ArgumentParser

def collect_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    copied_files = set()
    
    for root, _, files in os.walk(input_dir):
        for filename in files:
            source_path = os.path.join(root, filename)
            
            target_path = os.path.join(output_dir, filename)
            
            if filename not in copied_files:
                shutil.copy2(source_path, target_path)
                copied_files.add(filename)
            
def main():
    parser = ArgumentParser()
    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    args = parser.parse_args()
    
    if not os.path.isdir(args.input_dir):
        sys.exit(1)
        
    collect_files(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()
