from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_document_with_web_hook200_response import GetDocumentWithWebHook200Response
from openapi_server.models.model200_result import Model200Result
from openapi_server.models.model400 import Model400
from openapi_server.models.model404 import Model404
from openapi_server import util


async def delete_policy_module(request: web.Request, id, pretty=None) -> web.Response:
    """Delete a policy module

    This API endpoint removes an existing policy module from the server

    :param id: The name of a policy module
    :type id: str
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool

    """
    return web.Response(status=200)


async def get_policies(request: web.Request, pretty=None) -> web.Response:
    """List policies

    This API endpoint responds with a list of all policy modules on the server (result response)

    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool

    """
    return web.Response(status=200)


async def get_policy_module(request: web.Request, id, pretty=None) -> web.Response:
    """Get a policy module

    This API endpoint returns the details of the specified policy module (&#x60;{id}&#x60;)

    :param id: The name of a policy module
    :type id: str
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool

    """
    return web.Response(status=200)


async def put_policy_module(request: web.Request, id, body, pretty=None, metrics=None) -> web.Response:
    """Create or update a policy module

    - If the policy module does not exist, it is created. - If the policy module already exists, it is replaced.  If the policy module isn&#39;t correctly defined, a *bad request* (400) response is returned.  ### Example policy module &#x60;&#x60;&#x60;yaml package opa.examples  import data.servers import data.networks import data.ports  public_servers[server] {   some k, m    server :&#x3D; servers[_]    server.ports[_] &#x3D;&#x3D; ports[k].id    ports[k].networks[_] &#x3D;&#x3D; networks[m].id    networks[m].public &#x3D;&#x3D; true } &#x60;&#x60;&#x60;

    :param id: The name of a policy module
    :type id: str
    :param body: 
    :type body: str
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool
    :param metrics: If true, compiler performance metrics will be returned in the response.
    :type metrics: bool

    """
    return web.Response(status=200)
