# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_task_reservation_response import ListTaskReservationResponse
from openapi_server.models.list_worker_reservation_response import ListWorkerReservationResponse
from openapi_server.models.task_reservation_enum_call_status import TaskReservationEnumCallStatus
from openapi_server.models.task_reservation_enum_conference_event import TaskReservationEnumConferenceEvent
from openapi_server.models.task_reservation_enum_status import TaskReservationEnumStatus
from openapi_server.models.task_reservation_enum_supervisor_mode import TaskReservationEnumSupervisorMode
from openapi_server.models.taskrouter_v1_workspace_task_task_reservation import TaskrouterV1WorkspaceTaskTaskReservation
from openapi_server.models.taskrouter_v1_workspace_worker_worker_reservation import TaskrouterV1WorkspaceWorkerWorkerReservation
from openapi_server.models.worker_reservation_enum_call_status import WorkerReservationEnumCallStatus
from openapi_server.models.worker_reservation_enum_conference_event import WorkerReservationEnumConferenceEvent
from openapi_server.models.worker_reservation_enum_status import WorkerReservationEnumStatus


pytestmark = pytest.mark.asyncio

async def test_fetch_task_reservation(client):
    """Test case for fetch_task_reservation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}'.format(workspace_sid='workspace_sid_example', task_sid='task_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_worker_reservation(client):
    """Test case for fetch_worker_reservation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}'.format(workspace_sid='workspace_sid_example', worker_sid='worker_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_task_reservation(client):
    """Test case for list_task_reservation

    
    """
    params = [('ReservationStatus', openapi_server.TaskReservationEnumStatus()),
                    ('WorkerSid', 'worker_sid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations'.format(workspace_sid='workspace_sid_example', task_sid='task_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_worker_reservation(client):
    """Test case for list_worker_reservation

    
    """
    params = [('ReservationStatus', openapi_server.WorkerReservationEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations'.format(workspace_sid='workspace_sid_example', worker_sid='worker_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_task_reservation(client):
    """Test case for update_task_reservation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'beep': 'beep_example',
        'beep_on_customer_entrance': True,
        'call_accept': True,
        'call_from': 'call_from_example',
        'call_record': 'call_record_example',
        'call_status_callback_url': 'call_status_callback_url_example',
        'call_timeout': 56,
        'call_to': 'call_to_example',
        'call_url': 'call_url_example',
        'conference_record': 'conference_record_example',
        'conference_recording_status_callback': 'conference_recording_status_callback_example',
        'conference_recording_status_callback_method': 'conference_recording_status_callback_method_example',
        'conference_status_callback': 'conference_status_callback_example',
        'conference_status_callback_event': [openapi_server.TaskReservationEnumConferenceEvent()],
        'conference_status_callback_method': 'conference_status_callback_method_example',
        'conference_trim': 'conference_trim_example',
        'dequeue_from': 'dequeue_from_example',
        'dequeue_post_work_activity_sid': 'dequeue_post_work_activity_sid_example',
        'dequeue_record': 'dequeue_record_example',
        'dequeue_status_callback_event': ['dequeue_status_callback_event_example'],
        'dequeue_status_callback_url': 'dequeue_status_callback_url_example',
        'dequeue_timeout': 56,
        'dequeue_to': 'dequeue_to_example',
        'early_media': True,
        'end_conference_on_customer_exit': True,
        'end_conference_on_exit': True,
        '_from': '_from_example',
        'instruction': 'instruction_example',
        'jitter_buffer_size': 'jitter_buffer_size_example',
        'max_participants': 56,
        'muted': True,
        'post_work_activity_sid': 'post_work_activity_sid_example',
        'record': True,
        'recording_channels': 'recording_channels_example',
        'recording_status_callback': 'recording_status_callback_example',
        'recording_status_callback_method': 'recording_status_callback_method_example',
        'redirect_accept': True,
        'redirect_call_sid': 'redirect_call_sid_example',
        'redirect_url': 'redirect_url_example',
        'region': 'region_example',
        'reservation_status': openapi_server.TaskReservationEnumStatus(),
        'sip_auth_password': 'sip_auth_password_example',
        'sip_auth_username': 'sip_auth_username_example',
        'start_conference_on_enter': True,
        'status_callback': 'status_callback_example',
        'status_callback_event': [openapi_server.TaskReservationEnumCallStatus()],
        'status_callback_method': 'status_callback_method_example',
        'supervisor': 'supervisor_example',
        'supervisor_mode': openapi_server.TaskReservationEnumSupervisorMode(),
        'timeout': 56,
        'to': 'to_example',
        'wait_method': 'wait_method_example',
        'wait_url': 'wait_url_example',
        'worker_activity_sid': 'worker_activity_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}'.format(workspace_sid='workspace_sid_example', task_sid='task_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_worker_reservation(client):
    """Test case for update_worker_reservation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'beep': 'beep_example',
        'beep_on_customer_entrance': True,
        'call_accept': True,
        'call_from': 'call_from_example',
        'call_record': 'call_record_example',
        'call_status_callback_url': 'call_status_callback_url_example',
        'call_timeout': 56,
        'call_to': 'call_to_example',
        'call_url': 'call_url_example',
        'conference_record': 'conference_record_example',
        'conference_recording_status_callback': 'conference_recording_status_callback_example',
        'conference_recording_status_callback_method': 'conference_recording_status_callback_method_example',
        'conference_status_callback': 'conference_status_callback_example',
        'conference_status_callback_event': [openapi_server.WorkerReservationEnumConferenceEvent()],
        'conference_status_callback_method': 'conference_status_callback_method_example',
        'conference_trim': 'conference_trim_example',
        'dequeue_from': 'dequeue_from_example',
        'dequeue_post_work_activity_sid': 'dequeue_post_work_activity_sid_example',
        'dequeue_record': 'dequeue_record_example',
        'dequeue_status_callback_event': ['dequeue_status_callback_event_example'],
        'dequeue_status_callback_url': 'dequeue_status_callback_url_example',
        'dequeue_timeout': 56,
        'dequeue_to': 'dequeue_to_example',
        'early_media': True,
        'end_conference_on_customer_exit': True,
        'end_conference_on_exit': True,
        '_from': '_from_example',
        'instruction': 'instruction_example',
        'jitter_buffer_size': 'jitter_buffer_size_example',
        'max_participants': 56,
        'muted': True,
        'post_work_activity_sid': 'post_work_activity_sid_example',
        'record': True,
        'recording_channels': 'recording_channels_example',
        'recording_status_callback': 'recording_status_callback_example',
        'recording_status_callback_method': 'recording_status_callback_method_example',
        'redirect_accept': True,
        'redirect_call_sid': 'redirect_call_sid_example',
        'redirect_url': 'redirect_url_example',
        'region': 'region_example',
        'reservation_status': openapi_server.WorkerReservationEnumStatus(),
        'sip_auth_password': 'sip_auth_password_example',
        'sip_auth_username': 'sip_auth_username_example',
        'start_conference_on_enter': True,
        'status_callback': 'status_callback_example',
        'status_callback_event': [openapi_server.WorkerReservationEnumCallStatus()],
        'status_callback_method': 'status_callback_method_example',
        'timeout': 56,
        'to': 'to_example',
        'wait_method': 'wait_method_example',
        'wait_url': 'wait_url_example',
        'worker_activity_sid': 'worker_activity_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}'.format(workspace_sid='workspace_sid_example', worker_sid='worker_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

