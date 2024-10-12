# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.plan import Plan


pytestmark = pytest.mark.asyncio

async def test_delete_plan(client):
    """Test case for delete_plan

    Delete a Plan
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/plans/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plan(client):
    """Test case for get_plan

    Retrieve a plan
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/plans/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plan_collection(client):
    """Test case for get_plan_collection

    Retrieve a list of plans
    """
    params = [('filter', 'filter_example'),
                    ('sort', ['sort_example']),
                    ('limit', 56),
                    ('offset', 56),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_plan(client):
    """Test case for post_plan

    Create a plan
    """
    body = {"updatedTime":"","productOptions":{"color":"red","size":"xxl"},"currencySign":"currencySign","productId":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"isTrialOnly":True,"invoiceTimeShift":"","trial":{"period":{"unit":"day","length":5},"price":2.3021358869347655},"revision":1,"name":"name","createdTime":"","setup":{"price":5.962133916683182},"currency":"","id":"","pricing":{"formula":"fixed-fee"},"recurringInterval":{"unit":"day","billingTiming":"prepaid","length":0,"limit":6}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/plans',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_plan(client):
    """Test case for put_plan

    Create or update a Plan with predefined ID
    """
    body = {"updatedTime":"","productOptions":{"color":"red","size":"xxl"},"currencySign":"currencySign","productId":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"isTrialOnly":True,"invoiceTimeShift":"","trial":{"period":{"unit":"day","length":5},"price":2.3021358869347655},"revision":1,"name":"name","createdTime":"","setup":{"price":5.962133916683182},"currency":"","id":"","pricing":{"formula":"fixed-fee"},"recurringInterval":{"unit":"day","billingTiming":"prepaid","length":0,"limit":6}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/plans/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

