from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def airtravel_coordinates(request: web.Request, content_type, api_key_l1, api_key_l2, destination_airport_latitude, destination_airport_longitude, number_of_passengers, origin_airport_latitude, origin_airport_longitude, travel_class, travel_mode) -> web.Response:
    """airtravelCoordinates

    

    :param content_type: 
    :type content_type: str
    :param api_key_l1: Client Api Key
    :type api_key_l1: str
    :param api_key_l2: Integration Partner Api Key
    :type api_key_l2: str
    :param destination_airport_latitude: Destination latitude (like:  50.870752, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90)
    :type destination_airport_latitude: float
    :param destination_airport_longitude: Destination longitude (like:  4.669490, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180)
    :type destination_airport_longitude: float
    :param number_of_passengers: Number of passengers (like: 1, 2 ,3 )
    :type number_of_passengers: int
    :param origin_airport_latitude: Origin latitude (like: 23.372628 value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90 )
    :type origin_airport_latitude: float
    :param origin_airport_longitude: Origin longitude (like: 113.159339, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180 )
    :type origin_airport_longitude: float
    :param travel_class: Travel class can be &#39;First Class&#39;, &#39;Economy&#39;, &#39;Business&#39; or &#39;Premium Economy&#39;
    :type travel_class: str
    :param travel_mode: Travel mode can be &#39;one way&#39; or &#39;round trip&#39;
    :type travel_mode: str

    """
    return web.Response(status=200)


async def confirm_carbon_offset4(request: web.Request, carbon_offset, transaction_id, contact_email=None, contact_first_name=None, contact_last_name=None) -> web.Response:
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


async def confirm_payment4(request: web.Request, api_key_l1, api_key_l2, confirm_payment, payment_id, transaction_id) -> web.Response:
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


async def confirm_payment_of_transaction4(request: web.Request, confirm_transaction, transaction_id) -> web.Response:
    """confirmTransaction

    

    :param confirm_transaction: Confirm Payment Of Transaction (Value &#x3D; y/n)
    :type confirm_transaction: str
    :param transaction_id: transaction_id
    :type transaction_id: str

    """
    return web.Response(status=200)


async def confirms_planting4(request: web.Request, api_key_l1, api_key_l2, confirm_planting, transaction_id) -> web.Response:
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
