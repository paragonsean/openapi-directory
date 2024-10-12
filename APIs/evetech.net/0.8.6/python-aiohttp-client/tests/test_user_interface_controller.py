# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_ui_openwindow_newmail_new_mail import PostUiOpenwindowNewmailNewMail
from openapi_server.models.post_ui_openwindow_newmail_unprocessable_entity import PostUiOpenwindowNewmailUnprocessableEntity
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_post_ui_autopilot_waypoint(client):
    """Test case for post_ui_autopilot_waypoint

    Set Autopilot Waypoint
    """
    params = [('add_to_beginning', False),
                    ('clear_other_waypoints', False),
                    ('datasource', tranquility),
                    ('destination_id', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/ui/autopilot/waypoint/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_ui_openwindow_contract(client):
    """Test case for post_ui_openwindow_contract

    Open Contract Window
    """
    params = [('contract_id', 56),
                    ('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/ui/openwindow/contract/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_ui_openwindow_information(client):
    """Test case for post_ui_openwindow_information

    Open Information Window
    """
    params = [('datasource', tranquility),
                    ('target_id', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/ui/openwindow/information/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_ui_openwindow_marketdetails(client):
    """Test case for post_ui_openwindow_marketdetails

    Open Market Details
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example'),
                    ('type_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/ui/openwindow/marketdetails/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_ui_openwindow_newmail(client):
    """Test case for post_ui_openwindow_newmail

    Open New Mail Window
    """
    new_mail = openapi_server.PostUiOpenwindowNewmailNewMail()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/ui/openwindow/newmail/',
        headers=headers,
        json=new_mail,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

