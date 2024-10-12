from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_vendor_get(request: web.Request, duns) -> web.Response:
    """This endpoint returns a single vendor by their 9 digit DUNS number

    &lt;p&gt;This endpoint returns a single vendor by their 9 digit DUNS number. DUNS numbers can be looked up in the &lt;a href&#x3D;\&quot;https://www.sam.gov\&quot;&gt;System for Award Management&lt;/a&gt; by vendor name.&lt;/p&gt;

    :param duns: a nine digit DUNS number that uniquely identifies the vendor (required)
    :type duns: str

    """
    return web.Response(status=200)
