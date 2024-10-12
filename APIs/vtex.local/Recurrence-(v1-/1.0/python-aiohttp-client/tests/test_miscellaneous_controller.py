# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addrecurrenceitem_request import AddrecurrenceitemRequest
from openapi_server.models.reindexrecurrence_request import ReindexrecurrenceRequest
from openapi_server.models.updatepartialrecurrence_request import UpdatepartialrecurrenceRequest
from openapi_server.models.updaterecurrence_request import UpdaterecurrenceRequest
from openapi_server.models.updaterecurrencesettings_request import UpdaterecurrencesettingsRequest


pytestmark = pytest.mark.asyncio

async def test_addrecurrenceitem(client):
    """Test case for addrecurrenceitem

    Add Subscription item
    """
    body = {"frequency":{"interval":1,"periodicity":"monthly"},"quantity":2,"seller":"1","shippingAddressId":"-1461618656161","sku":"20"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{recurrence_id}/items'.format(recurrence_id='recurrence_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recurrencebyemail(client):
    """Test case for get_recurrencebyemail

    Get Subscriptions
    """
    params = [('email', '{{email}}'),
                    ('cycleStatus', '{{cycleStatus}}')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recurrencebyrecurrence_id(client):
    """Test case for get_recurrencebyrecurrence_id

    Get Subscription by recurrenceId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{recurrence_id}'.format(recurrence_id='recurrence_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getpaymentaccounts(client):
    """Test case for getpaymentaccounts

    Get payment accounts
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{recurrenceid}/accounts'.format(recurrenceid='recurrenceid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getrecurrenceaddresses(client):
    """Test case for getrecurrenceaddresses

    Get Subscription addresses
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{recurrence_id}/addresses'.format(recurrence_id='recurrence_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getrecurrencesettings(client):
    """Test case for getrecurrencesettings

    Get Subscription settings
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getselfrecurrence(client):
    """Test case for getselfrecurrence

    Get self Subscription
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindexrecurrence(client):
    """Test case for reindexrecurrence

    Reindex Subscription
    """
    body = {"frequency":{"interval":1,"periodicity":"yearly"}}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{recurrence_id}/reindex'.format(recurrence_id='recurrence_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updatepartialrecurrence(client):
    """Test case for updatepartialrecurrence

    Update partial Subscription
    """
    body = {"deliveryDay":18,"deliveryWeekday":"Monday","status":"inactive"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{recurrence_id}'.format(recurrence_id='recurrence_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updaterecurrence(client):
    """Test case for updaterecurrence

    Update Subscription
    """
    body = {"deliveryDay":26,"deliveryWeekday":"Friday","email":"user@vtex.com.br","items":[{"frequency":{"interval":1,"periodicity":"weekly"},"quantity":2,"seller":"1","shippingAddressId":"-1461618656161","sku":"18"}],"paymentAccountId":"87FE21B06C0D42908D31A5B11E6FC043"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updaterecurrencesettings(client):
    """Test case for updaterecurrencesettings

    Update Subscription settings
    """
    body = {"defaultSLA":"Normal","salesChannel":"1"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

