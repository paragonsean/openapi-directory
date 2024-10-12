# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quittung_comit_request import QuittungComitRequest
from openapi_server.models.quittung_create_request import QuittungCreateRequest
from openapi_server.models.quittung_tse200_response import QuittungTSE200Response


pytestmark = pytest.mark.asyncio

async def test_quittung_comit(client):
    """Test case for quittung_comit

    Finishs a collection of data and finalizes receipt. Use this method after collecting all data via quittung/prepare
    """
    body = openapi_server.QuittungComitRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/quittung/commit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quittung_create(client):
    """Test case for quittung_create

    Create a receipt for an energy delivery (only valid in Germany).
    """
    body = openapi_server.QuittungCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/quittung/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quittung_prepare(client):
    """Test case for quittung_prepare

    Allows to collect data with several requests (or a single) for a receipt.
    """
    body = openapi_server.QuittungComitRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2.0/quittung/prepare',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quittung_ts_esignature(client):
    """Test case for quittung_ts_esignature

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

async def test_quittung_tse(client):
    """Test case for quittung_tse

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

async def test_quittung_tse_data(client):
    """Test case for quittung_tse_data

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

async def test_quittung_zugferd(client):
    """Test case for quittung_zugferd

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

