# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_stream_source200_response import CreateStreamSource200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.stream_source_create_input import StreamSourceCreateInput
from openapi_server.models.stream_source_update_input import StreamSourceUpdateInput
from openapi_server.models.stream_sources import StreamSources


pytestmark = pytest.mark.asyncio

async def test_add_stream_source(client):
    """Test case for add_stream_source

    Deprecated operation
    """
    stream_source = openapi_server.StreamSourceCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/stream_sources/add',
        headers=headers,
        json=stream_source,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_stream_source(client):
    """Test case for create_stream_source

    Add a stream source
    """
    stream_source = openapi_server.StreamSourceCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/stream_sources',
        headers=headers,
        json=stream_source,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_stream_source(client):
    """Test case for delete_stream_source

    Delete a stream source
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/stream_sources/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_stream_sources(client):
    """Test case for list_stream_sources

    Fetch all stream sources
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_sources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_stream_source(client):
    """Test case for show_stream_source

    Fetch a stream source
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_sources/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_stream_source(client):
    """Test case for update_stream_source

    Update a stream source
    """
    stream_source = openapi_server.StreamSourceUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/stream_sources/{id}'.format(id='id_example'),
        headers=headers,
        json=stream_source,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

