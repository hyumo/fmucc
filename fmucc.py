import argparse
import os, shutil
import sys
from fmpy.util import compile_platform_binary


# Create argument parser
parser = argparse.ArgumentParser(description="Compile source FMU to Linux-FMU")
parser.add_argument('-f', '--fmus', type=str, help='Path of source fmus', default="./fmus")
parser.add_argument('-d', '--dst', type=str, help='Destination path of converted fmus', default="./converted")
args = parser.parse_args()

# Get fmu filenames
fmus = []
if os.path.isdir(args.fmus):
    for filename in os.listdir(args.fmus):
        if filename.endswith('.fmu'):
            fmus.append(os.path.join(args.fmus, filename))
    
    if len(fmus) == 0:
        print("Could not find any fmus within path: {}".format(args.fmus))
        sys.exit(-1)
else:
    if not args.fmus.endswith('.fmu'):
        print("Target file is not an FMU: {}".format(args.fmus))
        sys.exit(-1)
    if not os.path.exists(args.fmus):
        print("Could not find target fmu file: {}".format(args.fmus))
        sys.exit(-1)
    fmus.append(args.fmus)

# Create destrination directory
try: 
    os.mkdir(args.dst)
except OSError as error: 
    print(error)
    sys.exit(-1)



# Cross compile fmus with fmpy
for fmu in fmus:
    print("Compiling: {}...".format(fmu))

    filename = os.path.join(args.dst, os.path.basename(fmu))
    print("To destination: {}".format(filename))
    try: 
        compile_platform_binary(fmu, filename)
    except:
        print("Error compiling {}".format(fmu))


    
    