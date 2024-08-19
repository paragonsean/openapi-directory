# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.post_connectors_request import PostConnectorsRequest


pytestmark = pytest.mark.asyncio

async def test_delete_connector(client):
    """Test case for delete_connector

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/connectors/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connector(client):
    """Test case for get_connector

    
    """
    params = [('include_evse', True),
                    ('include_organization', True),
                    ('include_rate', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/connectors/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connectors(client):
    """Test case for get_connectors

    
    """
    params = [('paginate_limit', 20),
                    ('paginate_page', 'paginate_page_example'),
                    ('paginate_enabled', True),
                    ('sort_by', 'createdAt'),
                    ('sort_order', desc),
                    ('createdAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('createdAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('include_evse', True),
                    ('include_organization', True),
                    ('include_rate', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/connectors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_connector(client):
    """Test case for patch_connector

    
    """
    body = openapi_server.PostConnectorsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/connectors/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_connectors(client):
    """Test case for post_connectors

    
    """
    body = openapi_server.PostConnectorsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/connectors',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

