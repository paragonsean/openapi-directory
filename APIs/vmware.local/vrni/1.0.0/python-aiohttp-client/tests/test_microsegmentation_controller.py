# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.recommended_rules import RecommendedRules
from openapi_server.models.recommended_rules_request import RecommendedRulesRequest


pytestmark = pytest.mark.asyncio

async def test_export_nsx_recommended_rules(client):
    """Test case for export_nsx_recommended_rules

    Export recommended rules for NSX-V
    """
    body = {"group_1":{"entity":{"entity_id":"10000:562:1904698621","entity_type":"Tier"}},"group_2":{"entity":{"entity_id":"10000:562:1780351215","entity_type":"Tier"}}}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/micro-seg/recommended-rules/nsx',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_recommended_rules(client):
    """Test case for list_recommended_rules

    Get logical recommended rules
    """
    body = {"group_1":{"entity":{"entity_id":"10000:562:1904698621","entity_type":"Tier"}},"group_2":{"entity":{"entity_id":"10000:562:1780351215","entity_type":"Tier"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/micro-seg/recommended-rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

