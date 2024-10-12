from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_category import CustomerCategory
from openapi_server.models.customer_category_edit import CustomerCategoryEdit
from openapi_server.models.customers_to_customer_category import CustomersToCustomerCategory
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def customer_categories_id_customers_json_delete(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Delete Customers from an existing CustomerCategory.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomerCategory
    :type id: int
    :param body: Customer parameters.
    :type body: dict | bytes

    """
    body = CustomersToCustomerCategory.from_dict(body)
    return web.Response(status=200)


async def customer_categories_id_customers_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieves the customers in a CustomerCategory.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomerCategory
    :type id: int

    """
    return web.Response(status=200)


async def customer_categories_id_customers_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Adds Customers to a CustomerCategory.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomerCategory
    :type id: int
    :param body: Customer parameters.
    :type body: dict | bytes

    """
    body = CustomersToCustomerCategory.from_dict(body)
    return web.Response(status=200)


async def customer_categories_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing CustomerCategory.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomerCategory
    :type id: int

    """
    return web.Response(status=200)


async def customer_categories_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single CustomerCategory.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomerCategory
    :type id: int

    """
    return web.Response(status=200)


async def customer_categories_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a CustomerCategory.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomerCategory
    :type id: int
    :param body: CustomerCategory parameters.
    :type body: dict | bytes

    """
    body = CustomerCategoryEdit.from_dict(body)
    return web.Response(status=200)


async def customer_categories_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Customer Categories.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: List restriction
    :type limit: int
    :param page: List page
    :type page: int

    """
    return web.Response(status=200)


async def customer_categories_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new CustomerCategory.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: CustomerCategory parameters.
    :type body: dict | bytes

    """
    body = CustomerCategoryEdit.from_dict(body)
    return web.Response(status=200)
