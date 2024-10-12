# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_snippet_response import DeleteSnippetResponse
from openapi_server.models.retrieve_snippet_response import RetrieveSnippetResponse
from openapi_server.models.upsert_snippet_request import UpsertSnippetRequest
from openapi_server.models.upsert_snippet_response import UpsertSnippetResponse


pytestmark = pytest.mark.asyncio

async def test_delete_snippet(client):
    """Test case for delete_snippet

    DeleteSnippet
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/sites/{site_id}/snippet'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_snippet(client):
    """Test case for retrieve_snippet

    RetrieveSnippet
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/sites/{site_id}/snippet'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_snippet(client):
    """Test case for upsert_snippet

    UpsertSnippet
    """
    body = {"request_body":{"snippet":{"content":"<script>var js = 1;</script>"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/sites/{site_id}/snippet'.format(site_id='site_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

