from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_domains_domain import ApiCoreDtoDomainsDomain
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server import util


async def domains_count(request: web.Request, type=None, name=None) -> web.Response:
    """Retrieve count of domains

    

    :param type: Type of domain (\&quot;system\&quot;/\&quot;go\&quot;/\&quot;personal\&quot;/\&quot;dedicated\&quot;). If not specified default is \&quot;system\&quot;
    :type type: str
    :param name: Filter domains with this anmen
    :type name: str

    """
    return web.Response(status=200)


async def domains_delete(request: web.Request, id) -> web.Response:
    """Delete a domain

    

    :param id: Id of domain
    :type id: int

    """
    return web.Response(status=200)


async def domains_get(request: web.Request, offset=None, limit=None, type=None, name=None) -> web.Response:
    """Retrieve a list of domains

    

    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param type: Type of domain (\&quot;system\&quot;/\&quot;go\&quot;/\&quot;personal\&quot;/\&quot;dedicated\&quot;). If not specified default is \&quot;system\&quot;
    :type type: str
    :param name: Filter domains with this anmen
    :type name: str

    """
    return web.Response(status=200)


async def domains_id_get(request: web.Request, id) -> web.Response:
    """Get a domain

    

    :param id: Id of domain
    :type id: int

    """
    return web.Response(status=200)


async def domains_put(request: web.Request, body) -> web.Response:
    """Create a domain

    

    :param body: The domain to create
    :type body: dict | bytes

    """
    body = ApiCoreDtoDomainsDomain.from_dict(body)
    return web.Response(status=200)


async def domains_update(request: web.Request, id, body) -> web.Response:
    """Update a domain

    

    :param id: Id of domain
    :type id: int
    :param body: The domain to update
    :type body: dict | bytes

    """
    body = ApiCoreDtoDomainsDomain.from_dict(body)
    return web.Response(status=200)
