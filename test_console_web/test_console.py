from readgithubmd import ReadGithubMD

rgm = ReadGithubMD("https://github.com/themorpheustutorials/resources/blob/main/docs/books.md")
print(rgm.get_mdfile_html())