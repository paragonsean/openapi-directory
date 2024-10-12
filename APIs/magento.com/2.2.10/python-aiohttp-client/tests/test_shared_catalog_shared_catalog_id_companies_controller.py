# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_shared_catalog_company_management_v1_get_companies_get(client):
    """Test case for shared_catalog_company_management_v1_get_companies_get

    sharedCatalog/{sharedCatalogId}/companies
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/sharedCatalog/{shared_catalog_id}/companies'.format(shared_catalog_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

