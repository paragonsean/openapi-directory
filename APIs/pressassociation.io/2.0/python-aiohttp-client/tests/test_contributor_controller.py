# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_contributor(client):
    """Test case for get_contributor

    Contributor Detail
    """
    params = [('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/contributor/{contributor_id}'.format(contributor_id='contributor_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_contributor(client):
    """Test case for list_contributor

    Contributor Collection
    """
    params = [('updatedAfter', '2015-05-05T00:00:00.000Z'),
                    ('limit', 100),
                    ('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/contributor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

