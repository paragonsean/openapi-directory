# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bioassays import Bioassays


pytestmark = pytest.mark.asyncio

async def test_get_bioassays_using_get1(client):
    """Test case for get_bioassays_using_get1

    Get pubchem bioassays associated to particular substance ids (sid) & outcome
    """
    params = [('limit', 10),
                    ('outcome', 'outcome_example'),
                    ('page', 0),
                    ('sids', ['sids_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/pubchem/bioassays/sids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

