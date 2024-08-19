# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_entity import RequestEntity
from openapi_server.models.request_entity_relation import RequestEntityRelation


pytestmark = pytest.mark.asyncio

async def test_create_request_entity(client):
    """Test case for create_request_entity

    POST for request
    """
    body = {"path":"contact/111/comments?count=1","method":"GET","header":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
    }
    response = await client.request(
        method='POST',
        path='/v1/application/request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

