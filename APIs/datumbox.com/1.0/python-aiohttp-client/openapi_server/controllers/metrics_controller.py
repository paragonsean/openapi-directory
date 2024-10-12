from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def document_similarity(request: web.Request, api_key, copy=None, original=None) -> web.Response:
    """Estimates the similarity between 2 Documents

    The Document Similarity function estimates the degree of similarity between two documents. It can be used to detect duplicate webpages or detect plagiarism.

    :param api_key: Your API Key
    :type api_key: str
    :param copy: The second text. It should not contain HTML tags.
    :type copy: str
    :param original: The first text. It should not contain HTML tags.
    :type original: str

    """
    return web.Response(status=200)
