from typing import List, Dict
from aiohttp import web

from openapi_server.models.attested_data import AttestedData
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.instance import Instance
from openapi_server import util


async def attested_get_document(request: web.Request, api_version, metadata, nonce=None) -> web.Response:
    """attested_get_document

    Get Attested Data for the Virtual Machine.

    :param api_version: This is the API version to use.
    :type api_version: str
    :param metadata: This must be set to &#39;true&#39;.
    :type metadata: str
    :param nonce: This is a string of up to 32 random alphanumeric characters.
    :type nonce: str

    """
    return web.Response(status=200)


async def instances_get_metadata(request: web.Request, api_version, metadata) -> web.Response:
    """instances_get_metadata

    Get Instance Metadata for the Virtual Machine.

    :param api_version: This is the API version to use.
    :type api_version: str
    :param metadata: This must be set to &#39;true&#39;.
    :type metadata: str

    """
    return web.Response(status=200)
