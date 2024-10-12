# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.createorchangestoreconfiguration_request1 import CreateorchangestoreconfigurationRequest1
from openapi_server.models.savestoreconfig1 import Savestoreconfig1
from openapi_server.models.storeconfig1 import Storeconfig1


pytestmark = pytest.mark.asyncio

async def test_createorchangestoreconfiguration(client):
    """Test case for createorchangestoreconfiguration

    Create or change store configuration
    """
    body = {"automaticCheckingAccountCreationEnabled":false,"dailyInterestRate":"number(percent 0.1=10%) (float)","defaultCreditValue":"number (decimal)","invoicePostponementLimit":"number (int)","maxPostponementDays":"number (int","maxPreAuthorizationGrowthRate":"number (percent 0.1=10%) (float)","myCreditsEnabled":false,"postponementEnabled":false,"taxRate":"number(percent 0.1=10%) (float)","toleranceEnabled":false}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/storeconfig',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrievestoreconfiguration(client):
    """Test case for retrievestoreconfiguration

    Retrieve store configuration
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/creditcontrol/storeconfig',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

