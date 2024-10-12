# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_update_polygon_request import CreateUpdatePolygonRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_create_update_polygon(client):
    """Test case for create_update_polygon

    Create/update polygon
    """
    body = openapi_server.CreateUpdatePolygonRequest()
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/logistics/pvt/configuration/geoshape',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_polygon(client):
    """Test case for delete_polygon

    Delete polygon
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/logistics/pvt/configuration/geoshape/{polygon_name}'.format(polygon_name='polygon_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paged_polygons(client):
    """Test case for paged_polygons

    List paged polygons
    """
    params = [('page', '{{page}}'),
                    ('perPage', '{{perPage}}')]
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/geoshape',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_polygonby_id(client):
    """Test case for polygonby_id

    List polygon by ID
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/geoshape/{polygon_name}'.format(polygon_name='polygon_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

