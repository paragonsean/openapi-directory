from typing import List, Dict
from aiohttp import web

from openapi_server.models.url2pdfrequest import Url2pdfrequest
from openapi_server import util


async def url_to_pdf(request: web.Request, body) -> web.Response:
    """Save web page as PDF

    Automate URL to PDF Conversion right in your application.  Specify request parameters like URL, Proxy, and actions to render web pages to PDF using Headless Chrome.  Get resulted PDF even from websites blocked in your area for some reason utilizing our worldwide pool of proxies.  Simulate real-world human interaction with the page. For example, before saving a web page to PDF, you may need to scroll it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/url-to-pdf](https://dataflowkit.com/url-to-pdf)

    :param body: 
    :type body: dict | bytes

    """
    body = Url2pdfrequest.from_dict(body)
    return web.Response(status=200)
