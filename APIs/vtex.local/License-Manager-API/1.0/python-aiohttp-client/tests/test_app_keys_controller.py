# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.createnewappkey_request import CreatenewappkeyRequest
from openapi_server.models.createnewappkey_response import CreatenewappkeyResponse
from openapi_server.models.getappkeysfromaccount import Getappkeysfromaccount
from openapi_server.models.updateappkey_request import UpdateappkeyRequest
from openapi_server.models.vlm_error import VLMError


pytestmark = pytest.mark.asyncio

async def test_createnewappkey(client):
    """Test case for createnewappkey

    Create new appkey
    """
    body = {"label":"label"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/vlm/appkeys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getappkeysfromaccount(client):
    """Test case for getappkeysfromaccount

    Get appKeys from account
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/vlm/appkeys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updateappkey(client):
    """Test case for updateappkey

    Update appkey
    """
    body = {"isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/vlm/appkeys/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

