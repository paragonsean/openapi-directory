from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.global_jwt_verifier import GlobalJwtVerifier
from openapi_server.models.patch_inner import PatchInner
from openapi_server import util


async def create_global_jwt_verifier(request: web.Request, body=None) -> web.Response:
    """Create one global JWT verifiers

    Create one global JWT verifiers

    :param body: 
    :type body: dict | bytes

    """
    body = GlobalJwtVerifier.from_dict(body)
    return web.Response(status=200)


async def delete_global_jwt_verifier(request: web.Request, verifier_id) -> web.Response:
    """Delete one global JWT verifiers

    Delete one global JWT verifiers

    :param verifier_id: The jwt verifier id
    :type verifier_id: str

    """
    return web.Response(status=200)


async def find_all_global_jwt_verifiers(request: web.Request, ) -> web.Response:
    """Get all global JWT verifiers

    Get all global JWT verifiers


    """
    return web.Response(status=200)


async def find_global_jwt_verifiers_by_id(request: web.Request, verifier_id) -> web.Response:
    """Get one global JWT verifiers

    Get one global JWT verifiers

    :param verifier_id: The jwt verifier id
    :type verifier_id: str

    """
    return web.Response(status=200)


async def patch_global_jwt_verifier(request: web.Request, verifier_id, body=None) -> web.Response:
    """Update one global JWT verifiers

    Update one global JWT verifiers

    :param verifier_id: The jwt verifier id
    :type verifier_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_global_jwt_verifier(request: web.Request, verifier_id, body=None) -> web.Response:
    """Update one global JWT verifiers

    Update one global JWT verifiers

    :param verifier_id: The jwt verifier id
    :type verifier_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GlobalJwtVerifier.from_dict(body)
    return web.Response(status=200)
