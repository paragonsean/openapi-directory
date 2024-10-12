# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_item_resource import BusinessItemResource
from openapi_server.models.laid_paper_type import LaidPaperType
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_business_item_by_id(client):
    """Test case for get_business_item_by_id

    Returns business item by ID.
    """
    params = [('LaidPaper', openapi_server.LaidPaperType())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/BusinessItem/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

