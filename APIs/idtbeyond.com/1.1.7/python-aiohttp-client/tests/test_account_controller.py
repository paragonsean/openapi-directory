# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_iatu_balance_get(client):
    """Test case for iatu_balance_get

    Account balance
    """
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/balance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

