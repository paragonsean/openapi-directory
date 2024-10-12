from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.number_config import NumberConfig
from openapi_server.models.number_config_page import NumberConfigPage
from openapi_server.models.number_lease import NumberLease
from openapi_server.models.number_lease_page import NumberLeasePage
from openapi_server.models.number_list import NumberList
from openapi_server.models.region_page import RegionPage
from openapi_server import util


async def find_number_lease_configs(request: web.Request, limit=None, offset=None, prefix=None, city=None, state=None, zipcode=None, label_name=None, fields=None) -> web.Response:
    """Find lease configs

    Searches for all number lease configs for the user. Returns a paged list of NumberConfig

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param prefix: A 4-7 digit prefix
    :type prefix: str
    :param city: A city name
    :type city: str
    :param state: A two-letter state code. Example: CA, IL, etc.
    :type state: str
    :param zipcode: A five-digit Zipcode
    :type zipcode: str
    :param label_name: A label name
    :type label_name: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_number_leases(request: web.Request, limit=None, offset=None, prefix=None, city=None, state=None, zipcode=None, label_name=None, toll_free=None, fields=None) -> web.Response:
    """Find leases

    Searches for all numbers leased by account user. This API is useful for finding all numbers currently owned by the user. Returns a paged list of number leases.

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param prefix: A 4-7 digit prefix
    :type prefix: str
    :param city: A city name
    :type city: str
    :param state: A two-letter state code. Example: CA, IL, etc.
    :type state: str
    :param zipcode: A five-digit Zipcode
    :type zipcode: str
    :param label_name: A label name
    :type label_name: str
    :param toll_free: ~
    :type toll_free: bool
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_number_regions(request: web.Request, limit=None, offset=None, prefix=None, city=None, city_prefix=None, state=None, zipcode=None, country=None, fields=None) -> web.Response:
    """Find number regions

    Searches for region information. Use this API to obtain detailed region information that can be used to query for more specific phone numbers than a general query.

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param prefix: A 4-7 digit prefix
    :type prefix: str
    :param city: A city name
    :type city: str
    :param city_prefix: ~
    :type city_prefix: str
    :param state: A two-letter state code. Example: CA, IL, etc.
    :type state: str
    :param zipcode: A five-digit Zipcode
    :type zipcode: str
    :param country: ~
    :type country: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_numbers_local(request: web.Request, limit=None, prefix=None, city=None, state=None, zipcode=None, fields=None) -> web.Response:
    """Find local numbers

    Searches for numbers available for purchase in CallFire local numbers catalog . At least one additional parameter is required. User may filter local numbers by their region information. If all numbers with desirable zip code is already busy search will return available numbers with nearest zip code.

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param prefix: A 4-7 digit prefix
    :type prefix: str
    :param city: A city name
    :type city: str
    :param state: A two-letter state code. Example: CA, IL, etc.
    :type state: str
    :param zipcode: A five-digit Zipcode
    :type zipcode: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_numbers_tollfree(request: web.Request, pattern=None, limit=None, fields=None) -> web.Response:
    """Find tollfree numbers

    Searches for the toll free numbers which are available for purchase in the CallFire catalog

    :param pattern: Filter toll free numbers by prefix, pattern must be 3 char long and should end with &#39;*&#39;. Examples: 8**, 85*, 87* (but 855 will fail because pattern must end with &#39;*&#39;).
    :type pattern: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_number_lease(request: web.Request, number, fields=None) -> web.Response:
    """Find a specific lease

    Returns a single NumberLease instance for a given number

    :param number: A phone number in E.164 format (11-digit). Example: 12132000384
    :type number: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_number_lease_config(request: web.Request, number, fields=None) -> web.Response:
    """Find a specific lease config

    Returns a single NumberConfig instance for a given number lease

    :param number: A phone number in E.164 format (11-digit). Example: 12132000384
    :type number: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def update_number_lease(request: web.Request, number, body=None) -> web.Response:
    """Update a lease

    Updates a number lease instance. Ability to turn on/off autoRenew and toggle call/text features for a particular number

    :param number: A phone number in E.164 format (11-digit). Example: 12132000384
    :type number: str
    :param body: A NumberLease object to update
    :type body: dict | bytes

    """
    body = NumberLease.from_dict(body)
    return web.Response(status=200)


async def update_number_lease_config(request: web.Request, number, body=None) -> web.Response:
    """Update a lease config

    Updates a phone number lease configuration. Use this API endpoint to add an Inbound IVR or Call Tracking feature to a CallFire phone number. Call tracking configuration allows you to track the incoming calls, to analyze and to respond customers using sms or voice replies. For more information see [call tracking page](https://www.callfire.com/products/call-tracking)

    :param number: A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384
    :type number: str
    :param body: The configuration of a number lease object. There are two available types of configuration: IVR, TRACKING 
    :type body: dict | bytes

    """
    body = NumberConfig.from_dict(body)
    return web.Response(status=200)
