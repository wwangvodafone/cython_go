import argparse
import time
import os, glob
import sys
import shutil
import json
import csv

calender = ["20221127","20221128","20221129","20221130","20221201","20221202","20221203","20221204","20221205","20221206","20221207","20221208","20221209","20221210","20221211","20221212","20221213","20221214","20221215","20221216","20221217","20221218","20221219","20221220","20221221","20221222","20221223","20221224","20221225","20221226","20221227","20221228","20221229","20221230","20221231","20230101","20230102","20230103","20230104","20230105","20230106","20230107","20230108","20230109","20230110","20230111","20230112","20230113","20230114","20230115","20230116","20230117","20230118","20230119","20230120","20230121","20230122","20230123","20230124","20230125","20230126","20230127","20230128","20230129","20230130","20230131","20230201","20230202","20230203","20230204","20230205","20230206","20230207","20230208","20230209","20230210","20230211","20230212","20230213","20230214","20230215","20230216","20230217","20230218","20230219","20230220","20230221","20230222","20230223","20230224","20230225","20230226"]
def start_process(folder):
    filepaths = folder + '*'
    filepaths = [filepath for filepath in glob.glob(filepaths) if os.path.basename(filepath).endswith('.parquet')]
    for file in filepaths:
        pos = file.rfind("SimTrn")
        filename = file[pos:]
        new_file_list = [x + filename for x in calender]
        for new_file in new_file_list:
            new_file = os.path.join(folder, new_file)
            shutil.copyfile(file, new_file)
    filepaths = folder + '*'
    filepaths = [filepath for filepath in glob.glob(filepaths) if os.path.basename(filepath).endswith('.txt')]
    for file in filepaths:
        pos = file.rfind("SimTrn")
        filename = file[pos:]
        new_file_list = [x + filename for x in calender]
        for new_file in new_file_list:
            new_file = os.path.join(folder, new_file)
            shutil.copyfile(file, new_file)
def main(run_py_file):
    '''
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=str, required=True, help="importanceファイルのフォルダー")
    args = parser.parse_args()
    folder = args.folder

    start_process(folder)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    main(__file__)
    sys.exit(0)
