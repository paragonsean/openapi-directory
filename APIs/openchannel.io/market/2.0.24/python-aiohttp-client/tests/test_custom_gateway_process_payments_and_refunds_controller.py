# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transaction import Transaction


pytestmark = pytest.mark.asyncio

async def test_custom_gateway_payment_ownership_id_post(client):
    """Test case for custom_gateway_payment_ownership_id_post

    Adds a payment for an app on behalf of a user
    """
    params = [('amount', 56),
                    ('date', 56),
                    ('feeAmount', 56),
                    ('marketplaceAmount', 56),
                    ('developerAmount', 56),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/custom-gateway/payment/{ownership_id}'.format(ownership_id='ownership_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_gateway_refund_ownership_id_post(client):
    """Test case for custom_gateway_refund_ownership_id_post

    Fully or partially refund payment for an app on behalf of a user
    """
    params = [('amount', 56),
                    ('date', 56),
                    ('feeAmount', 56),
                    ('marketplaceAmount', 56),
                    ('developerAmount', 56),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/custom-gateway/refund/{ownership_id}'.format(ownership_id='ownership_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

