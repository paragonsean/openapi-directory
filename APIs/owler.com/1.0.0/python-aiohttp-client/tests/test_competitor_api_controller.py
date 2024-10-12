# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_competitor_vo import CompanyCompetitorVO


pytestmark = pytest.mark.asyncio

async def test_v1_company_competitor_id_company_id_get(client):
    """Test case for v1_company_competitor_id_company_id_get

    Get Competitor information by Id
    """
    params = [('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/competitor/id/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_company_competitor_url_website_get(client):
    """Test case for v1_company_competitor_url_website_get

    Get Competitor information by URL
    """
    params = [('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/competitor/url/{website}'.format(website='website_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

