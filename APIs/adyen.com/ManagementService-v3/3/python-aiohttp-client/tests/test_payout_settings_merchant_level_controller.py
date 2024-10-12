# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payout_settings import PayoutSettings
from openapi_server.models.payout_settings_request import PayoutSettingsRequest
from openapi_server.models.payout_settings_response import PayoutSettingsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_payout_settings_request import UpdatePayoutSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_delete_merchants_merchant_id_payout_settings_payout_settings_id(client):
    """Test case for delete_merchants_merchant_id_payout_settings_payout_settings_id

    Delete a payout setting
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/merchants/{merchant_id}/payoutSettings/{payout_settings_id}'.format(merchant_id='merchant_id_example', payout_settings_id='payout_settings_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_payout_settings(client):
    """Test case for get_merchants_merchant_id_payout_settings

    Get a list of payout settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/payoutSettings'.format(merchant_id='merchant_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_payout_settings_payout_settings_id(client):
    """Test case for get_merchants_merchant_id_payout_settings_payout_settings_id

    Get a payout setting
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/payoutSettings/{payout_settings_id}'.format(merchant_id='merchant_id_example', payout_settings_id='payout_settings_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_payout_settings_payout_settings_id(client):
    """Test case for patch_merchants_merchant_id_payout_settings_payout_settings_id

    Update a payout setting
    """
    body = {"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/payoutSettings/{payout_settings_id}'.format(merchant_id='merchant_id_example', payout_settings_id='payout_settings_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_payout_settings(client):
    """Test case for post_merchants_merchant_id_payout_settings

    Add a payout setting
    """
    body = {"transferInstrumentId":"transferInstrumentId","enabled":True,"enabledFromDate":"enabledFromDate"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/payoutSettings'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

