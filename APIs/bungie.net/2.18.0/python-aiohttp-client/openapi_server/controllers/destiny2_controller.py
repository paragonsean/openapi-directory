from typing import List, Dict
from aiohttp import web

from openapi_server.models.destiny2_awa_get_action_token200_response import Destiny2AwaGetActionToken200Response
from openapi_server.models.destiny2_awa_initialize_request200_response import Destiny2AwaInitializeRequest200Response
from openapi_server.models.destiny2_equip_item200_response import Destiny2EquipItem200Response
from openapi_server.models.destiny2_equip_items200_response import Destiny2EquipItems200Response
from openapi_server.models.destiny2_get_activity_history200_response import Destiny2GetActivityHistory200Response
from openapi_server.models.destiny2_get_character200_response import Destiny2GetCharacter200Response
from openapi_server.models.destiny2_get_clan_aggregate_stats200_response import Destiny2GetClanAggregateStats200Response
from openapi_server.models.destiny2_get_clan_banner_source200_response import Destiny2GetClanBannerSource200Response
from openapi_server.models.destiny2_get_clan_leaderboards200_response import Destiny2GetClanLeaderboards200Response
from openapi_server.models.destiny2_get_clan_weekly_reward_state200_response import Destiny2GetClanWeeklyRewardState200Response
from openapi_server.models.destiny2_get_collectible_node_details200_response import Destiny2GetCollectibleNodeDetails200Response
from openapi_server.models.destiny2_get_destiny_aggregate_activity_stats200_response import Destiny2GetDestinyAggregateActivityStats200Response
from openapi_server.models.destiny2_get_destiny_entity_definition200_response import Destiny2GetDestinyEntityDefinition200Response
from openapi_server.models.destiny2_get_destiny_manifest200_response import Destiny2GetDestinyManifest200Response
from openapi_server.models.destiny2_get_historical_stats200_response import Destiny2GetHistoricalStats200Response
from openapi_server.models.destiny2_get_historical_stats_definition200_response import Destiny2GetHistoricalStatsDefinition200Response
from openapi_server.models.destiny2_get_historical_stats_for_account200_response import Destiny2GetHistoricalStatsForAccount200Response
from openapi_server.models.destiny2_get_item200_response import Destiny2GetItem200Response
from openapi_server.models.destiny2_get_linked_profiles200_response import Destiny2GetLinkedProfiles200Response
from openapi_server.models.destiny2_get_post_game_carnage_report200_response import Destiny2GetPostGameCarnageReport200Response
from openapi_server.models.destiny2_get_profile200_response import Destiny2GetProfile200Response
from openapi_server.models.destiny2_get_public_milestone_content200_response import Destiny2GetPublicMilestoneContent200Response
from openapi_server.models.destiny2_get_public_milestones200_response import Destiny2GetPublicMilestones200Response
from openapi_server.models.destiny2_get_public_vendors200_response import Destiny2GetPublicVendors200Response
from openapi_server.models.destiny2_get_unique_weapon_history200_response import Destiny2GetUniqueWeaponHistory200Response
from openapi_server.models.destiny2_get_vendor200_response import Destiny2GetVendor200Response
from openapi_server.models.destiny2_get_vendors200_response import Destiny2GetVendors200Response
from openapi_server.models.destiny2_insert_socket_plug200_response import Destiny2InsertSocketPlug200Response
from openapi_server.models.destiny2_search_destiny_entities200_response import Destiny2SearchDestinyEntities200Response
from openapi_server.models.destiny2_search_destiny_player_by_bungie_name200_response import Destiny2SearchDestinyPlayerByBungieName200Response
from openapi_server import util


async def destiny2_awa_get_action_token(request: web.Request, correlation_id) -> web.Response:
    """destiny2_awa_get_action_token

    Returns the action token if user approves the request.

    :param correlation_id: The identifier for the advanced write action request.
    :type correlation_id: str

    """
    return web.Response(status=200)


async def destiny2_awa_initialize_request(request: web.Request, ) -> web.Response:
    """destiny2_awa_initialize_request

    Initialize a request to perform an advanced write action.


    """
    return web.Response(status=200)


async def destiny2_awa_provide_authorization_result(request: web.Request, ) -> web.Response:
    """destiny2_awa_provide_authorization_result

    Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.


    """
    return web.Response(status=200)


