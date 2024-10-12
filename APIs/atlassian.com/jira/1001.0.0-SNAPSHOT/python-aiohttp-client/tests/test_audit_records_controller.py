# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit_records import AuditRecords


pytestmark = pytest.mark.asyncio

async def test_get_audit_records(client):
    """Test case for get_audit_records

    Get audit records
    """
    params = [('offset', 0),
                    ('limit', 1000),
                    ('filter', 'filter_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/auditing/record',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

