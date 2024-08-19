# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_call58acde292109180bdcacc40c(client):
    """Test case for call58acde292109180bdcacc40c

    Halo 5 - Player Game Variant
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ugc/h5/players/{player}/gamevariants/{variant}'.format(player='player_example', variant='variant_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call58acde292109180bdcacc40d(client):
    """Test case for call58acde292109180bdcacc40d

    Halo 5 - Player Game Variants
    """
    params = [('start', 3.4),
                    ('count', 3.4),
                    ('sort', 3.4),
                    ('order', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ugc/h5/players/{player}/gamevariants'.format(player='player_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call58acde292109180bdcacc40e(client):
    """Test case for call58acde292109180bdcacc40e

    Halo 5 - Player Map Variant
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ugc/h5/players/{player}/mapvariants/{variant}'.format(player='player_example', variant='variant_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call58acde292109180bdcacc40f(client):
    """Test case for call58acde292109180bdcacc40f

    Halo 5 - Player Map Variants
    """
    params = [('start', 3.4),
                    ('count', 3.4),
                    ('sort', 3.4),
                    ('order', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ugc/h5/players/{player}/mapvariants'.format(player='player_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

