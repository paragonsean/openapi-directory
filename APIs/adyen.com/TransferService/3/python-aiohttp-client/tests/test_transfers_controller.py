# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.return_transfer_request import ReturnTransferRequest
from openapi_server.models.return_transfer_response import ReturnTransferResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.transfer import Transfer
from openapi_server.models.transfer_info import TransferInfo


pytestmark = pytest.mark.asyncio

async def test_post_transfers(client):
    """Test case for post_transfers

    Transfer funds
    """
    body = {"balanceAccountId":"balanceAccountId","reference":"reference","amount":{"currency":"currency","value":0},"referenceForBeneficiary":"referenceForBeneficiary","counterparty":{"balanceAccountId":"balanceAccountId","bankAccount":{"accountHolder":{"reference":"reference","firstName":"firstName","lastName":"lastName","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","line2":"line2","line1":"line1"},"fullName":"fullName","dateOfBirth":"2000-01-23","type":"unknown"},"accountIdentification":{"bsbCode":"bsbCode","accountNumber":"accountNumber","type":"auLocal"}},"transferInstrumentId":"transferInstrumentId"},"description":"description","paymentInstrumentId":"paymentInstrumentId","category":"bank","priority":"crossBorder","ultimateParty":{"reference":"reference","firstName":"firstName","lastName":"lastName","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","line2":"line2","line1":"line1"},"fullName":"fullName","dateOfBirth":"2000-01-23","type":"unknown"}}
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
        path='/btl/v3/transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transfers_transfer_id_returns(client):
    """Test case for post_transfers_transfer_id_returns

    Return a transfer
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'clientKey': 'special-key',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/btl/v3/transfers/{transfer_id}/returns'.format(transfer_id='transfer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

