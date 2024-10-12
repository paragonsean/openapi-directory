# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account


pytestmark = pytest.mark.asyncio

async def test_get_qr_enrol(client):
    """Test case for get_qr_enrol

    Generate data for an enrol qr code
    """
    params = [('name', 'name_example'),
                    ('userid', 'userid_example'),
                    ('img', 'img_example'),
                    ('s', 56)]
    headers = { 
        'Accept': 'application/octet-stream',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/sessions/qr/enrol'.format(serverid='serverid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_vash(client):
    """Test case for get_server_vash

    Visual hash of this server
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/vash'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_user_0(client):
    """Test case for register_user_0

    Register a userid for the currently logged in account.
    """
    params = [('userid', 'userid_example')]
    headers = { 
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/sessions/registeruser'.format(serverid='serverid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account_user_0(client):
    """Test case for update_account_user_0

    Update user of the given account.
    """
    params = [('userid', 'userid_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}/accounts/{accountid}/user'.format(serverid='serverid_example', accountid=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

