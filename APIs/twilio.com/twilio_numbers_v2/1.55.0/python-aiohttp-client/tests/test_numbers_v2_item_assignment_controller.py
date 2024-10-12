# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_item_assignment_response import ListItemAssignmentResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle_item_assignment import NumbersV2RegulatoryComplianceBundleItemAssignment


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_item_assignment(client):
    """Test case for create_item_assignment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'object_sid': 'object_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments'.format(bundle_sid='bundle_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_item_assignment(client):
    """Test case for delete_item_assignment

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}'.format(bundle_sid='bundle_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_item_assignment(client):
    """Test case for fetch_item_assignment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}'.format(bundle_sid='bundle_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_item_assignment(client):
    """Test case for list_item_assignment

    
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
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments'.format(bundle_sid='bundle_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

