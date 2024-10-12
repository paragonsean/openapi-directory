# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.series_membership_resource_collection import SeriesMembershipResourceCollection


pytestmark = pytest.mark.asyncio

async def test_get_series_memberships(client):
    """Test case for get_series_memberships

    Returns all series memberships.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/SeriesMembership',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

