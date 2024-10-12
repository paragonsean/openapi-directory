from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def confirm_carbon_offset5(request: web.Request, carbon_offset, transaction_id, contact_email=None, contact_first_name=None, contact_last_name=None) -> web.Response:
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


async def confirm_payment5(request: web.Request, api_key_l1, api_key_l2, confirm_payment, payment_id, transaction_id) -> web.Response:
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


async def confirm_payment_of_transaction5(request: web.Request, confirm_transaction, transaction_id) -> web.Response:
    """confirmTransaction

    

    :param confirm_transaction: Confirm Payment Of Transaction (Value &#x3D; y/n)
    :type confirm_transaction: str
    :param transaction_id: transaction_id
    :type transaction_id: str

    """
    return web.Response(status=200)


async def confirms_planting5(request: web.Request, api_key_l1, api_key_l2, confirm_planting, transaction_id) -> web.Response:
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


async def road_distance(request: web.Request, api_key_l1, api_key_l2, travel_distance, trip_end, trip_start, vehicle_type, vehicle_make=None, vehicle_year=None) -> web.Response:
    """RoadDistance

    

    :param api_key_l1: Client Api Key
    :type api_key_l1: str
    :param api_key_l2: Integration Partner Api Key
    :type api_key_l2: str
    :param travel_distance: 
    :type travel_distance: int
    :param trip_end: timestamp in epoch time (like: 1606780799)
    :type trip_end: int
    :param trip_start: timestamp in epoch time (like: 1604188800)
    :type trip_start: int
    :param vehicle_type: Vehicle type can be &#39;personal car&#39;, &#39;light truck&#39; or &#39;heavy-duty truck&#39;
    :type vehicle_type: str
    :param vehicle_make: vehicle make (like: Honda, Toyota, Smart), Required only when vehicle_type is &#39;personal car&#39; 
    :type vehicle_make: str
    :param vehicle_year: vehicle year (like: 2010, 2015, 2019), Required only when vehicle_type is &#39;personal car&#39; 
    :type vehicle_year: int

    """
    return web.Response(status=200)
