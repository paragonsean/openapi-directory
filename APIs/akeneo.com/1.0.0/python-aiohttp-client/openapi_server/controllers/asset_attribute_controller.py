from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_asset_families_code_attributes200_response_inner import GetAssetFamiliesCodeAttributes200ResponseInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_asset_families_code_attributes(request: web.Request, asset_family_code) -> web.Response:
    """Get the list of attributes of a given asset family

    This endpoint allows you to get the list of attributes of a given asset family.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str

    """
    return web.Response(status=200)


async def get_asset_family_attributes_code(request: web.Request, asset_family_code, code) -> web.Response:
    """Get an attribute of a given asset family

    This endpoint allows you to get the information about a given attribute for a given asset family.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_asset_family_attributes_code(request: web.Request, asset_family_code, code, body) -> web.Response:
    """Update/create an attribute of a given asset family

    This endpoint allows you to update a given attribute for a given asset family. Note that if the attribute does not already exist for the given asset family, it creates it.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetAssetFamiliesCodeAttributes200ResponseInner.from_dict(body)
    return web.Response(status=200)
