# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.charges_list_result import ChargesListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_charges_list(client):
    """Test case for charges_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$filter', 'filter_example'),
                    ('$apply', 'apply_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Consumption/charges'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

