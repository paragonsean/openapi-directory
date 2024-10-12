from typing import List, Dict
from aiohttp import web

from openapi_server.models.destiny2_get_clan_aggregate_stats200_response import Destiny2GetClanAggregateStats200Response
from openapi_server.models.destiny2_get_clan_leaderboards200_response import Destiny2GetClanLeaderboards200Response
from openapi_server.models.destiny2_get_public_vendors200_response import Destiny2GetPublicVendors200Response
from openapi_server.models.destiny2_insert_socket_plug200_response import Destiny2InsertSocketPlug200Response
from openapi_server import util


async def destiny2_get_clan_aggregate_stats_0(request: web.Request, group_id, modes=None) -> web.Response:
    """destiny2_get_clan_aggregate_stats_0

    Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

    :param group_id: Group ID of the clan whose leaderboards you wish to fetch.
    :type group_id: int
    :param modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    :type modes: str

    """
    return web.Response(status=200)


async def destiny2_get_clan_leaderboards_0(request: web.Request, group_id, maxtop=None, modes=None, statid=None) -> web.Response:
    """destiny2_get_clan_leaderboards_0

    Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

    :param group_id: Group ID of the clan whose leaderboards you wish to fetch.
    :type group_id: int
    :param maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
    :type maxtop: int
    :param modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    :type modes: str
    :param statid: ID of stat to return rather than returning all Leaderboard stats.
    :type statid: str

    """
    return web.Response(status=200)


async def destiny2_get_leaderboards_0(request: web.Request, destiny_membership_id, membership_type, maxtop=None, modes=None, statid=None) -> web.Response:
    """destiny2_get_leaderboards_0

    Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

    :param destiny_membership_id: The Destiny membershipId of the user to retrieve.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
    :type maxtop: int
    :param modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    :type modes: str
    :param statid: ID of stat to return rather than returning all Leaderboard stats.
    :type statid: str

    """
    return web.Response(status=200)


async def destiny2_get_leaderboards_for_character_0(request: web.Request, character_id, destiny_membership_id, membership_type, maxtop=None, modes=None, statid=None) -> web.Response:
    """destiny2_get_leaderboards_for_character_0

    Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

    :param character_id: The specific character to build the leaderboard around for the provided Destiny Membership.
    :type character_id: int
    :param destiny_membership_id: The Destiny membershipId of the user to retrieve.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
    :type maxtop: int
    :param modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    :type modes: str
    :param statid: ID of stat to return rather than returning all Leaderboard stats.
    :type statid: str

    """
    return web.Response(status=200)


async def destiny2_get_public_vendors_0(request: web.Request, components=None) -> web.Response:
    """destiny2_get_public_vendors_0

    Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor&#39;s available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: &#39;It&#39;s a long story...&#39;

    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]

    """
    return web.Response(status=200)


async def destiny2_insert_socket_plug_0(request: web.Request, ) -> web.Response:
    """destiny2_insert_socket_plug_0

    Insert a plug into a socketed item. I know how it sounds, but I assure you it&#39;s much more G-rated than you might be guessing. We haven&#39;t decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for &#39;InsertPlugs&#39; from the account owner.


    """
    return web.Response(status=200)


async def destiny2_insert_socket_plug_free_0(request: web.Request, ) -> web.Response:
    """destiny2_insert_socket_plug_free_0

    Insert a &#39;free&#39; plug into an item&#39;s socket. This does not require &#39;Advanced Write Action&#39; authorization and is available to 3rd-party apps, but will only work on &#39;free and reversible&#39; socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.


    """
    return web.Response(status=200)
