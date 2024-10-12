# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.reactions_add_error_schema import ReactionsAddErrorSchema
from openapi_server.models.reactions_add_schema import ReactionsAddSchema
from openapi_server.models.reactions_get_error_schema import ReactionsGetErrorSchema
from openapi_server.models.reactions_get_success_schema_inner import ReactionsGetSuccessSchemaInner
from openapi_server.models.reactions_list_error_schema import ReactionsListErrorSchema
from openapi_server.models.reactions_list_schema import ReactionsListSchema
from openapi_server.models.reactions_remove_error_schema import ReactionsRemoveErrorSchema
from openapi_server.models.reactions_remove_schema import ReactionsRemoveSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_reactions_add(client):
    """Test case for reactions_add

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'name': 'name_example',
        'timestamp': 'timestamp_example'
        }
    response = await client.request(
        method='POST',
        path='/api/reactions.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_get(client):
    """Test case for reactions_get

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example'),
                    ('file', 'file_example'),
                    ('file_comment', 'file_comment_example'),
                    ('full', True),
                    ('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/reactions.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactions_list(client):
    """Test case for reactions_list

    
    """
    params = [('token', 'token_example'),
                    ('user', 'user_example'),
                    ('full', True),
                    ('count', 56),
                    ('page', 56),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/reactions.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_reactions_remove(client):
    """Test case for reactions_remove

    
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
        'name': 'name_example',
        'timestamp': 'timestamp_example'
        }
    response = await client.request(
        method='POST',
        path='/api/reactions.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

