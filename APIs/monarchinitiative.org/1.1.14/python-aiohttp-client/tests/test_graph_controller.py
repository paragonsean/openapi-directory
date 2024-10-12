# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bio_object import BioObject
from openapi_server.models.graph import Graph


pytestmark = pytest.mark.asyncio

async def test_get_edge_resource(client):
    """Test case for get_edge_resource

    Returns edges emanating from a given node
    """
    params = [('depth', 1),
                    ('direction', BOTH),
                    ('relationship_type', ['relationship_type_example']),
                    ('entail', False),
                    ('graph', data)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/graph/edges/from/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_resource(client):
    """Test case for get_node_resource

    Returns a graph node
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/graph/node/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

