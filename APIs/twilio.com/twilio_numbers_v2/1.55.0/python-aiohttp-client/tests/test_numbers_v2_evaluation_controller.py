# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_evaluation_response import ListEvaluationResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle_evaluation import NumbersV2RegulatoryComplianceBundleEvaluation


pytestmark = pytest.mark.asyncio

async def test_create_evaluation(client):
    """Test case for create_evaluation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations'.format(bundle_sid='bundle_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_evaluation(client):
    """Test case for fetch_evaluation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}'.format(bundle_sid='bundle_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_evaluation(client):
    """Test case for list_evaluation

    
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
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations'.format(bundle_sid='bundle_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

