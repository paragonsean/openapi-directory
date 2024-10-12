# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_list_by_service200_response import IssueListByService200Response
from openapi_server.models.issue_list_by_service_default_response import IssueListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_issue_list_by_service(client):
    """Test case for issue_list_by_service

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/issues'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

