# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.todo import Todo


pytestmark = pytest.mark.asyncio

async def test_delete_v3_todos(client):
    """Test case for delete_v3_todos

    Mark all todos as done
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/todos',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_todos_id(client):
    """Test case for delete_v3_todos_id

    Mark a todo as done
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/todos/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_todos(client):
    """Test case for get_v3_todos

    Get a todo list
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/todos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

