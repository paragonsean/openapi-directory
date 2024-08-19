# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_company_specific_open_api_documentation(client):
    """Test case for get_company_specific_open_api_documentation

    Get Company-Specific Open API Documentation
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/openapi'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

