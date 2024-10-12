# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.source_control_sync_job_stream_by_id import SourceControlSyncJobStreamById
from openapi_server.models.source_control_sync_job_streams_list_by_sync_job import SourceControlSyncJobStreamsListBySyncJob
from openapi_server.models.source_control_sync_job_streams_list_by_sync_job_default_response import SourceControlSyncJobStreamsListBySyncJobDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_source_control_sync_job_streams_get(client):
    """Test case for source_control_sync_job_streams_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}/sourceControlSyncJobs/{source_control_sync_job_id}/streams/{stream_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', source_control_sync_job_id='source_control_sync_job_id_example', stream_id='stream_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_source_control_sync_job_streams_list_by_sync_job(client):
    """Test case for source_control_sync_job_streams_list_by_sync_job

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}/sourceControlSyncJobs/{source_control_sync_job_id}/streams'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', source_control_sync_job_id='source_control_sync_job_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

