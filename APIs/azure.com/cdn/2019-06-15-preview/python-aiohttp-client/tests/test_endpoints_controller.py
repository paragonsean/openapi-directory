# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint import Endpoint
from openapi_server.models.endpoint_list_result import EndpointListResult
from openapi_server.models.endpoint_update_parameters import EndpointUpdateParameters
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.load_parameters import LoadParameters
from openapi_server.models.purge_parameters import PurgeParameters
from openapi_server.models.resource_usage_list_result import ResourceUsageListResult
from openapi_server.models.validate_custom_domain_input import ValidateCustomDomainInput
from openapi_server.models.validate_custom_domain_output import ValidateCustomDomainOutput


pytestmark = pytest.mark.asyncio

async def test_endpoints_create(client):
    """Test case for endpoints_create

    
    """
    endpoint = {"properties":{"hostName":"hostName","origins":[{"name":"name","properties":{"hostName":"hostName","httpPort":5249,"httpsPort":39501}},{"name":"name","properties":{"hostName":"hostName","httpPort":5249,"httpsPort":39501}}],"resourceState":"Creating","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=endpoint,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_delete(client):
    """Test case for endpoints_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_get(client):
    """Test case for endpoints_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_list_by_profile(client):
    """Test case for endpoints_list_by_profile

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_list_resource_usage(client):
    """Test case for endpoints_list_resource_usage

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/checkResourceUsage'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_load_content(client):
    """Test case for endpoints_load_content

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/load'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=content_file_paths,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/purge'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=content_file_paths,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_start(client):
    """Test case for endpoints_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/start'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_stop(client):
    """Test case for endpoints_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/stop'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_update(client):
    """Test case for endpoints_update

    
    """
    endpoint_update_properties = {"properties":{"contentTypesToCompress":["contentTypesToCompress","contentTypesToCompress"],"deliveryPolicy":{"description":"description","rules":[{"name":"name","conditions":[{"name":"RemoteAddress"},{"name":"RemoteAddress"}],"actions":[{"name":"CacheExpiration"},{"name":"CacheExpiration"}],"order":0},{"name":"name","conditions":[{"name":"RemoteAddress"},{"name":"RemoteAddress"}],"actions":[{"name":"CacheExpiration"},{"name":"CacheExpiration"}],"order":0}]},"originPath":"originPath","originHostHeader":"originHostHeader","isHttpAllowed":True,"isHttpsAllowed":True,"optimizationType":"GeneralWebDelivery","isCompressionEnabled":True,"queryStringCachingBehavior":"IgnoreQueryString","geoFilters":[{"countryCodes":["countryCodes","countryCodes"],"relativePath":"relativePath","action":"Block"},{"countryCodes":["countryCodes","countryCodes"],"relativePath":"relativePath","action":"Block"}],"probePath":"probePath","webApplicationFirewallPolicyLink":{"id":"id"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=endpoint_update_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_validate_custom_domain(client):
    """Test case for endpoints_validate_custom_domain

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/validateCustomDomain'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=custom_domain_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

