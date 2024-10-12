# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quittung_tse200_response import QuittungTSE200Response


pytestmark = pytest.mark.asyncio

async def test_quittung_ts_esignature_0(client):
    """Test case for quittung_ts_esignature_0

    Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).
    """
    params = [('account', 'account_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2.0/quittung/tsesignature',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quittung_tse_0(client):
    """Test case for quittung_tse_0

    Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).
    """
    params = [('account', 'account_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/quittung/tse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quittung_tse_data_0(client):
    """Test case for quittung_tse_data_0

    Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).
    """
    params = [('account', 'account_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2.0/quittung/tsedata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quittung_zugferd_0(client):
    """Test case for quittung_zugferd_0

    Retrieve Zugferd XML for a given receipt (Strom-Quittung).
    """
    params = [('account', 'account_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2.0/quittung/zugferd',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

