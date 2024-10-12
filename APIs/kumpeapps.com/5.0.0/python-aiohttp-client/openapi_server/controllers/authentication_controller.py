from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response201 import InlineResponse201
from openapi_server.models.inline_response2011 import InlineResponse2011
from openapi_server.models.inline_response202 import InlineResponse202
from openapi_server.models.model403 import Model403
from openapi_server.models.model449 import Model449
from openapi_server import util


async def appkey_patch(request: web.Request, app_key, comments=None) -> web.Response:
    """Compromise app key

    Pass an app key to mark it as compromised. This may be submitted by the app owner or a concerned party that has optained the compromised app key.

    :param app_key: compromised app key
    :type app_key: str
    :param comments: Comments (like how was this compromised)
    :type comments: str

    """
    return web.Response(status=200)


async def appkey_post(request: web.Request, username, password, supports_yubikey) -> web.Response:
    """Request app key

    Request a new app key by passing username and password for app account

    :param username: Username assigned to your app
    :type username: str
    :param password: Password assigned to your app
    :type password: str
    :param supports_yubikey: App supports YubiKey OTP
    :type supports_yubikey: bool

    """
    return web.Response(status=200)


async def appkey_put(request: web.Request, app_key) -> web.Response:
    """Deactivate app key

    Pass your app key to deactivate the key

    :param app_key: app key to deactivate
    :type app_key: str

    """
    return web.Response(status=200)


async def auth_appkey_patch(request: web.Request, app_key, comments=None) -> web.Response:
    """Compromise app key

    Pass an app key to mark it as compromised. This may be submitted by the app owner or a concerned party that has optained the compromised app key.

    :param app_key: compromised app key
    :type app_key: str
    :param comments: Comments (like how was this compromised)
    :type comments: str

    """
    return web.Response(status=200)


async def auth_appkey_post(request: web.Request, username, password, supports_yubikey) -> web.Response:
    """Request app key

    Request a new app key by passing username and password for app account

    :param username: Username assigned to your app
    :type username: str
    :param password: Password assigned to your app
    :type password: str
    :param supports_yubikey: App supports YubiKey OTP
    :type supports_yubikey: bool

    """
    return web.Response(status=200)


async def auth_appkey_put(request: web.Request, app_key) -> web.Response:
    """Deactivate app key

    Pass your app key to deactivate the key

    :param app_key: app key to deactivate
    :type app_key: str

    """
    return web.Response(status=200)


async def auth_authkey_get(request: web.Request, username, password, otp=None, device_name=None, identifier_for_vendor=None) -> web.Response:
    """Request auth key for user (login user)

    Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

    :param username: Authenticated username
    :type username: str
    :param password: Authenticated password
    :type password: str
    :param otp: YubiKey OTP (if configured for user)
    :type otp: str
    :param device_name: User&#39;s device name
    :type device_name: str
    :param identifier_for_vendor: identifierForVendor for User&#39;s Device (if app is iOS)
    :type identifier_for_vendor: str

    """
    return web.Response(status=200)


async def auth_authkey_patch(request: web.Request, auth_key, comments=None) -> web.Response:
    """Compromise auth key

    Mark user auth key as compromised

    :param auth_key: auth key to mark as compromised
    :type auth_key: str
    :param comments: Comments (like how was this compromised)
    :type comments: str

    """
    return web.Response(status=200)


async def auth_authkey_post(request: web.Request, username, password, otp=None) -> web.Response:
    """Request auth key for user (login user)

    Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

    :param username: Authenticated username
    :type username: str
    :param password: Authenticated password
    :type password: str
    :param otp: YubiKey OTP (if configured for user)
    :type otp: str

    """
    return web.Response(status=200)


async def auth_authkey_put(request: web.Request, auth_key) -> web.Response:
    """Deactivate auth key (logout)

    Deactivate auth key for user logging them out of your application

    :param auth_key: auth key to logout
    :type auth_key: str

    """
    return web.Response(status=200)


async def auth_verifyotp_get(request: web.Request, otp) -> web.Response:
    """Verifies YubiKey OTP for authenticated user

    Verifies YubiKey OTP for authenticated user

    :param otp: YubiKey OTP code
    :type otp: str

    """
    return web.Response(status=200)


async def authkey_get(request: web.Request, username, password, otp=None) -> web.Response:
    """Request auth key for user (login user)

    Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

    :param username: Authenticated username
    :type username: str
    :param password: Authenticated password
    :type password: str
    :param otp: YubiKey OTP (if configured for user)
    :type otp: str

    """
    return web.Response(status=200)


async def authkey_patch(request: web.Request, auth_key, comments=None) -> web.Response:
    """Compromise auth key

    Mark user auth key as compromised

    :param auth_key: auth key to mark as compromised
    :type auth_key: str
    :param comments: Comments (like how was this compromised)
    :type comments: str

    """
    return web.Response(status=200)


async def authkey_post(request: web.Request, username, password, otp=None) -> web.Response:
    """Request auth key for user (login user)

    Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

    :param username: Authenticated username
    :type username: str
    :param password: Authenticated password
    :type password: str
    :param otp: YubiKey OTP (if configured for user)
    :type otp: str

    """
    return web.Response(status=200)


async def authkey_put(request: web.Request, auth_key) -> web.Response:
    """Deactivate auth key (logout)

    Deactivate auth key for user logging them out of your application

    :param auth_key: auth key to logout
    :type auth_key: str

    """
    return web.Response(status=200)
