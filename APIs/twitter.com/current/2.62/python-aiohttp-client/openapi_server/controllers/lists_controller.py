from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get2_lists_id_response import Get2ListsIdResponse
from openapi_server.models.get2_users_id_followed_lists_response import Get2UsersIdFollowedListsResponse
from openapi_server.models.get2_users_id_list_memberships_response import Get2UsersIdListMembershipsResponse
from openapi_server.models.get2_users_id_owned_lists_response import Get2UsersIdOwnedListsResponse
from openapi_server.models.get2_users_id_pinned_lists_response import Get2UsersIdPinnedListsResponse
from openapi_server.models.list_add_user_request import ListAddUserRequest
from openapi_server.models.list_create_request import ListCreateRequest
from openapi_server.models.list_create_response import ListCreateResponse
from openapi_server.models.list_delete_response import ListDeleteResponse
from openapi_server.models.list_followed_request import ListFollowedRequest
from openapi_server.models.list_followed_response import ListFollowedResponse
from openapi_server.models.list_mutate_response import ListMutateResponse
from openapi_server.models.list_pinned_request import ListPinnedRequest
from openapi_server.models.list_pinned_response import ListPinnedResponse
from openapi_server.models.list_unpin_response import ListUnpinResponse
from openapi_server.models.list_update_request import ListUpdateRequest
from openapi_server.models.list_update_response import ListUpdateResponse
from openapi_server.models.problem import Problem
from openapi_server import util


async def get_user_list_memberships(request: web.Request, id, max_results=None, pagination_token=None, list_fields=None, expansions=None, user_fields=None) -> web.Response:
    """Get a User&#39;s List Memberships

    Get a User&#39;s List Memberships.

    :param id: The ID of the User to lookup.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param list_fields: A comma separated list of List fields to display.
    :type list_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]

    """
    return web.Response(status=200)


async def list_add_member(request: web.Request, id, body=None) -> web.Response:
    """Add a List member

    Causes a User to become a member of a List.

    :param id: The ID of the List for which to add a member.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListAddUserRequest.from_dict(body)
    return web.Response(status=200)


async def list_id_create(request: web.Request, body=None) -> web.Response:
    """Create List

    Creates a new List.

    :param body: 
    :type body: dict | bytes

    """
    body = ListCreateRequest.from_dict(body)
    return web.Response(status=200)


async def list_id_delete(request: web.Request, id) -> web.Response:
    """Delete List

    Delete a List that you own.

    :param id: The ID of the List to delete.
    :type id: str

    """
    return web.Response(status=200)


async def list_id_get(request: web.Request, id, list_fields=None, expansions=None, user_fields=None) -> web.Response:
    """List lookup by List ID.

    Returns a List.

    :param id: The ID of the List.
    :type id: str
    :param list_fields: A comma separated list of List fields to display.
    :type list_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]

    """
    return web.Response(status=200)


async def list_id_update(request: web.Request, id, body=None) -> web.Response:
    """Update List.

    Update a List that you own.

    :param id: The ID of the List to modify.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def list_remove_member(request: web.Request, id, user_id) -> web.Response:
    """Remove a List member

    Causes a User to be removed from the members of a List.

    :param id: The ID of the List to remove a member.
    :type id: str
    :param user_id: The ID of User that will be removed from the List.
    :type user_id: str

    """
    return web.Response(status=200)


async def list_user_follow(request: web.Request, id, body=None) -> web.Response:
    """Follow a List

    Causes a User to follow a List.

    :param id: The ID of the authenticated source User that will follow the List.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListFollowedRequest.from_dict(body)
    return web.Response(status=200)


async def list_user_owned_lists(request: web.Request, id, max_results=None, pagination_token=None, list_fields=None, expansions=None, user_fields=None) -> web.Response:
    """Get a User&#39;s Owned Lists.

    Get a User&#39;s Owned Lists.

    :param id: The ID of the User to lookup.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param list_fields: A comma separated list of List fields to display.
    :type list_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]

    """
    return web.Response(status=200)


async def list_user_pin(request: web.Request, id, body) -> web.Response:
    """Pin a List

    Causes a User to pin a List.

    :param id: The ID of the authenticated source User that will pin the List.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListPinnedRequest.from_dict(body)
    return web.Response(status=200)


async def list_user_pinned_lists(request: web.Request, id, list_fields=None, expansions=None, user_fields=None) -> web.Response:
    """Get a User&#39;s Pinned Lists

    Get a User&#39;s Pinned Lists.

    :param id: The ID of the authenticated source User for whom to return results.
    :type id: str
    :param list_fields: A comma separated list of List fields to display.
    :type list_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]

    """
    return web.Response(status=200)


async def list_user_unfollow(request: web.Request, id, list_id) -> web.Response:
    """Unfollow a List

    Causes a User to unfollow a List.

    :param id: The ID of the authenticated source User that will unfollow the List.
    :type id: str
    :param list_id: The ID of the List to unfollow.
    :type list_id: str

    """
    return web.Response(status=200)


async def list_user_unpin(request: web.Request, id, list_id) -> web.Response:
    """Unpin a List

    Causes a User to remove a pinned List.

    :param id: The ID of the authenticated source User for whom to return results.
    :type id: str
    :param list_id: The ID of the List to unpin.
    :type list_id: str

    """
    return web.Response(status=200)


async def user_followed_lists(request: web.Request, id, max_results=None, pagination_token=None, list_fields=None, expansions=None, user_fields=None) -> web.Response:
    """Get User&#39;s Followed Lists

    Returns a User&#39;s followed Lists.

    :param id: The ID of the User to lookup.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param list_fields: A comma separated list of List fields to display.
    :type list_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]

    """
    return web.Response(status=200)
