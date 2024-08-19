# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.policies import Policies


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_policies_get(client):
    """Test case for api_public_v1_user_user_policies_get

    Get a list of paging policies for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/policies'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

