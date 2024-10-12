# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_permit_request import CreatePermitRequest
from openapi_server.models.create_permit_result import CreatePermitResult
from openapi_server.models.disable_permit_request import DisablePermitRequest
from openapi_server.models.disable_permit_result import DisablePermitResult
from openapi_server.models.disable_request import DisableRequest
from openapi_server.models.disable_result import DisableResult
from openapi_server.models.notify_shopper_request import NotifyShopperRequest
from openapi_server.models.notify_shopper_result import NotifyShopperResult
from openapi_server.models.recurring_details_request import RecurringDetailsRequest
from openapi_server.models.recurring_details_result import RecurringDetailsResult
from openapi_server.models.schedule_account_updater_request import ScheduleAccountUpdaterRequest
from openapi_server.models.schedule_account_updater_result import ScheduleAccountUpdaterResult
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_create_permit(client):
    """Test case for post_create_permit

    Create new permits linked to a recurring contract.
    """
    body = {"merchantAccount":"merchantAccount","permits":[{"profileReference":"profileReference","validTillDate":"2000-01-23T04:56:07.000+00:00","restriction":{"singleTransactionLimit":{"currency":"currency","value":0},"singleUse":True,"maxAmount":{"currency":"currency","value":0}},"resultKey":"resultKey","partnerId":"partnerId"},{"profileReference":"profileReference","validTillDate":"2000-01-23T04:56:07.000+00:00","restriction":{"singleTransactionLimit":{"currency":"currency","value":0},"singleUse":True,"maxAmount":{"currency":"currency","value":0}},"resultKey":"resultKey","partnerId":"partnerId"}],"recurringDetailReference":"recurringDetailReference","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Recurring/v67/createPermit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_disable(client):
    """Test case for post_disable

    Disable stored payment details
    """
    body = {"merchantAccount":"merchantAccount","contract":"contract","recurringDetailReference":"recurringDetailReference","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Recurring/v67/disable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_disable_permit(client):
    """Test case for post_disable_permit

    Disable an existing permit.
    """
    body = {"merchantAccount":"merchantAccount","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Recurring/v67/disablePermit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_list_recurring_details(client):
    """Test case for post_list_recurring_details

    Get stored payment details
    """
    body = {"merchantAccount":"merchantAccount","recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Recurring/v67/listRecurringDetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_notify_shopper(client):
    """Test case for post_notify_shopper

    Ask issuer to notify the shopper
    """
    body = {"reference":"reference","billingDate":"billingDate","amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","storedPaymentMethodId":"storedPaymentMethodId","displayedReference":"displayedReference","recurringDetailReference":"recurringDetailReference","billingSequenceNumber":"billingSequenceNumber","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Recurring/v67/notifyShopper',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_schedule_account_updater(client):
    """Test case for post_schedule_account_updater

    Schedule running the Account Updater
    """
    body = {"reference":"reference","merchantAccount":"merchantAccount","selectedRecurringDetailReference":"selectedRecurringDetailReference","additionalData":{"key":"additionalData"},"card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"},"shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Recurring/v67/scheduleAccountUpdater',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

