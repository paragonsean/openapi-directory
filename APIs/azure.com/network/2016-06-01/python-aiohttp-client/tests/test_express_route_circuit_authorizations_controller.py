# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorization_list_result import AuthorizationListResult
from openapi_server.models.express_route_circuit_authorization import ExpressRouteCircuitAuthorization


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_express_route_circuit_authorizations_create_or_update(client):
    """Test case for express_route_circuit_authorizations_create_or_update

    
    """
    authorization_parameters = {"name":"name","etag":"etag","properties":{"authorizationUseStatus":"Available","authorizationKey":"authorizationKey","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/authorizations/{authorization_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', authorization_name='authorization_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=authorization_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_authorizations_delete(client):
    """Test case for express_route_circuit_authorizations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/authorizations/{authorization_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', authorization_name='authorization_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_authorizations_get(client):
    """Test case for express_route_circuit_authorizations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/authorizations/{authorization_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', authorization_name='authorization_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_authorizations_list(client):
    """Test case for express_route_circuit_authorizations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/authorizations'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

