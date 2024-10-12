from typing import List, Dict
from aiohttp import web

from openapi_server.models.qrcode_decode_post_request import QrcodeDecodePostRequest
from openapi_server import util


async def qrcode_business_card_get(request: web.Request, firstname, lastname, email, middlename=None, company=None, phone_work=None, phone_home=None, phone_cell=None, street1=None, street2=None, city=None, zip=None, state=None, country=None, format=None) -> web.Response:
    """qrcode_business_card_get

    Get a QR Code image for a business card aka VCARD

    :param firstname: First Name
    :type firstname: str
    :param lastname: Last Name
    :type lastname: str
    :param email: Email id
    :type email: str
    :param middlename: Middle Name
    :type middlename: str
    :param company: Company Name
    :type company: str
    :param phone_work: Work Phone Number
    :type phone_work: str
    :param phone_home: Home Phone Number
    :type phone_home: str
    :param phone_cell: Cell Phone Number
    :type phone_cell: str
    :param street1: Street Address
    :type street1: str
    :param street2: Street Address 2
    :type street2: str
    :param city: City
    :type city: str
    :param zip: Zip Code
    :type zip: str
    :param state: State
    :type state: str
    :param country: Country
    :type country: str
    :param format: Output image format. Must be one of png/eps/raw/svg
    :type format: str

    """
    return web.Response(status=200)


async def qrcode_decode_post(request: web.Request, body) -> web.Response:
    """qrcode_decode_post

    Decode a QR Code image and return the cotents if successful

    :param body: 
    :type body: dict | bytes

    """
    body = QrcodeDecodePostRequest.from_dict(body)
    return web.Response(status=200)


async def qrcode_email_get(request: web.Request, email, subject=None, body=None, format=None) -> web.Response:
    """qrcode_email_get

    Get a QR Code image for an email

    :param email: Email id to send the email to
    :type email: str
    :param subject: Subject of the email(optional)
    :type subject: str
    :param body: Body of the email(optional)
    :type body: str
    :param format: Output image format. Must be one of png/png/eps/raw/svg
    :type format: str

    """
    return web.Response(status=200)


async def qrcode_phone_get(request: web.Request, number, format=None) -> web.Response:
    """qrcode_phone_get

    Get a QR Code image for a phone number

    :param number: Phone Number
    :type number: str
    :param format: Output image format. Must be one of png/eps/raw/svg
    :type format: str

    """
    return web.Response(status=200)


async def qrcode_raw_get(request: web.Request, rawtext, format=None) -> web.Response:
    """qrcode_raw_get

    Get a QR Code image for a block of raw data

    :param rawtext: Raw Text value
    :type rawtext: str
    :param format: Output image format. Must be one of png/eps/raw/svg
    :type format: str

    """
    return web.Response(status=200)


async def qrcode_skype_get(request: web.Request, username, format=None) -> web.Response:
    """qrcode_skype_get

    Get a QR Code image for a skype user

    :param username: Skype User name
    :type username: str
    :param format: Output image format. Must be one of png/eps/raw/svg
    :type format: str

    """
    return web.Response(status=200)


async def qrcode_sms_get(request: web.Request, number, format=None) -> web.Response:
    """qrcode_sms_get

    Get a QR Code image for a Phone number for SMS messaging

    :param number: Phone Number to SMS
    :type number: str
    :param format: Output image format. Must be one of png/eps/raw/svg
    :type format: str

    """
    return web.Response(status=200)


async def qrcode_text_get(request: web.Request, text, format=None) -> web.Response:
    """qrcode_text_get

    Get a QR Code image for a block of text

    :param text: Text value
    :type text: str
    :param format: Output image format. Must be one of png/eps/raw/svg
    :type format: str

    """
    return web.Response(status=200)


async def qrcode_url_get(request: web.Request, url, format=None) -> web.Response:
    """qrcode_url_get

    Get a QR Code image for a url

    :param url: URL value
    :type url: str
    :param format: Output image format. Must be one of png/raw/eps/svg
    :type format: str

    """
    return web.Response(status=200)
