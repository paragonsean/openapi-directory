# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.web_service_account import WebServiceAccount
from openapi_server.models.web_service_account_statistics import WebServiceAccountStatistics
from openapi_server.models.web_service_transfer_credits_request import WebServiceTransferCreditsRequest
from openapi_server.models.web_service_user import WebServiceUser
from openapi_server.models.web_service_users import WebServiceUsers


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_account_user_put(client):
    """Test case for api_rest_v1_account_user_put

    create
    """
    body = {"firstName":"firstName","lastName":"lastName","emailAddress":"emailAddress","password":"password","contactNumber":"contactNumber","company":"company","userId":9,"creditBalance":7.061401241503109}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/app/api/rest/v1/account/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_account_user_user_id_post(client):
    """Test case for api_rest_v1_account_user_user_id_post

    update
    """
    body = {"firstName":"firstName","lastName":"lastName","emailAddress":"emailAddress","password":"password","contactNumber":"contactNumber","company":"company","userId":9,"creditBalance":7.061401241503109}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/account/user/{user_id}'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_balance(client):
    """Test case for get_balance

    balance
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/account/balance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statistics(client):
    """Test case for get_statistics

    statistics
    """
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('userEmailAddress', 'user_email_address_example'),
                    ('campaign', 'campaign_example'),
                    ('includeRefundedAndOptout', True),
                    ('calculateCreditValue', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/account/statistics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    getUser
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/account/user/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    search
    """
    params = [('searchEmail', 'search_email_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/account/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_transfer(client):
    """Test case for transfer

    transfer
    """
    body = {"numberOfCreditsToTransfer":0,"transferFromEmailAddress":"transferFromEmailAddress","transferToEmailAddress":"transferToEmailAddress"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/account/transfer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

