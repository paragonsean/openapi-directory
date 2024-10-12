# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_item_resource import BusinessItemResource


pytestmark = pytest.mark.asyncio

async def test_get_business_item_by_id(client):
    """Test case for get_business_item_by_id

    Returns business item by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/BusinessItem/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

