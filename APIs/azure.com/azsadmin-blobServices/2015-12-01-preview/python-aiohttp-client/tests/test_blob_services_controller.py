# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blob_service import BlobService
from openapi_server.models.blob_services_list_metric_definitions200_response import BlobServicesListMetricDefinitions200Response
from openapi_server.models.blob_services_list_metrics200_response import BlobServicesListMetrics200Response


pytestmark = pytest.mark.asyncio

async def test_blob_services_get(client):
    """Test case for blob_services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/blobservices/{service_type}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', service_type='service_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_services_list_metric_definitions(client):
    """Test case for blob_services_list_metric_definitions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/blobservices/{service_type}/metricdefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', service_type='service_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_services_list_metrics(client):
    """Test case for blob_services_list_metrics

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/blobservices/{service_type}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', service_type='service_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

