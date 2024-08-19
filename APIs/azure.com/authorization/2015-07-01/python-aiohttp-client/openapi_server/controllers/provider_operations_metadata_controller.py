from typing import List, Dict
from aiohttp import web

from openapi_server.models.provider_operations_metadata import ProviderOperationsMetadata
from openapi_server.models.provider_operations_metadata_list_result import ProviderOperationsMetadataListResult
from openapi_server import util


async def provider_operations_metadata_get(request: web.Request, resource_provider_namespace, api_version, expand=None) -> web.Response:
    """provider_operations_metadata_get

    Gets provider operations metadata for the specified resource provider.

    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param expand: Specifies whether to expand the values.
    :type expand: str

    """
    return web.Response(status=200)


async def provider_operations_metadata_list(request: web.Request, api_version, expand=None) -> web.Response:
    """provider_operations_metadata_list

    Gets provider operations metadata for all resource providers.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param expand: Specifies whether to expand the values.
    :type expand: str

    """
    return web.Response(status=200)
