# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.service_error import ServiceError
from openapi_server.models.transfer_info_old import TransferInfoOld
from openapi_server.models.transfer_old import TransferOld


pytestmark = pytest.mark.asyncio

async def test_post_transfers(client):
    """Test case for post_transfers

    Transfer funds
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0},"destination":{"balanceAccountId":"balanceAccountId","paymentInstrumentId":"paymentInstrumentId"},"description":"description","source":{"balanceAccountId":"balanceAccountId","paymentInstrumentId":"paymentInstrumentId"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'www_authenticate': 'SCA realm=\"Transfer\" auth-param1=\"eyJjaGFsbGVuZ2UiOiJiVlV6ZW5wek0waFNl...\"',
        'Authorization': 'BasicZm9vOmJhcg==',
        'clientKey': 'special-key',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/btl/v1/transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

