# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_profile import ClientProfile
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.pam_message import PamMessage
from openapi_server.models.project_completion_report import ProjectCompletionReport


pytestmark = pytest.mark.asyncio

async def test_get_client_profile_for_pam(client):
    """Test case for get_client_profile_for_pam

    Get the Pam profile of a client for this client ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pam/profiles/client/{client_id}'.format(client_id=3707),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_completion_report_for_pam(client):
    """Test case for get_project_completion_report_for_pam

    Get completion report data of a project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pam/projects/{project_id}/completion-report'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_message(client):
    """Test case for post_message

    Sends a message to chat
    """
    body = {"slots":["slots","slots"],"thread_id":"thread_id","recipients":["recipients","recipients"],"thread_key":"thread_key","message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/pam/chat',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

