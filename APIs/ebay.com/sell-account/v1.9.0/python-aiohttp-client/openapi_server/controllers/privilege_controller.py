from typing import List, Dict
from aiohttp import web

from openapi_server.models.selling_privileges import SellingPrivileges
from openapi_server import util


async def get_privileges(request: web.Request, ) -> web.Response:
    """get_privileges

    This method retrieves the seller&#39;s current set of privileges, including whether or not the seller&#39;s eBay registration has been completed, as well as the details of their site-wide &lt;b&gt;sellingLimt&lt;/b&gt; (the amount and quantity they can sell on a given day).


    """
    return web.Response(status=200)
