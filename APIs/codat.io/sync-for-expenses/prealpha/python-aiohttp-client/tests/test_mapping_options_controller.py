# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mapping_options import MappingOptions


pytestmark = pytest.mark.asyncio

async def test_get_mapping_options(client):
    """Test case for get_mapping_options

    Mapping options
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/mappingOptions'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

