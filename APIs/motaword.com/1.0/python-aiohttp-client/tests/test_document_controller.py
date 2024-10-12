# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.continuous_project_document import ContinuousProjectDocument
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_subjects import DocumentSubjects
from openapi_server.models.error import Error
from openapi_server.models.list_order_type import ListOrderType
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.progress import Progress
from openapi_server.models.regenerate_preview_response import RegeneratePreviewResponse
from openapi_server.models.use_as_draft_payload import UseAsDraftPayload
from openapi_server.models.use_as_regular_payload import UseAsRegularPayload


pytestmark = pytest.mark.asyncio

async def test_get_all_document_subjects(client):
    """Test case for get_all_document_subjects

    Get a list of subjects of projects
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/documents/subjects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document(client):
    """Test case for get_document

    View a single document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/documents/{document_id}'.format(document_id='179469'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document_progress(client):
    """Test case for get_document_progress

    View a document translation progress
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/documents/{document_id}/progress'.format(document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_documents(client):
    """Test case for get_documents

    View your documents
    """
    params = [('recent', True),
                    ('search', 'search_example'),
                    ('type_filter', ALL),
                    ('language_code', 'language_code_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('order_by', updated_at),
                    ('order_type', openapi_server.ListOrderType()),
                    ('with[]', ['_with_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_documents(client):
    """Test case for get_similar_documents

    Find documents similar to this document.
    """
    params = [('per_page', 1),
                    ('with[]', ['_with_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/documents/{document_id}/similars'.format(document_id=179469),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_documents(client):
    """Test case for get_user_documents

    Get a list of your documents
    """
    params = [('recent', True),
                    ('search', 'search_example'),
                    ('type_filter', ALL),
                    ('language_code', 'language_code_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('order_by', updated_at),
                    ('order_type', openapi_server.ListOrderType())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/documents'.format(user_id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regenerate_preview(client):
    """Test case for regenerate_preview

    Regenerate preview and return preview URL for given file
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/documents/{document_id}/regenerate_preview'.format(document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_use_as_draft(client):
    """Test case for use_as_draft

    Use the translation of given source manual document as manual draft source for the given target document.
    """
    body = {"fromFileId":0.8008281904610115,"fromManualTranslationFileId":6.027456183070403,"toManualTranslationFileId":1.4658129805029452}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/documents/{document_id}/use_as_draft'.format(document_id=179469),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_use_as_regular(client):
    """Test case for use_as_regular

    Use the translation of the given manual document as a regular file.
    """
    body = {"fromManualTranslationFileId":0.8008281904610115,"allowOriginalFilePreview":True,"disableInvitations":True,"hideNumbers":True,"allowReviewInManualEditor":True,"recreate":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/documents/{document_id}/use_as_regular'.format(document_id=179469),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

