# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_cabwise_get(client):
    """Test case for cabwise_get

    Gets taxis and minicabs contact information
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('optype', 'optype_example'),
                    ('wc', 'wc_example'),
                    ('radius', 3.4),
                    ('name', 'name_example'),
                    ('maxResults', 56),
                    ('legacyFormat', True),
                    ('forceXml', True),
                    ('twentyFourSevenOnly', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Cabwise/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

