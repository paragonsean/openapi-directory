from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_dependent_phone_number_response import ListDependentPhoneNumberResponse
from openapi_server import util


async def list_dependent_phone_number(request: web.Request, account_sid, address_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_dependent_phone_number

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DependentPhoneNumber resources to read.
    :type account_sid: str
    :param address_sid: The SID of the Address resource associated with the phone number.
    :type address_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
