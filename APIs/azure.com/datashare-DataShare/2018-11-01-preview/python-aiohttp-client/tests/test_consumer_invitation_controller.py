# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.consumer_invitation import ConsumerInvitation
from openapi_server.models.consumer_invitation_list import ConsumerInvitationList
from openapi_server.models.data_share_error import DataShareError


pytestmark = pytest.mark.asyncio

async def test_consumer_invitations_get(client):
    """Test case for consumer_invitations_get

    Gets the invitation identified by invitationId
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.DataShare/locations/{location}/consumerInvitations/{invitation_id}'.format(location='location_example', invitation_id='invitation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_invitations_list_invitations(client):
    """Test case for consumer_invitations_list_invitations

    List the invitations
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.DataShare/ListInvitations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_invitations_reject_invitation(client):
    """Test case for consumer_invitations_reject_invitation

    Rejects the invitation identified by invitationId
    """
    invitation = {"properties":{"providerTenantName":"providerTenantName","description":"description","invitationId":"invitationId","respondedAt":"2000-01-23T04:56:07.000+00:00","sentAt":"2000-01-23T04:56:07.000+00:00","userName":"userName","termsOfUse":"termsOfUse","dataSetCount":0,"location":"location","userEmail":"userEmail","shareName":"shareName","invitationStatus":"Pending","providerEmail":"providerEmail","providerName":"providerName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.DataShare/locations/{location}/RejectInvitation'.format(location='location_example'),
        headers=headers,
        json=invitation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

