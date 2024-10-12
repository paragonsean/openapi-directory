from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.guid_alias import GuidAlias
from openapi_server.models.paginated_response_of_guid import PaginatedResponseOfGuid
from openapi_server import util


async def add_guid_alias(request: web.Request, id4n, alias_type, body) -> web.Response:
    """Add alias for GUID or Collection

    Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)

    :param id4n: The GUID or Collection to operate on
    :type id4n: str
    :param alias_type: Alias type, see the corresponding API model
    :type alias_type: str
    :param body: The alias to add or update
    :type body: dict | bytes

    """
    body = GuidAlias.from_dict(body)
    return web.Response(status=200)


async def get_guid_alias_types(request: web.Request, ) -> web.Response:
    """List all supported alias types

    Retrieve this list to find out all alias types to use with alias search and change operations


    """
    return web.Response(status=200)


async def get_guid_aliases(request: web.Request, id4n) -> web.Response:
    """Get all aliases for the given GUID or Collection.

    Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

    :param id4n: The GUID or Collection to operate on
    :type id4n: str

    """
    return web.Response(status=200)


async def remove_guid_alias(request: web.Request, id4n, alias_type) -> web.Response:
    """Remove aliases from GUID or Collection

    Remove the alias of the given type

    :param id4n: The GUID or Collection to operate on
    :type id4n: str
    :param alias_type: Alias type, see the corresponding API model
    :type alias_type: str

    """
    return web.Response(status=200)


async def search_by_alias(request: web.Request, alias, alias_type, offset=None, limit=None) -> web.Response:
    """Search for GUIDs by alias

    

    :param alias: The alias to search for
    :type alias: str
    :param alias_type: Alias type type to search for
    :type alias_type: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)
