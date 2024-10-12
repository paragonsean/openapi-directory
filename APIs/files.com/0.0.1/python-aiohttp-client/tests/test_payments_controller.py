# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_line_item_entity import AccountLineItemEntity


pytestmark = pytest.mark.asyncio

async def test_get_payments(client):
    """Test case for get_payments

    List Payments
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_id(client):
    """Test case for get_payments_id

    Show Payment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/payments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

