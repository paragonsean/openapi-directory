# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_recurring_payment200_response import DeleteRecurringPayment200Response
from openapi_server.models.get_many_plans200_response import GetManyPlans200Response
from openapi_server.models.get_many_recurring_payments200_response import GetManyRecurringPayments200Response
from openapi_server.models.get_one_plan200_response import GetOnePlan200Response
from openapi_server.models.get_one_plan404_response import GetOnePlan404Response
from openapi_server.models.get_one_recurring_payment200_response import GetOneRecurringPayment200Response
from openapi_server.models.get_one_recurring_payment404_response import GetOneRecurringPayment404Response
from openapi_server.models.update_plan_request import UpdatePlanRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_delete_recurring_payment(client):
    """Test case for delete_recurring_payment

    Delete recurring payment
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/subscriptions/{sub_id}'.format(sub_id='sub_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_many_plans(client):
    """Test case for get_many_plans

    Get many plans
    """
    params = [('limit', '10'),
                    ('offset', '3')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/subscriptions/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_get_many_recurring_payments(client):
    """Test case for get_many_recurring_payments

    Get many recurring payments
    """
    params = [('status', 'PARTIALLY_PAID'),
                    ('subscription_plan_id', '111394288'),
                    ('is_active', 'false'),
                    ('limit', '10'),
                    ('offset', '0')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_one_plan(client):
    """Test case for get_one_plan

    Get one plan
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/subscriptions/plans/{plan_id}'.format(plan_id='plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_get_one_recurring_payment(client):
    """Test case for get_one_recurring_payment

    Get one recurring payment
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/subscriptions/{sub_id}'.format(sub_id='sub_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_plan(client):
    """Test case for update_plan

    Update plan
    """
    body = {"amount":2,"currency":"usd","interval_day":1,"title":"test plan"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/subscriptions/plans/{plan_id}'.format(plan_id='plan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

