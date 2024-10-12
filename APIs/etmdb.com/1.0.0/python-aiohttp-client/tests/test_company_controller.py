# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_company_search_read(client):
    """Test case for company_search_read

    Return company search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/company/search/{company_name}'.format(company_name='company_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

