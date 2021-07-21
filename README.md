# readgithubmd
A python package to read markdown files on GitHub repositories(.md) and convert them into html or md.

> ## Small Documentation
1. import readgithubmd
  * example: `from readgithubmd import ReadGithubMD`
2. create instance of ReadGithubMD
  * Params: Link of the md-file on github
  * Example: `rgm:ReadGithubMD = ReadGithubMD("https://github.com/ismailpw/readgithubmd-python/blob/main/README.md")`
3. get_mdfile_html(function)
  * params: no
  * returns the html-script of the md-file on github
  * example: `print(rgm.get_mdfile_html())`
4. get_mdfile_md
  * params: no
  * returns the md-script of the md-file on github
  * example `print(rgm.get_mdfile_md())`
