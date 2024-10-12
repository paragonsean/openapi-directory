from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_host201_response import CreateHost201Response
from openapi_server.models.create_token200_response_inner import CreateToken200ResponseInner
from openapi_server import util


async def create_host(request: web.Request, id, x_request_id=None, annotations=None) -> web.Response:
    """Creates a Host using the Host Factory.

    Creates a Host using the Host Factory and returns a JSON description of it.  Requires a host factory token, which can be created using the create tokens API. In practice, this token is usually provided automatically as part of Conjur integration with your host provisioning infrastructure.  Note: If the token was created with a CIDR restriction, you must make this API request from a whitelisted address. 

    :param id: Identifier of the host to be created. It will be created within the account of the host factory.
    :type id: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param annotations: Annotations to apply to the new host
    :type annotations: dict | bytes

    """
    annotations = object.from_dict(annotations)
    return web.Response(status=200)


async def create_token(request: web.Request, expiration, host_factory, x_request_id=None, cidr=None, count=None) -> web.Response:
    """Creates one or more host identity tokens.

    Creates one or more tokens which can be used to bootstrap host identity. Responds with a JSON document containing the tokens and their restrictions.  If the tokens are created with a CIDR restriction, Conjur will only accept them from the whitelisted IP ranges.  ##### Permissions required # &#x60;execute&#x60; privilege on the Host Factory.\&quot; 

    :param expiration: &#x60;ISO 8601 datetime&#x60; denoting a requested expiration time.
    :type expiration: str
    :param host_factory: Fully qualified host factory ID
    :type host_factory: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param cidr: Number of host tokens to create
    :type cidr: List[str]
    :param count: Number of host tokens to create
    :type count: int

    """
    return web.Response(status=200)


async def revoke_token(request: web.Request, token, x_request_id=None) -> web.Response:
    """Revokes a token, immediately disabling it.

    Revokes a token, immediately disabling it.  ##### Permissions required  &#x60;update&#x60; privilege on the host factory.\&quot; 

    :param token: The host factory token to revoke
    :type token: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)
