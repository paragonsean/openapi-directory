# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_approved_private_link_services_result import AutoApprovedPrivateLinkServicesResult
from openapi_server.models.check_private_link_service_visibility_request import CheckPrivateLinkServiceVisibilityRequest
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server.models.private_link_service import PrivateLinkService
from openapi_server.models.private_link_service_list_result import PrivateLinkServiceListResult
from openapi_server.models.private_link_service_visibility import PrivateLinkServiceVisibility
from openapi_server.models.private_link_services_list_by_subscription_default_response import PrivateLinkServicesListBySubscriptionDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_private_link_services_check_private_link_service_visibility(client):
    """Test case for private_link_services_check_private_link_service_visibility

    
    """
    parameters = {"privateLinkServiceAlias":"privateLinkServiceAlias"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_check_private_link_service_visibility_by_resource_group(client):
    """Test case for private_link_services_check_private_link_service_visibility_by_resource_group

    
    """
    parameters = {"privateLinkServiceAlias":"privateLinkServiceAlias"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility'.format(location='location_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_delete(client):
    """Test case for private_link_services_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateLinkServices/{service_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_delete_private_endpoint_connection(client):
    """Test case for private_link_services_delete_private_endpoint_connection

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateLinkServices/{service_name}/privateEndpointConnections/{pe_connection_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', pe_connection_name='pe_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_get(client):
    """Test case for private_link_services_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateLinkServices/{service_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_list(client):
    """Test case for private_link_services_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateLinkServices'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_list_auto_approved_private_link_services(client):
    """Test case for private_link_services_list_auto_approved_private_link_services

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_list_auto_approved_private_link_services_by_resource_group(client):
    """Test case for private_link_services_list_auto_approved_private_link_services_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices'.format(location='location_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_list_by_subscription(client):
    """Test case for private_link_services_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/privateLinkServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_services_update_private_endpoint_connection(client):
    """Test case for private_link_services_update_private_endpoint_connection

    
    """
    parameters = {"name":"name","etag":"etag","type":"type","properties":{"privateLinkServiceConnectionState":{"actionsRequired":"actionsRequired","description":"description","status":"status"},"privateEndpoint":{"etag":"etag","properties":"{}"},"provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateLinkServices/{service_name}/privateEndpointConnections/{pe_connection_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', pe_connection_name='pe_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

