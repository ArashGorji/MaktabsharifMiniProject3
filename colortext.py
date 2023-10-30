class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ColorStr:
    '''HEADER, OKBLUE, OKCYAN, OKGREEN, WARNING, FAIL, ENDC, BOLD, UNDERLINE'''

    def __init__(self):
        pass

    def __call__(self, string, color=None, bold=False):
        if bold == True:
            if color == 'HEADER':
                return Color.BOLD + Color.HEADER + string + Color.ENDC
            elif color == 'OKBLUE':
                return Color.BOLD + Color.OKBLUE + string + Color.ENDC
            elif color == 'OKCYAN':
                return Color.BOLD + Color.OKCYAN + string + Color.ENDC
            elif color == 'OKGREEN':
                return Color.BOLD + Color.OKGREEN + string + Color.ENDC
            elif color == 'WARNING':
                return Color.BOLD + Color.WARNING + string + Color.ENDC
            elif color == 'FAIL':
                return Color.BOLD + Color.FAIL + string + Color.ENDC
            elif color == None:
                return Color.BOLD + string + Color.ENDC
            elif color == 'UNDERLINE':
                return Color.BOLD + Color.UNDERLINE + string + Color.ENDC
            else:
                return Color.ENDC
        else:
            if color == 'HEADER':
                return Color.HEADER + string + Color.ENDC
            elif color == 'OKBLUE':
                return Color.OKBLUE + string + Color.ENDC
            elif color == 'OKCYAN':
                return Color.OKCYAN + string + Color.ENDC
            elif color == 'OKGREEN':
                return Color.OKGREEN + string + Color.ENDC
            elif color == 'WARNING':
                return Color.WARNING + string + Color.ENDC
            elif color == 'FAIL':
                return Color.FAIL + string + Color.ENDC
            elif color == 'UNDERLINE':
                return Color.UNDERLINE + string + Color.ENDC
            else:
                return Color.ENDC


cstr = ColorStr()
if __name__ == "__main__":
    print(cstr("HEADER", color="HEADER", bold=True))
    print(cstr("OKBLUE", color="OKBLUE", bold=True))
    print(cstr("OKCYAN", color="OKCYAN", bold=True))
    print(cstr("WARNING", color="WARNING", bold=True))
    print(cstr("FAIL", color="FAIL", bold=True))
    print(cstr("BOLD", bold=True))
    print(cstr("UNDERLINE", color="UNDERLINE", bold=True))
