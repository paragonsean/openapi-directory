from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def v1_order_feedback_post(request: web.Request, id, key, action, format=None, notes=None) -> web.Response:
    """v1_order_feedback_post

    Feedback the status of an order transaction.

    :param id: 
    :type id: str
    :param key: 
    :type key: str
    :param action: 
    :type action: str
    :param format: 
    :type format: str
    :param notes: 
    :type notes: str

    """
    return web.Response(status=200)


async def v1_order_screen_post(request: web.Request, ip, key, format=None, last_name=None, first_name=None, bill_addr=None, bill_city=None, bill_state=None, bill_country=None, bill_zip_code=None, ship_addr=None, ship_city=None, ship_state=None, ship_country=None, ship_zip_code=None, email_domain=None, user_phone=None, email=None, email_hash=None, username_hash=None, password_hash=None, bin_no=None, card_hash=None, avs_result=None, cvv_result=None, user_order_id=None, user_order_memo=None, amount=None, quantity=None, currency=None, department=None, payment_mode=None, flp_checksum=None) -> web.Response:
    """v1_order_screen_post

    Screen order for payment fraud.

    :param ip: 
    :type ip: str
    :param key: 
    :type key: str
    :param format: 
    :type format: str
    :param last_name: 
    :type last_name: str
    :param first_name: 
    :type first_name: str
    :param bill_addr: 
    :type bill_addr: str
    :param bill_city: 
    :type bill_city: str
    :param bill_state: 
    :type bill_state: str
    :param bill_country: 
    :type bill_country: str
    :param bill_zip_code: 
    :type bill_zip_code: str
    :param ship_addr: 
    :type ship_addr: str
    :param ship_city: 
    :type ship_city: str
    :param ship_state: 
    :type ship_state: str
    :param ship_country: 
    :type ship_country: str
    :param ship_zip_code: 
    :type ship_zip_code: str
    :param email_domain: 
    :type email_domain: str
    :param user_phone: 
    :type user_phone: str
    :param email: 
    :type email: str
    :param email_hash: 
    :type email_hash: str
    :param username_hash: 
    :type username_hash: str
    :param password_hash: 
    :type password_hash: str
    :param bin_no: 
    :type bin_no: str
    :param card_hash: 
    :type card_hash: str
    :param avs_result: 
    :type avs_result: str
    :param cvv_result: 
    :type cvv_result: str
    :param user_order_id: 
    :type user_order_id: str
    :param user_order_memo: 
    :type user_order_memo: str
    :param amount: 
    :type amount: 
    :param quantity: 
    :type quantity: int
    :param currency: 
    :type currency: str
    :param department: 
    :type department: str
    :param payment_mode: 
    :type payment_mode: str
    :param flp_checksum: 
    :type flp_checksum: str

    """
    return web.Response(status=200)
