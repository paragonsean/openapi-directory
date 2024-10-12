from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.three_d_secure import ThreeDSecure
from openapi_server import util


async def get3_d_secure(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a ThreeDSecure entry

    Retrieve a ThreeDSecure entry with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get3_d_secure_collection(request: web.Request, organization_id=None, limit=None, offset=None) -> web.Response:
    """Retrieve a list of ThreeDSecure entries

    

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int

    """
    return web.Response(status=200)


async def post3_d_secure(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a ThreeDSecure entry

    Create a ThreeDSecure entry. 

    :param body: ThreeDSecure resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = ThreeDSecure.from_dict(body)
    return web.Response(status=200)
