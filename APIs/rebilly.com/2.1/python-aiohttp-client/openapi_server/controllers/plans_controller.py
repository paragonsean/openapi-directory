from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.plan import Plan
from openapi_server import util


async def delete_plan(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a Plan

    Delete a Plan with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_plan(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a plan

    Retrieve a plan with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_plan_collection(request: web.Request, organization_id=None, filter=None, sort=None, limit=None, offset=None, q=None) -> web.Response:
    """Retrieve a list of plans

    Retrieve a list of plans. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param q: The partial search of the text fields.
    :type q: str

    """
    return web.Response(status=200)


async def post_plan(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a plan

    Create a plan. 

    :param body: Plan resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Plan.from_dict(body)
    return web.Response(status=200)


async def put_plan(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create or update a Plan with predefined ID

    Create or update a Plan with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Plan resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Plan.from_dict(body)
    return web.Response(status=200)
