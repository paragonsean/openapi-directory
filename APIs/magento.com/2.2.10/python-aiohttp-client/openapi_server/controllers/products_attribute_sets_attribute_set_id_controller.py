from typing import List, Dict
from aiohttp import web

from openapi_server.models.eav_attribute_set_repository_v1_save_put_request import EavAttributeSetRepositoryV1SavePutRequest
from openapi_server.models.eav_data_attribute_set_interface import EavDataAttributeSetInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_attribute_set_repository_v1_delete_by_id_delete(request: web.Request, attribute_set_id) -> web.Response:
    """products/attribute-sets/{attributeSetId}

    Remove attribute set by given ID

    :param attribute_set_id: 
    :type attribute_set_id: int

    """
    return web.Response(status=200)


async def catalog_attribute_set_repository_v1_get_get(request: web.Request, attribute_set_id) -> web.Response:
    """products/attribute-sets/{attributeSetId}

    Retrieve attribute set information based on given ID

    :param attribute_set_id: 
    :type attribute_set_id: int

    """
    return web.Response(status=200)


async def catalog_attribute_set_repository_v1_save_put(request: web.Request, attribute_set_id, body=None) -> web.Response:
    """products/attribute-sets/{attributeSetId}

    Save attribute set data

    :param attribute_set_id: 
    :type attribute_set_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = EavAttributeSetRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
