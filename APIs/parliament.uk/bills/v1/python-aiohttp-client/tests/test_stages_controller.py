# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.stage_reference_search_result import StageReferenceSearchResult


pytestmark = pytest.mark.asyncio

async def test_api_v1_stages_get(client):
    """Test case for api_v1_stages_get

    Returns a list of Bill stages.
    """
    params = [('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Stages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

