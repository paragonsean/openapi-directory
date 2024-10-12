from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.create_guid_request import CreateGuidRequest
from openapi_server.models.guid import Guid
from openapi_server.models.guid_alias import GuidAlias
from openapi_server.models.id4n_presentation import Id4nPresentation
from openapi_server.models.import_gs1_codes_request import ImportGS1CodesRequest
from openapi_server.models.list_of_id4n_properties import ListOfId4nProperties
from openapi_server.models.list_of_id4ns import ListOfId4ns
from openapi_server.models.paginated_response_of_guid import PaginatedResponseOfGuid
from openapi_server.models.paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection
from openapi_server import util


async def add_guid_alias_0(request: web.Request, id4n, alias_type, body) -> web.Response:
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


async def create_guid(request: web.Request, body) -> web.Response:
    """Create GUID(s)

    Creating one or more GUIDs with a specified length.

    :param body: GUID creation model
    :type body: dict | bytes

    """
    body = CreateGuidRequest.from_dict(body)
    return web.Response(status=200)


async def delete_properties_0(request: web.Request, id4n, organization_id, body) -> web.Response:
    """Delete ID4n properties

    Partial deletion of id4n properties. If the property does not exist, it will be ignored.

    :param id4n: The id4n
    :type id4n: str
    :param organization_id: The organization namespace to work on while deleting the properties.
    :type organization_id: str
    :param body: A set of property keys to delete.
    :type body: List[str]

    """
    return web.Response(status=200)


async def get_collections(request: web.Request, id4n, organization_id=None, offset=None, limit=None) -> web.Response:
    """Retrieve collections of an ID

    Retrieving all owned or holding collections the specified id4n is assigned to.

    :param id4n: The ID which the collections should contain
    :type id4n: str
    :param organization_id: The organization holding the collections.
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_guid(request: web.Request, id4n, organization_id=None) -> web.Response:
    """Retrieve GUID information

    

    :param id4n: The GUID number
    :type id4n: str
    :param organization_id: The organization namespace to resolve.
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_guid_aliases_0(request: web.Request, id4n) -> web.Response:
    """Get all aliases for the given GUID or Collection.

    Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

    :param id4n: The GUID or Collection to operate on
    :type id4n: str

    """
    return web.Response(status=200)


async def get_guids_without_collection(request: web.Request, organization_id, offset=None, limit=None) -> web.Response:
    """Retrieve GUIDs not in any collection

    

    :param organization_id: The namespace of the organization to search GUIDs for
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_id4n(request: web.Request, id4n, organization_id=None) -> web.Response:
    """Retrieve ID4n information

    Retrieving basic information about an ID like the type and the creation time.

    :param id4n: The ID to resolve to
    :type id4n: str
    :param organization_id: The organization namespace to resolve.
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_multiple_properties_0(request: web.Request, id4ns, organization_id=None) -> web.Response:
    """Get multiple ID4n properties

    Get a list of ID4n properties for the specified ID4ns.

    :param id4ns: The list of ID4ns to resolve.
    :type id4ns: List[str]
    :param organization_id: The organization namespace.
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_properties_0(request: web.Request, id4n, organization_id=None) -> web.Response:
    """Retrieve ID4n properties

    List all properties of an id4n.

    :param id4n: The id4n
    :type id4n: str
    :param organization_id: The organization namespace.
    :type organization_id: str

    """
    return web.Response(status=200)


async def import_gs1_codes(request: web.Request, body) -> web.Response:
    """Import GS1/MAPP codes

    Importing GS1/MAPP codes that contain unique components.

    :param body: The information how the MAPP codes should be imported and the list of MAPP codes
    :type body: dict | bytes

    """
    body = ImportGS1CodesRequest.from_dict(body)
    return web.Response(status=200)


async def patch_properties_0(request: web.Request, id4n, organization_id, body) -> web.Response:
    """Patch ID4n properties

    Partial updating of id4n properties. If a property contains a null value the property will be deleted other values will be saved and overwritten if they already exist.

    :param id4n: The id4n
    :type id4n: str
    :param organization_id: The organization namespace to work on while patching the properties.
    :type organization_id: str
    :param body: The properties to update.
    :type body: Dict[str, str]

    """
    return web.Response(status=200)


async def remove_guid_alias_0(request: web.Request, id4n, alias_type) -> web.Response:
    """Remove aliases from GUID or Collection

    Remove the alias of the given type

    :param id4n: The GUID or Collection to operate on
    :type id4n: str
    :param alias_type: Alias type, see the corresponding API model
    :type alias_type: str

    """
    return web.Response(status=200)


async def update_guid(request: web.Request, id4n, body) -> web.Response:
    """Change GUID information.

    Allows ownership transfer.

    :param id4n: The GUID number
    :type id4n: str
    :param body: request
    :type body: dict | bytes

    """
    body = Guid.from_dict(body)
    return web.Response(status=200)
