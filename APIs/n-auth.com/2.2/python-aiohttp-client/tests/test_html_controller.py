# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.html_footer_body import HtmlFooterBody
from openapi_server.models.login_status import LoginStatus
from openapi_server.models.user_context import UserContext


pytestmark = pytest.mark.asyncio

async def test_get_html_enrol(client):
    """Test case for get_html_enrol

    Generate HTML to enrol a new user
    """
    params = [('name', 'name_example'),
                    ('userid', 'userid_example')]
    headers = { 
        'Accept': 'text/html',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/sessions/html/enrol'.format(serverid='serverid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_html_footer(client):
    """Test case for get_html_footer

    Generic HTML to add to footer. Required for login/logout/enrol functionality.
    """
    html_footer_body = {"sessions":[{"sessionid":"sessionid","serverid":"serverid"},{"sessionid":"sessionid","serverid":"serverid"}]}
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/sessions/html/footer'.format(serverid='serverid_example'),
        headers=headers,
        json=html_footer_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_html_login(client):
    """Test case for get_html_login

    Generate HTML for the login block
    """
    user_context = {"announceinfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"},"sessioninfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"}}
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/sessions/html/login'.format(serverid='serverid_example'),
        headers=headers,
        json=user_context,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session_0(client):
    """Test case for get_session_0

    Check if the user is logged in
    """
    headers = { 
        'Accept': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/sessions'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout_0(client):
    """Test case for logout_0

    Force a logout on the given session
    """
    headers = { 
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/sessions/logout'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

