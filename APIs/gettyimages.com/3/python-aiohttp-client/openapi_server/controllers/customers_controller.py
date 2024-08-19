from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_info_response import CustomerInfoResponse
from openapi_server import util


async def v3_customers_current_get(request: web.Request, accept_language=None) -> web.Response:
    """Returns information about the current user.

    Returns the first, middle and last name of the authenticated user.  You&#39;ll need an API key and access token to use this resource.   Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)
