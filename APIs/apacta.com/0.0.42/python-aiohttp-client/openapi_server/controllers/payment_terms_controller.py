from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.payment_terms_erp_get200_response import PaymentTermsErpGet200Response
from openapi_server.models.payment_terms_get200_response import PaymentTermsGet200Response
from openapi_server.models.payment_terms_payment_term_id_get200_response import PaymentTermsPaymentTermIdGet200Response
from openapi_server import util


async def payment_terms_erp_get(request: web.Request, ) -> web.Response:
    """Get integration payment terms list

    


    """
    return web.Response(status=200)


async def payment_terms_get(request: web.Request, ) -> web.Response:
    """Get a list of payment terms

    


    """
    return web.Response(status=200)


async def payment_terms_payment_term_id_get(request: web.Request, payment_term_id) -> web.Response:
    """Details of 1 payment term

    

    :param payment_term_id: 
    :type payment_term_id: str

    """
    return web.Response(status=200)
