# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.exude_response_bean import ExudeResponseBean


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_filter_file_data_stoppings(client):
    """Test case for filter_file_data_stoppings

    Filter the stopping words from the provided input file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/exude/{type}/file'.format(type='type_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_filter_stoppings(client):
    """Test case for filter_stoppings

    Filter the stopping words from the provided input data or links
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('data', 'data_example')
    data.add_field('links', ['links_example'])
    response = await client.request(
        method='POST',
        path='/exude/{type}/data'.format(type='stopping'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

