from typing import List, Dict
from aiohttp import web

from openapi_server.models.blocklist import Blocklist
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server import util


async def delete_blocklist(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a blocklist

    Delete a blocklist with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_blocklist(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a blocklist

    Retrieve a blocklist with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_blocklist_collection(request: web.Request, organization_id=None, limit=None, offset=None, sort=None, filter=None, q=None) -> web.Response:
    """Retrieve a list of blocklists

    Retrieve a list of blocklists. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param q: The partial search of the text fields.
    :type q: str

    """
    return web.Response(status=200)


async def post_blocklist(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a blocklist

    Create a blocklist. 

    :param body: Blocklist resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Blocklist.from_dict(body)
    return web.Response(status=200)


async def put_blocklist(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create a blocklist with predefined ID

    Create a blocklist with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Blocklist resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Blocklist.from_dict(body)
    return web.Response(status=200)
