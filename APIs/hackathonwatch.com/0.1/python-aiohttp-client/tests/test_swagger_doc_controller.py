# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_g_et_swagger_doc_format(client):
    """Test case for g_et_swagger_doc_format

    Swagger compatible API description
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/swagger_doc.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_swagger_doc_name_format(client):
    """Test case for g_et_swagger_doc_name_format

    Swagger compatible API description for specific API
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/swagger_doc/{name_jso}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

