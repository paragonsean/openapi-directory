# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_result import DocumentResult


pytestmark = pytest.mark.asyncio

async def test_analyze_get(client):
    """Test case for analyze_get

    Test api response without api key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/Analyze',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyze_post(client):
    """Test case for analyze_post

    Sentiment analysis service
    """
    request_doc = {"Secret":"Secret","IsTwitterContent":True,"DocumentText":"DocumentText","PrivateKey":"PrivateKey","DocumentLanguage":"DocumentLanguage","UserCategoryModelName":"UserCategoryModelName","RequestIdentifier":"RequestIdentifier","SerializeFormat":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/Analyze',
        headers=headers,
        json=request_doc,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

