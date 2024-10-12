# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.share import Share
from openapi_server.models.shares_list_metric_definitions200_response import SharesListMetricDefinitions200Response
from openapi_server.models.shares_list_metrics200_response import SharesListMetrics200Response


pytestmark = pytest.mark.asyncio

async def test_shares_get(client):
    """Test case for shares_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/{share_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_list(client):
    """Test case for shares_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_list_metric_definitions(client):
    """Test case for shares_list_metric_definitions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/{share_name}/metricdefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_list_metrics(client):
    """Test case for shares_list_metrics

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/{share_name}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

