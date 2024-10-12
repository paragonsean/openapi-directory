# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.disable_serial_console_result import DisableSerialConsoleResult
from openapi_server.models.enable_serial_console_result import EnableSerialConsoleResult
from openapi_server.models.get_serial_console_subscription_not_found import GetSerialConsoleSubscriptionNotFound
from openapi_server.models.serial_console_operations import SerialConsoleOperations
from openapi_server.models.serial_console_status import SerialConsoleStatus


pytestmark = pytest.mark.asyncio

async def test_disable_console(client):
    """Test case for disable_console

    Disable Serial Console for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.SerialConsole/consoleServices/{default}/disableConsole'.format(subscription_id='subscription_id_example', default='default_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_console(client):
    """Test case for enable_console

    Enable Serial Console for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.SerialConsole/consoleServices/{default}/enableConsole'.format(subscription_id='subscription_id_example', default='default_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_console_status(client):
    """Test case for get_console_status

    Get the disabled status for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.SerialConsole/consoleServices/{default}'.format(subscription_id='subscription_id_example', default='default_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_operations(client):
    """Test case for list_operations

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.SerialConsole/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

