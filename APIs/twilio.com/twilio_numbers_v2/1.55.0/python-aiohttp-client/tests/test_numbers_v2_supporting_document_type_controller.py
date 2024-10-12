# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_supporting_document_type_response import ListSupportingDocumentTypeResponse
from openapi_server.models.numbers_v2_regulatory_compliance_supporting_document_type import NumbersV2RegulatoryComplianceSupportingDocumentType


pytestmark = pytest.mark.asyncio

async def test_fetch_supporting_document_type(client):
    """Test case for fetch_supporting_document_type

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/SupportingDocumentTypes/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_supporting_document_type(client):
    """Test case for list_supporting_document_type

    
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
        path='/v2/RegulatoryCompliance/SupportingDocumentTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

