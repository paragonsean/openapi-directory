# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.capital_grant import CapitalGrant
from openapi_server.models.capital_grant_info import CapitalGrantInfo
from openapi_server.models.capital_grants import CapitalGrants
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_get_grants(client):
    """Test case for get_grants

    Get a capital account
    """
    params = [('counterpartyAccountHolderId', 'counterparty_account_holder_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'clientKey': 'special-key',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/btl/v3/grants',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_grants_id(client):
    """Test case for get_grants_id

    Get grant reference details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'clientKey': 'special-key',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/btl/v3/grants/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_grants(client):
    """Test case for post_grants

    Request a grant payout
    """
    body = {"grantAccountId":"grantAccountId","grantOfferId":"grantOfferId","counterparty":{"balanceAccountId":"balanceAccountId","accountHolderId":"accountHolderId","transferInstrumentId":"transferInstrumentId"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'clientKey': 'special-key',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/btl/v3/grants',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

