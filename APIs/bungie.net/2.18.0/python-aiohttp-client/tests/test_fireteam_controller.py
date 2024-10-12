# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.destiny2_equip_item200_response import Destiny2EquipItem200Response
from openapi_server.models.fireteam_get_available_clan_fireteams200_response import FireteamGetAvailableClanFireteams200Response
from openapi_server.models.fireteam_get_clan_fireteam200_response import FireteamGetClanFireteam200Response
from openapi_server.models.fireteam_get_my_clan_fireteams200_response import FireteamGetMyClanFireteams200Response


pytestmark = pytest.mark.asyncio

async def test_fireteam_get_active_private_clan_fireteam_count(client):
    """Test case for fireteam_get_active_private_clan_fireteam_count

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Fireteam/Clan/{group_id}/ActiveCount'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fireteam_get_available_clan_fireteams(client):
    """Test case for fireteam_get_available_clan_fireteams

    
    """
    params = [('excludeImmediate', True),
                    ('langFilter', 'lang_filter_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Fireteam/Clan/{group_id}/Available/{platform}/{activity_type}/{date_range}/{slot_filter}/{public_only}/{page}'.format(activity_type=56, date_range=56, group_id=56, page=56, platform=56, public_only=56, slot_filter=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fireteam_get_clan_fireteam(client):
    """Test case for fireteam_get_clan_fireteam

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Fireteam/Clan/{group_id}/Summary/{fireteam_id}'.format(fireteam_id=56, group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fireteam_get_my_clan_fireteams(client):
    """Test case for fireteam_get_my_clan_fireteams

    
    """
    params = [('groupFilter', True),
                    ('langFilter', 'lang_filter_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Fireteam/Clan/{group_id}/My/{platform}/{include_closed}/{page}'.format(group_id=56, include_closed=True, page=56, platform=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fireteam_search_public_available_clan_fireteams(client):
    """Test case for fireteam_search_public_available_clan_fireteams

    
    """
    params = [('excludeImmediate', True),
                    ('langFilter', 'lang_filter_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Fireteam/Search/Available/{platform}/{activity_type}/{date_range}/{slot_filter}/{page}'.format(activity_type=56, date_range=56, page=56, platform=56, slot_filter=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

