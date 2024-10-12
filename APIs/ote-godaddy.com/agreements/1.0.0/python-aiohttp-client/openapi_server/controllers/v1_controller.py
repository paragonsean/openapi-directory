from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.legal_agreement import LegalAgreement
from openapi_server import util


async def get(request: web.Request, keys, x_private_label_id=None, x_market_id=None) -> web.Response:
    """Retrieve Legal Agreements for provided agreements keys

    

    :param keys: Keys for Agreements whose details are to be retrieved
    :type keys: List[str]
    :param x_private_label_id: PrivateLabelId to operate as, if different from JWT
    :type x_private_label_id: int
    :param x_market_id: Unique identifier of the Market used to retrieve/translate Legal Agreements
    :type x_market_id: str

    """
    return web.Response(status=200)
