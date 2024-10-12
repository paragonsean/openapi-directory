from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.create_collection_request import CreateCollectionRequest
from openapi_server.models.guid_collection import GuidCollection
from openapi_server.models.id4n import Id4n
from openapi_server.models.list_of_id4n_properties import ListOfId4nProperties
from openapi_server.models.list_of_id4ns import ListOfId4ns
from openapi_server.models.paginated_response_of_guid import PaginatedResponseOfGuid
from openapi_server.models.paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection
from openapi_server import util


async def add_elements_to_collection(request: web.Request, id4n, body) -> web.Response:
    """Add elements to collection

    

    :param id4n: id4n
    :type id4n: str
    :param body: listOfGuids
    :type body: dict | bytes

    """
    body = ListOfId4ns.from_dict(body)
    return web.Response(status=200)


async def create_collection(request: web.Request, body) -> web.Response:
    """Create collection

    

    :param body: createInfo
    :type body: dict | bytes

    """
    body = CreateCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_collection(request: web.Request, id4n) -> web.Response:
    """Delete collection

    

    :param id4n: id4n
    :type id4n: str

    """
    return web.Response(status=200)


async def delete_properties(request: web.Request, id4n, organization_id, body) -> web.Response:
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


async def find_collection(request: web.Request, id4n) -> web.Response:
    """Find collection

    

    :param id4n: id4n
    :type id4n: str

    """
    return web.Response(status=200)


async def get_all_collections_of_organization(request: web.Request, organization_id, offset=None, limit=None, type=None, label=None, label_prefix=None, _property=None) -> web.Response:
    """Get collections of organization

    Retrieving all collections of an organization in a paginated manner. You may filter the results by specifying id4n properties with filter operations (eq, in, ne) in the query parameters. e.g. &#x60;com.yourcompany.orderId.eq&#x3D;1234&#x60;  

    :param organization_id: The namespace of the organization
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int
    :param type: Filter by this type
    :type type: str
    :param label: Filter by this label
    :type label: str
    :param label_prefix: Filter by this label prefix
    :type label_prefix: str
    :param _property: List of i4dn property filter. e.g. \&quot;com.myorga.state:IN:waiting|processing\&quot; or \&quot;com.myorga.orderId:EQ:SAP001\&quot;
    :type _property: List[str]

    """
    return web.Response(status=200)


async def get_multiple_properties(request: web.Request, id4ns, organization_id=None) -> web.Response:
    """Get multiple ID4n properties

    Get a list of ID4n properties for the specified ID4ns.

    :param id4ns: The list of ID4ns to resolve.
    :type id4ns: List[str]
    :param organization_id: The organization namespace.
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_properties(request: web.Request, id4n, organization_id=None) -> web.Response:
    """Retrieve ID4n properties

    List all properties of an id4n.

    :param id4n: The id4n
    :type id4n: str
    :param organization_id: The organization namespace.
    :type organization_id: str

    """
    return web.Response(status=200)


async def list_elements_of_collection(request: web.Request, id4n, offset=None, limit=None, organization_id=None) -> web.Response:
    """List contents of the collection

    

    :param id4n: id4n
    :type id4n: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int
    :param organization_id: The organization namespace.
    :type organization_id: str

    """
    return web.Response(status=200)


async def patch_properties(request: web.Request, id4n, organization_id, body) -> web.Response:
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


async def remove_elements_from_collection(request: web.Request, id4n, body) -> web.Response:
    """Remove elements from collection

    

    :param id4n: id4n
    :type id4n: str
    :param body: listOfGuids
    :type body: dict | bytes

    """
    body = ListOfId4ns.from_dict(body)
    return web.Response(status=200)


async def update_collection(request: web.Request, id4n, body) -> web.Response:
    """Update collection

    Update collection changing only the given values

    :param id4n: id4n
    :type id4n: str
    :param body: request
    :type body: dict | bytes

    """
    body = GuidCollection.from_dict(body)
    return web.Response(status=200)
