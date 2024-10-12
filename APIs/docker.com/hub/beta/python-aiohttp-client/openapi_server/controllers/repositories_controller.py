from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.paginated_tags import PaginatedTags
from openapi_server.models.tag import Tag
from openapi_server import util


async def v2_namespaces_namespace_repositories_repository_tags_get(request: web.Request, namespace, repository, page=None, page_size=None) -> web.Response:
    """List repository tags

    

    :param namespace: 
    :type namespace: str
    :param repository: 
    :type repository: str
    :param page: Page number to get. Defaults to 1.
    :type page: int
    :param page_size: Number of items to get per page. Defaults to 10. Max of 100.
    :type page_size: int

    """
    return web.Response(status=200)


async def v2_namespaces_namespace_repositories_repository_tags_head(request: web.Request, namespace, repository) -> web.Response:
    """Check repository tags

    

    :param namespace: 
    :type namespace: str
    :param repository: 
    :type repository: str

    """
    return web.Response(status=200)


async def v2_namespaces_namespace_repositories_repository_tags_tag_get(request: web.Request, namespace, repository, tag) -> web.Response:
    """Read repository tag

    

    :param namespace: 
    :type namespace: str
    :param repository: 
    :type repository: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def v2_namespaces_namespace_repositories_repository_tags_tag_head(request: web.Request, namespace, repository, tag) -> web.Response:
    """Check repository tag

    

    :param namespace: 
    :type namespace: str
    :param repository: 
    :type repository: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)
