# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server.models.dnd_end_dnd_error_schema import DndEndDndErrorSchema
from openapi_server.models.dnd_end_dnd_schema import DndEndDndSchema
from openapi_server.models.dnd_end_snooze_error_schema import DndEndSnoozeErrorSchema
from openapi_server.models.dnd_end_snooze_schema import DndEndSnoozeSchema
from openapi_server.models.dnd_info_error_schema import DndInfoErrorSchema
from openapi_server.models.dnd_info_schema import DndInfoSchema
from openapi_server.models.dnd_set_snooze_error_schema import DndSetSnoozeErrorSchema
from openapi_server.models.dnd_set_snooze_schema import DndSetSnoozeSchema


pytestmark = pytest.mark.asyncio

async def test_dnd_end_dnd(client):
    """Test case for dnd_end_dnd

    
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dnd.endDnd',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dnd_end_snooze(client):
    """Test case for dnd_end_snooze

    
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dnd.endSnooze',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dnd_info(client):
    """Test case for dnd_info

    
    """
    params = [('token', 'token_example'),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dnd.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dnd_set_snooze(client):
    """Test case for dnd_set_snooze

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'num_minutes': 'num_minutes_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/dnd.setSnooze',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dnd_team_info(client):
    """Test case for dnd_team_info

    
    """
    params = [('token', 'token_example'),
                    ('users', 'users_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dnd.teamInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

