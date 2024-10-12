# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.issue_attachment_collection import IssueAttachmentCollection
from openapi_server.models.issue_attachment_contract import IssueAttachmentContract


pytestmark = pytest.mark.asyncio

async def test_api_issue_attachment_delete(client):
    """Test case for api_issue_attachment_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/issues/{issue_id}/attachments/{attachment_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', issue_id='issue_id_example', attachment_id='attachment_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_issue_attachment_get(client):
    """Test case for api_issue_attachment_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/issues/{issue_id}/attachments/{attachment_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', issue_id='issue_id_example', attachment_id='attachment_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_issue_attachments_list_by_service(client):
    """Test case for api_issue_attachments_list_by_service

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/issues/{issue_id}/attachments'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', issue_id='issue_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

