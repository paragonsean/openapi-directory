# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diagnostic_logs_response import DiagnosticLogsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_diagnostic_signatures_logs_get_to_many_related(client):
    """Test case for diagnostic_signatures_logs_get_to_many_related

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/diagnosticSignatures/{id}/logs'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

