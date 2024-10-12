# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.organization_model import OrganizationModel
from openapi_server.models.organization_model_haljson import OrganizationModelHaljson


pytestmark = pytest.mark.asyncio

async def test_get_organizations(client):
    """Test case for get_organizations

    List Organizations
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

