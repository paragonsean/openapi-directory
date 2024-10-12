# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_company_credits_search_read(client):
    """Test case for company_credits_search_read

    Return company credits search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/company-credits/search/{movie_title}'.format(movie_title='movie_title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_credits_searchall_read(client):
    """Test case for company_credits_searchall_read

    Return company credits search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/company-credits/searchall/{param}'.format(param='param_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

