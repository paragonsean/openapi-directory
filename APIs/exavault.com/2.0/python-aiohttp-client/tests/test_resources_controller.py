# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.add_folder_request_body import AddFolderRequestBody
from openapi_server.models.compress_files_request_body import CompressFilesRequestBody
from openapi_server.models.copy_resources_request_body import CopyResourcesRequestBody
from openapi_server.models.delete_resources_request_body import DeleteResourcesRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.extract_files_request_body import ExtractFilesRequestBody
from openapi_server.models.move_resources_request_body import MoveResourcesRequestBody
from openapi_server.models.preview_file_response import PreviewFileResponse
from openapi_server.models.resource_collection_response import ResourceCollectionResponse
from openapi_server.models.resource_copy_move import ResourceCopyMove
from openapi_server.models.resource_multi_response import ResourceMultiResponse
from openapi_server.models.resource_response import ResourceResponse
from openapi_server.models.update_resource_by_id_request_body import UpdateResourceByIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_add_folder(client):
    """Test case for add_folder

    Create a folder
    """
    body = {"path":"path","parentResource":"parentResource","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/resources',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compress_files(client):
    """Test case for compress_files

    Compress resources
    """
    body = {"parentResource":"parentResource","archiveName":"archiveName","resources":["resources","resources"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/resources/compress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_resources(client):
    """Test case for copy_resources

    Copy resources
    """
    body = {"parentResource":"parentResource","resources":["resources","resources"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/resources/copy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_resource_by_id(client):
    """Test case for delete_resource_by_id

    Delete a Resource
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/resources/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_resources(client):
    """Test case for delete_resources

    Delete Resources
    """
    body = {"resources":["resources","resources"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/resources',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download(client):
    """Test case for download

    Download a file
    """
    params = [('resources[]', ['resources_example']),
                    ('downloadArchiveName', 'download_archive_name_example')]
    headers = { 
        'Accept': 'application/zip',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extract_files(client):
    """Test case for extract_files

    Extract resources
    """
    body = {"parentResource":"parentResource","resource":"resource"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/resources/extract',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_preview_image(client):
    """Test case for get_preview_image

    Preview a file
    """
    params = [('resource', 'resource_example'),
                    ('size', 'size_example'),
                    ('width', 56),
                    ('height', 56),
                    ('page', 0)]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/preview',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_resource_info(client):
    """Test case for get_resource_info

    Get Resource Properties
    """
    params = [('resource', 'resource_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_resource_info_by_id(client):
    """Test case for get_resource_info_by_id

    Get resource metadata
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_resource_contents(client):
    """Test case for list_resource_contents

    List contents of folder
    """
    params = [('sort', 'name'),
                    ('offset', 0),
                    ('limit', 56),
                    ('type', 'type_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/list/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_resources(client):
    """Test case for list_resources

    Get a list of all resources
    """
    params = [('resource', 'resource_example'),
                    ('sort', 'name'),
                    ('offset', 0),
                    ('limit', 56),
                    ('type', 'type_example'),
                    ('name', 'name_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_resources(client):
    """Test case for move_resources

    Move resources
    """
    body = {"parentResource":"/copyhere","resources":["/testone.jpg","/folder"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/resources/move',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_resource_by_id(client):
    """Test case for update_resource_by_id

    Rename a resource.
    """
    body = {"name":"my-renamed-file.txt"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
        'ev_api_key': 'ev_api_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/resources/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file(client):
    """Test case for upload_file

    Upload a file
    """
    params = [('path', 'path_example'),
                    ('fileSize', 2935),
                    ('resume', True),
                    ('allowOverwrite', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
        'offset_bytes': 4852,
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v2/resources/upload',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

