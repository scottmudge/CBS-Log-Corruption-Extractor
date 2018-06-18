import sys
import os


class CBSFinder:

    def __init__(self, log_file: str):
        self.log_file = log_file

        if not os.path.exists(self.log_file):
            raise FileNotFoundError("CBS Log File [{0}] does not exist!".format(cbs_logfile))

        print("Placing output into cbs_finder_out.txt")

        if hasattr(sys, 'frozen') and sys.frozen:
            path, filename = os.path.split(sys.executable)
            self.root_dir = path + "\\"
        else:
            self.root_dir = os.path.dirname(os.path.realpath(__file__)) + "\\"

        self.output_filename = self.root_dir + "cbs_finder_out.txt"
        if os.path.exists(self.output_filename):
            os.remove(self.output_filename)

        with open(self.output_filename, 'w') as out_file, open(self.log_file, 'r') as cbs_file:
            for i, line in enumerate(cbs_file):
                if "Repairing corrupted file" in line:
                    out_file.write(line)


if __name__ == '__main__':
    cbs_logfile = ""

    if len(sys.argv) > 1:
        cbs_logfile = sys.argv[1]
        if not os.path.exists(cbs_logfile):
            print("Warning -- supplied logfile does not exist! Using default.")
            cbs_logfile = ""

    if len(cbs_logfile) < 3:
        cbs_logfile = os.environ['WINDIR'] + "\\Logs\\CBS\\CBS.log"

    if not os.path.exists(cbs_logfile):
        raise FileNotFoundError("CBS Log File [{0}] does not exist!".format(cbs_logfile))

    finder = CBSFinder(cbs_logfile)

    input("Press Enter to continue...")