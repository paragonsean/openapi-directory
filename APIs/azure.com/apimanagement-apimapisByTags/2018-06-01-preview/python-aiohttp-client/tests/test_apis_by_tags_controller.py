# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_list_by_tags200_response import ApiListByTags200Response
from openapi_server.models.api_list_by_tags_default_response import ApiListByTagsDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_api_list_by_tags(client):
    """Test case for api_list_by_tags

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('includeNotTaggedApis', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apisByTags'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

