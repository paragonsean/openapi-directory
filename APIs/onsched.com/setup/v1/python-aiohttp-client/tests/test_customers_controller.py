# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_list_view_model import CustomerListViewModel
from openapi_server.models.customer_privacy_view_model import CustomerPrivacyViewModel
from openapi_server.models.customer_view_model import CustomerViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_customers_get(client):
    """Test case for setup_v1_customers_get

    List Customers
    """
    params = [('locationId', 'location_id_example'),
                    ('groupId', 'group_id_example'),
                    ('email', 'email_example'),
                    ('lastname', 'lastname_example'),
                    ('deleted', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_customers_id_get(client):
    """Test case for setup_v1_customers_id_get

    Get Customer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/customers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_customers_id_privacy_get(client):
    """Test case for setup_v1_customers_id_privacy_get

    Get Customer Data
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/customers/{id}/privacy'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

