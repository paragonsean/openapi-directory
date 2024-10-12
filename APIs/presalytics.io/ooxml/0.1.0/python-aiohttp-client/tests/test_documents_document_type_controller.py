# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_type import DocumentType
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_documents_documenttype_get(client):
    """Test case for documents_documenttype_get

    DocumentType: List All Possible Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Documents/DocumentType',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_documenttype_get_id(client):
    """Test case for documents_documenttype_get_id

    DocumentType: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Documents/DocumentType/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_documenttype_typeid_get_type_id(client):
    """Test case for documents_documenttype_typeid_get_type_id

    DocumentType: Get By Type Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Documents/DocumentType/TypeId/{type_id}'.format(type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

