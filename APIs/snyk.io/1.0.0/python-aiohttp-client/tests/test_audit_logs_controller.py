# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_group_level_audit_logs_request import GetGroupLevelAuditLogsRequest
from openapi_server.models.get_organization_level_audit_logs_request import GetOrganizationLevelAuditLogsRequest


pytestmark = pytest.mark.asyncio

async def test_get_group_level_audit_logs(client):
    """Test case for get_group_level_audit_logs

    Get group level audit logs
    """
    body = openapi_server.GetGroupLevelAuditLogsRequest()
    params = [('from', '2019-07-01'),
                    ('to', '2019-07-07'),
                    ('page', 1),
                    ('sortOrder', 'ASC')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/group/{group_id}/audit'.format(group_id='4a18d42f-0706-4ad0-b127-24078731fbea'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_level_audit_logs(client):
    """Test case for get_organization_level_audit_logs

    Get organization level audit logs
    """
    body = openapi_server.GetOrganizationLevelAuditLogsRequest()
    params = [('from', '2019-07-01'),
                    ('to', '2019-07-07'),
                    ('page', 1),
                    ('sortOrder', 'ASC')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/audit'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbea'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

