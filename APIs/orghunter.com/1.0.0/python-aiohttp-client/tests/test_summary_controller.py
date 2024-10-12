# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_summary(client):
    """Test case for get_summary

    Get summary data!
    """
    params = [('ein', 'ein_example'),
                    ('searchTerm', 'search_term_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('zipCode', 'zip_code_example'),
                    ('category', 'category_example'),
                    ('eligible', 'eligible_example'),
                    ('start', 'start_example'),
                    ('rows', 'rows_example')]
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/charitysearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

