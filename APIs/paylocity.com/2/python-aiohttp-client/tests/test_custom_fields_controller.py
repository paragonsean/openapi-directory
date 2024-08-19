# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field_definition import CustomFieldDefinition
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_all_custom_fields_by_category(client):
    """Test case for get_all_custom_fields_by_category

    Get All Custom Fields
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/customfields/{category}'.format(company_id='company_id_example', category='category_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

