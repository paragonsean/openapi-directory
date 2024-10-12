# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.charity_org import CharityOrg
from openapi_server.models.charity_search_response import CharitySearchResponse


pytestmark = pytest.mark.asyncio

async def test_get_charity_org(client):
    """Test case for get_charity_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/charity/v1/charity_org/{charity_org_id}'.format(charity_org_id='charity_org_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_charity_orgs(client):
    """Test case for get_charity_orgs

    
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('q', 'q_example'),
                    ('registration_ids', 'registration_ids_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/charity/v1/charity_org',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

