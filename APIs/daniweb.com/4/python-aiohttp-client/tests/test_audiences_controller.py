# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_get_audiences import EndpointGetAudiences
from openapi_server.models.endpoint_get_audiences_id import EndpointGetAudiencesID
from openapi_server.models.endpoint_post_audiences_id_memberships import EndpointPostAudiencesIDMemberships


pytestmark = pytest.mark.asyncio

async def test_audiences_get(client):
    """Test case for audiences_get

    
    """
    params = [('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/audiences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_audiences_id_memberships_post(client):
    """Test case for audiences_id_memberships_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/connect/api/v4/audiences/{id}/memberships'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_audiences_idget(client):
    """Test case for audiences_idget

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/audiences/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

