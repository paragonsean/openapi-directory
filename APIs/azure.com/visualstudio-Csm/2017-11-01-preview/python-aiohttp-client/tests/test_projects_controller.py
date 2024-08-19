# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.project_resource import ProjectResource
from openapi_server.models.project_resource_list_result import ProjectResourceListResult
from openapi_server.models.project_resource_update_parameters import ProjectResourceUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_project_list_by_account_resource(client):
    """Test case for project_list_by_account_resource

    Projects_ListByAccountResource
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.visualstudio/account/{root_resource_name}/project'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', root_resource_name='root_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_create(client):
    """Test case for projects_create

    Projects_Create
    """
    body = {"kind":"project","properties":{"processTemplateId":"Scrum","ownerUpn":"ownerUpn","tfsUniqueIdentifier":"tfsUniqueIdentifier","bootstrapPipelineTemplate":{"authorizationDetails":{"key":{"authorizationType":"authorizationToken","parameters":{"key":"parameters"}}},"applicationTarget":{"resources":[{"role":"role","authorizationReference":"authorizationReference","id":"id"},{"role":"role","authorizationReference":"authorizationReference","id":"id"}],"targetType":"WindowsAppService"},"applicationSource":{"applicationType":"AspDotNet","sourceType":"CodeTemplate","applicationConfiguration":{"key":"applicationConfiguration"}}},"versionControlOption":"Git"}}
    params = [('api-version', 'api_version_example'),
                    ('validating', 'validating_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.visualstudio/account/{root_resource_name}/project/{resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', root_resource_name='root_resource_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get(client):
    """Test case for projects_get

    Projects_Get
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.visualstudio/account/{root_resource_name}/project/{resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', root_resource_name='root_resource_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update(client):
    """Test case for projects_update

    Projects_Update
    """
    body = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.visualstudio/account/{root_resource_name}/project/{resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', root_resource_name='root_resource_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

