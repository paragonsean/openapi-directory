# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.append_block_children200_response import AppendBlockChildren200Response
from openapi_server.models.append_block_children_request import AppendBlockChildrenRequest
from openapi_server.models.delete_a_block200_response import DeleteABlock200Response
from openapi_server.models.retrieve_a_block200_response import RetrieveABlock200Response
from openapi_server.models.retrieve_block_children200_response import RetrieveBlockChildren200Response
from openapi_server.models.update_a_block_request import UpdateABlockRequest


pytestmark = pytest.mark.asyncio

async def test_append_block_children(client):
    """Test case for append_block_children

    Append block children
    """
    body = {"children":[{"heading_2":{"text":[{"text":{"content":"Lacinato kale"},"type":"text"}]},"object":"block","type":"heading_2"},{"object":"block","paragraph":{"rich_text":[{"text":{"content":"Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.","link":{"url":"https://en.wikipedia.org/wiki/Lacinato_kale"}},"type":"text"}]},"type":"paragraph"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/blocks/{id}/children'.format(id='{{PAGE_ID}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_a_block(client):
    """Test case for delete_a_block

    Delete a block
    """
    headers = { 
        'Accept': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/blocks/{id}'.format(id='{{BLOCK_ID}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_block(client):
    """Test case for retrieve_a_block

    Retrieve a block
    """
    headers = { 
        'Accept': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/blocks/{id}'.format(id='{{BLOCK_ID}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_block_children(client):
    """Test case for retrieve_block_children

    Retrieve block children
    """
    params = [('page_size', '100')]
    headers = { 
        'Accept': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/blocks/{id}/children'.format(id='{{PAGE_ID}}'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_block(client):
    """Test case for update_a_block

    Update a block
    """
    body = {"paragraph":{"rich_text":[{"text":{"content":"hello to you"},"type":"text"}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/blocks/{id}'.format(id='{{BLOCK_ID}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

