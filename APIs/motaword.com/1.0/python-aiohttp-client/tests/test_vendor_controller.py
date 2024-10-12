# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_vendors_filter import AvailableVendorsFilter
from openapi_server.models.user_list import UserList


pytestmark = pytest.mark.asyncio

async def test_get_available_vendors(client):
    """Test case for get_available_vendors

    Get a list of vendors available for the criteria given
    """
    body = {"targetLanguages":["targetLanguages","targetLanguages"],"types":["translator","translator"],"manualWorkPermission":True,"sourceLanguage":"sourceLanguage","corporateId":0.8008281904610115}
    params = [('with[]', ['_with_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/available-vendors',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

