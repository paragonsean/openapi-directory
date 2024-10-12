# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill_stage_sitting_search_result import BillStageSittingSearchResult
from openapi_server.models.house import House
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_sittings(client):
    """Test case for get_sittings

    Returns a list of Sittings.
    """
    params = [('House', openapi_server.House()),
                    ('DateFrom', '2013-10-20T19:20:30+01:00'),
                    ('DateTo', '2013-10-20T19:20:30+01:00'),
                    ('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Sittings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

