# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_instrument import PaymentInstrument
from openapi_server.models.payment_instrument_info import PaymentInstrumentInfo
from openapi_server.models.payment_instrument_reveal_info import PaymentInstrumentRevealInfo
from openapi_server.models.payment_instrument_update_request import PaymentInstrumentUpdateRequest
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction_rules_response import TransactionRulesResponse
from openapi_server.models.update_payment_instrument import UpdatePaymentInstrument


pytestmark = pytest.mark.asyncio

async def test_get_payment_instruments_id(client):
    """Test case for get_payment_instruments_id

    Get a payment instrument
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/paymentInstruments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_instruments_id_reveal(client):
    """Test case for get_payment_instruments_id_reveal

    Get the PAN of a payment instrument
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/paymentInstruments/{id}/reveal'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_instruments_id_transaction_rules(client):
    """Test case for get_payment_instruments_id_transaction_rules

    Get all transaction rules for a payment instrument
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/paymentInstruments/{id}/transactionRules'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_payment_instruments_id(client):
    """Test case for patch_payment_instruments_id

    Update a payment instrument
    """
    body = {"balanceAccountId":"balanceAccountId","statusComment":"statusComment","card":{"brandVariant":"brandVariant","configuration":{"cardImageId":"cardImageId","logoImageId":"logoImageId","configurationProfileId":"configurationProfileId","insert":"insert","language":"language","bulkAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode","mobile":"mobile","company":"company","email":"email"},"carrierImageId":"carrierImageId","shipmentMethod":"shipmentMethod","carrier":"carrier","envelope":"envelope","currency":"currency","activation":"activation","activationUrl":"activationUrl","pinMailer":"pinMailer"},"formFactor":"physical","cardholderName":"cardholderName","deliveryContact":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"webAddress":"webAddress","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName"},"email":"email"},"brand":"brand","authentication":{"password":"password","phone":{"number":"number","type":"Landline"},"email":"email"}},"status":"Active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bcl/v1/paymentInstruments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_instruments(client):
    """Test case for post_payment_instruments

    Create a payment instrument
    """
    body = {"balanceAccountId":"balanceAccountId","reference":"reference","description":"description","type":"bankAccount","issuingCountryCode":"issuingCountryCode","paymentInstrumentGroupId":"paymentInstrumentGroupId","card":{"brandVariant":"brandVariant","configuration":{"cardImageId":"cardImageId","logoImageId":"logoImageId","configurationProfileId":"configurationProfileId","insert":"insert","language":"language","bulkAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode","mobile":"mobile","company":"company","email":"email"},"carrierImageId":"carrierImageId","shipmentMethod":"shipmentMethod","carrier":"carrier","envelope":"envelope","currency":"currency","activation":"activation","activationUrl":"activationUrl","pinMailer":"pinMailer"},"formFactor":"physical","cardholderName":"cardholderName","deliveryContact":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phoneNumber":{"phoneType":"Fax","phoneNumber":"phoneNumber","phoneCountryCode":"phoneCountryCode"},"webAddress":"webAddress","personalData":{"nationality":"nationality","dateOfBirth":"dateOfBirth","idNumber":"idNumber"},"fullPhoneNumber":"fullPhoneNumber","name":{"firstName":"firstName","lastName":"lastName"},"email":"email"},"brand":"brand","authentication":{"password":"password","phone":{"number":"number","type":"Landline"},"email":"email"}},"status":"Active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/paymentInstruments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

