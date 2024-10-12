# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_user_defined_field_dto import PageResultUserDefinedFieldDto


pytestmark = pytest.mark.asyncio

async def test_user_defined_fields_get(client):
    """Test case for user_defined_fields_get

    Returns a list of company's User Defined Fields. Supports OData querying protocol.  Filtering is allowed by \"categoryTypeId\" field.  Ordering is allowed by \"id\" and \"orderIndex\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/userDefinedFields',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

