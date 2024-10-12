# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit_node_info_response import AuditNodeInfoResponse
from openapi_server.models.audit_node_response import AuditNodeResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_event_list import LogEventList
from openapi_server.models.log_operation_list import LogOperationList


pytestmark = pytest.mark.asyncio

async def test_request_audit_node_info(client):
    """Test case for request_audit_node_info

    Request nodes
    """
    params = [('parent_id', 56),
                    ('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/eventlog/audits/node_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_audit_node_user_data(client):
    """Test case for request_audit_node_user_data

    Request node assigned users with permissions
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/eventlog/audits/nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_log_events_as_json(client):
    """Test case for request_log_events_as_json

    Request system events
    """
    params = [('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('date_start', 'date_start_example'),
                    ('date_end', 'date_end_example'),
                    ('type', 56),
                    ('user_id', 56),
                    ('status', 'status_example'),
                    ('user_client', 'user_client_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/eventlog/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_log_operations(client):
    """Test case for request_log_operations

    Request allowed Log Operations
    """
    params = [('is_deprecated', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/eventlog/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

