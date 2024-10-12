from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.validation_authority import ValidationAuthority
from openapi_server import util


async def create_client_validator(request: web.Request, body=None) -> web.Response:
    """Create one validation authorities

    Create one validation authorities

    :param body: 
    :type body: dict | bytes

    """
    body = ValidationAuthority.from_dict(body)
    return web.Response(status=200)


async def delete_client_validator(request: web.Request, id) -> web.Response:
    """Delete one validation authorities by id

    Delete one validation authorities by id

    :param id: The validation authorities id
    :type id: str

    """
    return web.Response(status=200)


async def find_all_client_validators(request: web.Request, ) -> web.Response:
    """Get all validation authoritiess

    Get all validation authoritiess


    """
    return web.Response(status=200)


async def find_client_validator_by_id(request: web.Request, id) -> web.Response:
    """Get one validation authorities by id

    Get one validation authorities by id

    :param id: The auth. config id
    :type id: str

    """
    return web.Response(status=200)


async def patch_client_validator(request: web.Request, id, body=None) -> web.Response:
    """Update one validation authorities by id

    Update one validation authorities by id

    :param id: The validation authorities id
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_client_validator(request: web.Request, id, body=None) -> web.Response:
    """Update one validation authorities by id

    Update one validation authorities by id

    :param id: The validation authorities id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ValidationAuthority.from_dict(body)
    return web.Response(status=200)
