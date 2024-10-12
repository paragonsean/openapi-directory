# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gsi_dispatch200_response import GsiDispatch200Response
from openapi_server.models.gsi_marketdata200_response import GsiMarketdata200Response
from openapi_server.models.gsi_prediction200_response import GsiPrediction200Response


pytestmark = pytest.mark.asyncio

async def test_gsi_besthour(client):
    """Test case for gsi_besthour

    Get best hour (with most regional green energy) in a given timeframe.
    """
    params = [('zip', 'zip_example'),
                    ('key', 'key_example'),
                    ('timeframe', 56),
                    ('hours', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/gsi/bestHour',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gsi_dispatch(client):
    """Test case for gsi_dispatch

    Dispatch (Green Energy Distribution Schedule)
    """
    params = [('zip', 'zip_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/gsi/dispatch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gsi_marketdata(client):
    """Test case for gsi_marketdata

    Marketdata
    """
    params = [('zip', 'zip_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/gsi/marketdata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gsi_prediction(client):
    """Test case for gsi_prediction

    Prediction
    """
    params = [('zip', 'zip_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/gsi/prediction',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

