# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancellation_token import CancellationToken
from openapi_server.models.total_count_response import TotalCountResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_blocks_get_blocks_async(client):
    """Test case for blocks_get_blocks_async

    Gets a list of blocks.
    """
    token = openapi_server.CancellationToken()
    params = [('hotelId', 56),
                    ('groupCode', 'group_code_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('status', 'status_example'),
                    ('ratePlanCodes', ['rate_plan_codes_example']),
                    ('countDetails', True),
                    ('skip', 56),
                    ('top', 56),
                    ('inlinecount', 'inlinecount_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/blocks',
        headers=headers,
        json=token,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_blocks_get_blocks_count_async(client):
    """Test case for blocks_get_blocks_count_async

    Get total blocks count that match the given filter criteria.
    """
    token = openapi_server.CancellationToken()
    params = [('hotelId', 56),
                    ('groupCode', 'group_code_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('status', 'status_example'),
                    ('ratePlanCodes', ['rate_plan_codes_example']),
                    ('countDetails', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/blocks/$count',
        headers=headers,
        json=token,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_blocks_get_single_block_async(client):
    """Test case for blocks_get_single_block_async

    Gets the details for a specific block.
    """
    token = openapi_server.CancellationToken()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/blocks/{block_code}'.format(block_code='block_code_example'),
        headers=headers,
        json=token,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

