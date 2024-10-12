from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_address import ApiV2010AccountAddress
from openapi_server.models.list_address_response import ListAddressResponse
from openapi_server import util


async def create_address(request: web.Request, account_sid, city, customer_name, iso_country, postal_code, region, street, auto_correct_address=None, emergency_enabled=None, friendly_name=None, street_secondary=None) -> web.Response:
    """create_address

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Address resource.
    :type account_sid: str
    :param city: The city of the new address.
    :type city: str
    :param customer_name: The name to associate with the new address.
    :type customer_name: str
    :param iso_country: The ISO country code of the new address.
    :type iso_country: str
    :param postal_code: The postal code of the new address.
    :type postal_code: str
    :param region: The state or region of the new address.
    :type region: str
    :param street: The number and street address of the new address.
    :type street: str
    :param auto_correct_address: Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide.
    :type auto_correct_address: bool
    :param emergency_enabled: Whether to enable emergency calling on the new address. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type emergency_enabled: bool
    :param friendly_name: A descriptive string that you create to describe the new address. It can be up to 64 characters long.
    :type friendly_name: str
    :param street_secondary: The additional number and street address of the address.
    :type street_secondary: str

    """
    return web.Response(status=200)


async def delete_address(request: web.Request, account_sid, sid) -> web.Response:
    """delete_address

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Address resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_address(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_address

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Address resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_address(request: web.Request, account_sid, customer_name=None, friendly_name=None, iso_country=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_address

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read.
    :type account_sid: str
    :param customer_name: The &#x60;customer_name&#x60; of the Address resources to read.
    :type customer_name: str
    :param friendly_name: The string that identifies the Address resources to read.
    :type friendly_name: str
    :param iso_country: The ISO country code of the Address resources to read.
    :type iso_country: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_address(request: web.Request, account_sid, sid, auto_correct_address=None, city=None, customer_name=None, emergency_enabled=None, friendly_name=None, postal_code=None, region=None, street=None, street_secondary=None) -> web.Response:
    """update_address

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Address resource to update.
    :type sid: str
    :param auto_correct_address: Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide.
    :type auto_correct_address: bool
    :param city: The city of the address.
    :type city: str
    :param customer_name: The name to associate with the address.
    :type customer_name: str
    :param emergency_enabled: Whether to enable emergency calling on the address. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type emergency_enabled: bool
    :param friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
    :type friendly_name: str
    :param postal_code: The postal code of the address.
    :type postal_code: str
    :param region: The state or region of the address.
    :type region: str
    :param street: The number and street address of the address.
    :type street: str
    :param street_secondary: The additional number and street address of the address.
    :type street_secondary: str

    """
    return web.Response(status=200)
