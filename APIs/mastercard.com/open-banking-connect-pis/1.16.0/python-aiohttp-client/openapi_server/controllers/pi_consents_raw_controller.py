from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_consents_raw_ok_body import PostPaymentsConsentsRawOKBody
from openapi_server.models.post_payments_consents_raw_params_body import PostPaymentsConsentsRawParamsBody
from openapi_server import util


async def payments_consents_raw_post(request: web.Request, body) -> web.Response:
    """Extracts the original raw consent given by the aspsp

    Extracts the original raw consent given by the aspsp

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostPaymentsConsentsRawParamsBody.from_dict(body)
    return web.Response(status=200)
