from formatter import formatter, parameter
from sys import argv
from os.path import isfile

input_path = str()
output_path = str()
parameter_path = str()


# Check if all files are given
def check_params():
    if input_path == '':
        print("Add input file with command '-i <input_file_name>' ")
        return False
    if parameter_path == '':
        print("No parameters file found. Add param file with command -c <param_file>")
    return True


# Check if input and parameter files exist
def check_input_file():
    if not isfile(input_path):
        print("Input file does not exist or is not a file")
        return False
    return True


def get_parameter():
    if not isfile(parameter_path):
        if parameter_path != '':
            print("Provided parameter file doest not exist or is not a file")
            print("Using default formatting settings")
        return parameter.Parameters()
    return parameter.Parameters(parameter_path)


for i in range(len(argv)):
    # Input file
    if argv[i] == '-i' and i + 1 < len(argv):
        input_path = argv[i + 1]
    # Parameters file
        elif argv[i] == '-o' and i + 1 < len(argv):
        output_path = argv[i + 1]
    elif argv[i] == '-c' and i + 1 < len(argv):
        parameter_path = argv[i + 1]
    # Output file


# If output not provided, write result to input file
if output_path == '':
    output_path = input_path


if check_params() and check_input_file():
    param = get_parameter()
    frm = formatter.Formatter(param, input_path, output_path)
    frm.format_file()
