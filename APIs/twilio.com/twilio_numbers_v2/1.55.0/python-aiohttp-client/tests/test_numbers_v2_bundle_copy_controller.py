# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_bundle_copy_response import ListBundleCopyResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle_bundle_copy import NumbersV2RegulatoryComplianceBundleBundleCopy


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_bundle_copy(client):
    """Test case for create_bundle_copy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies'.format(bundle_sid='bundle_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bundle_copy(client):
    """Test case for list_bundle_copy

    
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
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies'.format(bundle_sid='bundle_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

