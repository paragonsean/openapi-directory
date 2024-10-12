from typing import List, Dict
from aiohttp import web

from openapi_server.models.rsa_mfa_server_config import RsaMfaServerConfig
from openapi_server.models.rsa_mfa_server_config_update import RsaMfaServerConfigUpdate
from openapi_server.models.rsa_mfa_server_detail import RsaMfaServerDetail
from openapi_server.models.rsa_mfa_server_detail_list_response import RsaMfaServerDetailListResponse
from openapi_server import util


async def create_rsa_mfa_server(request: web.Request, body) -> web.Response:
    """Register a new RSA server

    Register a new RSA server using specified configuration.

    :param body: Configuration of RSA server.
    :type body: dict | bytes

    """
    body = RsaMfaServerConfig.from_dict(body)
    return web.Response(status=200)


async def delete_rsa_mfa_server(request: web.Request, id) -> web.Response:
    """Delete RSA server

    Delete RSA server configuration.

    :param id: ID of the RSA server.
    :type id: str

    """
    return web.Response(status=200)


async def get_rsa_mfa_server(request: web.Request, id) -> web.Response:
    """Get RSA server configuration

    Get RSA server configuration.

    :param id: ID of the RSA server.
    :type id: str

    """
    return web.Response(status=200)


async def query_rsa_mfa_servers(request: web.Request, ) -> web.Response:
    """Get RSA server configuration

    Get RSA server configuration.


    """
    return web.Response(status=200)


async def update_rsa_mfa_server(request: web.Request, id, body) -> web.Response:
    """Update RSA server configuration

    Update an existing RSA server using specified configuration.

    :param id: ID of the RSA server.
    :type id: str
    :param body: Configuration of RSA server.
    :type body: dict | bytes

    """
    body = RsaMfaServerConfigUpdate.from_dict(body)
    return web.Response(status=200)
