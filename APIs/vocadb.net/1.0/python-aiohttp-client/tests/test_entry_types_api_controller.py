# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entry_type import EntryType
from openapi_server.models.tag_for_api_contract import TagForApiContract
from openapi_server.models.tag_optional_fields import TagOptionalFields


pytestmark = pytest.mark.asyncio

async def test_api_entry_types_entry_type_sub_type_tag_get(client):
    """Test case for api_entry_types_entry_type_sub_type_tag_get

    
    """
    params = [('fields', openapi_server.TagOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/entry-types/{entry_type}/{sub_type}/tag'.format(entry_type=openapi_server.EntryType(), sub_type='sub_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

