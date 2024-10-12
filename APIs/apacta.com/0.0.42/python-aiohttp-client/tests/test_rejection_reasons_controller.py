# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.overview_rejection_reasons_get200_response import OverviewRejectionReasonsGet200Response


pytestmark = pytest.mark.asyncio

async def test_overview_rejection_reasons_get(client):
    """Test case for overview_rejection_reasons_get

    Get a statistics data for rejection reasons
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/overview/rejection_reasons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

