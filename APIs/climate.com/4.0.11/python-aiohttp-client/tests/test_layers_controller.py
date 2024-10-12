# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_activities import ApplicationActivities
from openapi_server.models.application_activity_contents import ApplicationActivityContents
from openapi_server.models.error import Error
from openapi_server.models.harvest_activities import HarvestActivities
from openapi_server.models.harvest_activity_contents import HarvestActivityContents
from openapi_server.models.planting_activities import PlantingActivities
from openapi_server.models.planting_activity_contents import PlantingActivityContents
from openapi_server.models.scouting_observation import ScoutingObservation
from openapi_server.models.scouting_observation_attachment_contents import ScoutingObservationAttachmentContents
from openapi_server.models.scouting_observation_attachments import ScoutingObservationAttachments
from openapi_server.models.scouting_observations import ScoutingObservations


pytestmark = pytest.mark.asyncio

async def test_v4_layers_as_applied_activity_id_contents_get(client):
    """Test case for v4_layers_as_applied_activity_id_contents_get

    Retrieve the raw application activity
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'range': 'range_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/asApplied/{activity_id}/contents'.format(activity_id='activity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_as_applied_get(client):
    """Test case for v4_layers_as_applied_get

    Retrieve a list of application activities
    """
    params = [('resourceOwnerId', 'resource_owner_id_example'),
                    ('occurredAfter', '2013-10-20T19:20:30+01:00'),
                    ('occurredBefore', '2013-10-20T19:20:30+01:00'),
                    ('updatedAfter', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'x_next_token': 'x_next_token_example',
        'x_limit': 56,
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/asApplied',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_as_harvested_activity_id_contents_get(client):
    """Test case for v4_layers_as_harvested_activity_id_contents_get

    Retrieve the raw harvest activity
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'range': 'range_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/asHarvested/{activity_id}/contents'.format(activity_id='activity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_as_harvested_get(client):
    """Test case for v4_layers_as_harvested_get

    Retrieve a list of harvest activities
    """
    params = [('resourceOwnerId', 'resource_owner_id_example'),
                    ('occurredAfter', '2013-10-20T19:20:30+01:00'),
                    ('occurredBefore', '2013-10-20T19:20:30+01:00'),
                    ('updatedAfter', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'x_next_token': 'x_next_token_example',
        'x_limit': 56,
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/asHarvested',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_as_planted_activity_id_contents_get(client):
    """Test case for v4_layers_as_planted_activity_id_contents_get

    Retrieve the raw planting activity
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'range': 'range_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/asPlanted/{activity_id}/contents'.format(activity_id='activity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_as_planted_get(client):
    """Test case for v4_layers_as_planted_get

    Retrieve a list of planting activities
    """
    params = [('resourceOwnerId', 'resource_owner_id_example'),
                    ('occurredAfter', '2013-10-20T19:20:30+01:00'),
                    ('occurredBefore', '2013-10-20T19:20:30+01:00'),
                    ('updatedAfter', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'x_next_token': 'x_next_token_example',
        'x_limit': 56,
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/asPlanted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_scouting_observations_get(client):
    """Test case for v4_layers_scouting_observations_get

    Retrieve a list of scouting observations
    """
    params = [('occurredAfter', '2013-10-20T19:20:30+01:00'),
                    ('occurredBefore', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'x_next_token': 'x_next_token_example',
        'x_limit': 56,
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/scoutingObservations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_scouting_observations_scouting_observation_id_attachments_attachment_id_contents_get(client):
    """Test case for v4_layers_scouting_observations_scouting_observation_id_attachments_attachment_id_contents_get

    Retrieve the binary contents of a scouting observation’s attachment.
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'range': 'range_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/scoutingObservations/{scouting_observation_id}/attachments/{attachment_id}/contents'.format(scouting_observation_id='scouting_observation_id_example', attachment_id='attachment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_scouting_observations_scouting_observation_id_attachments_get(client):
    """Test case for v4_layers_scouting_observations_scouting_observation_id_attachments_get

    Retrieve attachments associated with a given scouting observation.
    """
    headers = { 
        'Accept': 'application/json',
        'x_next_token': 'x_next_token_example',
        'x_limit': 56,
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/scoutingObservations/{scouting_observation_id}/attachments'.format(scouting_observation_id='scouting_observation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_layers_scouting_observations_scouting_observation_id_get(client):
    """Test case for v4_layers_scouting_observations_scouting_observation_id_get

    Retrieve individual scouting observation
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/layers/scoutingObservations/{scouting_observation_id}'.format(scouting_observation_id='scouting_observation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

