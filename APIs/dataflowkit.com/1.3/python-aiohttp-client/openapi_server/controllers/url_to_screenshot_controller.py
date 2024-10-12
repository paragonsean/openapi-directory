from typing import List, Dict
from aiohttp import web

from openapi_server.models.url2screenshotrequest import Url2screenshotrequest
from openapi_server import util


async def url_to_screenshot(request: web.Request, body) -> web.Response:
    """Capture web page Screenshots.

    Automate URL to Screenshot Conversion right in your application.  Specify request parameters like URL, Proxy, and actions to convert web pages to screenshots using Headless Chrome.  Get resulted pictures in JPG or PNG formats even from websites blocked in your area for some reason utilizing our worldwide pool of proxies.  Simulate real-world human interaction with the page. For example, before capturing a web page, you may need to scroll it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/url-to-screenshot](https://dataflowkit.com/url-to-screenshot)

    :param body: 
    :type body: dict | bytes

    """
    body = Url2screenshotrequest.from_dict(body)
    return web.Response(status=200)
