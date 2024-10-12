# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_failed_ipns import ListFailedIPNs
from openapi_server.models.list_subscribed_addresses import ListSubscribedAddresses
from openapi_server.models.resend_failed_ipn import ResendFailedIPN
from openapi_server.models.resend_failed_ipn_request import ResendFailedIPNRequest
from openapi_server.models.subscribe_address import SubscribeAddress
from openapi_server.models.subscribe_address_request import SubscribeAddressRequest
from openapi_server.models.unsubscribe_address import UnsubscribeAddress
from openapi_server.models.unsubscribe_address_request import UnsubscribeAddressRequest


pytestmark = pytest.mark.asyncio

async def test_list_failed_ipns(client):
    """Test case for list_failed_ipns

    listFailedIPNs
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/listFailedIPNs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_subscribed_addresses(client):
    """Test case for list_subscribed_addresses

    listSubscribedAddresses
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/listSubscribedAddresses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_failed_ipn(client):
    """Test case for resend_failed_ipn

    resendFailedIPN
    """
    body = {"id":17766}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/resendFailedIPN',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_address(client):
    """Test case for subscribe_address

    subscribeAddress
    """
    body = {"contractaddress":"0x514910771af9ca656af840dff83e8264ecf986ca","ethereumaddress":"0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974","url":"https://yoururl.com/ipnreceiver.php"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/subscribeAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_address(client):
    """Test case for unsubscribe_address

    unsubscribeAddress
    """
    body = {"contractaddress":"0x514910771af9ca656af840dff83e8264ecf986ca","ethereumaddress":"0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974","url":"https://yoururl.com/ipnreceiver.php"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/unsubscribeAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

