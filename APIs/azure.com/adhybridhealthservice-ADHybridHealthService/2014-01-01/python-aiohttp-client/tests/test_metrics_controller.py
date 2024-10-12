# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connector_metadata import ConnectorMetadata
from openapi_server.models.metric_metadata import MetricMetadata
from openapi_server.models.metric_metadata_list import MetricMetadataList
from openapi_server.models.metric_sets import MetricSets
from openapi_server.models.metrics import Metrics


pytestmark = pytest.mark.asyncio

async def test_service_get_metrics(client):
    """Test case for service_get_metrics

    
    """
    params = [('groupKey', 'group_key_example'),
                    ('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/metrics/{metric_name}/groups/{group_name}'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_get_connector_metadata(client):
    """Test case for service_members_get_connector_metadata

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/metrics/{metric_name}'.format(service_name='service_name_example', service_member_id='service_member_id_example', metric_name='metric_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_get_metrics(client):
    """Test case for service_members_get_metrics

    
    """
    params = [('groupKey', 'group_key_example'),
                    ('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/metrics/{metric_name}/groups/{group_name}'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get_metric_metadata(client):
    """Test case for services_get_metric_metadata

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/metricmetadata/{metric_name}'.format(service_name='service_name_example', metric_name='metric_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get_metric_metadata_for_group(client):
    """Test case for services_get_metric_metadata_for_group

    
    """
    params = [('groupKey', 'group_key_example'),
                    ('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/metricmetadata/{metric_name}/groups/{group_name}'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_metric_metadata(client):
    """Test case for services_list_metric_metadata

    
    """
    params = [('$filter', 'filter_example'),
                    ('perfCounter', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/metricmetadata'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_metrics_average(client):
    """Test case for services_list_metrics_average

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/metrics/{metric_name}/groups/{group_name}/average'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_metrics_sum(client):
    """Test case for services_list_metrics_sum

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/metrics/{metric_name}/groups/{group_name}/sum'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

