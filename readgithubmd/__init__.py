# External libraries
from bs4 import BeautifulSoup
from bs4.element import PageElement
import requests
from markdownify import markdownify

# Exceptions
from readgithubmd.exceptions import LinkDoesNotExist

class ReadGithubMD:
# Public:                 -> I know i like c++ :>
    def __init__(self, md_link) -> None:
        try:
            self.md_link = md_link
            self.md_link_content = requests.get(self.md_link).content
            
            self.md_link_soup:BeautifulSoup = BeautifulSoup(
                self.md_link_content, 
                'html.parser'
            )

            self.mdfile_html:PageElement = self.md_link_soup.find(
                "article",
                {"class": "markdown-body entry-content container-lg"}
            )

        except:
            raise LinkDoesNotExist()

    def get_mdfile_html(self) -> str:
        style:str = "<style>.markdown-body { word-wrap: break-word; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size: 16px; line-height: 1.5;}</style>"

        return style + "\n" + str(self.mdfile_html)

    def get_mdfile_md(self) -> str:
        return str(
            markdownify(
                str(self.mdfile_html)  
            )
        )