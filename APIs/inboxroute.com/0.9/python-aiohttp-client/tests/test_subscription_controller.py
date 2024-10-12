# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contacts_get401_response_inner import ContactsGet401ResponseInner
from openapi_server.models.contacts_get404_response_inner import ContactsGet404ResponseInner
from openapi_server.models.contacts_get422_response_inner import ContactsGet422ResponseInner
from openapi_server.models.subscription_request import SubscriptionRequest


pytestmark = pytest.mark.asyncio

async def test_subscription_listid_post(client):
    """Test case for subscription_listid_post

    
    """
    subscription = {"ip":"ip","singleoptin":True,"fullname":"fullname","lang":"lang","confirmed":"2000-01-23T04:56:07.000+00:00","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/subscription/{listid}'.format(listid='listid_example'),
        headers=headers,
        json=subscription,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

