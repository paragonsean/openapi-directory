# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_team_member_get_collection200_response import ApiTeamMemberGetCollection200Response
from openapi_server.models.team_member_get import TeamMemberGet
from openapi_server.models.team_member_jsonld_get import TeamMemberJsonldGet
from openapi_server.models.team_member_jsonld_put import TeamMemberJsonldPut
from openapi_server.models.team_member_patch import TeamMemberPatch
from openapi_server.models.team_member_put import TeamMemberPut


pytestmark = pytest.mark.asyncio

async def test_api_team_member_get_collection(client):
    """Test case for api_team_member_get_collection

    Retrieves the collection of TeamMember resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('userAccount', 'user_account_example'),
                    ('userAccount[]', ['user_account_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team-member',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_team_member_id_delete(client):
    """Test case for api_team_member_id_delete

    Removes the TeamMember resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/team-member/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_team_member_id_get(client):
    """Test case for api_team_member_id_get

    Retrieves a TeamMember resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team-member/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_team_member_id_patch(client):
    """Test case for api_team_member_id_patch

    Updates the TeamMember resource.
    """
    body = openapi_server.TeamMemberPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/team-member/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_team_member_id_put(client):
    """Test case for api_team_member_id_put

    Replaces the TeamMember resource.
    """
    body = openapi_server.TeamMemberPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/team-member/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

