from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_available_locales200_response import GetAvailableLocales200Response
from openapi_server.models.user_get_available_themes200_response import UserGetAvailableThemes200Response
from openapi_server.models.user_get_bungie_net_user_by_id200_response import UserGetBungieNetUserById200Response
from openapi_server.models.user_get_credential_types_for_target_account200_response import UserGetCredentialTypesForTargetAccount200Response
from openapi_server.models.user_get_membership_data_by_id200_response import UserGetMembershipDataById200Response
from openapi_server.models.user_get_membership_from_hard_linked_credential200_response import UserGetMembershipFromHardLinkedCredential200Response
from openapi_server.models.user_search_by_global_name_post200_response import UserSearchByGlobalNamePost200Response
from openapi_server import util


async def user_get_available_themes(request: web.Request, ) -> web.Response:
    """user_get_available_themes

    Returns a list of all available user themes.


    """
    return web.Response(status=200)


async def user_get_bungie_net_user_by_id(request: web.Request, id) -> web.Response:
    """user_get_bungie_net_user_by_id

    Loads a bungienet user by membership id.

    :param id: The requested Bungie.net membership id.
    :type id: int

    """
    return web.Response(status=200)


async def user_get_credential_types_for_target_account(request: web.Request, membership_id) -> web.Response:
    """user_get_credential_types_for_target_account

    Returns a list of credential types attached to the requested account

    :param membership_id: The user&#39;s membership id
    :type membership_id: int

    """
    return web.Response(status=200)


async def user_get_membership_data_by_id(request: web.Request, membership_id, membership_type) -> web.Response:
    """user_get_membership_data_by_id

    Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

    :param membership_id: The membership ID of the target user.
    :type membership_id: int
    :param membership_type: Type of the supplied membership ID.
    :type membership_type: int

    """
    return web.Response(status=200)


async def user_get_membership_data_for_current_user(request: web.Request, ) -> web.Response:
    """user_get_membership_data_for_current_user

    Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.


    """
    return web.Response(status=200)


async def user_get_membership_from_hard_linked_credential(request: web.Request, credential, cr_type) -> web.Response:
    """user_get_membership_from_hard_linked_credential

    Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

    :param credential: The credential to look up. Must be a valid SteamID64.
    :type credential: str
    :param cr_type: The credential type. &#39;SteamId&#39; is the only valid value at present.
    :type cr_type: int

    """
    return web.Response(status=200)


async def user_get_sanitized_platform_display_names(request: web.Request, membership_id) -> web.Response:
    """user_get_sanitized_platform_display_names

    Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

    :param membership_id: The requested membership id to load.
    :type membership_id: int

    """
    return web.Response(status=200)


async def user_search_by_global_name_post(request: web.Request, page) -> web.Response:
    """user_search_by_global_name_post

    Given the prefix of a global display name, returns all users who share that name.

    :param page: The zero-based page of results you desire.
    :type page: int

    """
    return web.Response(status=200)


async def user_search_by_global_name_prefix(request: web.Request, display_name_prefix, page) -> web.Response:
    """user_search_by_global_name_prefix

    [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

    :param display_name_prefix: The display name prefix you&#39;re looking for.
    :type display_name_prefix: str
    :param page: The zero-based page of results you desire.
    :type page: int

    """
    return web.Response(status=200)
