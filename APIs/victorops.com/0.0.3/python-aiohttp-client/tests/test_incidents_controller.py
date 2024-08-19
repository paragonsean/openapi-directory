# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ack_or_resolve_by_user_request import AckOrResolveByUserRequest
from openapi_server.models.ack_or_resolve_request import AckOrResolveRequest
from openapi_server.models.ack_or_resolve_response import AckOrResolveResponse
from openapi_server.models.active_incident_list import ActiveIncidentList
from openapi_server.models.create_incident_request import CreateIncidentRequest
from openapi_server.models.created_incident import CreatedIncident
from openapi_server.models.reroute_collection import RerouteCollection
from openapi_server.models.reroute_status_response import RerouteStatusResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_incidents_ack_patch(client):
    """Test case for api_public_v1_incidents_ack_patch

    Acknowledge an incident or list of incidents
    """
    body = openapi_server.AckOrResolveRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api-public/v1/incidents/ack',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_incidents_by_user_ack_patch(client):
    """Test case for api_public_v1_incidents_by_user_ack_patch

    Acknowledge all incidents for which a user was paged.
    """
    body = openapi_server.AckOrResolveByUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api-public/v1/incidents/byUser/ack',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_incidents_by_user_resolve_patch(client):
    """Test case for api_public_v1_incidents_by_user_resolve_patch

    Resolve all incidents for which a user was paged.
    """
    body = openapi_server.AckOrResolveByUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api-public/v1/incidents/byUser/resolve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_incidents_get(client):
    """Test case for api_public_v1_incidents_get

    Get current incident information
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/incidents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_incidents_post(client):
    """Test case for api_public_v1_incidents_post

    Create a new incident
    """
    body = openapi_server.CreateIncidentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/incidents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_incidents_reroute_post(client):
    """Test case for api_public_v1_incidents_reroute_post

    Reroute one or more incidents to one or more new routable destinations.
    """
    body = openapi_server.RerouteCollection()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/incidents/reroute',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_incidents_resolve_patch(client):
    """Test case for api_public_v1_incidents_resolve_patch

    Resolve an incident or list of incidents
    """
    body = openapi_server.AckOrResolveRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api-public/v1/incidents/resolve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

