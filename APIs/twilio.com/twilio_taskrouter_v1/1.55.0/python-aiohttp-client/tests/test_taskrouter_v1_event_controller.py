# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_event_response import ListEventResponse
from openapi_server.models.taskrouter_v1_workspace_event import TaskrouterV1WorkspaceEvent


pytestmark = pytest.mark.asyncio

async def test_fetch_event(client):
    """Test case for fetch_event

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Events/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_event(client):
    """Test case for list_event

    
    """
    params = [('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('EventType', 'event_type_example'),
                    ('Minutes', 56),
                    ('ReservationSid', 'reservation_sid_example'),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('TaskQueueSid', 'task_queue_sid_example'),
                    ('TaskSid', 'task_sid_example'),
                    ('WorkerSid', 'worker_sid_example'),
                    ('WorkflowSid', 'workflow_sid_example'),
                    ('TaskChannel', 'task_channel_example'),
                    ('Sid', 'sid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Events'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

