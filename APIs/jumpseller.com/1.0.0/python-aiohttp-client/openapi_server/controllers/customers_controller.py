from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.customer import Customer
from openapi_server.models.customer_with_password_no_id import CustomerWithPasswordNoID
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def customers_count_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Count all Customers.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def customers_email_email_json_get(request: web.Request, login, authtoken, email) -> web.Response:
    """Retrieve a single Customer by email.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param email: Email of the Customer
    :type email: str

    """
    return web.Response(status=200)


async def customers_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing Customer.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int

    """
    return web.Response(status=200)


async def customers_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Customer by id.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int

    """
    return web.Response(status=200)


async def customers_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a new Customer.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int
    :param body: Customer parameters.
    :type body: dict | bytes

    """
    body = CustomerWithPasswordNoID.from_dict(body)
    return web.Response(status=200)


async def customers_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Customers.

    

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


async def customers_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Customer.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Customer parameters.
    :type body: dict | bytes

    """
    body = CustomerWithPasswordNoID.from_dict(body)
    return web.Response(status=200)
