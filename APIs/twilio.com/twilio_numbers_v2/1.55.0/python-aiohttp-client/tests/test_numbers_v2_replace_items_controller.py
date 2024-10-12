# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.numbers_v2_regulatory_compliance_bundle_replace_items import NumbersV2RegulatoryComplianceBundleReplaceItems


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_replace_items(client):
    """Test case for create_replace_items

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'from_bundle_sid': 'from_bundle_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems'.format(bundle_sid='bundle_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

