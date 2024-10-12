# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_keyword_extraction(client):
    """Test case for keyword_extraction

    Extracts the Keywords of the Document
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'n': 56,
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/KeywordExtraction.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_text_extraction(client):
    """Test case for text_extraction

    Extracts the clear text from Webpage
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/TextExtraction.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

