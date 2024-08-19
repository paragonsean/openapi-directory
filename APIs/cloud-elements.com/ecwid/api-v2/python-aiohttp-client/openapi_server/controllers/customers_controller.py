from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_patch import CustomerPatch
from openapi_server.models.customer_post import CustomerPost
from openapi_server.models.order import Order
from openapi_server import util


async def create_customer(request: web.Request, authorization, customer) -> web.Response:
    """Create a new customer in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Customer&#39; model are those required to create a new customer

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param customer: The customer object to be created
    :type customer: dict | bytes

    """
    customer = CustomerPost.from_dict(customer)
    return web.Response(status=200)


async def delete_customer_by_id(request: web.Request, authorization, id) -> web.Response:
    """Delete a customer associated with a given ID from your eCommerce system. Specifying a customer associated with a given ID that does not exist will result in an error message

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the customer to delete from the eCommerce system
    :type id: str

    """
    return web.Response(status=200)


async def get_customer_by_id(request: web.Request, authorization, id) -> web.Response:
    """Retrieve a customer associated with a given ID from the eCommerce system. Specifying a customer with an ID that does not exist will result in an error response

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the customer to retrieve from the eCommerce system
    :type id: str

    """
    return web.Response(status=200)


async def get_customers(request: web.Request, authorization, where=None, page_size=None, next_page=None, fields=None) -> web.Response:
    """Find customers in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param where: The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: customer_id and customer_email. All other search criteria are ignored. NOTE: When searching by customer_id, do not quote the value (ex: customer_id&#x3D;15693430), as the ID is a number rather than a string.  When searching by email, quote the value (ex: customer_email&#x3D;&#39;a@b.c&#39;), as the email parameter is a string
    :type where: str
    :param page_size: The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def get_customers_orders(request: web.Request, authorization, id, page_size=None, next_page=None, fields=None) -> web.Response:
    """Find orders in the customer associated with a given ID. If the customer does not exist, an error response will be returned. If no orders are found in the given customer then an empty array will be returned

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the customer to get orders form in the eCommerce system
    :type id: str
    :param page_size: The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def update_customer_by_id(request: web.Request, authorization, id, customer) -> web.Response:
    """Update an customer associated with a given ID in the eCommerce system.The update API uses the PATCH HTTP verb, so only those fields provided in the customer object will be updated, and those fields not provided will be left alone. Updating a customer with a specified ID that does not exist will result in an error response

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the customer to update in the eCommerce system
    :type id: str
    :param customer: The customer object to be created
    :type customer: dict | bytes

    """
    customer = CustomerPatch.from_dict(customer)
    return web.Response(status=200)
