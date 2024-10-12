# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_create_corpus_request import AdminCreateCorpusRequest
from openapi_server.models.admin_create_corpus_response import AdminCreateCorpusResponse
from openapi_server.models.admin_delete_corpus_request import AdminDeleteCorpusRequest
from openapi_server.models.admin_delete_corpus_response import AdminDeleteCorpusResponse
from openapi_server.models.admin_list_corpora_request import AdminListCorporaRequest
from openapi_server.models.admin_list_corpora_response import AdminListCorporaResponse
from openapi_server.models.admin_reset_corpus_request import AdminResetCorpusRequest
from openapi_server.models.admin_reset_corpus_response import AdminResetCorpusResponse
from openapi_server.models.googlerpc_status import GooglerpcStatus


pytestmark = pytest.mark.asyncio

async def test_create_corpus(client):
    """Test case for create_corpus

    
    """
    body = openapi_server.AdminCreateCorpusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/create-corpus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_corpus(client):
    """Test case for delete_corpus

    
    """
    body = openapi_server.AdminDeleteCorpusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/delete-corpus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_corpora(client):
    """Test case for list_corpora

    
    """
    body = openapi_server.AdminListCorporaRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/list-corpora',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_corpus(client):
    """Test case for reset_corpus

    
    """
    body = openapi_server.AdminResetCorpusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/reset-corpus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

