# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_codes import CompanyCodes
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_all_company_codes_and_descriptions_by_resource(client):
    """Test case for get_all_company_codes_and_descriptions_by_resource

    Get All Company Codes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/codes/{code_resource}'.format(company_id='company_id_example', code_resource='code_resource_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

