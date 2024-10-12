# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.marketplaces_list_result import MarketplacesListResult


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list(client):
    """Test case for marketplaces_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Consumption/marketplaces'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

