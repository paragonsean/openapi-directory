from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_pci_url_request import GetPciUrlRequest
from openapi_server.models.get_pci_url_response import GetPciUrlResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_get_pci_questionnaire_url(request: web.Request, body=None) -> web.Response:
    """Get a link to a PCI compliance questionnaire

    Returns a link to a PCI compliance questionnaire that you can send to your account holder.  &gt; You should only use this endpoint if you have a [partner platform setup](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners).

    :param body: 
    :type body: dict | bytes

    """
    body = GetPciUrlRequest.from_dict(body)
    return web.Response(status=200)
