from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.keyword_purchase_request import KeywordPurchaseRequest
from openapi_server.models.number_order import NumberOrder
from openapi_server.models.number_purchase_request import NumberPurchaseRequest
from openapi_server.models.page_number_order import PageNumberOrder
from openapi_server.models.resource_id import ResourceId
from openapi_server import util


async def find_orders(request: web.Request, limit=None, offset=None, fields=None, status=None, interval_begin=None, interval_end=None) -> web.Response:
    """Find orders

    Searches for account orders

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param status: Filter by order status, accepts multiple values in comma separated string, available values: [PROCESSING, FINISHED, PAYMENT_ERROR, VOID, WAIT_FOR_PAYMENT, PARTIALLY_ADJUSTED, ADJUSTED]
    :type status: List[str]
    :param interval_begin: Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    :type interval_begin: int
    :param interval_end: End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    :type interval_end: int

    """
    return web.Response(status=200)


async def get_order(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific order

    Returns a single NumberOrder instance for a given order id. Order contains information about purchased keywords, local, toll-free numbers

    :param id: An id of an order
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def order_keywords(request: web.Request, fields=None, body=None) -> web.Response:
    """Purchase keywords

    Purchase keywords. Send a list of available keywords into this API to purchase them using CallFire credits. Make sure the account has enough credits before trying to purchase the keywords. Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param body: Request object which contains a list of keywords to buy
    :type body: dict | bytes

    """
    body = KeywordPurchaseRequest.from_dict(body)
    return web.Response(status=200)


async def order_numbers(request: web.Request, fields=None, body=None) -> web.Response:
    """Purchase numbers

    Purchase numbers. There are many ways to purchase a number. Set either &#39;tollFreeCount&#39; or &#39;localCount&#39; along with some querying fields to purchase numbers by bulk query. Set the list of numbers to purchase by list. Available numbers will be purchased using CallFire credits owned by the user. Make sure the account has enough credits before trying to purchase

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param body: Request object contains a list of numbers to buy, you can filter the numbers by their region information: city, state, zipcode, etc
    :type body: dict | bytes

    """
    body = NumberPurchaseRequest.from_dict(body)
    return web.Response(status=200)
