# Gene-description-scrapper

## Description
<p id="Description">
  Takes a list of gene names, gets their summary from the NCBI database and writes them in a tab-separated format. I use it to add information to mutation lists obtained from whole exome sequencing.<br>
  While NCBI has a way to <a href="https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/languages/">build APIs</a> that is probably faster, it requires downloading the data to your machine and setting the environment up. Instead, this program automates command-line tool queries.
</p>

## Dependencies
<p id="Dependencies">
  Language: Python 3<br>
  Modules: logging, os, sys, and json (all part of the standard library).<br>
  File: datsets.exe installed in the same folder as the python file. Download from the NCBI <a href="https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/download-and-install/">command-line tools page</a>. The one included here is Windows 64-bit, up-to-date as of 01/05/2025.
</p>

## Usage
<p id="Usage">
  This program takes a list of gene names (found in "./input", basically a newline-separated list of gene names) in <a href="https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats#GRP:_Gene_set_file_format_.28.2A.grp.29">grp format</a> and an optional <a href="https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/api-keys/">NCBI API key</a> (also in "./input", which you can generate in your NCBI account settings), and returns a tab-separated list of gene summaries (in the format "Gene\tSummary\n".
</p>
