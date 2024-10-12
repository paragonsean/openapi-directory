# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_gateway import ApplicationGateway
from openapi_server.models.application_gateway_list_result import ApplicationGatewayListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_application_gateways_create_or_update(client):
    """Test case for application_gateways_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"gatewayIPConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"provisioningState":"provisioningState"}}],"sslCertificates":[{"name":"name","etag":"etag","properties":{"password":"password","data":"data","provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"password":"password","data":"data","provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"resourceGuid":"resourceGuid","backendHttpSettingsCollection":[{"name":"name","etag":"etag","properties":{"protocol":"Http","port":0,"cookieBasedAffinity":"Enabled","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"protocol":"Http","port":0,"cookieBasedAffinity":"Enabled","provisioningState":"provisioningState"}}],"frontendIPConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}}],"operationalState":"Stopped","provisioningState":"provisioningState","backendAddressPools":[{"name":"name","etag":"etag","properties":{"backendIPConfigurations":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState","backendAddresses":[{"fqdn":"fqdn","ipAddress":"ipAddress"},{"fqdn":"fqdn","ipAddress":"ipAddress"}]}},{"name":"name","etag":"etag","properties":{"backendIPConfigurations":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState","backendAddresses":[{"fqdn":"fqdn","ipAddress":"ipAddress"},{"fqdn":"fqdn","ipAddress":"ipAddress"}]}}],"sku":{"tier":"Standard","name":"Standard_Small","capacity":1},"httpListeners":[{"name":"name","etag":"etag","properties":{"protocol":"Http","sslCertificate":{"id":"id"},"frontendIPConfiguration":{"id":"id"},"frontendPort":{"id":"id"},"provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"protocol":"Http","sslCertificate":{"id":"id"},"frontendIPConfiguration":{"id":"id"},"frontendPort":{"id":"id"},"provisioningState":"provisioningState"}}],"frontendPorts":[{"name":"name","etag":"etag","properties":{"port":6,"provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"port":6,"provisioningState":"provisioningState"}}],"requestRoutingRules":[{"name":"name","etag":"etag","properties":{"httpListener":{"id":"id"},"ruleType":"Basic","backendAddressPool":{"id":"id"},"provisioningState":"provisioningState","backendHttpSettings":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"httpListener":{"id":"id"},"ruleType":"Basic","backendAddressPool":{"id":"id"},"provisioningState":"provisioningState","backendHttpSettings":{"id":"id"}}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_delete(client):
    """Test case for application_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_get(client):
    """Test case for application_gateways_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_list(client):
    """Test case for application_gateways_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_list_all(client):
    """Test case for application_gateways_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/applicationGateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_start(client):
    """Test case for application_gateways_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}/start'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_stop(client):
    """Test case for application_gateways_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}/stop'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

