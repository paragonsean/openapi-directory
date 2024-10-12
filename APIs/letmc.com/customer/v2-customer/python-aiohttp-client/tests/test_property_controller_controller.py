# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.landlord_photo_model_results import LandlordPhotoModelResults


pytestmark = pytest.mark.asyncio

async def test_property_controller_get_properties_photos(client):
    """Test case for property_controller_get_properties_photos

    A collection showing all the photos linked to a specific block, property or room
    """
    params = [('token', 'token_example'),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/property/{property_id}/photos'.format(short_name='short_name_example', property_id='property_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

