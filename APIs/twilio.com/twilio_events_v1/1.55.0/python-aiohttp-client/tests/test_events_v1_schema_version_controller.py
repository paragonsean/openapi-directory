# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.events_v1_schema_schema_version import EventsV1SchemaSchemaVersion
from openapi_server.models.list_schema_version_response import ListSchemaVersionResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_schema_version(client):
    """Test case for fetch_schema_version

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Schemas/{id}/Versions/{schema_version}'.format(id='id_example', schema_version=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_schema_version(client):
    """Test case for list_schema_version

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Schemas/{id}/Versions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

