# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_halo5_player_appearance(client):
    """Test case for halo5_player_appearance

    Halo 5 - Player Appearance
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/profile/h5/profiles/{player}/appearance'.format(player='player_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_emblem_image(client):
    """Test case for halo5_player_emblem_image

    Halo 5 - Player Emblem Image
    """
    params = [('size', 3.4)]
    headers = { 
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/profile/h5/profiles/{player}/emblem'.format(player='player_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_spartan_image(client):
    """Test case for halo5_player_spartan_image

    Halo 5 - Player Spartan Image
    """
    params = [('size', 3.4),
                    ('crop', 'crop_example')]
    headers = { 
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/profile/h5/profiles/{player}/spartan'.format(player='player_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

