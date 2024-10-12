# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.log_get200_response import LogGet200Response
from openapi_server.models.log_pk_get200_response import LogPkGet200Response
from openapi_server.models.log_post201_response import LogPost201Response
from openapi_server.models.log_rest_api_post import LogRestApiPost


pytestmark = pytest.mark.asyncio

async def test_log_get(client):
    """Test case for log_get

    
    """
    params = [('q', openapi_server.GetListSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/log/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_pk_get(client):
    """Test case for log_pk_get

    
    """
    params = [('q', openapi_server.GetItemSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/log/{pk}'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_post(client):
    """Test case for log_post

    
    """
    body = openapi_server.LogRestApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/log/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

