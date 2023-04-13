import argparse
import os
import subprocess
# Define function to check if directory exists
def check_dir(directory):
    if not os.path.isdir(directory):
        print(f"Error: Directory {directory} does not exist.")
        return False
    else:
        return True

# Parse command line arguments
parser = argparse.ArgumentParser(description="Verify and retrieve the name of the person a watermark was issued to")
parser.add_argument("-inputdir", type=str, required=True, help="input directory containing image files")
args = parser.parse_args()

# Check if input directory exists
if not check_dir(args.inputdir):
    exit(1)

# Process image files in input directory
for file in os.listdir(args.inputdir):
    if file.endswith(".jpg") or file.endswith(".png"):
        inputfile = os.path.join(args.inputdir, file)
        cmd = ["openstego", "info", "-sf", "watermark.png", "-mf", inputfile]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if "Watermark detected!" in result.stdout:
            print(f"{inputfile}: {result.stdout.split()[7]}")
        else:
            print(f"{inputfile}: No watermark found")