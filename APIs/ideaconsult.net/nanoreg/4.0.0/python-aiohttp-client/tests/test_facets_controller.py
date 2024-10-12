# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.facet import Facet


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_summary_0(client):
    """Test case for get_endpoint_summary_0

    Search endpoint summary
    """
    params = [('top', 'top_example'),
                    ('category', 'category_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nanoreg1/enm/{db}/query/study'.format(db=nanoreg1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

