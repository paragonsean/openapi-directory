from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_api_key_privilege_request import AddApiKeyPrivilegeRequest
from openapi_server.models.api_error import ApiError
from openapi_server.models.api_key_change_request import ApiKeyChangeRequest
from openapi_server.models.api_key_creation_request import ApiKeyCreationRequest
from openapi_server.models.api_key_presentation import ApiKeyPresentation
from openapi_server.models.list_of_id4ns import ListOfId4ns
from openapi_server.models.paginated_response_of_api_key_presentation import PaginatedResponseOfApiKeyPresentation
from openapi_server.models.paginated_response_of_api_key_privilege import PaginatedResponseOfApiKeyPrivilege
from openapi_server.models.paginated_response_of_api_key_privilege_info import PaginatedResponseOfApiKeyPrivilegeInfo
from openapi_server.models.paginated_response_of_id4n_presentation import PaginatedResponseOfId4nPresentation
from openapi_server.models.remove_api_key_privilege_request import RemoveApiKeyPrivilegeRequest
from openapi_server import util


async def add_api_key_privilege(request: web.Request, key, body) -> web.Response:
    """Add privilege

    

    :param key: key
    :type key: str
    :param body: addApiKeyPrivilegeRequest
    :type body: dict | bytes

    """
    body = AddApiKeyPrivilegeRequest.from_dict(body)
    return web.Response(status=200)


async def add_api_key_privilege_for_id4ns(request: web.Request, key, privilege, body) -> web.Response:
    """Add ID4ns of a privilege

    

    :param key: key
    :type key: str
    :param privilege: privilege
    :type privilege: str
    :param body: id4ns
    :type body: dict | bytes

    """
    body = ListOfId4ns.from_dict(body)
    return web.Response(status=200)


async def create_new_api_key(request: web.Request, body) -> web.Response:
    """Create API key

    Creation of a new API key.

    :param body: API key to be created.
    :type body: dict | bytes

    """
    body = ApiKeyCreationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_api_key(request: web.Request, key) -> web.Response:
    """Delete API key

    Deletion of an API key.

    :param key: The API key to delete.
    :type key: str

    """
    return web.Response(status=200)


async def get_api_key(request: web.Request, key) -> web.Response:
    """Show API key

    Showing the details of an API key.

    :param key: The API key to show.
    :type key: str

    """
    return web.Response(status=200)


async def list_all_api_key_privileges(request: web.Request, id4n_concerning=None, offset=None, limit=None) -> web.Response:
    """List all privileges

    Listing all possible API key privileges.

    :param id4n_concerning: id4nConcerning
    :type id4n_concerning: bool
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def list_all_api_keys_of_organization(request: web.Request, organization_id=None, offset=None, limit=None) -> web.Response:
    """Find API key by organization

    Finding all API key assigned to the specified organization in a paginated manner.

    :param organization_id: The namespace of the organization to search in.
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def list_api_key_privileges(request: web.Request, key, offset=None, limit=None) -> web.Response:
    """List privileges

    

    :param key: key
    :type key: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def list_id4ns(request: web.Request, key, privilege, offset=None, limit=None) -> web.Response:
    """ID4ns of a privilege

    Listing ID4ns of a id4n concerning privilege

    :param key: key
    :type key: str
    :param privilege: privilege
    :type privilege: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def remove_api_key_privilege(request: web.Request, key, body) -> web.Response:
    """Remove privilege

    

    :param key: key
    :type key: str
    :param body: removeApiKeyPrivilegeRequest
    :type body: dict | bytes

    """
    body = RemoveApiKeyPrivilegeRequest.from_dict(body)
    return web.Response(status=200)


async def remove_api_key_privilege_for_id4ns(request: web.Request, key, privilege, body) -> web.Response:
    """Remove id4ns of a privilege

    

    :param key: key
    :type key: str
    :param privilege: privilege
    :type privilege: str
    :param body: id4ns
    :type body: dict | bytes

    """
    body = ListOfId4ns.from_dict(body)
    return web.Response(status=200)


async def update_api_key(request: web.Request, key, body) -> web.Response:
    """Update API keys

    API keys can be updated with new labels, and be activated and deactivated. The secret or UUID cannot be changed.

    :param key: The API key to be updated.
    :type key: str
    :param body: The new values to apply.
    :type body: dict | bytes

    """
    body = ApiKeyChangeRequest.from_dict(body)
    return web.Response(status=200)
