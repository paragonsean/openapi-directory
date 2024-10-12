# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_jsontoxml_post(client):
    """Test case for jsontoxml_post

    
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/transform/1.0.0/jsontoxml',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_xmltojson_post(client):
    """Test case for xmltojson_post

    
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'text/xml',
    }
    response = await client.request(
        method='POST',
        path='/transform/1.0.0/xmltojson',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

