# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.statement_response import StatementResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_get_statements(client):
    """Test case for get_statements

    Get Statements
    """
    params = [('accountId', 'account_id_example'),
                    ('container', 'container_example'),
                    ('fromDate', 'from_date_example'),
                    ('isLatest', 'is_latest_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/statements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

