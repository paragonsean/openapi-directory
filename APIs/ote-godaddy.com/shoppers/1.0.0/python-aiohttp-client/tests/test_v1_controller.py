# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.password_error import PasswordError
from openapi_server.models.secret import Secret
from openapi_server.models.shopper import Shopper
from openapi_server.models.shopper_id import ShopperId
from openapi_server.models.shopper_status import ShopperStatus
from openapi_server.models.shopper_update import ShopperUpdate
from openapi_server.models.subaccount_create import SubaccountCreate


pytestmark = pytest.mark.asyncio

async def test_change_password(client):
    """Test case for change_password

    Set subaccount's password
    """
    body = {"secret":"P@55w0rd+"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/shoppers/{shopper_id}/factors/password'.format(shopper_id='shopper_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_subaccount(client):
    """Test case for create_subaccount

    Create a Subaccount owned by the authenticated Reseller
    """
    body = {"nameLast":"nameLast","password":"password","nameFirst":"nameFirst","externalId":0,"email":"email","marketId":"en-US"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/shoppers/subaccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    Request the deletion of a shopper profile
    """
    params = [('auditClientIp', 'audit_client_ip_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/shoppers/{shopper_id}'.format(shopper_id='shopper_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Get details for the specified Shopper
    """
    params = [('includes', ['includes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shoppers/{shopper_id}'.format(shopper_id='shopper_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    Get details for the specified Shopper
    """
    params = [('auditClientIp', 'audit_client_ip_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shoppers/{shopper_id}/status'.format(shopper_id='shopper_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update(client):
    """Test case for update

    Update details for the specified Shopper
    """
    body = {"nameLast":"nameLast","nameFirst":"nameFirst","externalId":0,"email":"email","marketId":"da-DK"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/shoppers/{shopper_id}'.format(shopper_id='shopper_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

