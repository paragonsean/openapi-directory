from typing import List, Dict
from aiohttp import web

from openapi_server.models.estimation_change_status_api_model import EstimationChangeStatusApiModel
from openapi_server.models.estimation_create_api_model import EstimationCreateApiModel
from openapi_server.models.estimation_delete_api_model import EstimationDeleteApiModel
from openapi_server.models.estimation_full_details_api_model import EstimationFullDetailsApiModel
from openapi_server.models.estimation_update_api_model import EstimationUpdateApiModel
from openapi_server.models.estimation_uri_api_model import EstimationUriApiModel
from openapi_server.models.invoice_full_details_api_model import InvoiceFullDetailsApiModel
from openapi_server.models.list_result_estimation_details_api_model import ListResultEstimationDetailsApiModel
from openapi_server.models.send_estimation_to_client_api_model import SendEstimationToClientApiModel
from openapi_server import util


async def estimation_api_all(request: web.Request, x_auth_key, x_auth_secret, query_options_page=None, query_options_page_size=None) -> web.Response:
    """Return all estimation for the account

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param query_options_page: 
    :type query_options_page: int
    :param query_options_page_size: 
    :type query_options_page_size: int

    """
    return web.Response(status=200)


async def estimation_api_change_status(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Change estimation status

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = EstimationChangeStatusApiModel.from_dict(body)
    return web.Response(status=200)


async def estimation_api_convert(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Convert the estimation to an invoice

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: int

    """
    return web.Response(status=200)


async def estimation_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing estimation

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = EstimationDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def estimation_api_details(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return estimation data

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def estimation_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create an estimation

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = EstimationCreateApiModel.from_dict(body)
    return web.Response(status=200)


async def estimation_api_send_to_client(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Send the provided estimation to the client

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendEstimationToClientApiModel.from_dict(body)
    return web.Response(status=200)


async def estimation_api_status(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Retrieve the status of the estimation

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def estimation_api_update(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Update an existing estimation

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = EstimationUpdateApiModel.from_dict(body)
    return web.Response(status=200)


async def estimation_api_uri(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return the unique url to the client&#39;s invoice

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)
