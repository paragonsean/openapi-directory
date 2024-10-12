# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_products_list_by_apis200_response import ApiProductsListByApis200Response
from openapi_server.models.apis_list_by_service_default_response import ApisListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_api_products_list_by_apis(client):
    """Test case for api_products_list_by_apis

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/products'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

