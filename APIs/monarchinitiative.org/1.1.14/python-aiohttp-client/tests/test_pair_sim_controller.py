# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_pair_sim_jaccard_resource(client):
    """Test case for get_pair_sim_jaccard_resource

    Get pairwise similarity
    """
    params = [('object_category', 'object_category_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/pair/sim/jaccard/{id1}/{id2}'.format(id2='id2_example', id1='id1_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

