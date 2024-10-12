# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.farm_organization import FarmOrganization


pytestmark = pytest.mark.asyncio

async def test_fetch_farm_organization_by_type_and_id(client):
    """Test case for fetch_farm_organization_by_type_and_id

    Retrieve a specific farm organization by organization type and ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/farmOrganizations/{farm_organization_type}/{farm_organization_id}'.format(farm_organization_type='farm_organization_type_example', farm_organization_id='farm_organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

