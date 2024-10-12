from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.delete_fleets_fleet_id_members_member_id_not_found import DeleteFleetsFleetIdMembersMemberIdNotFound
from openapi_server.models.delete_fleets_fleet_id_squads_squad_id_not_found import DeleteFleetsFleetIdSquadsSquadIdNotFound
from openapi_server.models.delete_fleets_fleet_id_wings_wing_id_not_found import DeleteFleetsFleetIdWingsWingIdNotFound
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_fleet_not_found import GetCharactersCharacterIdFleetNotFound
from openapi_server.models.get_characters_character_id_fleet_ok import GetCharactersCharacterIdFleetOk
from openapi_server.models.get_fleets_fleet_id_members200_ok import GetFleetsFleetIdMembers200Ok
from openapi_server.models.get_fleets_fleet_id_members_not_found import GetFleetsFleetIdMembersNotFound
from openapi_server.models.get_fleets_fleet_id_not_found import GetFleetsFleetIdNotFound
from openapi_server.models.get_fleets_fleet_id_ok import GetFleetsFleetIdOk
from openapi_server.models.get_fleets_fleet_id_wings200_ok import GetFleetsFleetIdWings200Ok
from openapi_server.models.get_fleets_fleet_id_wings_not_found import GetFleetsFleetIdWingsNotFound
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_fleets_fleet_id_members_invitation import PostFleetsFleetIdMembersInvitation
from openapi_server.models.post_fleets_fleet_id_members_not_found import PostFleetsFleetIdMembersNotFound
from openapi_server.models.post_fleets_fleet_id_members_unprocessable_entity import PostFleetsFleetIdMembersUnprocessableEntity
from openapi_server.models.post_fleets_fleet_id_wings_created import PostFleetsFleetIdWingsCreated
from openapi_server.models.post_fleets_fleet_id_wings_not_found import PostFleetsFleetIdWingsNotFound
from openapi_server.models.post_fleets_fleet_id_wings_wing_id_squads_created import PostFleetsFleetIdWingsWingIdSquadsCreated
from openapi_server.models.post_fleets_fleet_id_wings_wing_id_squads_not_found import PostFleetsFleetIdWingsWingIdSquadsNotFound
from openapi_server.models.put_fleets_fleet_id_members_member_id_movement import PutFleetsFleetIdMembersMemberIdMovement
from openapi_server.models.put_fleets_fleet_id_members_member_id_not_found import PutFleetsFleetIdMembersMemberIdNotFound
from openapi_server.models.put_fleets_fleet_id_members_member_id_unprocessable_entity import PutFleetsFleetIdMembersMemberIdUnprocessableEntity
from openapi_server.models.put_fleets_fleet_id_new_settings import PutFleetsFleetIdNewSettings
from openapi_server.models.put_fleets_fleet_id_not_found import PutFleetsFleetIdNotFound
from openapi_server.models.put_fleets_fleet_id_squads_squad_id_naming import PutFleetsFleetIdSquadsSquadIdNaming
from openapi_server.models.put_fleets_fleet_id_squads_squad_id_not_found import PutFleetsFleetIdSquadsSquadIdNotFound
from openapi_server.models.put_fleets_fleet_id_wings_wing_id_naming import PutFleetsFleetIdWingsWingIdNaming
from openapi_server.models.put_fleets_fleet_id_wings_wing_id_not_found import PutFleetsFleetIdWingsWingIdNotFound
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def delete_fleets_fleet_id_members_member_id(request: web.Request, fleet_id, member_id, datasource=None, token=None) -> web.Response:
    """Kick fleet member

    Kick a fleet member  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/{member_id}/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param member_id: The character ID of a member in this fleet
    :type member_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def delete_fleets_fleet_id_squads_squad_id(request: web.Request, fleet_id, squad_id, datasource=None, token=None) -> web.Response:
    """Delete fleet squad

    Delete a fleet squad, only empty squads can be deleted  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/squads/{squad_id}/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param squad_id: The squad to delete
    :type squad_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def delete_fleets_fleet_id_wings_wing_id(request: web.Request, fleet_id, wing_id, datasource=None, token=None) -> web.Response:
    """Delete fleet wing

    Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/{wing_id}/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param wing_id: The wing to delete
    :type wing_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_fleet(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get character fleet info

    Return the fleet ID the character is in, if any.  --- Alternate route: &#x60;/dev/characters/{character_id}/fleet/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/fleet/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/fleet/&#x60;  --- This route is cached for up to 60 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_fleets_fleet_id(request: web.Request, fleet_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get fleet information

    Return details about a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/&#x60;  --- This route is cached for up to 5 seconds

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_fleets_fleet_id_members(request: web.Request, fleet_id, accept_language=None, datasource=None, if_none_match=None, language=None, token=None) -> web.Response:
    """Get fleet members

    Return information about fleet members  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/&#x60;  --- This route is cached for up to 5 seconds

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_fleets_fleet_id_wings(request: web.Request, fleet_id, accept_language=None, datasource=None, if_none_match=None, language=None, token=None) -> web.Response:
    """Get fleet wings

    Return information about wings in a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/&#x60;  --- This route is cached for up to 5 seconds

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_fleets_fleet_id_members(request: web.Request, fleet_id, invitation, datasource=None, token=None) -> web.Response:
    """Create fleet invitation

    Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param invitation: Details of the invitation
    :type invitation: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    invitation = PostFleetsFleetIdMembersInvitation.from_dict(invitation)
    return web.Response(status=200)


