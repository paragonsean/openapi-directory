# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.kpi_list_result import KpiListResult
from openapi_server.models.kpi_resource_format import KpiResourceFormat


pytestmark = pytest.mark.asyncio

async def test_kpi_create_or_update(client):
    """Test case for kpi_create_or_update

    
    """
    parameters = {"properties":{"aliases":[{"aliasName":"aliasName","expression":"expression"},{"aliasName":"aliasName","expression":"expression"}],"expression":"expression","displayName":{"key":"displayName"},"entityType":"None","calculationWindowFieldName":"calculationWindowFieldName","description":{"key":"description"},"entityTypeName":"entityTypeName","kpiName":"kpiName","groupBy":["groupBy","groupBy"],"provisioningState":"Provisioning","groupByMetadata":[{"fieldName":"fieldName","displayName":{"key":"displayName"},"fieldType":"fieldType"},{"fieldName":"fieldName","displayName":{"key":"displayName"},"fieldType":"fieldType"}],"filter":"filter","unit":"unit","participantProfilesMetadata":[{"typeName":"typeName"},{"typeName":"typeName"}],"function":"Sum","tenantId":"tenantId","calculationWindow":"Lifetime","extracts":[{"expression":"expression","extractName":"extractName"},{"expression":"expression","extractName":"extractName"}],"thresHolds":{"increasingKpi":True,"upperLimit":6.027456183070403,"lowerLimit":0.8008281904610115}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/kpi/{kpi_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', kpi_name='kpi_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kpi_delete(client):
    """Test case for kpi_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/kpi/{kpi_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', kpi_name='kpi_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kpi_get(client):
    """Test case for kpi_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/kpi/{kpi_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', kpi_name='kpi_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kpi_list_by_hub(client):
    """Test case for kpi_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/kpi'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kpi_reprocess(client):
    """Test case for kpi_reprocess

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/kpi/{kpi_name}/reprocess'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', kpi_name='kpi_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

