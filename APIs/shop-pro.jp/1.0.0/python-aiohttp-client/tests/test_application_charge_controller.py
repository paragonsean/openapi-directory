# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_usage_charge201_response import CreateUsageCharge201Response
from openapi_server.models.create_usage_charge_request import CreateUsageChargeRequest
from openapi_server.models.post_application_charge201_response import PostApplicationCharge201Response
from openapi_server.models.post_application_charge_request import PostApplicationChargeRequest


pytestmark = pytest.mark.asyncio

async def test_create_usage_charge(client):
    """Test case for create_usage_charge

    従量課金データの作成
    """
    body = openapi_server.CreateUsageChargeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_appstore_usage_charge_token': 'x_appstore_usage_charge_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/appstore/v1/recurring_application_charges/{recurring_application_charge_id}/usage_charges.json'.format(recurring_application_charge_id='recurring_application_charge_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_application_charge(client):
    """Test case for post_application_charge

    アプリ内課金データの作成
    """
    body = openapi_server.PostApplicationChargeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/appstore/v1/application_charges.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

