from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def keyword_extraction(request: web.Request, api_key, n=None, text=None) -> web.Response:
    """Extracts the Keywords of the Document

    The Keyword Extraction function enables you to extract from an arbitrary document all the keywords and word-combinations along with their occurrences in the text.

    :param api_key: Your API Key
    :type api_key: str
    :param n: The number of keyword combinations (n-grams) that you wish to extract.
    :type n: int
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def text_extraction(request: web.Request, api_key, text=None) -> web.Response:
    """Extracts the clear text from Webpage

    The Text Extraction function enables you to extract the important information from a given webpage. Extracting the clear text of the documents is an important step before any other analysis.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The HTML source of the webpage.
    :type text: str

    """
    return web.Response(status=200)
