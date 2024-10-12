# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.widget_type_list_result import WidgetTypeListResult
from openapi_server.models.widget_type_resource_format import WidgetTypeResourceFormat


pytestmark = pytest.mark.asyncio

async def test_widget_types_get(client):
    """Test case for widget_types_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/widgetTypes/{widget_type_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', widget_type_name='widget_type_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_widget_types_list_by_hub(client):
    """Test case for widget_types_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/widgetTypes'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

