from readgithubmd import ReadGithubMD
import os
import sys

rgm = ReadGithubMD("https://github.com/ismailpw/readgithubmd-python/blob/main/README.md")
with open(os.path.abspath(__file__) + "-test.html", 'w+') as fo:
    fo.write(rgm.get_mdfile_html())
    fo.flush()
    fo.close()