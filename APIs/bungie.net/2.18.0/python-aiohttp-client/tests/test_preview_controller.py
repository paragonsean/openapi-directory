# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.destiny2_get_clan_aggregate_stats200_response import Destiny2GetClanAggregateStats200Response
from openapi_server.models.destiny2_get_clan_leaderboards200_response import Destiny2GetClanLeaderboards200Response
from openapi_server.models.destiny2_get_public_vendors200_response import Destiny2GetPublicVendors200Response
from openapi_server.models.destiny2_insert_socket_plug200_response import Destiny2InsertSocketPlug200Response


pytestmark = pytest.mark.asyncio

async def test_destiny2_get_clan_aggregate_stats_0(client):
    """Test case for destiny2_get_clan_aggregate_stats_0

    
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

async def test_destiny2_get_clan_leaderboards_0(client):
    """Test case for destiny2_get_clan_leaderboards_0

    
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

async def test_destiny2_get_leaderboards_0(client):
    """Test case for destiny2_get_leaderboards_0

    
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

async def test_destiny2_get_leaderboards_for_character_0(client):
    """Test case for destiny2_get_leaderboards_for_character_0

    
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

async def test_destiny2_get_public_vendors_0(client):
    """Test case for destiny2_get_public_vendors_0

    
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

async def test_destiny2_insert_socket_plug_0(client):
    """Test case for destiny2_insert_socket_plug_0

    
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

async def test_destiny2_insert_socket_plug_free_0(client):
    """Test case for destiny2_insert_socket_plug_free_0

    
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

