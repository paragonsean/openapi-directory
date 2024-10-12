from typing import List, Dict
from aiohttp import web

from openapi_server.models.body import Body
from openapi_server.models.payment_data import PaymentData
from openapi_server.models.payment_provider import PaymentProvider
from openapi_server import util


async def delete_organisations_id_payments_billings_bid_1(request: web.Request, id, bid) -> web.Response:
    """delete_organisations_id_payments_billings_bid_1

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def delete_organisations_id_payments_recurring_1(request: web.Request, id) -> web.Response:
    """delete_organisations_id_payments_recurring_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_self_payments_billings_bid_0(request: web.Request, bid) -> web.Response:
    """delete_self_payments_billings_bid_0

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def delete_self_payments_methods_mid_0(request: web.Request, m_id) -> web.Response:
    """delete_self_payments_methods_mid_0

    

    :param m_id: 
    :type m_id: str

    """
    return web.Response(status=200)


async def delete_self_payments_recurring_0(request: web.Request, ) -> web.Response:
    """delete_self_payments_recurring_0

    


    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_1(request: web.Request, id) -> web.Response:
    """get_organisations_id_payments_billings_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_bid_1(request: web.Request, id, bid) -> web.Response:
    """get_organisations_id_payments_billings_bid_1

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_bid_pdf_1(request: web.Request, id, bid, token=None) -> web.Response:
    """get_organisations_id_payments_billings_bid_pdf_1

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_full_price_price_1(request: web.Request, id, price) -> web.Response:
    """get_organisations_id_payments_full_price_price_1

    

    :param id: 
    :type id: str
    :param price: 
    :type price: str

    """
    return web.Response(status=200)


async def get_payments_coupons_name_0(request: web.Request, name) -> web.Response:
    """get_payments_coupons_name_0

    

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_payments_providers_0(request: web.Request, ) -> web.Response:
    """get_payments_providers_0

    


    """
    return web.Response(status=200)


async def get_payments_tokens_stripe_0(request: web.Request, ) -> web.Response:
    """get_payments_tokens_stripe_0

    


    """
    return web.Response(status=200)


async def get_self_payments_billings_0(request: web.Request, ) -> web.Response:
    """get_self_payments_billings_0

    


    """
    return web.Response(status=200)


async def get_self_payments_billings_bid_0(request: web.Request, bid) -> web.Response:
    """get_self_payments_billings_bid_0

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def get_self_payments_billings_bid_pdf_0(request: web.Request, bid, token=None) -> web.Response:
    """get_self_payments_billings_bid_pdf_0

    

    :param bid: 
    :type bid: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_self_payments_fullprice_price_0(request: web.Request, price) -> web.Response:
    """get_self_payments_fullprice_price_0

    

    :param price: 
    :type price: str

    """
    return web.Response(status=200)


async def get_self_payments_methods_0(request: web.Request, ) -> web.Response:
    """get_self_payments_methods_0

    


    """
    return web.Response(status=200)


async def organisations_id_payments_billings_unpaid_get_1(request: web.Request, id) -> web.Response:
    """organisations_id_payments_billings_unpaid_get_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_default_get_1(request: web.Request, id) -> web.Response:
    """organisations_id_payments_methods_default_get_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_default_put_1(request: web.Request, id, body) -> web.Response:
    """organisations_id_payments_methods_default_put_1

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentData.from_dict(body)
    return web.Response(status=200)


async def organisations_id_payments_methods_get_1(request: web.Request, id) -> web.Response:
    """organisations_id_payments_methods_get_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_mid_delete_1(request: web.Request, m_id, id) -> web.Response:
    """organisations_id_payments_methods_mid_delete_1

    

    :param m_id: 
    :type m_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_post_1(request: web.Request, id, body) -> web.Response:
    """organisations_id_payments_methods_post_1

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def organisations_id_payments_monthlyinvoice_get_1(request: web.Request, id) -> web.Response:
    """organisations_id_payments_monthlyinvoice_get_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_monthlyinvoice_maxcredit_put_1(request: web.Request, id) -> web.Response:
    """organisations_id_payments_monthlyinvoice_maxcredit_put_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_recurring_get_1(request: web.Request, id) -> web.Response:
    """organisations_id_payments_recurring_get_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def payments_assets_pay_button_token_button_png_get_0(request: web.Request, token) -> web.Response:
    """payments_assets_pay_button_token_button_png_get_0

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def payments_bid_end_stripe_post_0(request: web.Request, bid) -> web.Response:
    """payments_bid_end_stripe_post_0

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def post_organisations_id_payments_billings_1(request: web.Request, id) -> web.Response:
    """post_organisations_id_payments_billings_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_self_payments_billings_0(request: web.Request, ) -> web.Response:
    """post_self_payments_billings_0

    


    """
    return web.Response(status=200)


async def post_self_payments_methods_0(request: web.Request, ) -> web.Response:
    """post_self_payments_methods_0

    


    """
    return web.Response(status=200)


async def put_organisations_id_payments_billings_bid_1(request: web.Request, id, bid) -> web.Response:
    """put_organisations_id_payments_billings_bid_1

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def put_self_payments_billings_bid_0(request: web.Request, bid) -> web.Response:
    """put_self_payments_billings_bid_0

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def self_payments_methods_default_get_0(request: web.Request, ) -> web.Response:
    """self_payments_methods_default_get_0

    


    """
    return web.Response(status=200)


async def self_payments_methods_default_put_0(request: web.Request, ) -> web.Response:
    """self_payments_methods_default_put_0

    


    """
    return web.Response(status=200)


async def self_payments_monthlyinvoice_get_0(request: web.Request, ) -> web.Response:
    """self_payments_monthlyinvoice_get_0

    


    """
    return web.Response(status=200)


async def self_payments_monthlyinvoice_maxcredit_put_0(request: web.Request, ) -> web.Response:
    """self_payments_monthlyinvoice_maxcredit_put_0

    


    """
    return web.Response(status=200)


async def self_payments_recurring_get_0(request: web.Request, ) -> web.Response:
    """self_payments_recurring_get_0

    


    """
    return web.Response(status=200)


async def self_payments_tokens_stripe_get_0(request: web.Request, ) -> web.Response:
    """self_payments_tokens_stripe_get_0

    


    """
    return web.Response(status=200)
