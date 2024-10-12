# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_refund_in import CreateRefundIn
from openapi_server.models.create_refund_out import CreateRefundOut
from openapi_server.models.list_refunds_out import ListRefundsOut


pytestmark = pytest.mark.asyncio

async def test_create_refund(client):
    """Test case for create_refund

    Create a refund
    """
    input = openapi_server.CreateRefundIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{key}/refunds'.format(key='key_example'),
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_refunds(client):
    """Test case for list_refunds

    Get transaction refunds
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transactions/{key}/refunds'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

