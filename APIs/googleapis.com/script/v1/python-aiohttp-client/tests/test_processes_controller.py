# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_script_processes_response import ListScriptProcessesResponse
from openapi_server.models.list_user_processes_response import ListUserProcessesResponse


pytestmark = pytest.mark.asyncio

async def test_script_processes_list(client):
    """Test case for script_processes_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('userProcessFilter.deploymentId', 'user_process_filter_deployment_id_example'),
                    ('userProcessFilter.endTime', 'user_process_filter_end_time_example'),
                    ('userProcessFilter.functionName', 'user_process_filter_function_name_example'),
                    ('userProcessFilter.projectName', 'user_process_filter_project_name_example'),
                    ('userProcessFilter.scriptId', 'user_process_filter_script_id_example'),
                    ('userProcessFilter.startTime', 'user_process_filter_start_time_example'),
                    ('userProcessFilter.statuses', ['user_process_filter_statuses_example']),
                    ('userProcessFilter.types', ['user_process_filter_types_example']),
                    ('userProcessFilter.userAccessLevels', ['user_process_filter_user_access_levels_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/processes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_script_processes_list_script_processes(client):
    """Test case for script_processes_list_script_processes

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('scriptId', 'script_id_example'),
                    ('scriptProcessFilter.deploymentId', 'script_process_filter_deployment_id_example'),
                    ('scriptProcessFilter.endTime', 'script_process_filter_end_time_example'),
                    ('scriptProcessFilter.functionName', 'script_process_filter_function_name_example'),
                    ('scriptProcessFilter.startTime', 'script_process_filter_start_time_example'),
                    ('scriptProcessFilter.statuses', ['script_process_filter_statuses_example']),
                    ('scriptProcessFilter.types', ['script_process_filter_types_example']),
                    ('scriptProcessFilter.userAccessLevels', ['script_process_filter_user_access_levels_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/processes:listScriptProcesses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

