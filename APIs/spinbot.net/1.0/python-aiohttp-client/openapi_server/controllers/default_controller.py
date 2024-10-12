from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_info(request: web.Request, key) -> web.Response:
    """Return the user credit information.

    Return the user credit information.

    :param key: Your api key
    :type key: str

    """
    return web.Response(status=200)


async def post_article(request: web.Request, key, url, faster_mode=None) -> web.Response:
    """Extracting the main article of the given URL.

    Extracting the main article of the given URL. The response is in JSON format.

    :param key: Your spinbot API key
    :type key: str
    :param url: The url of target article
    :type url: str
    :param faster_mode: you can set this input value to 1 to skip detecting the size (width and height in pixel) of all the images inside the extracted article. The response time of your request will be shortened if you set this input value to 1.
    :type faster_mode: str

    """
    return web.Response(status=200)


async def post_pretty_spinner(request: web.Request, key, text, keep, accuracy) -> web.Response:
    """Human readable auto rewrite your article.

    Human readable auto rewrite your article. The response is in JSON format.

    :param key: Your spinbot API key
    :type key: str
    :param text: Input article that need to be rewrited.
    :type text: str
    :param keep: Keep words/phrases, separated by newline, those remain unchanged during the rewrite process.
    :type keep: str
    :param accuracy: Rewrite accuracy profile, accepted values are very-low, low, medium, high, very-high
    :type accuracy: str

    """
    return web.Response(status=200)


async def post_spinner(request: web.Request, key, text) -> web.Response:
    """Rewriting (spinning) your input article.

    Rewriting (spinning) you input article. The response is in JSON format.

    :param key: Your spinbot API key
    :type key: str
    :param text: Input article that need to be rewrited.
    :type text: str

    """
    return web.Response(status=200)


async def post_spintax(request: web.Request, key, text, full_mode=None) -> web.Response:
    """Generate Spintax format for the input article

    Generate Spintax format for the input article, so you can rewrite it yourself. The response is in JSON format.

    :param key: Your spinbot API key
    :type key: str
    :param text: Input article that need to be rewritten.
    :type text: str
    :param full_mode: Full mode option.
    :type full_mode: str

    """
    return web.Response(status=200)
