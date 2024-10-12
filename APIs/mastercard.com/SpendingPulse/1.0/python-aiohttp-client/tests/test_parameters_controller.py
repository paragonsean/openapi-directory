# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.parameter_list_response import ParameterListResponse


pytestmark = pytest.mark.asyncio

async def test_parameters_get(client):
    """Test case for parameters_get

    Returns a distinct list of all reports are available and that one is subscribed to.
    """
    params = [('CurrentRow', '1'),
                    ('Offset', '25')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/spendingpulse/v1/spulse.svc/parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

