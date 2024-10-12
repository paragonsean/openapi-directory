from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.payment_term_types_get200_response import PaymentTermTypesGet200Response
from openapi_server.models.payment_term_types_payment_term_type_id_get200_response import PaymentTermTypesPaymentTermTypeIdGet200Response
from openapi_server import util


async def payment_term_types_get(request: web.Request, ) -> web.Response:
    """Get a list of payment term types

    


    """
    return web.Response(status=200)


async def payment_term_types_payment_term_type_id_get(request: web.Request, payment_term_type_id) -> web.Response:
    """Details of 1 payment term type

    

    :param payment_term_type_id: 
    :type payment_term_type_id: str

    """
    return web.Response(status=200)
