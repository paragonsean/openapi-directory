from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_qr_code import AutoQRCode
from openapi_server.models.auto_qr_code_multipart_body import AutoQRCodeMultipartBody
from openapi_server.models.contact_qr_code import ContactQRCode
from openapi_server.models.contact_qr_code_multipart_body import ContactQRCodeMultipartBody
from openapi_server.models.crypto_payment_qr_code import CryptoPaymentQRCode
from openapi_server.models.crypto_payment_qr_code_multipart_body import CryptoPaymentQRCodeMultipartBody
from openapi_server.models.email_qr_code import EmailQRCode
from openapi_server.models.email_qr_code_multipart_body import EmailQRCodeMultipartBody
from openapi_server.models.generic_error import GenericError
from openapi_server.models.geolocation_qr_code import GeolocationQRCode
from openapi_server.models.geolocation_qr_code_multipart_body import GeolocationQRCodeMultipartBody
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.phone_qr_code import PhoneQRCode
from openapi_server.models.phone_qr_code_multipart_body import PhoneQRCodeMultipartBody
from openapi_server.models.smsqr_code import SMSQRCode
from openapi_server.models.smsqr_code_multipart_body import SMSQRCodeMultipartBody
from openapi_server.models.text_qr_code import TextQRCode
from openapi_server.models.text_qr_code_multipart_body import TextQRCodeMultipartBody
from openapi_server.models.wi_fi_qr_code import WiFiQRCode
from openapi_server.models.wi_fi_qr_code_multipart_body import WiFiQRCodeMultipartBody
from openapi_server import util


async def dispatcher_qrcode_contact_post(request: web.Request, body=None) -> web.Response:
    """Contact QR Code

    This endpoint allows you to create a QR Code that allows user to quickly add contact information to the phone book. The code contains an appropriately encoded electronic business card. After scanning, the device prompts to save the contact in the phone book.

    :param body: 
    :type body: dict | bytes

    """
    body = ContactQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_crypto_post(request: web.Request, body=None) -> web.Response:
    """Cryptocurrency payment QR Code

    This endpoint allows you to create a QR Code that allows user to make a quick cryptocurrency transfer. The code contains appropriately encoded data for the payment. After scanning the code, the cryptocurrency wallet application asks user to perform the transfer without rewriting all necessary data.

    :param body: 
    :type body: dict | bytes

    """
    body = CryptoPaymentQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_email_post(request: web.Request, body=None) -> web.Response:
    """Email QR Code

    This endpoint allows the creation of a QR Code allowing the user to quickly send an email. The code contains an appropriately encoded message template. After scanning, the device starts the e-mail client with pre-filled specified fields.

    :param body: 
    :type body: dict | bytes

    """
    body = EmailQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_geo_post(request: web.Request, body=None) -> web.Response:
    """Geolocation QR Code

    This endpoint allows you to create a QR Code that allows to share location with the user. The code contains appropriately encoded geographic coordinates. After scanning the code, device maps application is invoked, pointing to the selected location (address).

    :param body: 
    :type body: dict | bytes

    """
    body = GeolocationQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_phone_post(request: web.Request, body=None) -> web.Response:
    """Telephone QR Code

    This endpoint allows you to create a QR Code that allows user to make quick telephone call. The code contains appropriately encoded telephone number. After scanning the code, device dialer is invoked with prefilled phone number. To make a call, the user only needs to press the green phone key.

    :param body: 
    :type body: dict | bytes

    """
    body = PhoneQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_post(request: web.Request, body=None) -> web.Response:
    """Arbitrary data type QR Code

    This endpoint aggregates the functionality of all other endpoints in the group. The data type in the &#x60;data&#x60; field is recognized automatically and the data is encoded in an appropriate way.

    :param body: 
    :type body: dict | bytes

    """
    body = AutoQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_sms_post(request: web.Request, body=None) -> web.Response:
    """SMS QR Code

    This endpoint allows you to create a QR Code that allows user to quickly send SMS. The code contains appropriately encoded recipient number and message template. After scanning the code, device message application is invoked with prefilled phone number and text, ready to be sent. To send a SMS, the user only needs to press *Send* button.

    :param body: 
    :type body: dict | bytes

    """
    body = SMSQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_text_post(request: web.Request, body=None) -> web.Response:
    """Text QR Code

    This endpoint allows you to create a QR Code containing any text, in particular, an URL that may redirect the user to the website. After QR code is scanned, website will be displayed to the user.

    :param body: 
    :type body: dict | bytes

    """
    body = TextQRCode.from_dict(body)
    return web.Response(status=200)


async def dispatcher_qrcode_wifi_post(request: web.Request, body=None) -> web.Response:
    """WiFi QR Code

    This endpoint allows you to create a QR Code that allows user to quickly connect to a WiFi network. The code contains properly encoded network credentials. After scanning, the device can automatically connect to the network without having to enter the password manually.

    :param body: 
    :type body: dict | bytes

    """
    body = WiFiQRCode.from_dict(body)
    return web.Response(status=200)
