from os import environ
from os.path import expanduser
home = expanduser("~")

# path to the data directory
data_dir_path = environ.get("ALGORAND_DATA", home + "/node/testnetdata")
kmd_folder_name = "kmd-v0.5"

if data_dir_path and kmd_folder_name:
    if not data_dir_path[-1] == "/":
        data_dir_path += "/"
    if not kmd_folder_name[-1] == "/":
        kmd_folder_name += "/"
    algod_token = open(data_dir_path + "algod.token", "r").read().strip("\n")
    algod_address = "http://" + open(data_dir_path + "algod.net", "r").read().strip("\n")
    kmd_token = open(data_dir_path + kmd_folder_name + "kmd.token", "r").read().strip("\n")
    kmd_address = "http://" + open(data_dir_path + kmd_folder_name + "kmd.net", "r").read().strip("\n")