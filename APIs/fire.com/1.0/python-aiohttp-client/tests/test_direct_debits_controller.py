# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.direct_debit import DirectDebit
from openapi_server.models.direct_debits import DirectDebits
from openapi_server.models.mandate import Mandate
from openapi_server.models.mandates import Mandates


pytestmark = pytest.mark.asyncio

async def test_activate_mandate(client):
    """Test case for activate_mandate

    Activate a direct debit mandate
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/mandates/{mandate_uuid}/activate'.format(mandate_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_mandate_by_uuid(client):
    """Test case for cancel_mandate_by_uuid

    Cancel a direct debit mandate
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/mandates/{mandate_uuid}/cancel'.format(mandate_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_direct_debit_by_uuid(client):
    """Test case for get_direct_debit_by_uuid

    Get the details of a direct debit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/directdebits/{direct_debit_uuid}'.format(direct_debit_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_direct_debit_mandates(client):
    """Test case for get_direct_debit_mandates

    List all direct debit mandates
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/mandates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_direct_debits_for_mandate_uuid(client):
    """Test case for get_direct_debits_for_mandate_uuid

    Get all DD payments associated with a direct debit mandate
    """
    params = [('mandateUuid', '1A07774B-1461-4595-BC4B-423B739712AF')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/directdebits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mandate(client):
    """Test case for get_mandate

    Get direct debit mandate details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/mandates/{mandate_uuid}'.format(mandate_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reject_direct_debit(client):
    """Test case for reject_direct_debit

    Reject a direct debit payment
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/directdebits/{direct_debit_uuid}/reject'.format(direct_debit_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_mandate_alias(client):
    """Test case for update_mandate_alias

    Update a direct debit mandate alias
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/mandates/{mandate_uuid}'.format(mandate_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

