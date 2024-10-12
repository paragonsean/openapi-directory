from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetchrequest import Fetchrequest
from openapi_server import util


async def fetch(request: web.Request, body) -> web.Response:
    """Download web page content

    Use fetch endpoint to download web pages.

    :param body: - _Base fetcher type_ is the right choice for fetching server-side rendered pages. It takes fewer resources and works faster than rendering HTML with _Chrome fetcher_ - But for rendering Angular, React, and Vue.js web sites, you should always specify _Chrome fetcher type_. In this case, headless chrome fetcher renders dynamic Javascript content in the same way as real web browsers would do it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/render-web](https://dataflowkit.com/render-web) 
    :type body: dict | bytes

    """
    body = Fetchrequest.from_dict(body)
    return web.Response(status=200)
