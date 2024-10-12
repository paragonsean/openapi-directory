# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.slug_request_body import SlugRequestBody
from openapi_server.models.workspace_create import WorkspaceCreate
from openapi_server.models.workspace_give_feedback import WorkspaceGiveFeedback
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_server.models.workspace_read import WorkspaceRead
from openapi_server.models.workspace_read_list import WorkspaceReadList
from openapi_server.models.workspace_update import WorkspaceUpdate
from openapi_server.models.workspace_update_name import WorkspaceUpdateName


pytestmark = pytest.mark.asyncio

async def test_create_workspace(client):
    """Test case for create_workspace

    Creates a workspace
    """
    body = {"displaySetupWizard":True,"news":True,"defaultGeography":"auto","webhookConfigs":[{"authToken":"authToken","name":"name","validationUrl":"validationUrl"},{"authToken":"authToken","name":"name","validationUrl":"validationUrl"}],"anonymousDataCollection":True,"name":"name","email":"email","notifications":[{"slackConfiguration":{"webhook":"webhook"},"customerioConfiguration":"{}","sendOnFailure":True,"sendOnSuccess":False,"notificationType":"slack"},{"slackConfiguration":{"webhook":"webhook"},"customerioConfiguration":"{}","sendOnFailure":True,"sendOnSuccess":False,"notificationType":"slack"}],"securityUpdates":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workspace(client):
    """Test case for delete_workspace

    Deletes a workspace
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspace(client):
    """Test case for get_workspace

    Find workspace by ID
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspace_by_connection_id(client):
    """Test case for get_workspace_by_connection_id

    Find workspace by connection id
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/get_by_connection_id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspace_by_slug(client):
    """Test case for get_workspace_by_slug

    Find workspace by slug
    """
    body = {"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/get_by_slug',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_workspaces(client):
    """Test case for list_workspaces

    List all workspaces registered in the current Airbyte deployment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workspace(client):
    """Test case for update_workspace

    Update workspace state
    """
    body = {"displaySetupWizard":True,"news":True,"initialSetupComplete":True,"defaultGeography":"auto","webhookConfigs":[{"authToken":"authToken","name":"name","validationUrl":"validationUrl"},{"authToken":"authToken","name":"name","validationUrl":"validationUrl"}],"anonymousDataCollection":True,"email":"email","notifications":[{"slackConfiguration":{"webhook":"webhook"},"customerioConfiguration":"{}","sendOnFailure":True,"sendOnSuccess":False,"notificationType":"slack"},{"slackConfiguration":{"webhook":"webhook"},"customerioConfiguration":"{}","sendOnFailure":True,"sendOnSuccess":False,"notificationType":"slack"}],"securityUpdates":True,"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workspace_feedback(client):
    """Test case for update_workspace_feedback

    Update workspace feedback state
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/tag_feedback_status_as_done',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workspace_name(client):
    """Test case for update_workspace_name

    Update workspace name
    """
    body = {"name":"name","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/workspaces/update_name',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

