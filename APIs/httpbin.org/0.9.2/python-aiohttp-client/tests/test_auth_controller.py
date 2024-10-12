# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_basic_auth_user_passwd_get(client):
    """Test case for basic_auth_user_passwd_get

    Prompts the user for authorization using HTTP Basic Auth.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/basic-auth/{user}/{passwd}'.format(user='user_example', passwd='passwd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bearer_get(client):
    """Test case for bearer_get

    Prompts the user for authorization using bearer authentication.
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/bearer',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digest_auth_qop_user_passwd_algorithm_get(client):
    """Test case for digest_auth_qop_user_passwd_algorithm_get

    Prompts the user for authorization using Digest Auth + Algorithm.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/digest-auth/{qop}/{user}/{passwd}/{algorithm}'.format(qop='qop_example', user='user_example', passwd='passwd_example', algorithm='MD5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digest_auth_qop_user_passwd_algorithm_stale_after_get(client):
    """Test case for digest_auth_qop_user_passwd_algorithm_stale_after_get

    Prompts the user for authorization using Digest Auth + Algorithm.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}'.format(qop='qop_example', user='user_example', passwd='passwd_example', algorithm='MD5', stale_after='never'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digest_auth_qop_user_passwd_get(client):
    """Test case for digest_auth_qop_user_passwd_get

    Prompts the user for authorization using Digest Auth.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/digest-auth/{qop}/{user}/{passwd}'.format(qop='qop_example', user='user_example', passwd='passwd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hidden_basic_auth_user_passwd_get(client):
    """Test case for hidden_basic_auth_user_passwd_get

    Prompts the user for authorization using HTTP Basic Auth.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/hidden-basic-auth/{user}/{passwd}'.format(user='user_example', passwd='passwd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

