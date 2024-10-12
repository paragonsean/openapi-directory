from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_model import ClientModel
from openapi_server.models.clients_model import ClientsModel
from openapi_server import util


async def clients_post_by_model(request: web.Request, model) -> web.Response:
    """clients_post_by_model

    Description: This operation submits the Fact Finder data to an external system.&lt;br /&gt;                Purpose: Allows Fact Finder data to be persisted in another system for that system&#39;s consumption and use.

    :param model: 
    :type model: dict | bytes

    """
    model = ClientsModel.from_dict(model)
    return web.Response(status=200)
