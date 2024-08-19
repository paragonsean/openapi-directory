# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.store_detail_and_submit_request import StoreDetailAndSubmitRequest
from openapi_server.models.store_detail_and_submit_response import StoreDetailAndSubmitResponse
from openapi_server.models.store_detail_request import StoreDetailRequest
from openapi_server.models.store_detail_response import StoreDetailResponse
from openapi_server.models.submit_request import SubmitRequest
from openapi_server.models.submit_response import SubmitResponse


pytestmark = pytest.mark.asyncio

async def test_post_store_detail(client):
    """Test case for post_store_detail

    Store payout details
    """
    body = {"fraudOffset":0,"entityType":"NaturalPerson","recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"socialSecurityNumber":"socialSecurityNumber","dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","bank":{"ownerName":"ownerName","countryCode":"countryCode","taxId":"taxId","iban":"iban","bankAccountNumber":"bankAccountNumber","bankName":"bankName","bankLocationId":"bankLocationId","bic":"bic","bankCity":"bankCity"},"shopperName":{"firstName":"firstName","lastName":"lastName"},"merchantAccount":"merchantAccount","nationality":"nationality","additionalData":{"key":"additionalData"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"selectedBrand":"selectedBrand","card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"},"shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payout/v40/storeDetail',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_store_detail_and_submit_third_party(client):
    """Test case for post_store_detail_and_submit_third_party

    Store details and submit a payout
    """
    body = {"fraudOffset":0,"amount":{"currency":"currency","value":0},"entityType":"NaturalPerson","recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"socialSecurityNumber":"socialSecurityNumber","dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","reference":"reference","bank":{"ownerName":"ownerName","countryCode":"countryCode","taxId":"taxId","iban":"iban","bankAccountNumber":"bankAccountNumber","bankName":"bankName","bankLocationId":"bankLocationId","bic":"bic","bankCity":"bankCity"},"shopperName":{"firstName":"firstName","lastName":"lastName"},"merchantAccount":"merchantAccount","nationality":"nationality","additionalData":{"key":"additionalData"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"selectedBrand":"selectedBrand","card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payout/v40/storeDetailAndSubmitThirdParty',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_submit_third_party(client):
    """Test case for post_submit_third_party

    Submit a payout
    """
    body = {"fraudOffset":0,"amount":{"currency":"currency","value":0},"entityType":"NaturalPerson","recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"socialSecurityNumber":"socialSecurityNumber","dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"merchantAccount":"merchantAccount","nationality":"nationality","selectedRecurringDetailReference":"selectedRecurringDetailReference","additionalData":{"key":"additionalData"},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payout/v40/submitThirdParty',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

