# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attachment import Attachment
from openapi_server.models.error import Error
from openapi_server.models.file import File
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.post_file_request import PostFileRequest


pytestmark = pytest.mark.asyncio

async def test_delete_attachment(client):
    """Test case for delete_attachment

    Delete an Attachment
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/attachments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_file(client):
    """Test case for delete_file

    Delete a File
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attachment(client):
    """Test case for get_attachment

    Retrieve an Attachment
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/attachments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attachment_collection(client):
    """Test case for get_attachment_collection

    Retrieve a list of Attachments
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('expand', 'expand_example'),
                    ('fields', 'fields_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/attachments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file(client):
    """Test case for get_file

    Retrieve a File Record
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_collection(client):
    """Test case for get_file_collection

    Retrieve a list of files
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('expand', 'expand_example'),
                    ('fields', 'fields_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_download(client):
    """Test case for get_file_download

    Download a file
    """
    params = [('imageSize', '700x700')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/{id}/download'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_download_extension(client):
    """Test case for get_file_download_extension

    Download image in specific format
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/{id}/download{extension}'.format(id='id_example', extension='extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_attachment(client):
    """Test case for post_attachment

    Create an Attachment
    """
    body = {"updatedTime":"","relatedType":"customer","_embedded":[{"file":{"updatedTime":"","extension":"extension","_links":[{"rel":"self"},{"rel":"self"}],"mime":"image/png","description":"description","tags":["tags","tags"],"sha1":"sha1","size":6,"name":"name","width":1,"createdTime":"","isPublic":True,"id":"","height":0}},{"file":{"updatedTime":"","extension":"extension","_links":[{"rel":"self"},{"rel":"self"}],"mime":"image/png","description":"description","tags":["tags","tags"],"sha1":"sha1","size":6,"name":"name","width":1,"createdTime":"","isPublic":True,"id":"","height":0}}],"_links":[{"rel":"self"},{"rel":"self"}],"name":"name","createdTime":"","description":"description","id":"","fileId":"fileId","relatedId":"relatedId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/attachments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_file(client):
    """Test case for post_file

    Create a file
    """
    body = openapi_server.PostFileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/files',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_attachment(client):
    """Test case for put_attachment

    Update the Attachment with predefined ID
    """
    body = {"updatedTime":"","relatedType":"customer","_embedded":[{"file":{"updatedTime":"","extension":"extension","_links":[{"rel":"self"},{"rel":"self"}],"mime":"image/png","description":"description","tags":["tags","tags"],"sha1":"sha1","size":6,"name":"name","width":1,"createdTime":"","isPublic":True,"id":"","height":0}},{"file":{"updatedTime":"","extension":"extension","_links":[{"rel":"self"},{"rel":"self"}],"mime":"image/png","description":"description","tags":["tags","tags"],"sha1":"sha1","size":6,"name":"name","width":1,"createdTime":"","isPublic":True,"id":"","height":0}}],"_links":[{"rel":"self"},{"rel":"self"}],"name":"name","createdTime":"","description":"description","id":"","fileId":"fileId","relatedId":"relatedId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/attachments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_file(client):
    """Test case for put_file

    Update the File with predefined ID
    """
    body = {"updatedTime":"","extension":"extension","_links":[{"rel":"self"},{"rel":"self"}],"mime":"image/png","description":"description","tags":["tags","tags"],"sha1":"sha1","size":6,"name":"name","width":1,"createdTime":"","isPublic":True,"id":"","height":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/files/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

