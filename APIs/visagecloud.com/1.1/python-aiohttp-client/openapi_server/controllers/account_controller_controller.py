from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_response import RestResponse
from openapi_server import util


async def change_password_using_post(request: web.Request, email, old_password, new_password) -> web.Response:
    """Change password for an account using old password

    

    :param email: email
    :type email: str
    :param old_password: oldPassword
    :type old_password: str
    :param new_password: newPassword
    :type new_password: str

    """
    return web.Response(status=200)


async def get_account_by_access_key_using_get(request: web.Request, access_key, secret_key) -> web.Response:
    """Get account information by accessKey and secretKey

    

    :param access_key: accessKey
    :type access_key: str
    :param secret_key: secretKey
    :type secret_key: str

    """
    return web.Response(status=200)


async def get_billing_per_account_using_get(request: web.Request, access_key, secret_key, start_date_time=None, end_date_time=None, date_template=None) -> web.Response:
    """Get billing information by accessKey and secretKey

    

    :param access_key: accessKey
    :type access_key: str
    :param secret_key: secretKey
    :type secret_key: str
    :param start_date_time: startDateTime
    :type start_date_time: str
    :param end_date_time: endDateTime
    :type end_date_time: str
    :param date_template: dateTemplate
    :type date_template: str

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)


async def login_with_email_using_post(request: web.Request, email, password) -> web.Response:
    """Get account information including accessKey and secretKey by email and password

    

    :param email: email
    :type email: str
    :param password: password
    :type password: str

    """
    return web.Response(status=200)
