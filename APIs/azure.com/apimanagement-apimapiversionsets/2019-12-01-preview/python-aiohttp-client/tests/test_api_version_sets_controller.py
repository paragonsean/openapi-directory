# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_version_set_list_by_service_default_response import ApiVersionSetListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_api_version_set_delete(client):
    """Test case for api_version_set_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apiVersionSets/{version_set_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', version_set_id='version_set_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

