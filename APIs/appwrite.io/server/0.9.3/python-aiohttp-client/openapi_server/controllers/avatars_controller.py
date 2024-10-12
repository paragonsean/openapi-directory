from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def avatars_get_browser(request: web.Request, code, width=None, height=None, quality=None) -> web.Response:
    """Get Browser Icon

    You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user /account/sessions endpoint. Use width, height and quality arguments to change the output settings.

    :param code: Browser Code.
    :type code: str
    :param width: Image width. Pass an integer between 0 to 2000. Defaults to 100.
    :type width: int
    :param height: Image height. Pass an integer between 0 to 2000. Defaults to 100.
    :type height: int
    :param quality: Image quality. Pass an integer between 0 to 100. Defaults to 100.
    :type quality: int

    """
    return web.Response(status=200)


async def avatars_get_credit_card(request: web.Request, code, width=None, height=None, quality=None) -> web.Response:
    """Get Credit Card Icon

    The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.

    :param code: Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.
    :type code: str
    :param width: Image width. Pass an integer between 0 to 2000. Defaults to 100.
    :type width: int
    :param height: Image height. Pass an integer between 0 to 2000. Defaults to 100.
    :type height: int
    :param quality: Image quality. Pass an integer between 0 to 100. Defaults to 100.
    :type quality: int

    """
    return web.Response(status=200)


async def avatars_get_favicon(request: web.Request, url) -> web.Response:
    """Get Favicon

    Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL. 

    :param url: Website URL which you want to fetch the favicon from.
    :type url: str

    """
    return web.Response(status=200)


async def avatars_get_flag(request: web.Request, code, width=None, height=None, quality=None) -> web.Response:
    """Get Country Flag

    You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings.

    :param code: Country Code. ISO Alpha-2 country code format.
    :type code: str
    :param width: Image width. Pass an integer between 0 to 2000. Defaults to 100.
    :type width: int
    :param height: Image height. Pass an integer between 0 to 2000. Defaults to 100.
    :type height: int
    :param quality: Image quality. Pass an integer between 0 to 100. Defaults to 100.
    :type quality: int

    """
    return web.Response(status=200)


async def avatars_get_image(request: web.Request, url, width=None, height=None) -> web.Response:
    """Get Image from URL

    Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.

    :param url: Image URL which you want to crop.
    :type url: str
    :param width: Resize preview image width, Pass an integer between 0 to 2000.
    :type width: int
    :param height: Resize preview image height, Pass an integer between 0 to 2000.
    :type height: int

    """
    return web.Response(status=200)


async def avatars_get_initials(request: web.Request, name=None, width=None, height=None, color=None, background=None) -> web.Response:
    """Get User Initials

    Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the &#39;name&#39; parameter. If no name is given and no user is logged, an empty avatar will be returned.  You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user&#39;s initials when reloading the same theme will always return for the same initials.

    :param name: Full Name. When empty, current user name or email will be used. Max length: 128 chars.
    :type name: str
    :param width: Image width. Pass an integer between 0 to 2000. Defaults to 100.
    :type width: int
    :param height: Image height. Pass an integer between 0 to 2000. Defaults to 100.
    :type height: int
    :param color: Changes text color. By default a random color will be picked and stay will persistent to the given name.
    :type color: str
    :param background: Changes background color. By default a random color will be picked and stay will persistent to the given name.
    :type background: str

    """
    return web.Response(status=200)


async def avatars_get_qr(request: web.Request, text, size=None, margin=None, download=None) -> web.Response:
    """Get QR Code

    Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.

    :param text: Plain text to be converted to QR code image.
    :type text: str
    :param size: QR code size. Pass an integer between 0 to 1000. Defaults to 400.
    :type size: int
    :param margin: Margin from edge. Pass an integer between 0 to 10. Defaults to 1.
    :type margin: int
    :param download: Return resulting image with &#39;Content-Disposition: attachment &#39; headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.
    :type download: bool

    """
    return web.Response(status=200)
