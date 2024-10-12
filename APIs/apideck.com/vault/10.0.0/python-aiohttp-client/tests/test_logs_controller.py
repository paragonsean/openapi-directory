# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.get_logs_response import GetLogsResponse
from openapi_server.models.logs_filter import LogsFilter
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse


pytestmark = pytest.mark.asyncio

async def test_logs_all(client):
    """Test case for logs_all

    Get all consumer request logs
    """
    params = [('filter', openapi_server.LogsFilter()),
                    ('cursor', 'cursor_example'),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/logs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

