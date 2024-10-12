# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_supporting_document_response import ListSupportingDocumentResponse
from openapi_server.models.numbers_v2_regulatory_compliance_supporting_document import NumbersV2RegulatoryComplianceSupportingDocument


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_supporting_document(client):
    """Test case for create_supporting_document

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': None,
        'friendly_name': 'friendly_name_example',
        'type': 'type_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/SupportingDocuments',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_supporting_document(client):
    """Test case for delete_supporting_document

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/RegulatoryCompliance/SupportingDocuments/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_supporting_document(client):
    """Test case for fetch_supporting_document

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/SupportingDocuments/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_supporting_document(client):
    """Test case for list_supporting_document

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/SupportingDocuments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_supporting_document(client):
    """Test case for update_supporting_document

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': None,
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/SupportingDocuments/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

