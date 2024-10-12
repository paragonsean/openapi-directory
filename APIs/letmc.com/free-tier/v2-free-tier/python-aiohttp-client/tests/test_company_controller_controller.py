# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_model import CompanyModel


pytestmark = pytest.mark.asyncio

async def test_company_controller_get_company(client):
    """Test case for company_controller_get_company

    Information about a specific company
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/company'.format(short_name='short_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

