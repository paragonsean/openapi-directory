# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.currency_history_dto import CurrencyHistoryDTO


pytestmark = pytest.mark.asyncio

async def test_create_exchange_rate(client):
    """Test case for create_exchange_rate

    Adding currency exchange rates.
    """
    body = {"exchangeRate":"exchangeRate","originDetails":"originDetails","lastModification":{"value":6},"dateFrom":{"value":6},"publicationDate":{"value":6}}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/dictionaries/currency/{iso_code}/exchangeRate'.format(iso_code='iso_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_iso_code(client):
    """Test case for get_by_iso_code

    Returns currency exchange rates.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/dictionaries/currency/{iso_code}/exchangeRate'.format(iso_code='iso_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

