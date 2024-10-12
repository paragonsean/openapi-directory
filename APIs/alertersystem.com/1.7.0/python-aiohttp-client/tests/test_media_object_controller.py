# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.api_media_object_get_collection200_response import ApiMediaObjectGetCollection200Response
from openapi_server.models.media_object_get import MediaObjectGet
from openapi_server.models.media_object_jsonld_get import MediaObjectJsonldGet


pytestmark = pytest.mark.asyncio

async def test_api_media_object_get_collection(client):
    """Test case for api_media_object_get_collection

    Retrieves the collection of MediaObject resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/media-object',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_media_object_id_delete(client):
    """Test case for api_media_object_id_delete

    Removes the MediaObject resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/media-object/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_media_object_id_get(client):
    """Test case for api_media_object_id_get

    Retrieves a MediaObject resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/media-object/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_media_object_post(client):
    """Test case for api_media_object_post

    Creates a MediaObject resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('data_segment_code', 'data_segment_code_example')
    data.add_field('file', '/path/to/file')
    data.add_field('keywords', 'keywords_example')
    data.add_field('partition', 'partition_example')
    response = await client.request(
        method='POST',
        path='/api/media-object',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

