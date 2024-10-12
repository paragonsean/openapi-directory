# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.merchant_name_add_payload import MerchantNameAddPayload
from openapi_server.models.receipt_feedback_add_payload import ReceiptFeedbackAddPayload
from openapi_server.models.result import Result


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_account_v1_feedback(client):
    """Test case for post_api_account_v1_feedback

    Add manually verified receipt data to a given receipt for feedback and training purposes
    """
    body = openapi_server.ReceiptFeedbackAddPayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/account/v1/feedback',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_account_v1_merchantname_add(client):
    """Test case for post_api_account_v1_merchantname_add

    Add a keyword to your account's model to predict merchant name. Changes in your account's model are updated daily.
    """
    body = openapi_server.MerchantNameAddPayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/account/v1/merchantname/add',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

