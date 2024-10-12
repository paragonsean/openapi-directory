# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.node import Node
from openapi_server.models.view_only_links import ViewOnlyLinks


pytestmark = pytest.mark.asyncio

async def test_view_only_links_node_list(client):
    """Test case for view_only_links_node_list

    List all nodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/view_only_links/{link_id}/nodes'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_view_only_links_read(client):
    """Test case for view_only_links_read

    Retrieve a view only link
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/view_only_links/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

