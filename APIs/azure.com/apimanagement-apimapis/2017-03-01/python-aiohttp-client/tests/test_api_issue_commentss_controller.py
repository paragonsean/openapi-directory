# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.issue_comment_contract import IssueCommentContract


pytestmark = pytest.mark.asyncio

async def test_api_issu_comment_head(client):
    """Test case for api_issu_comment_head

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/issues/{issue_id}/comments/{comment_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', issue_id='issue_id_example', comment_id='comment_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_issue_comment_create_or_update(client):
    """Test case for api_issue_comment_create_or_update

    
    """
    parameters = {"properties":{"createdDate":"2000-01-23T04:56:07.000+00:00","text":"text","userId":"userId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/issues/{issue_id}/comments/{comment_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', issue_id='issue_id_example', comment_id='comment_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

