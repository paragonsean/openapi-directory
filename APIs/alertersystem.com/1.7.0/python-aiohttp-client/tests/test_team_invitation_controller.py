# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_team_invitation_get_collection200_response import ApiTeamInvitationGetCollection200Response
from openapi_server.models.team_invitation_get import TeamInvitationGet
from openapi_server.models.team_invitation_jsonld_get import TeamInvitationJsonldGet
from openapi_server.models.team_invitation_jsonld_post import TeamInvitationJsonldPost
from openapi_server.models.team_invitation_post import TeamInvitationPost


pytestmark = pytest.mark.asyncio

async def test_api_team_invitation_get_collection(client):
    """Test case for api_team_invitation_get_collection

    Retrieves the collection of TeamInvitation resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('inviteeEmail', 'invitee_email_example'),
                    ('inviteeEmail[]', ['invitee_email_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team-invitation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_team_invitation_id_delete(client):
    """Test case for api_team_invitation_id_delete

    Removes the TeamInvitation resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/team-invitation/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_team_invitation_id_get(client):
    """Test case for api_team_invitation_id_get

    Retrieves a TeamInvitation resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team-invitation/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_team_invitation_post(client):
    """Test case for api_team_invitation_post

    Creates a TeamInvitation resource.
    """
    body = openapi_server.TeamInvitationPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/team-invitation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