async def destiny2_clear_loadout(request: web.Request, ) -> web.Response:
    """destiny2_clear_loadout

    Clear the identifiers and items of a loadout.


    """
    return web.Response(status=200)


async def destiny2_equip_item(request: web.Request, ) -> web.Response:
    """destiny2_equip_item

    Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.


    """
    return web.Response(status=200)


async def destiny2_equip_items(request: web.Request, ) -> web.Response:
    """destiny2_equip_items

    Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.


    """
    return web.Response(status=200)


async def destiny2_equip_loadout(request: web.Request, ) -> web.Response:
    """destiny2_equip_loadout

    Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.


    """
    return web.Response(status=200)


async def destiny2_get_activity_history(request: web.Request, character_id, destiny_membership_id, membership_type, count=None, mode=None, page=None) -> web.Response:
    """destiny2_get_activity_history

    Gets activity history stats for indicated character.

    :param character_id: The id of the character to retrieve.
    :type character_id: int
    :param destiny_membership_id: The Destiny membershipId of the user to retrieve.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param count: Number of rows to return
    :type count: int
    :param mode: A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
    :type mode: int
    :param page: Page number to return, starting with 0.
    :type page: int

    """
    return web.Response(status=200)


async def destiny2_get_character(request: web.Request, character_id, destiny_membership_id, membership_type, components=None) -> web.Response:
    """destiny2_get_character

    Returns character information for the supplied character.

    :param character_id: ID of the character.
    :type character_id: int
    :param destiny_membership_id: Destiny membership ID.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]

    """
    return web.Response(status=200)


async def destiny2_get_clan_aggregate_stats(request: web.Request, group_id, modes=None) -> web.Response:
    """destiny2_get_clan_aggregate_stats

    Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

    :param group_id: Group ID of the clan whose leaderboards you wish to fetch.
    :type group_id: int
    :param modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    :type modes: str

    """
    return web.Response(status=200)


async def destiny2_get_clan_banner_source(request: web.Request, ) -> web.Response:
    """destiny2_get_clan_banner_source

    Returns the dictionary of values for the Clan Banner


    """
    return web.Response(status=200)


async def destiny2_get_clan_leaderboards(request: web.Request, group_id, maxtop=None, modes=None, statid=None) -> web.Response:
    """destiny2_get_clan_leaderboards

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


async def destiny2_get_clan_weekly_reward_state(request: web.Request, group_id) -> web.Response:
    """destiny2_get_clan_weekly_reward_state

    Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

    :param group_id: A valid group id of clan.
    :type group_id: int

    """
    return web.Response(status=200)


async def destiny2_get_collectible_node_details(request: web.Request, character_id, collectible_presentation_node_hash, destiny_membership_id, membership_type, components=None) -> web.Response:
    """destiny2_get_collectible_node_details

    Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

    :param character_id: The Destiny Character ID of the character for whom we&#39;re getting collectible detail info.
    :type character_id: int
    :param collectible_presentation_node_hash: The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
    :type collectible_presentation_node_hash: int
    :param destiny_membership_id: Destiny membership ID of another user. You may be denied.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]

    """
    return web.Response(status=200)


async def destiny2_get_destiny_aggregate_activity_stats(request: web.Request, character_id, destiny_membership_id, membership_type) -> web.Response:
    """destiny2_get_destiny_aggregate_activity_stats

    Gets all activities the character has participated in together with aggregate statistics for those activities.

    :param character_id: The specific character whose activities should be returned.
    :type character_id: int
    :param destiny_membership_id: The Destiny membershipId of the user to retrieve.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int

    """
    return web.Response(status=200)


async def destiny2_get_destiny_entity_definition(request: web.Request, entity_type, hash_identifier) -> web.Response:
    """destiny2_get_destiny_entity_definition

    Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don&#39;t use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

    :param entity_type: The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
    :type entity_type: str
    :param hash_identifier: The hash identifier for the specific Entity you want returned.
    :type hash_identifier: int

    """
    return web.Response(status=200)


async def destiny2_get_destiny_manifest(request: web.Request, ) -> web.Response:
    """destiny2_get_destiny_manifest

    Returns the current version of the manifest as a json object.


    """
    return web.Response(status=200)


async def destiny2_get_historical_stats(request: web.Request, character_id, destiny_membership_id, membership_type, dayend=None, daystart=None, groups=None, modes=None, period_type=None) -> web.Response:
    """destiny2_get_historical_stats

    Gets historical stats for indicated character.

    :param character_id: The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
    :type character_id: int
    :param destiny_membership_id: The Destiny membershipId of the user to retrieve.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param dayend: Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
    :type dayend: str
    :param daystart: First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
    :type daystart: str
    :param groups: Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals
    :type groups: List[int]
    :param modes: Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    :type modes: List[int]
    :param period_type: Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity
    :type period_type: int

    """
    dayend = util.deserialize_datetime(dayend)
    daystart = util.deserialize_datetime(daystart)
    return web.Response(status=200)


async def destiny2_get_historical_stats_definition(request: web.Request, ) -> web.Response:
    """destiny2_get_historical_stats_definition

    Gets historical stats definitions.


    """
    return web.Response(status=200)


async def destiny2_get_historical_stats_for_account(request: web.Request, destiny_membership_id, membership_type, groups=None) -> web.Response:
    """destiny2_get_historical_stats_for_account

    Gets aggregate historical stats organized around each character for a given account.

    :param destiny_membership_id: The Destiny membershipId of the user to retrieve.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param groups: Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
    :type groups: List[int]

    """
    return web.Response(status=200)


async def destiny2_get_item(request: web.Request, destiny_membership_id, item_instance_id, membership_type, components=None) -> web.Response:
    """destiny2_get_item

    Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

    :param destiny_membership_id: The membership ID of the destiny profile.
    :type destiny_membership_id: int
    :param item_instance_id: The Instance ID of the destiny item.
    :type item_instance_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]

    """
    return web.Response(status=200)


async def destiny2_get_leaderboards(request: web.Request, destiny_membership_id, membership_type, maxtop=None, modes=None, statid=None) -> web.Response:
    """destiny2_get_leaderboards

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


