# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ee_bt_eligibility import EeBtEligibility
from openapi_server.models.ee_create_pin_request import EeCreatePinRequest
from openapi_server.models.ee_create_pin_response import EeCreatePinResponse
from openapi_server.models.ee_create_token_response import EeCreateTokenResponse
from openapi_server.models.ee_offers_request import EeOffersRequest
from openapi_server.models.ee_offers_response import EeOffersResponse
from openapi_server.models.ee_plan_list_item import EePlanListItem
from openapi_server.models.ee_plans import EePlans
from openapi_server.models.ee_validate_pin_request import EeValidatePinRequest
from openapi_server.models.ee_validate_pin_response import EeValidatePinResponse
from openapi_server.models.itv_assign_msisdn_request import ItvAssignMsisdnRequest
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_assign_msisdn(client):
    """Test case for assign_msisdn

    
    """
    body = {"profileToken":"profileToken","msisdn":"msisdn","trackingHeader":"trackingHeader","eeProductId":"eeProductId"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ee/msisdn',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_ee_bt_eligibility(client):
    """Test case for check_ee_bt_eligibility

    
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

async def test_create_pin_request(client):
    """Test case for create_pin_request

    
    """
    body = {"accessToken":"wxg0fG4GQjBQVjAT0AhKxSkrxFbs","msisdn":"447931234567","trackingHeader":"1234E682-2C74-46A4-B8B3-5BBD3B3E165D"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/ee/pin',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_token(client):
    """Test case for create_token

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/ee/token/create',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ee_plans_get(client):
    """Test case for ee_plans_get

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/ee/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_eligible_offers(client):
    """Test case for get_eligible_offers

    
    """
    body = {"accessToken":"wxg0fG4GQjBQVjAT0AhKxSkrxFbs","msisdn":"447931234567","trackingHeader":"1234E682-2C74-46A4-B8B3-5BBD3B3E165D"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/ee/offers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plan(client):
    """Test case for get_plan

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/ee/plans/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_pin_request(client):
    """Test case for validate_pin_request

    
    """
    body = {"accessToken":"wxg0fG4GQjBQVjAT0AhKxSkrxFbs","pin":"123456","pinReference":"9897222307534","trackingHeader":"1234E682-2C74-46A4-B8B3-5BBD3B3E165D"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/ee/pin',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

