# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.project_expand_vo import ProjectExpandVO
from openapi_server.models.project_id_list_vo import ProjectIdListVO
from openapi_server.models.project_list_vo import ProjectListVO
from openapi_server.models.project_patch_po import ProjectPatchPO
from openapi_server.models.project_persist_vo import ProjectPersistVO
from openapi_server.models.project_vo import ProjectVO


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_attach_project(client):
    """Test case for attach_project

    Attach children projects to specific Project
    """
    body = {"childProjectIds":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/children'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    Archieve a specific Project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project(client):
    """Test case for get_project

    Get a specific Project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_list(client):
    """Test case for get_project_list

    List the projects
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_patch_project(client):
    """Test case for patch_project

    Patch a specific Project
    """
    body = {"project_status_id":1,"comments":"sample comments","is_active":False,"client_user_id":1,"custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"client_workgroup_id":1,"project_name":"sample project_name","project_category_id":1,"project_description":"sample project_description","project_number":"sample project_number","is_hot":False,"completion_date":"2000-01-23","deactivation_reason_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_project(client):
    """Test case for post_project

    Create a Project
    """
    body = {"project_status_id":1,"comments":"sample comments","is_active":False,"client_user_id":1,"custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"client_workgroup_id":1,"is_paper_direct":False,"project_name":"sample project_name","client_account":"sample client_account","project_category_id":1,"project_owner_user_id":1,"project_description":"sample project_description","project_number":"sample project_number","is_hot":False,"completion_date":"2000-01-23","deactivation_reason_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_project(client):
    """Test case for put_project

    Update a specific Project
    """
    body = {"project_status_id":1,"comments":"sample comments","is_active":False,"client_user_id":1,"custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"client_workgroup_id":1,"is_paper_direct":False,"project_name":"sample project_name","client_account":"sample client_account","project_category_id":1,"project_owner_user_id":1,"project_description":"sample project_description","project_number":"sample project_number","is_hot":False,"completion_date":"2000-01-23","deactivation_reason_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

