import argparse
import os
import subprocess
import sys

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Insert a personalized watermark on a set of image files')
    parser.add_argument('-inputdir', type=str, required=True, help='input directory containing image files')
    parser.add_argument('-peoplelist', type=str, required=True, help='file containing list of people to issue watermarks to')
    parser.add_argument('-outputdir', type=str, required=True, help='output directory to save watermarked images')
    args = parser.parse_args()

    # Check if input directory exists
    if not os.path.isdir(args.inputdir):
        print(f'Error: Input directory {args.inputdir} does not exist')
        sys.exit(1)

    # Check if output directory exists, create it if not
    if not os.path.isdir(args.outputdir):
        os.makedirs(args.outputdir)

    # Insert watermark using openstego
    for filename in os.listdir(args.inputdir):
        if filename.endswith(('.jpg', '.png')):
            inputfile = os.path.join(args.inputdir, filename)
            outputfile = os.path.join(args.outputdir, f'{os.path.splitext(filename)[0]}-watermarked{os.path.splitext(filename)[1]}')
            cmd = ['openstego', 'embed', '-a', '2', '-mf', inputfile, '-cf', args.peoplelist, '-sf', 'watermark.png', '-out', outputfile]
            subprocess.run(cmd)

    print('Watermarking complete.')

if __name__ == '__main__':
    main()