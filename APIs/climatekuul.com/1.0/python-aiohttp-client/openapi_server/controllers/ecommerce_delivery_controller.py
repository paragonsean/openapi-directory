from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def confirm_carbon_offset1(request: web.Request, carbon_offset, transaction_id, contact_email=None, contact_first_name=None, contact_last_name=None) -> web.Response:
    """confirmCarbonOffset

    

    :param carbon_offset: Confirm Carbon Offset (Value &#x3D; y/n)
    :type carbon_offset: str
    :param transaction_id: transaction_id
    :type transaction_id: str
    :param contact_email: Contact email
    :type contact_email: str
    :param contact_first_name: Contact first name
    :type contact_first_name: str
    :param contact_last_name: Contact last name
    :type contact_last_name: str

    """
    return web.Response(status=200)


async def confirm_payment1(request: web.Request, api_key_l1, api_key_l2, confirm_payment, payment_id, transaction_id) -> web.Response:
    """confirmPayment

    

    :param api_key_l1: apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    :type api_key_l1: str
    :param api_key_l2: apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    :type api_key_l2: str
    :param confirm_payment: Confirm Payment (Value &#x3D; y/n)
    :type confirm_payment: str
    :param payment_id: Payment Id
    :type payment_id: int
    :param transaction_id: transaction_id
    :type transaction_id: str

    """
    return web.Response(status=200)


async def confirm_payment_of_transaction1(request: web.Request, confirm_transaction, transaction_id) -> web.Response:
    """confirmTransaction

    

    :param confirm_transaction: Confirm Payment Of Transaction (Value &#x3D; y/n)
    :type confirm_transaction: str
    :param transaction_id: transaction_id
    :type transaction_id: str

    """
    return web.Response(status=200)


async def confirms_planting2(request: web.Request, api_key_l1, api_key_l2, confirm_planting, transaction_id) -> web.Response:
    """confirmPlanting

    

    :param api_key_l1: apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    :type api_key_l1: str
    :param api_key_l2: apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    :type api_key_l2: str
    :param confirm_planting: Confirm Planting (Value &#x3D; y/n)
    :type confirm_planting: str
    :param transaction_id: transaction_id
    :type transaction_id: str

    """
    return web.Response(status=200)


async def ecommerce_delivery(request: web.Request, content_type, api_key_l1, api_key_l2, destination_latitude, destination_longitude, origin_latitude, origin_longitude, volumetric_weight, waybill_type, destination_airport_code=None, origin_airport_code=None) -> web.Response:
    """ecommerceDelivery

    

    :param content_type: 
    :type content_type: str
    :param api_key_l1: Client Api Key
    :type api_key_l1: str
    :param api_key_l2: Integration Partner Api Key
    :type api_key_l2: str
    :param destination_latitude: valid latitude of destination
    :type destination_latitude: float
    :param destination_longitude: valid longitude of destination
    :type destination_longitude: float
    :param origin_latitude: valid latitude of origin
    :type origin_latitude: float
    :param origin_longitude: valid longitude of origin
    :type origin_longitude: float
    :param volumetric_weight: Volumetric weight&#39; (like:2.70)
    :type volumetric_weight: float
    :param waybill_type: this can be &#39;air only&#39;, &#39;road only&#39; or &#39;air and road&#39;
    :type waybill_type: str
    :param destination_airport_code: valid airport code of destination
    :type destination_airport_code: str
    :param origin_airport_code: valid airport code of origin
    :type origin_airport_code: str

    """
    return web.Response(status=200)
