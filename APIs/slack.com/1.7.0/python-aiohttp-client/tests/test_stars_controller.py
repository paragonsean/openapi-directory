# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.stars_add_error_schema import StarsAddErrorSchema
from openapi_server.models.stars_add_schema import StarsAddSchema
from openapi_server.models.stars_list_error_schema import StarsListErrorSchema
from openapi_server.models.stars_list_schema import StarsListSchema
from openapi_server.models.stars_remove_error_schema import StarsRemoveErrorSchema
from openapi_server.models.stars_remove_schema import StarsRemoveSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_stars_add(client):
    """Test case for stars_add

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'file': 'file_example',
        'file_comment': 'file_comment_example',
        'timestamp': 'timestamp_example'
        }
    response = await client.request(
        method='POST',
        path='/api/stars.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stars_list(client):
    """Test case for stars_list

    
    """
    params = [('token', 'token_example'),
                    ('count', 'count_example'),
                    ('page', 'page_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/stars.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_stars_remove(client):
    """Test case for stars_remove

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'file': 'file_example',
        'file_comment': 'file_comment_example',
        'timestamp': 'timestamp_example'
        }
    response = await client.request(
        method='POST',
        path='/api/stars.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

