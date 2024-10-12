from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.framework_metadata_object_interface import FrameworkMetadataObjectInterface
from openapi_server import util


async def rma_rma_attributes_management_v1_get_custom_attributes_metadata_get(request: web.Request, data_object_class_name=None) -> web.Response:
    """returnsAttributeMetadata/custom

    Get custom attribute metadata for the given Data object&#39;s attribute set

    :param data_object_class_name: Data object class name
    :type data_object_class_name: str

    """
    return web.Response(status=200)
