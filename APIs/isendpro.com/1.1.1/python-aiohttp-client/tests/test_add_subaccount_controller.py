# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.subaccount_add_request import SubaccountAddRequest
from openapi_server.models.subaccount_add_response import SubaccountAddResponse


pytestmark = pytest.mark.asyncio

async def test_subaccount_add(client):
    """Test case for subaccount_add

    Ajoute un sous compte
    """
    body = {"subAccountPassword":"subAccountPassword","keyid":"keyid","subAccountLogin":"subAccountLogin","subAccountEdit":"addAccount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/subaccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

