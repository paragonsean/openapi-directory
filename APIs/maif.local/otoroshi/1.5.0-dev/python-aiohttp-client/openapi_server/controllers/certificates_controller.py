from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner
from openapi_server import util


async def all_certs(request: web.Request, ) -> web.Response:
    """Get all certificates

    Get all certificates


    """
    return web.Response(status=200)


async def create_cert(request: web.Request, body=None) -> web.Response:
    """Create one certificate

    Create one certificate

    :param body: 
    :type body: dict | bytes

    """
    body = Certificate.from_dict(body)
    return web.Response(status=200)


async def delete_cert(request: web.Request, id) -> web.Response:
    """Delete one certificate by id

    Delete one certificate by id

    :param id: The certificate id
    :type id: str

    """
    return web.Response(status=200)


async def one_cert(request: web.Request, id) -> web.Response:
    """Get one certificate by id

    Get one certificate by id

    :param id: The auth. config id
    :type id: str

    """
    return web.Response(status=200)


async def patch_cert(request: web.Request, id, body=None) -> web.Response:
    """Update one certificate by id

    Update one certificate by id

    :param id: The certificate id
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def put_cert(request: web.Request, id, body=None) -> web.Response:
    """Update one certificate by id

    Update one certificate by id

    :param id: The certificate id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Certificate.from_dict(body)
    return web.Response(status=200)
