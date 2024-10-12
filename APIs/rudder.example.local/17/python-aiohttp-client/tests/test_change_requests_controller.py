# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_change_request200_response import AcceptChangeRequest200Response
from openapi_server.models.accept_change_request_request import AcceptChangeRequestRequest
from openapi_server.models.change_request_details200_response import ChangeRequestDetails200Response
from openapi_server.models.decline_change_request200_response import DeclineChangeRequest200Response
from openapi_server.models.list_change_requests200_response import ListChangeRequests200Response
from openapi_server.models.list_users200_response import ListUsers200Response
from openapi_server.models.remove_validated_user200_response import RemoveValidatedUser200Response
from openapi_server.models.save_workflow_user200_response import SaveWorkflowUser200Response
from openapi_server.models.save_workflow_user_request import SaveWorkflowUserRequest
from openapi_server.models.update_change_request200_response import UpdateChangeRequest200Response
from openapi_server.models.update_change_request_request import UpdateChangeRequestRequest


pytestmark = pytest.mark.asyncio

async def test_accept_change_request(client):
    """Test case for accept_change_request

    Accept a request details
    """
    body = openapi_server.AcceptChangeRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/changeRequests/{change_request_id}/accept'.format(change_request_id=37),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_request_details(client):
    """Test case for change_request_details

    Get a change request details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/changeRequests/{change_request_id}'.format(change_request_id=37),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_decline_change_request(client):
    """Test case for decline_change_request

    Decline a request details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/changeRequests/{change_request_id}'.format(change_request_id=37),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_change_requests(client):
    """Test case for list_change_requests

    List all change requests
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/api/changeRequests',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_users(client):
    """Test case for list_users

    List user
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_validated_user(client):
    """Test case for remove_validated_user

    Remove an user from validated user list
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/validatedUsers/{username}'.format(username='JaneDoe'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_workflow_user(client):
    """Test case for save_workflow_user

    Update validated user list
    """
    body = openapi_server.SaveWorkflowUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/validatedUsers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_change_request(client):
    """Test case for update_change_request

    Update a request details
    """
    body = openapi_server.UpdateChangeRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/changeRequests/{change_request_id}'.format(change_request_id=37),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

