from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_asset_family_attributes_attribute_code_options200_response_inner import GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_asset_attributes_attribute_code_options_code(request: web.Request, asset_family_code, attribute_code, code) -> web.Response:
    """Get an attribute option for a given attribute of a given asset family

    This endpoint allows you to get the information about a given asset attribute option.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def get_asset_family_attributes_attribute_code_options(request: web.Request, asset_family_code, attribute_code) -> web.Response:
    """Get a list of attribute options of a given attribute for a given asset family

    This endpoint allows you to get a list of attribute options for a given asset family.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param attribute_code: Code of the attribute
    :type attribute_code: str

    """
    return web.Response(status=200)


async def patch_asset_attributes_attribute_code_options_code(request: web.Request, asset_family_code, attribute_code, code, body) -> web.Response:
    """Update/create an asset attribute option for a given asset family

    This endpoint allows you to update a given option for a given attribute and a given asset family. Learn more about the &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the option does not already exist for the given attribute of the given asset family, it creates it.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner.from_dict(body)
    return web.Response(status=200)