async def post_fleets_fleet_id_wings(request: web.Request, fleet_id, datasource=None, token=None) -> web.Response:
    """Create fleet wing

    Create a new wing in a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_fleets_fleet_id_wings_wing_id_squads(request: web.Request, fleet_id, wing_id, datasource=None, token=None) -> web.Response:
    """Create fleet squad

    Create a new squad in a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/{wing_id}/squads/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/{wing_id}/squads/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/{wing_id}/squads/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param wing_id: The wing_id to create squad in
    :type wing_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def put_fleets_fleet_id(request: web.Request, fleet_id, new_settings, datasource=None, token=None) -> web.Response:
    """Update fleet

    Update settings about a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param new_settings: What to update for this fleet
    :type new_settings: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    new_settings = PutFleetsFleetIdNewSettings.from_dict(new_settings)
    return web.Response(status=200)


async def put_fleets_fleet_id_members_member_id(request: web.Request, fleet_id, member_id, movement, datasource=None, token=None) -> web.Response:
    """Move fleet member

    Move a fleet member around  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/{member_id}/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param member_id: The character ID of a member in this fleet
    :type member_id: int
    :param movement: Details of the invitation
    :type movement: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    movement = PutFleetsFleetIdMembersMemberIdMovement.from_dict(movement)
    return web.Response(status=200)


async def put_fleets_fleet_id_squads_squad_id(request: web.Request, fleet_id, squad_id, naming, datasource=None, token=None) -> web.Response:
    """Rename fleet squad

    Rename a fleet squad  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/squads/{squad_id}/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param squad_id: The squad to rename
    :type squad_id: int
    :param naming: New name of the squad
    :type naming: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    naming = PutFleetsFleetIdSquadsSquadIdNaming.from_dict(naming)
    return web.Response(status=200)


async def put_fleets_fleet_id_wings_wing_id(request: web.Request, fleet_id, wing_id, naming, datasource=None, token=None) -> web.Response:
    """Rename fleet wing

    Rename a fleet wing  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/{wing_id}/&#x60; 

    :param fleet_id: ID for a fleet
    :type fleet_id: int
    :param wing_id: The wing to rename
    :type wing_id: int
    :param naming: New name of the wing
    :type naming: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    naming = PutFleetsFleetIdWingsWingIdNaming.from_dict(naming)
    return web.Response(status=200)
