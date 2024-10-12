# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_https_configuration import CustomHttpsConfiguration
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.front_door import FrontDoor
from openapi_server.models.front_door_list_result import FrontDoorListResult
from openapi_server.models.frontend_endpoint import FrontendEndpoint
from openapi_server.models.frontend_endpoints_list_result import FrontendEndpointsListResult
from openapi_server.models.purge_parameters import PurgeParameters
from openapi_server.models.validate_custom_domain_input import ValidateCustomDomainInput
from openapi_server.models.validate_custom_domain_output import ValidateCustomDomainOutput


pytestmark = pytest.mark.asyncio

async def test_endpoints_purge_content(client):
    """Test case for endpoints_purge_content

    
    """
    content_file_paths = {"contentPaths":["contentPaths","contentPaths"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}/purge'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example'),
        headers=headers,
        json=content_file_paths,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_front_doors_create_or_update(client):
    """Test case for front_doors_create_or_update

    
    """
    front_door_parameters = {"properties":{"cname":"cname","resourceState":"Creating","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example'),
        headers=headers,
        json=front_door_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_front_doors_delete(client):
    """Test case for front_doors_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_front_doors_get(client):
    """Test case for front_doors_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_front_doors_list(client):
    """Test case for front_doors_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/frontDoors'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_front_doors_list_by_resource_group(client):
    """Test case for front_doors_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_front_doors_validate_custom_domain(client):
    """Test case for front_doors_validate_custom_domain

    
    """
    custom_domain_properties = {"hostName":"hostName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}/validateCustomDomain'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example'),
        headers=headers,
        json=custom_domain_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_frontend_endpoints_disable_https(client):
    """Test case for frontend_endpoints_disable_https

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}/frontendEndpoints/{frontend_endpoint_name}/disableHttps'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example', frontend_endpoint_name='frontend_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_frontend_endpoints_enable_https(client):
    """Test case for frontend_endpoints_enable_https

    
    """
    custom_https_configuration = {"frontDoorCertificateSourceParameters":{"certificateType":"Dedicated"},"keyVaultCertificateSourceParameters":{"secretName":"secretName","secretVersion":"secretVersion","vault":{"id":"id"}},"protocolType":"ServerNameIndication","certificateSource":"AzureKeyVault"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}/frontendEndpoints/{frontend_endpoint_name}/enableHttps'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example', frontend_endpoint_name='frontend_endpoint_name_example'),
        headers=headers,
        json=custom_https_configuration,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_frontend_endpoints_get(client):
    """Test case for frontend_endpoints_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}/frontendEndpoints/{frontend_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example', frontend_endpoint_name='frontend_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_frontend_endpoints_list_by_front_door(client):
    """Test case for frontend_endpoints_list_by_front_door

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/frontDoors/{front_door_name}/frontendEndpoints'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', front_door_name='front_door_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

