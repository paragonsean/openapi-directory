from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.document import Document
from openapi_server.models.organization import Organization
from openapi_server.models.paginated_response_of_document import PaginatedResponseOfDocument
from openapi_server.models.paginated_response_of_history_item import PaginatedResponseOfHistoryItem
from openapi_server.models.route import Route
from openapi_server.models.who_is_response import WhoIsResponse
from openapi_server import util


async def get_public_document(request: web.Request, organization_id, id4n, file_name) -> web.Response:
    """Retrieve a public document (meta-data only, no content)

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str

    """
    return web.Response(status=200)


async def get_routes(request: web.Request, id4n, type, interpolate=None) -> web.Response:
    """Retrieve all public routes for a GUID

    

    :param id4n: id4n
    :type id4n: str
    :param type: type
    :type type: str
    :param interpolate: interpolate
    :type interpolate: bool

    """
    return web.Response(status=200)


async def go(request: web.Request, guid) -> web.Response:
    """Forward

    Forwarding to the designated route defined in the routing,

    :param guid: guid
    :type guid: str

    """
    return web.Response(status=200)


async def list_all_public_documents(request: web.Request, id4n, organization_id=None, owner=None, offset=None, limit=None) -> web.Response:
    """List public documents

    Listing all public documents of an id4n

    :param id4n: id4n
    :type id4n: str
    :param organization_id: organizationId
    :type organization_id: str
    :param owner: Filter by owner organization
    :type owner: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def list_public_history(request: web.Request, id4n, offset=None, limit=None) -> web.Response:
    """Shows the public history of the given GUID

    Only contains public history items

    :param id4n: GUID to retrieve the history for
    :type id4n: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def read_organization_info(request: web.Request, organization_id) -> web.Response:
    """Read public organization information

    

    :param organization_id: Organization ID
    :type organization_id: str

    """
    return web.Response(status=200)


async def read_public_document(request: web.Request, organization_id, id4n, file_name) -> web.Response:
    """Read public document contents

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str

    """
    return web.Response(status=200)


async def resolve_image_using_get_0(request: web.Request, image_id) -> web.Response:
    """Resolve image

    

    :param image_id: The id of the image to be resolved.
    :type image_id: str

    """
    return web.Response(status=200)


async def resolve_who_is_entry(request: web.Request, id4n) -> web.Response:
    """Resolve owner of id4n

    

    :param id4n: id4n
    :type id4n: str

    """
    return web.Response(status=200)
