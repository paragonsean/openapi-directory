# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.invitation import Invitation
from openapi_server.models.invitation_list import InvitationList


pytestmark = pytest.mark.asyncio

async def test_invitations_create(client):
    """Test case for invitations_create

    Sends a new invitation to a recipient to access a share.
    """
    invitation = {"properties":{"targetObjectId":"targetObjectId","targetEmail":"targetEmail","targetActiveDirectoryId":"targetActiveDirectoryId","userEmail":"userEmail","invitationId":"invitationId","respondedAt":"2000-01-23T04:56:07.000+00:00","sentAt":"2000-01-23T04:56:07.000+00:00","userName":"userName","invitationStatus":"Pending"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/invitations/{invitation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', invitation_name='invitation_name_example'),
        headers=headers,
        json=invitation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invitations_delete(client):
    """Test case for invitations_delete

    Delete Invitation in a share.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/invitations/{invitation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', invitation_name='invitation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invitations_get(client):
    """Test case for invitations_get

    Get Invitation in a share.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/invitations/{invitation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', invitation_name='invitation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invitations_list_by_share(client):
    """Test case for invitations_list_by_share

    List all Invitations in a share.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/invitations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

