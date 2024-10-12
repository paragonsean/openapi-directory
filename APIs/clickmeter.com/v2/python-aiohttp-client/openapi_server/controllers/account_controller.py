from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_accounting_domain_whitelist_entry import ApiCoreDtoAccountingDomainWhitelistEntry
from openapi_server.models.api_core_dto_accounting_guest import ApiCoreDtoAccountingGuest
from openapi_server.models.api_core_dto_accounting_ip_blacklist_entry import ApiCoreDtoAccountingIpBlacklistEntry
from openapi_server.models.api_core_dto_accounting_plan import ApiCoreDtoAccountingPlan
from openapi_server.models.api_core_dto_accounting_user import ApiCoreDtoAccountingUser
from openapi_server.models.api_core_requests_permission_patch_request import ApiCoreRequestsPermissionPatchRequest
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_accounting_domain_whitelist_entry import ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry
from openapi_server.models.api_core_responses_entities_response_api_core_dto_accounting_ip_blacklist_entry import ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry
from openapi_server.models.api_core_responses_entities_response_api_core_dto_grants_grant import ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server import util


async def account_delete_domain_whitelist(request: web.Request, whitelist_id) -> web.Response:
    """Delete an domain entry

    

    :param whitelist_id: The id of the domain to delete
    :type whitelist_id: str

    """
    return web.Response(status=200)


async def account_delete_guest(request: web.Request, guest_id) -> web.Response:
    """Delete a guest

    

    :param guest_id: Id of the guest
    :type guest_id: int

    """
    return web.Response(status=200)


async def account_delete_ip_blacklist(request: web.Request, blacklist_id) -> web.Response:
    """Delete an ip blacklist entry

    

    :param blacklist_id: The id of the ip to delete
    :type blacklist_id: str

    """
    return web.Response(status=200)


async def account_get(request: web.Request, ) -> web.Response:
    """Retrieve current account data

    


    """
    return web.Response(status=200)


async def account_get_domain_whitelist(request: web.Request, offset=None, limit=None) -> web.Response:
    """Retrieve list of a domains allowed to redirect in DDU mode

    

    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int

    """
    return web.Response(status=200)


async def account_get_guest(request: web.Request, guest_id) -> web.Response:
    """Retrieve a guest

    

    :param guest_id: Id of the guest
    :type guest_id: int

    """
    return web.Response(status=200)


async def account_get_guests(request: web.Request, offset=None, limit=None, sort_by=None, sort_direction=None, text_search=None) -> web.Response:
    """Retrieve list of a guest

    

    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param sort_by: Field to sort by
    :type sort_by: str
    :param sort_direction: Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot;
    :type sort_direction: str
    :param text_search: Filter fields by this pattern
    :type text_search: str

    """
    return web.Response(status=200)


async def account_get_guests_count(request: web.Request, text_search=None) -> web.Response:
    """Retrieve count of guests

    

    :param text_search: Filter fields by this pattern
    :type text_search: str

    """
    return web.Response(status=200)


async def account_get_ip_blacklist(request: web.Request, offset=None, limit=None) -> web.Response:
    """Retrieve list of a ip to exclude from event tracking

    

    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int

    """
    return web.Response(status=200)


async def account_get_permissions(request: web.Request, guest_id, entity_type=None, offset=None, limit=None, type=None, entity_id=None) -> web.Response:
    """Retrieve permissions for a guest

    

    :param guest_id: Id of the guest
    :type guest_id: int
    :param entity_type: Can be \&quot;datapoint\&quot; or \&quot;group\&quot;
    :type entity_type: str
    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param type: Can be \&quot;w\&quot; or \&quot;r\&quot;
    :type type: str
    :param entity_id: Optional id of the datapoint/group entity to filter by
    :type entity_id: int

    """
    return web.Response(status=200)


async def account_get_permissions_count(request: web.Request, guest_id, entity_type=None, type=None, entity_id=None) -> web.Response:
    """Retrieve count of the permissions for a guest

    

    :param guest_id: Id of the guest
    :type guest_id: int
    :param entity_type: Can be \&quot;datapoint\&quot; or \&quot;group\&quot;
    :type entity_type: str
    :param type: Can be \&quot;w\&quot; or \&quot;r\&quot;
    :type type: str
    :param entity_id: Optional id of the datapoint/group entity to filter by
    :type entity_id: int

    """
    return web.Response(status=200)


async def account_get_plan(request: web.Request, ) -> web.Response:
    """Retrieve current account plan

    


    """
    return web.Response(status=200)


async def account_guests_guest_id_type_permissions_patch_post(request: web.Request, guest_id, type, body) -> web.Response:
    """Change the permission on a shared object

    

    :param guest_id: Id of the guest
    :type guest_id: int
    :param type: Can be \&quot;datapoint\&quot; or \&quot;group\&quot;
    :type type: str
    :param body: The patch permission request
    :type body: dict | bytes

    """
    body = ApiCoreRequestsPermissionPatchRequest.from_dict(body)
    return web.Response(status=200)


async def account_patch_permissions(request: web.Request, guest_id, type, body) -> web.Response:
    """Change the permission on a shared object

    

    :param guest_id: Id of the guest
    :type guest_id: int
    :param type: Can be \&quot;datapoint\&quot; or \&quot;group\&quot;
    :type type: str
    :param body: The patch permission request
    :type body: dict | bytes

    """
    body = ApiCoreRequestsPermissionPatchRequest.from_dict(body)
    return web.Response(status=200)


async def account_post(request: web.Request, body) -> web.Response:
    """Update current account data

    

    :param body: 
    :type body: dict | bytes

    """
    body = ApiCoreDtoAccountingUser.from_dict(body)
    return web.Response(status=200)


async def account_post_guest(request: web.Request, guest_id, body) -> web.Response:
    """Update a guest

    

    :param guest_id: Id of the guest
    :type guest_id: int
    :param body: Guest object with field updated
    :type body: dict | bytes

    """
    body = ApiCoreDtoAccountingGuest.from_dict(body)
    return web.Response(status=200)


async def account_put_domain_whitelist(request: web.Request, body) -> web.Response:
    """Create an domain entry

    

    :param body: The entry to add
    :type body: dict | bytes

    """
    body = ApiCoreDtoAccountingDomainWhitelistEntry.from_dict(body)
    return web.Response(status=200)


async def account_put_guest(request: web.Request, body) -> web.Response:
    """Create a guest

    

    :param body: Guest object to create
    :type body: dict | bytes

    """
    body = ApiCoreDtoAccountingGuest.from_dict(body)
    return web.Response(status=200)


async def account_put_ip_blacklist(request: web.Request, body) -> web.Response:
    """Create an ip blacklist entry

    

    :param body: The entry to add
    :type body: dict | bytes

    """
    body = ApiCoreDtoAccountingIpBlacklistEntry.from_dict(body)
    return web.Response(status=200)
