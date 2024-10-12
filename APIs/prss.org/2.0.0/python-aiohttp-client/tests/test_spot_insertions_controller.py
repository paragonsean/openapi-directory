# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.spot_insertion import SpotInsertion


pytestmark = pytest.mark.asyncio

async def test_api_v2_spotinsertions_get(client):
    """Test case for api_v2_spotinsertions_get

    Returns the spot insertions matching the query parameters.
    """
    params = [('pageStart', 0),
                    ('pageSize', 500),
                    ('orderById', 'order_by_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spotinsertions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_spotinsertions_id_delete(client):
    """Test case for api_v2_spotinsertions_id_delete

    Deletes the spot insertion with the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/spotinsertions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_spotinsertions_id_get(client):
    """Test case for api_v2_spotinsertions_id_get

    Returns the spot insertion matching the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spotinsertions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_spotinsertions_post(client):
    """Test case for api_v2_spotinsertions_post

    Creates a new spot insertion.
    """
    body = {"duration":1,"cue":"S:000_SPOT","createdDate":"2000-01-23T04:56:07.000+00:00","endDate":"2020-01-31","customerId":0,"spots":[2,2],"id":0,"programId":0,"startDate":"2020-01-31","broadcastServiceId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/spotinsertions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

