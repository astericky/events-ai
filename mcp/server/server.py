import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from mcp.server.fastmcp import FastMCP
from common.paths import Paths
from bs4 import BeautifulSoup

# Create an MCP server
mcp = FastMCP("Demo")



@mcp.tool()
def recommendations(number_of_items : int = 10) -> str:
    """
        Returns recommendations in html format that have been suggested for the day.
        This takes an optional argument for how many results to retrieve
        from recommendations that have been bound to the file system
        from a pre-fetch operation. The number of arguments must be positive and
        non-zero.

        For instructions about how to pre-fetch recommendations, please
        see the README.md
    """

    html_file = os.path.join(Paths.DATA_DIR, "all.html")
    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    ul = soup.find('ul')
    list_items = ul.find_all('li')

    top_items = list_items[:number_of_items]

    ul_to_return = soup.new_tag('ul')
    for item in top_items:
        ul_to_return.append(item)

    return ul_to_return.prettify()
        


    


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"

if __name__ == "__main__":
    # mcp.run()
    print(recommendations())