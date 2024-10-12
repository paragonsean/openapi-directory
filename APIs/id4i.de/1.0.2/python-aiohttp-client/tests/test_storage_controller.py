# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.api_error import ApiError
from openapi_server.models.document import Document
from openapi_server.models.document_update import DocumentUpdate
from openapi_server.models.paginated_response_of_document import PaginatedResponseOfDocument


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_document(client):
    """Test case for create_document

    Create an document for an id4n
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'special-key',
    }
    data = FormData()
    data.add_field('content', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/documents/{id4n}/{organization_id}'.format(organization_id='organization_id_example', id4n='id4n_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_document(client):
    """Test case for delete_document

    Delete a document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/documents/{id4n}/{organization_id}/{file_name}'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document(client):
    """Test case for get_document

    Retrieve a document (meta-data only, no content)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/documents/{id4n}/{organization_id}/{file_name}/metadata'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_document_0(client):
    """Test case for get_public_document_0

    Retrieve a public document (meta-data only, no content)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/documents/{id4n}/{organization_id}/{file_name}/metadata'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_documents(client):
    """Test case for list_all_documents

    List documents
    """
    params = [('owner', 'owner_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/documents/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_public_documents_0(client):
    """Test case for list_all_public_documents_0

    List public documents
    """
    params = [('organizationId', 'organization_id_example'),
                    ('owner', 'owner_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/documents/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_documents(client):
    """Test case for list_documents

    List organization specific documents
    """
    params = [('owner', 'owner_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/documents/{id4n}/{organization_id}'.format(organization_id='organization_id_example', id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_put_document(client):
    """Test case for put_document

    Put an document for an id4n
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'special-key',
    }
    data = FormData()
    data.add_field('content', '/path/to/file')
    response = await client.request(
        method='PUT',
        path='/api/v1/documents/{id4n}/{organization_id}'.format(organization_id='organization_id_example', id4n='id4n_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_document(client):
    """Test case for read_document

    Read document contents
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/documents/{id4n}/{organization_id}/{file_name}'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_from_microstorage(client):
    """Test case for read_from_microstorage

    Read data from microstorage
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/microstorage/{id4n}/{organization}'.format(organization='organization_example', id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_public_document_0(client):
    """Test case for read_public_document_0

    Read public document contents
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/documents/{id4n}/{organization_id}/{file_name}'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_document_metadata(client):
    """Test case for update_document_metadata

    Update a document
    """
    body = {"filename":"publicInfo.pdf","visibility":{"sharedWithOrganizationIds":["de.acme","com.porsche","de.bluerain"],"public":True},"mimeType":"text/plain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/documents/{id4n}/{organization_id}/{file_name}/metadata'.format(organization_id='organization_id_example', id4n='id4n_example', file_name='file_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_write_to_microstorage(client):
    """Test case for write_to_microstorage

    Write data to microstorage
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'content_length': 56,
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/microstorage/{id4n}/{organization}'.format(organization='organization_example', id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

