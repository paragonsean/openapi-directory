from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_params import BadParams
from openapi_server.models.customer_additional_field import CustomerAdditionalField
from openapi_server.models.customer_additional_field_edit import CustomerAdditionalFieldEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def customers_id_fields_field_id_delete(request: web.Request, login, authtoken, id, field_id) -> web.Response:
    """Delete a Customer Additional Field.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int
    :param field_id: Id of the Customer Additional Field
    :type field_id: int

    """
    return web.Response(status=200)


async def customers_id_fields_field_id_get(request: web.Request, login, authtoken, id, field_id) -> web.Response:
    """Retrieve a single Customer Additional Field.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int
    :param field_id: Id of the Customer Additional Field
    :type field_id: int

    """
    return web.Response(status=200)


async def customers_id_fields_field_id_put(request: web.Request, login, authtoken, id, field_id, body) -> web.Response:
    """Update a Customer Additional Field.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int
    :param field_id: Id of the Customer Additional Field
    :type field_id: int
    :param body: Customer Additional Field parameters.
    :type body: dict | bytes

    """
    body = CustomerAdditionalFieldEdit.from_dict(body)
    return web.Response(status=200)


async def customers_id_fields_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieves the Customer Additional Field of a Customer.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int

    """
    return web.Response(status=200)


async def customers_id_fields_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Adds Customer Additional Fields to a Customer.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Customer
    :type id: int
    :param body: Customer Additional Field parameters.
    :type body: dict | bytes

    """
    body = CustomerAdditionalFieldEdit.from_dict(body)
    return web.Response(status=200)
