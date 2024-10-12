# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_sync_status import CompanySyncStatus


pytestmark = pytest.mark.asyncio

async def test_get_last_successful_sync(client):
    """Test case for get_last_successful_sync

    Last successful sync
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/syncs/lastSuccessful/status'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_sync(client):
    """Test case for get_latest_sync

    Latest sync status
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/syncs/latest/status'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sync_by_id(client):
    """Test case for get_sync_by_id

    Get Sync status
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/syncs/{sync_id}/status'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002', sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_syncs(client):
    """Test case for list_syncs

    List sync statuses
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/syncs/list/status'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

