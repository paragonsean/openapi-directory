# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.kyc_document2 import KycDocument2
from openapi_server.models.kyc_document_rejection import KycDocumentRejection
from openapi_server.models.kyc_request import KycRequest
from openapi_server.models.patch_kyc_request_request import PatchKycRequestRequest
from openapi_server.models.post_kyc_document_matches_request import PostKycDocumentMatchesRequest


pytestmark = pytest.mark.asyncio

async def test_delete_kyc_request(client):
    """Test case for delete_kyc_request

    Delete the KYC request
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/kyc-requests/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_kyc_document(client):
    """Test case for get_kyc_document

    Retrieve a KYC Document
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/kyc-documents/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_kyc_document_collection(client):
    """Test case for get_kyc_document_collection

    Retrieve a list of KYC documents
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/kyc-documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_kyc_request(client):
    """Test case for get_kyc_request

    Retrieve a KYC request
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/kyc-requests/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_kyc_request_collection(client):
    """Test case for get_kyc_request_collection

    Retrieve a list of KYC requests
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/kyc-requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_kyc_request(client):
    """Test case for patch_kyc_request

    Update a KYC request
    """
    body = openapi_server.PatchKycRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/kyc-requests/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_kyc_document(client):
    """Test case for post_kyc_document

    Create a KYC Document
    """
    body = openapi_server.KycDocument2()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/kyc-documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_kyc_document_acceptance(client):
    """Test case for post_kyc_document_acceptance

    Accept a KYC document
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/kyc-documents/{id}/acceptance'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_kyc_document_matches(client):
    """Test case for post_kyc_document_matches

    Update a KYC document's documentMatches
    """
    body = openapi_server.PostKycDocumentMatchesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/kyc-documents/{id}/matches'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_kyc_document_rejection(client):
    """Test case for post_kyc_document_rejection

    Reject a KYC document
    """
    body = {"message":"Provided document is unreadable","type":"document-unreadable"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/kyc-documents/{id}/rejection'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_kyc_document_review(client):
    """Test case for post_kyc_document_review

    Review a KYC document
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/kyc-documents/{id}/review'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_kyc_request(client):
    """Test case for post_kyc_request

    Create a KYC Request
    """
    body = {"updatedTime":"","reason":"reason","redirectUrl":"https://openapi-generator.tech","matchLevel":2,"documents":[{"maxAttempts":8,"type":"","subtypes":["passport","passport"]},{"maxAttempts":8,"type":"","subtypes":["passport","passport"]}],"_links":[{"rel":"self"},{"rel":"self"}],"expirationTime":"2000-01-23T04:56:07.000+00:00","customerId":"","createdTime":"","id":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/kyc-requests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_kyc_document(client):
    """Test case for put_kyc_document

    Create or update a KYC document with predefined ID
    """
    body = openapi_server.KycDocument2()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/kyc-documents/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

