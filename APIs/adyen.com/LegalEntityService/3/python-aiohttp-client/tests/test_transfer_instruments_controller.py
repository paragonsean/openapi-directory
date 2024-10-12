# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.transfer_instrument import TransferInstrument
from openapi_server.models.transfer_instrument_info import TransferInstrumentInfo


pytestmark = pytest.mark.asyncio

async def test_delete_transfer_instruments_id(client):
    """Test case for delete_transfer_instruments_id

    Delete a transfer instrument
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/lem/v3/transferInstruments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transfer_instruments_id(client):
    """Test case for get_transfer_instruments_id

    Get a transfer instrument
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v3/transferInstruments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_transfer_instruments_id(client):
    """Test case for patch_transfer_instruments_id

    Update a transfer instrument
    """
    body = {"bankAccount":{"accountIdentification":{"formFactor":"physical","bsbCode":"bsbCode","accountNumber":"accountNumber","type":"auLocal"},"countryCode":"countryCode","accountType":"accountType","trustedSource":True,"bankName":"bankName"},"legalEntityId":"legalEntityId","type":"bankAccount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_requested_verification_code': '1',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/lem/v3/transferInstruments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transfer_instruments(client):
    """Test case for post_transfer_instruments

    Create a transfer instrument
    """
    body = {"bankAccount":{"accountIdentification":{"formFactor":"physical","bsbCode":"bsbCode","accountNumber":"accountNumber","type":"auLocal"},"countryCode":"countryCode","accountType":"accountType","trustedSource":True,"bankName":"bankName"},"legalEntityId":"legalEntityId","type":"bankAccount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_requested_verification_code': '17002',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v3/transferInstruments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

