# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.publication_document import PublicationDocument


pytestmark = pytest.mark.asyncio

async def test_api_v1_publications_publication_id_documents_document_id_download_get(client):
    """Test case for api_v1_publications_publication_id_documents_document_id_download_get

    Return a document.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Publications/{publication_id}/Documents/{document_id}/Download'.format(publication_id=56, document_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_publications_publication_id_documents_document_id_get(client):
    """Test case for api_v1_publications_publication_id_documents_document_id_get

    Return information on a document.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Publications/{publication_id}/Documents/{document_id}'.format(publication_id=56, document_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

