# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bt_plan_list_item import BtPlanListItem
from openapi_server.models.bt_plans import BtPlans
from openapi_server.models.ee_bt_eligibility import EeBtEligibility
from openapi_server.models.itv_assign_bt_token_request import ItvAssignBtTokenRequest
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_assign_token(client):
    """Test case for assign_token

    
    """
    body = {"profileToken":"profileToken","token":"token"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/bt/token/assign',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_ee_bt_eligibility_0(client):
    """Test case for check_ee_bt_eligibility_0

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ee-bt/eligibility',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_user_token(client):
    """Test case for check_user_token

    
    """
    params = [('id', 'id_example'),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bt/token/validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plan_by_token(client):
    """Test case for get_plan_by_token

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bt/plan/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plans(client):
    """Test case for get_plans

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bt/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

