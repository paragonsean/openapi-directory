from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_agreements_data_agreement_interface import CheckoutAgreementsDataAgreementInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def checkout_agreements_checkout_agreements_repository_v1_get_list_get(request: web.Request, ) -> web.Response:
    """carts/licence

    Lists active checkout agreements.


    """
    return web.Response(status=200)
