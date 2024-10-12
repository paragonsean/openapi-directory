from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def confirm_carbon_offset(request: web.Request, carbon_offset, transaction_id, contact_email=None, contact_first_name=None, contact_last_name=None) -> web.Response:
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


async def confirm_payment(request: web.Request, api_key_l1, api_key_l2, confirm_payment, payment_id, transaction_id) -> web.Response:
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


async def confirm_payment_of_transaction(request: web.Request, confirm_transaction, transaction_id) -> web.Response:
    """confirmTransaction

    

    :param confirm_transaction: Confirm Payment Of Transaction (Value &#x3D; y/n)
    :type confirm_transaction: str
    :param transaction_id: transaction_id
    :type transaction_id: str

    """
    return web.Response(status=200)


async def confirms_planting(request: web.Request, api_key_l1, api_key_l2, confirm_planting, transaction_id) -> web.Response:
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


async def urban_delivery(request: web.Request, api_key_l1, api_key_l2, destination_latitude, destination_longitude, item_count, origin_latitude, origin_longitude, vehicle_type) -> web.Response:
    """urbanDelivery

    

    :param api_key_l1: Client Api Key
    :type api_key_l1: str
    :param api_key_l2: Integration Partner Api Key
    :type api_key_l2: str
    :param destination_latitude: Destination latitude (like: 50.870752, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90)
    :type destination_latitude: float
    :param destination_longitude: Destination longitude (like: 4.669490, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180)
    :type destination_longitude: float
    :param item_count: item_count&#39; (like:2, value &#x3D; 0&lt;x&lt;&#x3D;100)
    :type item_count: int
    :param origin_latitude: Origin latitude (like: 23.372628, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90)
    :type origin_latitude: float
    :param origin_longitude: Origin longitude (like: 113.159339, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180)
    :type origin_longitude: float
    :param vehicle_type: Vehicle type (like: private car, motorcycle,cargo van,zero-emission)
    :type vehicle_type: str

    """
    return web.Response(status=200)
