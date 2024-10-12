# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_list_result import PeeringListResult


pytestmark = pytest.mark.asyncio

async def test_legacy_peerings_list(client):
    """Test case for legacy_peerings_list

    
    """
    params = [('peeringLocation', 'peering_location_example'),
                    ('kind', 'kind_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Peering/legacyPeerings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

