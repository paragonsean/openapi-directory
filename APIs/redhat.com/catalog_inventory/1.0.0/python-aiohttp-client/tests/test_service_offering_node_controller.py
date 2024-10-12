# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.service_offering_node import ServiceOfferingNode
from openapi_server.models.service_offering_nodes_collection import ServiceOfferingNodesCollection


pytestmark = pytest.mark.asyncio

async def test_list_service_offering_nodes(client):
    """Test case for list_service_offering_nodes

    List ServiceOfferingNodes
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_offering_nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_service_offering_node(client):
    """Test case for show_service_offering_node

    Show an existing ServiceOfferingNode
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_offering_nodes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

