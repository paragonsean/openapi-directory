# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_domain import CustomDomain
from openapi_server.models.custom_domain_https_parameters import CustomDomainHttpsParameters
from openapi_server.models.custom_domain_list_result import CustomDomainListResult
from openapi_server.models.custom_domain_parameters import CustomDomainParameters
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_custom_domains_create(client):
    """Test case for custom_domains_create

    
    """
    custom_domain_properties = {"properties":{"hostName":"hostName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/customDomains/{custom_domain_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', custom_domain_name='custom_domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=custom_domain_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_domains_delete(client):
    """Test case for custom_domains_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/customDomains/{custom_domain_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', custom_domain_name='custom_domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_domains_disable_custom_https(client):
    """Test case for custom_domains_disable_custom_https

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/customDomains/{custom_domain_name}/disableCustomHttps'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', custom_domain_name='custom_domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_domains_enable_custom_https(client):
    """Test case for custom_domains_enable_custom_https

    
    """
    custom_domain_https_parameters = {"minimumTlsVersion":"None","protocolType":"ServerNameIndication","certificateSource":"AzureKeyVault"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/customDomains/{custom_domain_name}/enableCustomHttps'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', custom_domain_name='custom_domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=custom_domain_https_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_domains_get(client):
    """Test case for custom_domains_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/customDomains/{custom_domain_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', custom_domain_name='custom_domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_domains_list_by_endpoint(client):
    """Test case for custom_domains_list_by_endpoint

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/customDomains'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

