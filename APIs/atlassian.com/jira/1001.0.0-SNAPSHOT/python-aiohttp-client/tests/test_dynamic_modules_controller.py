# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connect_modules import ConnectModules
from openapi_server.models.error_message import ErrorMessage


pytestmark = pytest.mark.asyncio

async def test_dynamic_modules_resource_get_modules_get(client):
    """Test case for dynamic_modules_resource_get_modules_get

    Get modules
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/atlassian-connect/1/app/module/dynamic',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dynamic_modules_resource_register_modules_post(client):
    """Test case for dynamic_modules_resource_register_modules_post

    Register modules
    """
    body = {"jiraEntityProperties":[{"entityType":"issue","key":"dynamic-attachment-entity-property","keyConfigurations":[{"extractions":[{"alias":"attachmentExtension","objectName":"extension","type":"text"}],"propertyKey":"attachment"}],"name":{"value":"Attachment Index Document"}}],"jiraIssueFields":[{"description":{"value":"A dynamically added single-select field"},"extractions":[{"name":"categoryName","path":"category","type":"text"}],"key":"dynamic-select-field","name":{"value":"Dynamic single select"},"type":"single_select"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/atlassian-connect/1/app/module/dynamic',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dynamic_modules_resource_remove_modules_delete(client):
    """Test case for dynamic_modules_resource_remove_modules_delete

    Remove modules
    """
    params = [('moduleKey', ['module_key_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/atlassian-connect/1/app/module/dynamic',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

