# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_service_exception import DocumentServiceException
from openapi_server.models.search_exception import SearchException
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.suggest_response import SuggestResponse
from openapi_server.models.upload_documents_request import UploadDocumentsRequest
from openapi_server.models.upload_documents_response import UploadDocumentsResponse


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    
    """
    params = [('cursor', 'cursor_example'),
                    ('expr', 'expr_example'),
                    ('facet', 'facet_example'),
                    ('fq', 'fq_example'),
                    ('highlight', 'highlight_example'),
                    ('partial', True),
                    ('q', 'q_example'),
                    ('q.options', 'q_options_example'),
                    ('q.parser', 'q_parser_example'),
                    ('return', '_return_example'),
                    ('size', 56),
                    ('sort', 'sort_example'),
                    ('start', 56),
                    ('stats', 'stats_example'),
                    ('format', 'format_example'),
                    ('pretty', 'pretty_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-01-01/search#format=sdk&pretty=true&q',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggest(client):
    """Test case for suggest

    
    """
    params = [('q', 'q_example'),
                    ('suggester', 'suggester_example'),
                    ('size', 56),
                    ('format', 'format_example'),
                    ('pretty', 'pretty_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-01-01/suggest#format=sdk&pretty=true&q&suggester',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_documents(client):
    """Test case for upload_documents

    
    """
    body = {"documents":""}
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'content_type': 'content_type_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-01-01/documents/batch#format=sdk&Content-Type',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

