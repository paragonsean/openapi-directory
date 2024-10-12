# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.competitors import Competitors


pytestmark = pytest.mark.asyncio

async def test_v1_company_competitorpremium_id_company_id_get(client):
    """Test case for v1_company_competitorpremium_id_company_id_get

    Get Competitor information by Id
    """
    params = [('pagination_id', 'pagination_id_example'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/competitorpremium/id/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_company_competitorpremium_url_website_get(client):
    """Test case for v1_company_competitorpremium_url_website_get

    Get Competitor information by Url
    """
    params = [('pagination_id', 'pagination_id_example'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/competitorpremium/url/{website}'.format(website='website_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

