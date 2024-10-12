from typing import List, Dict
from aiohttp import web

from openapi_server.models.collections_list import CollectionsList
from openapi_server import util


async def v3_collections_get(request: web.Request, accept_language=None) -> web.Response:
    """Gets collections applicable for the customer.

    Use this endpoint to retrieve collections associated with your Getty Images account. To browse available collections see our [Image collections page]( http://www.gettyimages.com/creative-images/collections).  You&#39;ll need an API key and access token to use this resource. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)
