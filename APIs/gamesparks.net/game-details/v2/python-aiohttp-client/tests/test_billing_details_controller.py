# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_details_model import BillingDetailsModel
from openapi_server.models.message_model import MessageModel


pytestmark = pytest.mark.asyncio

async def test_get_billing_details(client):
    """Test case for get_billing_details

    Retrieves the Billing Details
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/billingDetails'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_billing_details(client):
    """Test case for put_billing_details

    Updates the Billing Details
    """
    body = {"country":"country","firstName1":"firstName1","city":"city","firstName2":"firstName2","companyName":"companyName","postcode":"postcode","taxNumber":"taxNumber","firstName3":"firstName3","building":"building","email3":"email3","email2":"email2","email1":"email1","street":"street","lastName1":"lastName1","lastName2":"lastName2","lastName3":"lastName3","state":"state"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/restv2/game/{api_key}/admin/billingDetails'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

