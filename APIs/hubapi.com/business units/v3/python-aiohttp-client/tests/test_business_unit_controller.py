# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_public_business_unit_no_paging import CollectionResponsePublicBusinessUnitNoPaging
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_business_units_v3_business_units_user_user_id_get_by_user_id(client):
    """Test case for get_business_units_v3_business_units_user_user_id_get_by_user_id

    Get Business Units for a user
    """
    params = [('properties', ['properties_example']),
                    ('name', ['name_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/business-units/v3/business-units/user/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

