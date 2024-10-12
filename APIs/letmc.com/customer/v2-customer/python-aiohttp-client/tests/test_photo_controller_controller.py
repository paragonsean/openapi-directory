# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_photo_controller_get_photo_download(client):
    """Test case for photo_controller_get_photo_download

    Downloads the photo of a property given the photo ID.
    """
    params = [('token', 'token_example'),
                    ('photoID', 'photo_id_example'),
                    ('width', 56),
                    ('height', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/photo/download'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

