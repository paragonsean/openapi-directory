# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_traces_response import ListTracesResponse
from openapi_server.models.trace import Trace
from openapi_server.models.traces import Traces


pytestmark = pytest.mark.asyncio

async def test_cloudtrace_projects_patch_traces(client):
    """Test case for cloudtrace_projects_patch_traces

    
    """
    body = {"traces":[{"traceId":"traceId","spans":[{"spanId":"spanId","kind":"SPAN_KIND_UNSPECIFIED","name":"name","startTime":"startTime","endTime":"endTime","parentSpanId":"parentSpanId","labels":{"key":"labels"}},{"spanId":"spanId","kind":"SPAN_KIND_UNSPECIFIED","name":"name","startTime":"startTime","endTime":"endTime","parentSpanId":"parentSpanId","labels":{"key":"labels"}}],"projectId":"projectId"},{"traceId":"traceId","spans":[{"spanId":"spanId","kind":"SPAN_KIND_UNSPECIFIED","name":"name","startTime":"startTime","endTime":"endTime","parentSpanId":"parentSpanId","labels":{"key":"labels"}},{"spanId":"spanId","kind":"SPAN_KIND_UNSPECIFIED","name":"name","startTime":"startTime","endTime":"endTime","parentSpanId":"parentSpanId","labels":{"key":"labels"}}],"projectId":"projectId"}]}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/projects/{project_id}/traces'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudtrace_projects_traces_get(client):
    """Test case for cloudtrace_projects_traces_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/traces/{trace_id}'.format(project_id='project_id_example', trace_id='trace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudtrace_projects_traces_list(client):
    """Test case for cloudtrace_projects_traces_list

    
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
                    ('endTime', 'end_time_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('startTime', 'start_time_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/traces'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

