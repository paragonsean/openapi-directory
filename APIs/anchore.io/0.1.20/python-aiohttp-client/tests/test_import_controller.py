# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.anchore_image import AnchoreImage
from openapi_server.models.api_error_response import ApiErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_import_image_archive(client):
    """Test case for import_image_archive

    Import an anchore image tar.gz archive file. This is a deprecated API replaced by the \"/imports/images\" route
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('archive_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/import/images',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

