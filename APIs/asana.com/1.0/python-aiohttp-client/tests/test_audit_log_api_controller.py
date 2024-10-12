# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_audit_log_events200_response import GetAuditLogEvents200Response


pytestmark = pytest.mark.asyncio

async def test_get_audit_log_events(client):
    """Test case for get_audit_log_events

    Get audit log events
    """
    params = [('start_at', '2013-10-20T19:20:30+01:00'),
                    ('end_at', '2013-10-20T19:20:30+01:00'),
                    ('event_type', 'event_type_example'),
                    ('actor_type', 'actor_type_example'),
                    ('actor_gid', 'actor_gid_example'),
                    ('resource_gid', 'resource_gid_example'),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/workspaces/{workspace_gid}/audit_log_events'.format(workspace_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

