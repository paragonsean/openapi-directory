# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.reminders_add_error_schema import RemindersAddErrorSchema
from openapi_server.models.reminders_add_schema import RemindersAddSchema
from openapi_server.models.reminders_complete_error_schema import RemindersCompleteErrorSchema
from openapi_server.models.reminders_complete_schema import RemindersCompleteSchema
from openapi_server.models.reminders_delete_error_schema import RemindersDeleteErrorSchema
from openapi_server.models.reminders_delete_schema import RemindersDeleteSchema
from openapi_server.models.reminders_info_error_schema import RemindersInfoErrorSchema
from openapi_server.models.reminders_info_schema import RemindersInfoSchema
from openapi_server.models.reminders_list_error_schema import RemindersListErrorSchema
from openapi_server.models.reminders_list_schema import RemindersListSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_reminders_add(client):
    """Test case for reminders_add

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'text': 'text_example',
        'time': 'time_example',
        'user': 'user_example'
        }
    response = await client.request(
        method='POST',
        path='/api/reminders.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_reminders_complete(client):
    """Test case for reminders_complete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'reminder': 'reminder_example'
        }
    response = await client.request(
        method='POST',
        path='/api/reminders.complete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_reminders_delete(client):
    """Test case for reminders_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'reminder': 'reminder_example'
        }
    response = await client.request(
        method='POST',
        path='/api/reminders.delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminders_info(client):
    """Test case for reminders_info

    
    """
    params = [('token', 'token_example'),
                    ('reminder', 'reminder_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/reminders.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminders_list(client):
    """Test case for reminders_list

    
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/reminders.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

