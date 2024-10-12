# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dps_message import DpsMessage
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection


pytestmark = pytest.mark.asyncio

async def test_delete_dps_message(client):
    """Test case for delete_dps_message

    Deletes the DPS message
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/DpsMessage/{dps_message_id}'.format(employer_id='employer_id_example', dps_message_id='dps_message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dps_message_from_employer(client):
    """Test case for get_dps_message_from_employer

    Gets the DPS message
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/DpsMessage/{dps_message_id}'.format(employer_id='employer_id_example', dps_message_id='dps_message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dps_messages_from_employer(client):
    """Test case for get_dps_messages_from_employer

    Gets the DPS messages
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/DpsMessages'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dps_message(client):
    """Test case for patch_dps_message

    Patches the DPS message
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/DpsMessage/{dps_message_id}'.format(employer_id='employer_id_example', dps_message_id='dps_message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_dps_message(client):
    """Test case for post_dps_message

    Posta the DPS message
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/DpsMessages'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_dps_message(client):
    """Test case for put_dps_message

    Puts the DPS message
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/DpsMessage/{dps_message_id}'.format(employer_id='employer_id_example', dps_message_id='dps_message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