async def destiny2_get_leaderboards_for_character(request: web.Request, character_id, destiny_membership_id, membership_type, maxtop=None, modes=None, statid=None) -> web.Response:
    """destiny2_get_leaderboards_for_character

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


async def destiny2_get_linked_profiles(request: web.Request, membership_id, membership_type, get_all_memberships=None) -> web.Response:
    """destiny2_get_linked_profiles

    Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

    :param membership_id: The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don&#39;t pass us a PSN membership ID and the XBox membership type, it&#39;s not going to work!
    :type membership_id: int
    :param membership_type: The type for the membership whose linked Destiny accounts you want returned.
    :type membership_type: int
    :param get_all_memberships: (optional) if set to &#39;true&#39;, all memberships regardless of whether they&#39;re obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.
    :type get_all_memberships: bool

    """
    return web.Response(status=200)


async def destiny2_get_post_game_carnage_report(request: web.Request, activity_id) -> web.Response:
    """destiny2_get_post_game_carnage_report

    Gets the available post game carnage report for the activity ID.

    :param activity_id: The ID of the activity whose PGCR is requested.
    :type activity_id: int

    """
    return web.Response(status=200)


async def destiny2_get_profile(request: web.Request, destiny_membership_id, membership_type, components=None) -> web.Response:
    """destiny2_get_profile

    Returns Destiny Profile information for the supplied membership.

    :param destiny_membership_id: Destiny membership ID.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]

    """
    return web.Response(status=200)


async def destiny2_get_public_milestone_content(request: web.Request, milestone_hash) -> web.Response:
    """destiny2_get_public_milestone_content

    Gets custom localized content for the milestone of the given hash, if it exists.

    :param milestone_hash: The identifier for the milestone to be returned.
    :type milestone_hash: int

    """
    return web.Response(status=200)


async def destiny2_get_public_milestones(request: web.Request, ) -> web.Response:
    """destiny2_get_public_milestones

    Gets public information about currently available Milestones.


    """
    return web.Response(status=200)


async def destiny2_get_public_vendors(request: web.Request, components=None) -> web.Response:
    """destiny2_get_public_vendors

    Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor&#39;s available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: &#39;It&#39;s a long story...&#39;

    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]

    """
    return web.Response(status=200)


async def destiny2_get_unique_weapon_history(request: web.Request, character_id, destiny_membership_id, membership_type) -> web.Response:
    """destiny2_get_unique_weapon_history

    Gets details about unique weapon usage, including all exotic weapons.

    :param character_id: The id of the character to retrieve.
    :type character_id: int
    :param destiny_membership_id: The Destiny membershipId of the user to retrieve.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int

    """
    return web.Response(status=200)


async def destiny2_get_vendor(request: web.Request, character_id, destiny_membership_id, membership_type, vendor_hash, components=None) -> web.Response:
    """destiny2_get_vendor

    Get the details of a specific Vendor.

    :param character_id: The Destiny Character ID of the character for whom we&#39;re getting vendor info.
    :type character_id: int
    :param destiny_membership_id: Destiny membership ID of another user. You may be denied.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param vendor_hash: The Hash identifier of the Vendor to be returned.
    :type vendor_hash: int
    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]

    """
    return web.Response(status=200)


async def destiny2_get_vendors(request: web.Request, character_id, destiny_membership_id, membership_type, components=None, filter=None) -> web.Response:
    """destiny2_get_vendors

    Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

    :param character_id: The Destiny Character ID of the character for whom we&#39;re getting vendor info.
    :type character_id: int
    :param destiny_membership_id: Destiny membership ID of another user. You may be denied.
    :type destiny_membership_id: int
    :param membership_type: A valid non-BungieNet membership type.
    :type membership_type: int
    :param components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    :type components: List[int]
    :param filter: The filter of what vendors and items to return, if any.
    :type filter: int

    """
    return web.Response(status=200)


async def destiny2_insert_socket_plug(request: web.Request, ) -> web.Response:
    """destiny2_insert_socket_plug

    Insert a plug into a socketed item. I know how it sounds, but I assure you it&#39;s much more G-rated than you might be guessing. We haven&#39;t decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for &#39;InsertPlugs&#39; from the account owner.


    """
    return web.Response(status=200)


async def destiny2_insert_socket_plug_free(request: web.Request, ) -> web.Response:
    """destiny2_insert_socket_plug_free

    Insert a &#39;free&#39; plug into an item&#39;s socket. This does not require &#39;Advanced Write Action&#39; authorization and is available to 3rd-party apps, but will only work on &#39;free and reversible&#39; socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.


    """
    return web.Response(status=200)


async def destiny2_pull_from_postmaster(request: web.Request, ) -> web.Response:
    """destiny2_pull_from_postmaster

    Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it&#39;s an instanced item.


    """
    return web.Response(status=200)


async def destiny2_report_offensive_post_game_carnage_report_player(request: web.Request, activity_id) -> web.Response:
    """destiny2_report_offensive_post_game_carnage_report_player

    Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

    :param activity_id: The ID of the activity where you ran into the brigand that you&#39;re reporting.
    :type activity_id: int

    """
    return web.Response(status=200)


async def destiny2_search_destiny_entities(request: web.Request, search_term, type, page=None) -> web.Response:
    """destiny2_search_destiny_entities

    Gets a page list of Destiny items.

    :param search_term: The string to use when searching for Destiny entities.
    :type search_term: str
    :param type: The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;.
    :type type: str
    :param page: Page number to return, starting with 0.
    :type page: int

    """
    return web.Response(status=200)


async def destiny2_search_destiny_player_by_bungie_name(request: web.Request, membership_type) -> web.Response:
    """destiny2_search_destiny_player_by_bungie_name

    Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

    :param membership_type: A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.
    :type membership_type: int

    """
    return web.Response(status=200)


async def destiny2_set_item_lock_state(request: web.Request, ) -> web.Response:
    """destiny2_set_item_lock_state

    Set the Lock State for an instanced item. You must have a valid Destiny Account.


    """
    return web.Response(status=200)


async def destiny2_set_quest_tracked_state(request: web.Request, ) -> web.Response:
    """destiny2_set_quest_tracked_state

    Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it&#39;s an item.


    """
    return web.Response(status=200)


async def destiny2_snapshot_loadout(request: web.Request, ) -> web.Response:
    """destiny2_snapshot_loadout

    Snapshot a loadout with the currently equipped items.


    """
    return web.Response(status=200)


async def destiny2_transfer_item(request: web.Request, ) -> web.Response:
    """destiny2_transfer_item

    Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it&#39;s an instanced item. itshappening.gif


    """
    return web.Response(status=200)


async def destiny2_update_loadout_identifiers(request: web.Request, ) -> web.Response:
    """destiny2_update_loadout_identifiers

    Update the color, icon, and name of a loadout.


    """
    return web.Response(status=200)
