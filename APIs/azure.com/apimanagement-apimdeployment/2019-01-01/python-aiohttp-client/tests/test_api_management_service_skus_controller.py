# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_sku_results import ResourceSkuResults


pytestmark = pytest.mark.asyncio

async def test_api_management_service_skus_list_available_service_skus(client):
    """Test case for api_management_service_skus_list_available_service_skus

    Gets available SKUs for API Management service
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/skus'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

