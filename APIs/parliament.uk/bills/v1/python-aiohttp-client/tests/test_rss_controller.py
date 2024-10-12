# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_api_v1_rss_allbills_rss_get(client):
    """Test case for api_v1_rss_allbills_rss_get

    Returns an Rss feed of all Bills.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Rss/allbills.rss',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_rss_bills_id_rss_get(client):
    """Test case for api_v1_rss_bills_id_rss_get

    Returns an Rss feed of a certain Bill.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Rss/Bills/{id_rs}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_rss_privatebills_rss_get(client):
    """Test case for api_v1_rss_privatebills_rss_get

    Returns an Rss feed of private Bills.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Rss/privatebills.rss',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_rss_publicbills_rss_get(client):
    """Test case for api_v1_rss_publicbills_rss_get

    Returns an Rss feed of public Bills.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Rss/publicbills.rss',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

