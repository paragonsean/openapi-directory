# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.automatic_invitations_list_vo import AutomaticInvitationsListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.profile_image_vo import ProfileImageVO
from openapi_server.models.team_template_expand_vo import TeamTemplateExpandVO
from openapi_server.models.team_template_list_vo import TeamTemplateListVO


pytestmark = pytest.mark.asyncio

async def test_get_automatic_invitation_list(client):
    """Test case for get_automatic_invitation_list

    List current user's automatic invitations info 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/automaticInvitations'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_template_detail(client):
    """Test case for get_team_template_detail

    Get current user's team template detal info 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/teamTemplates/{team_template_id}'.format(workgroup_id='workgroup_id_example', team_template_id='team_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_template_list(client):
    """Test case for get_team_template_list

    List current user's team templates info 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/teamTemplates'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload_profile_image(client):
    """Test case for upload_profile_image

    Upload Profile Image.  A multipart/form-data request with a name \"file\"
    """
    body = '/path/to/file'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/profileImage'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

