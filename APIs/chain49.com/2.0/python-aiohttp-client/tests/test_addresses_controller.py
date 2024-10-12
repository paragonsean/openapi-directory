# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_balance_history_v2200_response_inner import GetBalanceHistoryV2200ResponseInner
from openapi_server.models.get_xpub_v2200_response import GetXpubV2200Response


pytestmark = pytest.mark.asyncio

async def test_get_address_v2(client):
    """Test case for get_address_v2

    Get address V2
    """
    params = [('page', 1),
                    ('pageSize', 1000),
                    ('fromBlock', 10),
                    ('toBlock', 100),
                    ('details', txids),
                    ('contract', '0xdAC17F958D2ee523a2206206994597C13D831ec7'),
                    ('secondary', 'usd')]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/address/{address}'.format(blockchain='bitcoin', address='321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_balance_history_v2(client):
    """Test case for get_balance_history_v2

    Get Balance History V2
    """
    params = [('fromDate', '1578391200'),
                    ('toDate', '1599053802'),
                    ('fiatcurrency', 'usd'),
                    ('groupBy', 3600)]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/balancehistory/{address_or_xpub}'.format(blockchain='bitcoin', address_or_xpub='321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_utxov2(client):
    """Test case for get_utxov2

    Get UTXO V2
    """
    params = [('confirmed', true)]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/utxo/{address_or_xpub}'.format(blockchain='bitcoin', address_or_xpub='321x69Cb9HZLWwAWGiUBT1U81r1zPLnEjL'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_xpub_v2(client):
    """Test case for get_xpub_v2

    Get xpub V2
    """
    params = [('page', 1),
                    ('pageSize', 1000),
                    ('fromBlock', 10),
                    ('toBlock', 100),
                    ('details', txids),
                    ('tokens', nonzero),
                    ('secondary', 'usd')]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/xpub/{xpub}'.format(blockchain='bitcoin', xpub='tpubDC88gkaZi5HvJGxGDNLADkvtdpni3mLmx6vr2KnXmWMG8zfkBRggsxHVBkUpgcwPe2KKpkyvTJCdXHb1UHEWE64vczyyPQfHr1skBcsRedN'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

