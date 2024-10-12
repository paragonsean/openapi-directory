# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.report_config import ReportConfig
from openapi_server.models.report_config_list_result import ReportConfigListResult


pytestmark = pytest.mark.asyncio

async def test_report_config_create_or_update(client):
    """Test case for report_config_create_or_update

    
    """
    parameters = {"properties":{"schedule":{"recurrence":"Daily","recurrencePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"status":"Active"},"deliveryInfo":{"destination":{"container":"container","resourceId":"resourceId","rootFolderPath":"rootFolderPath"}},"format":"Csv","definition":{"timeframe":"WeekToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"columnType":"Tag","name":"name"},{"columnType":"Tag","name":"name"}]}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/reportconfigs/{report_config_name}'.format(subscription_id='subscription_id_example', report_config_name='report_config_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_config_create_or_update_by_resource_group_name(client):
    """Test case for report_config_create_or_update_by_resource_group_name

    
    """
    parameters = {"properties":{"schedule":{"recurrence":"Daily","recurrencePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"status":"Active"},"deliveryInfo":{"destination":{"container":"container","resourceId":"resourceId","rootFolderPath":"rootFolderPath"}},"format":"Csv","definition":{"timeframe":"WeekToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"columnType":"Tag","name":"name"},{"columnType":"Tag","name":"name"}]}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/reportconfigs/{report_config_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', report_config_name='report_config_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_config_delete(client):
    """Test case for report_config_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/reportconfigs/{report_config_name}'.format(subscription_id='subscription_id_example', report_config_name='report_config_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_config_delete_by_resource_group_name(client):
    """Test case for report_config_delete_by_resource_group_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/reportconfigs/{report_config_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', report_config_name='report_config_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_config_get(client):
    """Test case for report_config_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/reportconfigs/{report_config_name}'.format(subscription_id='subscription_id_example', report_config_name='report_config_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_config_get_by_resource_group_name(client):
    """Test case for report_config_get_by_resource_group_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/reportconfigs/{report_config_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', report_config_name='report_config_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_config_list(client):
    """Test case for report_config_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/reportconfigs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_config_list_by_resource_group_name(client):
    """Test case for report_config_list_by_resource_group_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/reportconfigs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

