# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.route import Route
from openapi_server.models.routing_file import RoutingFile
from openapi_server.models.routing_file_request import RoutingFileRequest


pytestmark = pytest.mark.asyncio

async def test_get_all_routes(client):
    """Test case for get_all_routes

    Retrieve all routes of a GUID (or ID4N)
    """
    params = [('organizationId', 'organization_id_example'),
                    ('interpolate', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/routingfiles/{id4n}/routes/{type}'.format(id4n='id4n_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_route(client):
    """Test case for get_route

    Retrieve current route of a GUID (or ID4N)
    """
    params = [('privateRoutes', True),
                    ('publicRoutes', True),
                    ('interpolate', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/routingfiles/{id4n}/route/{type}'.format(id4n='id4n_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_routing_file(client):
    """Test case for get_routing_file

    Retrieve routing file
    """
    params = [('organizationId', 'organization_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/routingfiles/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_routing_file(client):
    """Test case for update_routing_file

    Store routing file
    """
    body = {"organizationId":"organizationId","routing":{"routes":[{"public":True,"validUntil":6,"params":{"key":"params"},"priority":0,"type":"type"},{"public":True,"validUntil":6,"params":{"key":"params"},"priority":0,"type":"type"}],"options":{"deleteOutdatedRoutes":True}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/routingfiles/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

