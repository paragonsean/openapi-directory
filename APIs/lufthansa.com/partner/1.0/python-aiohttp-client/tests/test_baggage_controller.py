# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_baggage_trip_and_contact(client):
    """Test case for baggage_trip_and_contact

    Baggage Trip and Contact
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/baggage/baggagetripandcontact/{search_id}'.format(search_id='search_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

