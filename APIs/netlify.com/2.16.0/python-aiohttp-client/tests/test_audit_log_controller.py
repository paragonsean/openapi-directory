# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit_log import AuditLog
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_list_account_audit_events(client):
    """Test case for list_account_audit_events

    
    """
    params = [('query', 'query_example'),
                    ('log_type', 'log_type_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{account_id}/audit'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

