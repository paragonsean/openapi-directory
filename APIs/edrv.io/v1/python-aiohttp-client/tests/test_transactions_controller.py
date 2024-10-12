# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_transactions200_response import GetTransactions200Response


pytestmark = pytest.mark.asyncio

async def test_get_transaction(client):
    """Test case for get_transaction

    
    """
    params = [('include_chargestation', True),
                    ('include_evse', True),
                    ('include_connector', True),
                    ('include_driver', True),
                    ('include_token', True),
                    ('include_reservation', True),
                    ('include_organization', True),
                    ('include_rate', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transactions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_cost(client):
    """Test case for get_transaction_cost

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transactions/{id}/cost'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions(client):
    """Test case for get_transactions

    
    """
    params = [('status', 'status_example'),
                    ('paginate_limit', 20),
                    ('paginate_page', 'paginate_page_example'),
                    ('paginate_enabled', True),
                    ('sort_by', 'createdAt'),
                    ('sort_order', desc),
                    ('createdAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('createdAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('include_chargestation', True),
                    ('include_evse', True),
                    ('include_connector', True),
                    ('include_driver', True),
                    ('include_token', True),
                    ('include_reservation', True),
                    ('include_organization', True),
                    ('include_rate', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

