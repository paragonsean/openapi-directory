# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_destiny2_awa_get_action_token(client):
    """Test case for destiny2_awa_get_action_token

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Awa/GetActionToken/{correlation_id}'.format(correlation_id='correlation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_awa_initialize_request(client):
    """Test case for destiny2_awa_initialize_request

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Awa/Initialize/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_awa_provide_authorization_result(client):
    """Test case for destiny2_awa_provide_authorization_result

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Awa/AwaProvideAuthorizationResult/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_clear_loadout(client):
    """Test case for destiny2_clear_loadout

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Loadouts/ClearLoadout/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_equip_item(client):
    """Test case for destiny2_equip_item

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/EquipItem/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_equip_items(client):
    """Test case for destiny2_equip_items

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/EquipItems/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_equip_loadout(client):
    """Test case for destiny2_equip_loadout

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Loadouts/EquipLoadout/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_activity_history(client):
    """Test case for destiny2_get_activity_history

    
    """
    params = [('count', 56),
                    ('mode', 56),
                    ('page', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats/Activities'.format(character_id=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_character(client):
    """Test case for destiny2_get_character

    
    """
    params = [('components', [56])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}'.format(character_id=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_clan_aggregate_stats(client):
    """Test case for destiny2_get_clan_aggregate_stats

    
    """
    params = [('modes', 'modes_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Stats/AggregateClanStats/{group_id}'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_clan_banner_source(client):
    """Test case for destiny2_get_clan_banner_source

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Clan/ClanBannerDictionary/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_clan_leaderboards(client):
    """Test case for destiny2_get_clan_leaderboards

    
    """
    params = [('maxtop', 56),
                    ('modes', 'modes_example'),
                    ('statid', 'statid_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Stats/Leaderboards/Clans/{group_id}'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_clan_weekly_reward_state(client):
    """Test case for destiny2_get_clan_weekly_reward_state

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Clan/{group_id}/WeeklyRewardState'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_collectible_node_details(client):
    """Test case for destiny2_get_collectible_node_details

    
    """
    params = [('components', [56])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}/Collectibles/{collectible_presentation_node_hash}'.format(character_id=56, collectible_presentation_node_hash=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_destiny_aggregate_activity_stats(client):
    """Test case for destiny2_get_destiny_aggregate_activity_stats

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats/AggregateActivityStats'.format(character_id=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_destiny_entity_definition(client):
    """Test case for destiny2_get_destiny_entity_definition

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Manifest/{entity_type}/{hash_identifier}'.format(entity_type='entity_type_example', hash_identifier=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_destiny_manifest(client):
    """Test case for destiny2_get_destiny_manifest

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Manifest/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_historical_stats(client):
    """Test case for destiny2_get_historical_stats

    
    """
    params = [('dayend', '2013-10-20T19:20:30+01:00'),
                    ('daystart', '2013-10-20T19:20:30+01:00'),
                    ('groups', [56]),
                    ('modes', [56]),
                    ('periodType', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats'.format(character_id=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_historical_stats_definition(client):
    """Test case for destiny2_get_historical_stats_definition

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Stats/Definition/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_historical_stats_for_account(client):
    """Test case for destiny2_get_historical_stats_for_account

    
    """
    params = [('groups', [56])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Account/{destiny_membership_id}/Stats'.format(destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_item(client):
    """Test case for destiny2_get_item

    
    """
    params = [('components', [56])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Item/{item_instance_id}'.format(destiny_membership_id=56, item_instance_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_leaderboards(client):
    """Test case for destiny2_get_leaderboards

    
    """
    params = [('maxtop', 56),
                    ('modes', 'modes_example'),
                    ('statid', 'statid_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Account/{destiny_membership_id}/Stats/Leaderboards'.format(destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_leaderboards_for_character(client):
    """Test case for destiny2_get_leaderboards_for_character

    
    """
    params = [('maxtop', 56),
                    ('modes', 'modes_example'),
                    ('statid', 'statid_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Stats/Leaderboards/{membership_type}/{destiny_membership_id}/{character_id}'.format(character_id=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_linked_profiles(client):
    """Test case for destiny2_get_linked_profiles

    
    """
    params = [('getAllMemberships', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Profile/{membership_id}/LinkedProfiles'.format(membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_post_game_carnage_report(client):
    """Test case for destiny2_get_post_game_carnage_report

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Stats/PostGameCarnageReport/{activity_id}'.format(activity_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_profile(client):
    """Test case for destiny2_get_profile

    
    """
    params = [('components', [56])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Profile/{destiny_membership_id}'.format(destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_public_milestone_content(client):
    """Test case for destiny2_get_public_milestone_content

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Milestones/{milestone_hash}/Content'.format(milestone_hash=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_public_milestones(client):
    """Test case for destiny2_get_public_milestones

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Milestones/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_public_vendors(client):
    """Test case for destiny2_get_public_vendors

    
    """
    params = [('components', [56])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Vendors/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_unique_weapon_history(client):
    """Test case for destiny2_get_unique_weapon_history

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats/UniqueWeapons'.format(character_id=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_vendor(client):
    """Test case for destiny2_get_vendor

    
    """
    params = [('components', [56])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}/Vendors/{vendor_hash}'.format(character_id=56, destiny_membership_id=56, membership_type=56, vendor_hash=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_vendors(client):
    """Test case for destiny2_get_vendors

    
    """
    params = [('components', [56]),
                    ('filter', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}/Vendors'.format(character_id=56, destiny_membership_id=56, membership_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_insert_socket_plug(client):
    """Test case for destiny2_insert_socket_plug

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/InsertSocketPlug/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_insert_socket_plug_free(client):
    """Test case for destiny2_insert_socket_plug_free

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/InsertSocketPlugFree/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_pull_from_postmaster(client):
    """Test case for destiny2_pull_from_postmaster

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/PullFromPostmaster/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_report_offensive_post_game_carnage_report_player(client):
    """Test case for destiny2_report_offensive_post_game_carnage_report_player

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Stats/PostGameCarnageReport/{activity_id}/Report'.format(activity_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_search_destiny_entities(client):
    """Test case for destiny2_search_destiny_entities

    
    """
    params = [('page', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Destiny2/Armory/Search/{type}/{search_term}'.format(search_term='search_term_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_search_destiny_player_by_bungie_name(client):
    """Test case for destiny2_search_destiny_player_by_bungie_name

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/SearchDestinyPlayerByBungieName/{membership_type}'.format(membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_set_item_lock_state(client):
    """Test case for destiny2_set_item_lock_state

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/SetLockState/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_set_quest_tracked_state(client):
    """Test case for destiny2_set_quest_tracked_state

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/SetTrackedState/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_snapshot_loadout(client):
    """Test case for destiny2_snapshot_loadout

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Loadouts/SnapshotLoadout/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_transfer_item(client):
    """Test case for destiny2_transfer_item

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Items/TransferItem/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destiny2_update_loadout_identifiers(client):
    """Test case for destiny2_update_loadout_identifiers

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

