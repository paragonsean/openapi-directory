# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_microsoft_teams_get_collection200_response import ApiTransportMicrosoftTeamsGetCollection200Response
from openapi_server.models.transport_microsoft_teams_get import TransportMicrosoftTeamsGet
from openapi_server.models.transport_microsoft_teams_jsonld_get import TransportMicrosoftTeamsJsonldGet
from openapi_server.models.transport_microsoft_teams_jsonld_post import TransportMicrosoftTeamsJsonldPost
from openapi_server.models.transport_microsoft_teams_jsonld_put import TransportMicrosoftTeamsJsonldPut
from openapi_server.models.transport_microsoft_teams_patch import TransportMicrosoftTeamsPatch
from openapi_server.models.transport_microsoft_teams_post import TransportMicrosoftTeamsPost
from openapi_server.models.transport_microsoft_teams_put import TransportMicrosoftTeamsPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_microsoft_teams_get_collection(client):
    """Test case for api_transport_microsoft_teams_get_collection

    Retrieves the collection of TransportMicrosoftTeams resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-microsoft-teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_microsoft_teams_id_delete(client):
    """Test case for api_transport_microsoft_teams_id_delete

    Removes the TransportMicrosoftTeams resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-microsoft-teams/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_microsoft_teams_id_get(client):
    """Test case for api_transport_microsoft_teams_id_get

    Retrieves a TransportMicrosoftTeams resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-microsoft-teams/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_microsoft_teams_id_patch(client):
    """Test case for api_transport_microsoft_teams_id_patch

    Updates the TransportMicrosoftTeams resource.
    """
    body = openapi_server.TransportMicrosoftTeamsPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-microsoft-teams/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_microsoft_teams_id_put(client):
    """Test case for api_transport_microsoft_teams_id_put

    Replaces the TransportMicrosoftTeams resource.
    """
    body = openapi_server.TransportMicrosoftTeamsPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-microsoft-teams/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_microsoft_teams_post(client):
    """Test case for api_transport_microsoft_teams_post

    Creates a TransportMicrosoftTeams resource.
    """
    body = openapi_server.TransportMicrosoftTeamsPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-microsoft-teams',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

