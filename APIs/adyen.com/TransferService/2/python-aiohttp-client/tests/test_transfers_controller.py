# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.service_error import ServiceError
from openapi_server.models.transfer import Transfer
from openapi_server.models.transfer_info import TransferInfo


pytestmark = pytest.mark.asyncio

async def test_post_transfers(client):
    """Test case for post_transfers

    Transfer funds
    """
    body = {"balanceAccountId":"balanceAccountId","reference":"reference","amount":{"currency":"currency","value":0},"bank":{"priority":"crossBorder"},"referenceForBeneficiary":"referenceForBeneficiary","counterparty":{"balanceAccountId":"balanceAccountId","bankAccount":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"ownerName":{"firstName":"firstName","lastName":"lastName","fullName":"fullName","infix":"infix"},"iban":"iban"},"transferInstrumentId":"transferInstrumentId"},"description":"description","paymentInstrumentId":"paymentInstrumentId"}
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
        path='/btl/v2/transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

