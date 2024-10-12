# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_data_hierarchy_interface import CompanyDataHierarchyInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_company_hierarchy_v1_get_company_hierarchy_get(client):
    """Test case for company_company_hierarchy_v1_get_company_hierarchy_get

    hierarchy/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/hierarchy/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

