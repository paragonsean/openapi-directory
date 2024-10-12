# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_category_list import DocumentCategoryList
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_list_document_categories(client):
    """Test case for list_document_categories

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/document_categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

