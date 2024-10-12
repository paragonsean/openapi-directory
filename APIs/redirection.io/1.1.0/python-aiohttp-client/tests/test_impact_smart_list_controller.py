# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.impact_smart_list_read import ImpactSmartListRead
from openapi_server.models.impact_smart_list_write import ImpactSmartListWrite


pytestmark = pytest.mark.asyncio

async def test_get_impact_smart_list_item(client):
    """Test case for get_impact_smart_list_item

    Retrieves a ImpactSmartList resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/impact-smart-lists/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_impact_smart_list_collection(client):
    """Test case for post_impact_smart_list_collection

    Creates a ImpactSmartList resource.
    """
    impact_smart_list = openapi_server.ImpactSmartListWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/impact-smart-lists',
        headers=headers,
        json=impact_smart_list,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

