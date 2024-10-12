# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count_result import CountResult
from openapi_server.models.error_result import ErrorResult


pytestmark = pytest.mark.asyncio

async def test_transit(client):
    """Test case for transit

    Transit between basic residential units
    """
    params = [('fromType', 'from_type_example'),
                    ('toType', 'to_type_example'),
                    ('uniques', '0')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/mobility/sandbox/api/transit/{_from}/{to}'.format(_from='127752', to='127761'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

