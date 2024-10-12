# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.association import Association
from openapi_server.models.file_object import FileObject
from openapi_server.models.files import Files
from openapi_server.models.folder import Folder


pytestmark = pytest.mark.asyncio

async def test_create_file_association(client):
    """Test case for create_file_association

    Creates a new file association
    """
    body = {"ObjectType":"Unknown","ObjectId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ObjectGroup":"Account","FileId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/files.xro/1.0/Files/{file_id}/Associations'.format(file_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_folder(client):
    """Test case for create_folder

    Creates a new folder
    """
    body = {"IsInbox":True,"Email":"foo@bar.com","FileCount":5,"Id":"4ff1e5cc-9835-40d5-bb18-09fdb118db9c","Name":"assets"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/files.xro/1.0/Folders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_file(client):
    """Test case for delete_file

    Deletes a specific file
    """
    headers = { 
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files.xro/1.0/Files/{file_id}'.format(file_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_file_association(client):
    """Test case for delete_file_association

    Deletes an existing file association
    """
    headers = { 
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files.xro/1.0/Files/{file_id}/Associations/{object_id}'.format(file_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c', object_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_folder(client):
    """Test case for delete_folder

    Deletes a folder
    """
    headers = { 
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files.xro/1.0/Folders/{folder_id}'.format(folder_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_associations_by_object(client):
    """Test case for get_associations_by_object

    Retrieves an association object using a unique object ID
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Associations/{object_id}'.format(object_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file(client):
    """Test case for get_file

    Retrieves a file by a unique file ID
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Files/{file_id}'.format(file_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_associations(client):
    """Test case for get_file_associations

    Retrieves a specific file associations
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Files/{file_id}/Associations'.format(file_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_content(client):
    """Test case for get_file_content

    Retrieves the content of a specific file
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Files/{file_id}/Content'.format(file_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files(client):
    """Test case for get_files

    Retrieves files
    """
    params = [('pagesize', 50),
                    ('page', 2),
                    ('sort', 'CreatedDateUTC DESC')]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_folder(client):
    """Test case for get_folder

    Retrieves specific folder by using a unique folder ID
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Folders/{folder_id}'.format(folder_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_folders(client):
    """Test case for get_folders

    Retrieves folders
    """
    params = [('sort', 'CreatedDateUTC DESC')]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Folders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_inbox(client):
    """Test case for get_inbox

    Retrieves inbox folder
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files.xro/1.0/Inbox',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_file(client):
    """Test case for update_file

    Update a file
    """
    body = {"CreatedDateUtc":"2020-12-03T19:04:58.6970000","User":{"FirstName":"John","FullName":"Smith","Id":"4ff1e5cc-9835-40d5-bb18-09fdb118db9c","LastName":"Smith","Name":"john.smith@mail.com"},"UpdatedDateUtc":"2020-12-03T19:04:58.6970000","Size":3615,"FolderId":"0f8ccf21-7267-4268-9167-a1e2c40c84c8","Id":"d290f1ee-6c54-4b01-90e6-d701748f0851","MimeType":"image/jpeg","Name":"File2.jpg"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/files.xro/1.0/Files/{file_id}'.format(file_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_folder(client):
    """Test case for update_folder

    Updates an existing folder
    """
    body = {"IsInbox":True,"Email":"foo@bar.com","FileCount":5,"Id":"4ff1e5cc-9835-40d5-bb18-09fdb118db9c","Name":"assets"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/files.xro/1.0/Folders/{folder_id}'.format(folder_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file(client):
    """Test case for upload_file

    Uploads a File
    """
    params = [('FolderId', '4ff1e5cc-9835-40d5-bb18-09fdb118db9c')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    data.add_field('filename', 'filename_example')
    data.add_field('mime_type', 'mime_type_example')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/files.xro/1.0/Files',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

