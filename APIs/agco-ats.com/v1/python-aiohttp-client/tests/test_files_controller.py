# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_file_download import APIIPagedResponseGlobalResourcesSharedModelsFileDownload
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_file_download import GlobalResourcesSharedModelsFileDownload


pytestmark = pytest.mark.asyncio

async def test_files_delete_file(client):
    """Test case for files_delete_file

    Mark a file as 'Removed'. Disables download of the file and hides metadata from GET all method
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Files/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_file(client):
    """Test case for files_get_file

    Gets a file's metadata.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Files/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_file_contents(client):
    """Test case for files_get_file_contents

    Download the contents of a file. The current State of the File should be 'Available'.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Files/{id}/FileContents'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_files(client):
    """Test case for files_get_files

    Get a paged response of file metadata.
    """
    params = [('includeDeleted', True),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_files_post_file(client):
    """Test case for files_post_file

    Create the metadata for a file before uploading. The State of the File should be 'Created'.
    """
    body = openapi_server.GlobalResourcesSharedModelsFileDownload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Files',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_files_put_file(client):
    """Test case for files_put_file

    Update the metadata for a file. Size may not be modified by the client.
    """
    body = openapi_server.GlobalResourcesSharedModelsFileDownload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Files/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_put_file_contents(client):
    """Test case for files_put_file_contents

    Upload the contents of a file. The current State of the File should be 'Created'.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Files/{id}/FileContents'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

