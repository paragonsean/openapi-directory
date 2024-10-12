# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.created_panelist import CreatedPanelist
from openapi_server.models.panelist import Panelist
from openapi_server.models.panelist_req_create import PanelistReqCreate


pytestmark = pytest.mark.asyncio

async def test_create_panelists(client):
    """Test case for create_panelists

    Create Panelists
    """
    body = {"name":"name","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/panelists'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_webinar_panelist(client):
    """Test case for delete_webinar_panelist

    Delete webinar panelist
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/panelists/{panelist_key}'.format(organizer_key=56, webinar_key=56, panelist_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_panelists(client):
    """Test case for get_panelists

    Get webinar panelists
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/panelists'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_panelist_invitation(client):
    """Test case for resend_panelist_invitation

    Resend panelist invitation
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/panelists/{panelist_key}/resendInvitation'.format(organizer_key=56, webinar_key=56, panelist_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

