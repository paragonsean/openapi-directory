# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_platform import BalancePlatform
from openapi_server.models.paginated_account_holders_response import PaginatedAccountHoldersResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_get_balance_platforms_id(client):
    """Test case for get_balance_platforms_id

    Get a balance platform
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/balancePlatforms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_balance_platforms_id_account_holders(client):
    """Test case for get_balance_platforms_id_account_holders

    Get all account holders under a balance platform
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/balancePlatforms/{id}/accountHolders'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

