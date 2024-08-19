from typing import List, Dict
from aiohttp import web

from openapi_server.models.order import Order
from openapi_server.models.order_patch import OrderPatch
from openapi_server.models.order_post import OrderPost
from openapi_server.models.payment import Payment
from openapi_server import util


async def create_order(request: web.Request, authorization, order) -> web.Response:
    """Create an order in the eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Order&#39; model are those required to create a new order.The paymentStatus can only be AWAITING_PAYMENT or INCOMPLETE.The fulfillmentStatus can only be AWAITING_PROCESSING

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param order: The order object to be created
    :type order: dict | bytes

    """
    order = OrderPost.from_dict(order)
    return web.Response(status=200)


async def delete_order_by_id(request: web.Request, authorization, id) -> web.Response:
    """Delete an order associated with a given ID from your eCommerce system. Specifying an order associated with a given ID that does not exist will result in an error message

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the order to delete from the eCommerce system
    :type id: str

    """
    return web.Response(status=200)


async def get_order_by_id(request: web.Request, authorization, id) -> web.Response:
    """Retrieve an order associated with a given ID from the eCommerce system. Specifying an order with an ID that does not exist will result in an error response

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the order to retrieve from the eCommerce system
    :type id: str

    """
    return web.Response(status=200)


async def get_orders(request: web.Request, authorization, where=None, page_size=None, next_page=None, fields=None) -> web.Response:
    """Find orders in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param where: The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: date, from_date, to_date, from_update_date, to_update_date, order, from_order, to_order, customer_id, customer_email and statuses. All other search criteria are ignored
    :type where: str
    :param page_size: The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def get_orders_payments(request: web.Request, authorization, order_id, page_size=None, next_page=None, fields=None) -> web.Response:
    """Retrieve the payments in the eCommerce system for the specified order

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param order_id: The ID of the order to retrieve payments from in the eCommerce system
    :type order_id: str
    :param page_size: The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def get_orders_refunds(request: web.Request, authorization, order_id, page_size=None, next_page=None, fields=None) -> web.Response:
    """Retrieve the refunds in the eCommerce system for the specified order

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param order_id: The ID of the order to retrieve refunds from in the eCommerce system
    :type order_id: str
    :param page_size: The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def update_order_by_id(request: web.Request, authorization, id, order, action=None) -> web.Response:
    """Update an order associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the order object will be updated, and those fields not provided will be left alone. Updating an order with a specified ID that does not exist will result in an error response&lt;/strong&gt;

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the order to update in the eCommerce system
    :type id: str
    :param order: The order object, with those fields that are to be updated
    :type order: dict | bytes
    :param action: An action to perform on the order: cancel, reopen or close. If left blank then the order is updated but no action is taken
    :type action: str

    """
    order = OrderPatch.from_dict(order)
    return web.Response(status=200)
