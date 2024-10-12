# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.photo_model import PhotoModel
from openapi_server.models.photo_model_results import PhotoModelResults


pytestmark = pytest.mark.asyncio

async def test_photo_controller_get_photo_download(client):
    """Test case for photo_controller_get_photo_download

    Downloads the photo of a property given the property and photo ID.
    """
    params = [('width', 56),
                    ('height', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/photos/photo/{photo_id}/download'.format(short_name='short_name_example', photo_id='photo_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_photo_photos_get(client):
    """Test case for v2_tier2_short_name_photo_photos_get

    A collection of all photos in the company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/photo/photos'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_photo_photos_photo_idget(client):
    """Test case for v2_tier2_short_name_photo_photos_photo_idget

    Get a specific photo given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/photo/photos/{photo_id}'.format(short_name='short_name_example', photo_id='photo_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

