# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_audit_actions_response import GetAuditActionsResponse
from openapi_server.models.get_audit_logs_response import GetAuditLogsResponse
from openapi_server.models.rpc_status import RpcStatus


pytestmark = pytest.mark.asyncio

async def test_audit_logs_get_audit_actions(client):
    """Test case for audit_logs_get_audit_actions

    Returns list of audit log actions.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/auditlogs/{account}/actions'.format(account='account_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_audit_logs_get_audit_logs(client):
    """Test case for audit_logs_get_audit_logs

    Returns list of audit log  events.
    """
    params = [('action', 'action_example'),
                    ('name', 'name_example'),
                    ('actor', 'actor_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('page', 1),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/auditlogs/{account}'.format(account='account_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

