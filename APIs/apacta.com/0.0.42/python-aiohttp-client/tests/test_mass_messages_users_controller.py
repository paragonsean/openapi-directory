# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.mass_messages_users_get200_response import MassMessagesUsersGet200Response
from openapi_server.models.mass_messages_users_mass_messages_user_id_get200_response import MassMessagesUsersMassMessagesUserIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_mass_messages_users_get(client):
    """Test case for mass_messages_users_get

    View list of mass messages for specific user
    """
    params = [('is_read', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mass_messages_users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mass_messages_users_mass_messages_user_id_get(client):
    """Test case for mass_messages_users_mass_messages_user_id_get

    View mass message
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mass_messages_users/{mass_messages_user_id}'.format(mass_messages_user_id='mass_messages_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mass_messages_users_mass_messages_user_id_put(client):
    """Test case for mass_messages_users_mass_messages_user_id_put

    Edit mass message
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/mass_messages_users/{mass_messages_user_id}'.format(mass_messages_user_id='mass_messages_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

