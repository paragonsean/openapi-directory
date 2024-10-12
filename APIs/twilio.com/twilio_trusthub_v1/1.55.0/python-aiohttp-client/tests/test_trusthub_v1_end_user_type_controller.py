# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_end_user_type_response import ListEndUserTypeResponse
from openapi_server.models.trusthub_v1_end_user_type import TrusthubV1EndUserType


pytestmark = pytest.mark.asyncio

async def test_fetch_end_user_type(client):
    """Test case for fetch_end_user_type

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/EndUserTypes/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_end_user_type(client):
    """Test case for list_end_user_type

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/EndUserTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

