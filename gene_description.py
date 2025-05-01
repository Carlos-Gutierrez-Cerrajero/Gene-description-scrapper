###Gene description
#Reads a list of genes from ./input/gene_list.grp, with an optional api key (./input/api_key.txt) to speed up querying
#Queries NCBI database by automating command line tools and returns a list in ./output/result.tab in the format "Gene\tSummary\n"

#Define a function to display message and exit program
def critical_error(message):
    logging.critical(message)
    logging.info("Press enter to Quit")
    input()
    exit()

#Import necessary modules
try:
    import logging
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s", datefmt="%H:%M:%S")
    import os
    import sys
    import json
except ModuleNotFoundError:
    critical_error("Module not found, please make sure all required modules are installed")

#Change working directory to the python file location
os.chdir(sys.path[0])

#Check if there is an api key file and if it has information. This is not necessary, but doubles query speed
api_key_path ="./input/api_key.txt"
if os.path.exists(api_key_path):
    with open(api_key_path, "r") as api_key_file:
        api_key = api_key_file.read()
    if api_key == "":
        logging.warning("No api key in file. Continuing without API key, query speed will be reduced")
else:

    logging.warning("No api_key.txt file found in input folder. Continuing without API key, query speed will be reduced")
    api_key = ""

#Checks if there is a non-empty gene list and if there is, generates gene list
gene_list_path = "./input/gene_list.grp"
if not os.path.exists(gene_list_path):
    critical_error("No gene_list.grp file found in input folder")
with open(gene_list_path, "r") as gene_list_file:
    gene_list = [gene for gene in gene_list_file.read().split("\n") if gene != ""]
if gene_list == []:
    critical_error("Gene list is empty")

#Checks if datasets.exe is in current folder
if not os.path.exists("./datasets.exe"):
    critical_error("datasets.exe not in installation folder")

#Creates output directory if absent
if not os.path.exists("./output"):
    os.mkdir("./output")

#Queries NCBI database using datasets command line tools, extracts informations and writes it to file
with open("./output/result.tab", "w") as output_file:
    output_file.write("Gene\tSummary\n")
    for gene in gene_list:
        logging.info("Processing: " + gene)
        try:
            res = os.popen(f"datasets summary gene symbol {gene} --api-key string {api_key}")
            res_dict = json.loads(res.read())
            summary = res_dict["reports"][0]["gene"]["summary"][0]["description"]
            output_file.write(gene + "\t" + summary + "\n")
        except:
            output_file.write(gene + "\tNA\n")
