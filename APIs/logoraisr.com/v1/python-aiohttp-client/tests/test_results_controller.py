# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.result_response import ResultResponse


pytestmark = pytest.mark.asyncio

async def test_results_read(client):
    """Test case for results_read

    Get the result from image processing
    """
    headers = { 
        'Accept': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-v1/results/{result_file_id}'.format(result_file_id='result_file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

