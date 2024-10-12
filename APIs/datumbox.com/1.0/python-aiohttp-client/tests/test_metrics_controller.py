# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_document_similarity(client):
    """Test case for document_similarity

    Estimates the similarity between 2 Documents
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'copy': 'copy_example',
        'original': 'original_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/DocumentSimilarity.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

