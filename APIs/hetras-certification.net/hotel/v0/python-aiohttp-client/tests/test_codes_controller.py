# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.code_full_entry import CodeFullEntry
from openapi_server.models.codes_list_response import CodesListResponse


pytestmark = pytest.mark.asyncio

async def test_codes_get_code(client):
    """Test case for codes_get_code

    Get all the details for a specific code available for the hotel.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/codes/{id}'.format(hotel_id=56, id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_codes_get_codes(client):
    """Test case for codes_get_codes

    Get a list of codes for the specified hotel either filtered by type or code.
    """
    params = [('code', 'code_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/codes'.format(hotel_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

