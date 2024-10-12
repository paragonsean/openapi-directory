# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_upload_failure import DocumentUploadFailure
from openapi_server.models.document_upload_status_guid_list import DocumentUploadStatusGuidList
from openapi_server.models.get_benefits_document_upload_status200_response import GetBenefitsDocumentUploadStatus200Response
from openapi_server.models.get_benefits_document_upload_status404_response import GetBenefitsDocumentUploadStatus404Response
from openapi_server.models.get_benefits_document_upload_status_report200_response import GetBenefitsDocumentUploadStatusReport200Response
from openapi_server.models.post_benefits_document_upload202_response import PostBenefitsDocumentUpload202Response
from openapi_server.models.post_benefits_document_upload403_response import PostBenefitsDocumentUpload403Response
from openapi_server.models.post_benefits_document_upload_validate_document200_response import PostBenefitsDocumentUploadValidateDocument200Response
from openapi_server.models.post_benefits_document_upload_validate_document422_response import PostBenefitsDocumentUploadValidateDocument422Response
from openapi_server.models.put_benefits_document_upload401_response import PutBenefitsDocumentUpload401Response
from openapi_server.models.put_benefits_document_upload422_response import PutBenefitsDocumentUpload422Response
from openapi_server.models.put_benefits_document_upload429_response import PutBenefitsDocumentUpload429Response
from openapi_server.models.put_benefits_document_upload500_response import PutBenefitsDocumentUpload500Response


pytestmark = pytest.mark.asyncio

async def test_get_benefits_document_upload_download(client):
    """Test case for get_benefits_document_upload_download

    Download zip of \"what the server sees\"
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/vba_documents/v1/uploads/{id}/download'.format(id='6d8433c1-cd55-4c24-affd-f592287a7572'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_benefits_document_upload_status(client):
    """Test case for get_benefits_document_upload_status

    Get status for a previous benefits document upload
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/vba_documents/v1/uploads/{id}'.format(id='6d8433c1-cd55-4c24-affd-f592287a7572'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_benefits_document_upload_status_report(client):
    """Test case for get_benefits_document_upload_status_report

    Get a bulk status report for a list of previous uploads
    """
    body = {"ids":["6d8433c1-cd55-4c24-affd-f592287a7572","6d8433c1-cd55-4c24-affd-f592287a7572","6d8433c1-cd55-4c24-affd-f592287a7572","6d8433c1-cd55-4c24-affd-f592287a7572","6d8433c1-cd55-4c24-affd-f592287a7572"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/services/vba_documents/v1/uploads/report',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_benefits_document_upload(client):
    """Test case for post_benefits_document_upload

    Get a location for subsequent document upload PUT request
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/services/vba_documents/v1/uploads',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_benefits_document_upload_validate_document(client):
    """Test case for post_benefits_document_upload_validate_document

    Validate an individual document against system file requirements
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/services/vba_documents/v1/uploads/validate_document',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_benefits_document_upload(client):
    """Test case for put_benefits_document_upload

    Accepts document upload.
    """
    headers = { 
        'Accept': 'application/json',
        'content_md5': 'content_md5_example',
    }
    response = await client.request(
        method='PUT',
        path='/services/vba_documents/v1/path',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

