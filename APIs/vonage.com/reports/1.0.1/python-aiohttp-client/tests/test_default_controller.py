# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call_logs_hal_response import CallLogsHalResponse
from openapi_server.models.validation_errors_response import ValidationErrorsResponse


pytestmark = pytest.mark.asyncio

async def test_get_call_logs(client):
    """Test case for get_call_logs

    Retrieve call logs for your account
    """
    params = [('start:gte', '2019-01-01 00:00:00'),
                    ('start:lte', '2019-01-01 00:00:00'),
                    ('end:gte', '2019-01-01 00:00:00'),
                    ('end:lte', '2019-01-01 00:00:00'),
                    ('page_size', 10),
                    ('page', 0),
                    ('to', '17325550100'),
                    ('from', '17325550100'),
                    ('source_user', 'source_user_example'),
                    ('destination_user', 'destination_user_example'),
                    ('direction', 'Inbound')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/reports/accounts/{account_id}/call-logs'.format(account_id='913874'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

