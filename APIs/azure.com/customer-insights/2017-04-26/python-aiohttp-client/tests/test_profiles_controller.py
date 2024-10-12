# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.kpi_definition import KpiDefinition
from openapi_server.models.profile_list_result import ProfileListResult
from openapi_server.models.profile_resource_format import ProfileResourceFormat


pytestmark = pytest.mark.asyncio

async def test_profiles_create_or_update(client):
    """Test case for profiles_create_or_update

    
    """
    parameters = {"properties":{"strongIds":[{"strongIdName":"strongIdName","keyPropertyNames":["keyPropertyNames","keyPropertyNames"],"displayName":{"key":"displayName"},"description":{"key":"description"}},{"strongIdName":"strongIdName","keyPropertyNames":["keyPropertyNames","keyPropertyNames"],"displayName":{"key":"displayName"},"description":{"key":"description"}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/profiles/{profile_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_delete(client):
    """Test case for profiles_delete

    
    """
    params = [('locale-code', 'en-us'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/profiles/{profile_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_get(client):
    """Test case for profiles_get

    
    """
    params = [('locale-code', 'en-us'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/profiles/{profile_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_get_enriching_kpis(client):
    """Test case for profiles_get_enriching_kpis

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/profiles/{profile_name}/getEnrichingKpis'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', profile_name='profile_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_list_by_hub(client):
    """Test case for profiles_list_by_hub

    
    """
    params = [('locale-code', 'en-us'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/profiles'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

