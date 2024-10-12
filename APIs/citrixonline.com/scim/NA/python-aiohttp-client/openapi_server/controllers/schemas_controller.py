from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_schema import ResourceSchema
from openapi_server.models.service_provider_configs import ServiceProviderConfigs
from openapi_server import util


async def get_service_provider_configs(request: web.Request, authorization) -> web.Response:
    """Get Service Provider Configurations

    Queries service provider configurations. The service provider configurations are defined in SCIM Core Schema (http://www.simplecloud.info/specs/draft-scim-core-schema-01.html#anchor6). This call returns a description, a documentationURL, name, and specURL.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str

    """
    return web.Response(status=200)


async def get_user_schema(request: web.Request, authorization) -> web.Response:
    """Get User Schema

    Queries the user schema. The user schema is defined in SCIM Core Schema (http://www.simplecloud.info/specs/draft-scim-core-schema-01.html#resource-schema).

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str

    """
    return web.Response(status=200)
