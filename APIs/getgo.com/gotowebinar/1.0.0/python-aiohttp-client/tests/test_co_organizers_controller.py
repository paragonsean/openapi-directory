# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.coorganizer import Coorganizer
from openapi_server.models.coorganizer_req_create import CoorganizerReqCreate


pytestmark = pytest.mark.asyncio

async def test_create_coorganizers(client):
    """Test case for create_coorganizers

    Create co-organizers
    """
    body = {"external":True,"givenName":"givenName","organizerKey":"organizerKey","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/coorganizers'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_coorganizer(client):
    """Test case for delete_coorganizer

    Delete co-organizer
    """
    params = [('external', True)]
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/coorganizers/{coorganizer_key}'.format(organizer_key=56, webinar_key=56, coorganizer_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_coorganizers(client):
    """Test case for get_coorganizers

    Get co-organizers
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/coorganizers'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_coorganizer_invitation(client):
    """Test case for resend_coorganizer_invitation

    Resend invitation
    """
    params = [('external', True)]
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/coorganizers/{coorganizer_key}/resendInvitation'.format(organizer_key=56, webinar_key=56, coorganizer_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

