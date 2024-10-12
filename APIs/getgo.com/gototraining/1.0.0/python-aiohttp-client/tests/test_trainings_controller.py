# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.host_url import HostUrl
from openapi_server.models.notified_parties import NotifiedParties
from openapi_server.models.organizer import Organizer
from openapi_server.models.registration_settings import RegistrationSettings
from openapi_server.models.training import Training
from openapi_server.models.training_name_description import TrainingNameDescription
from openapi_server.models.training_organizers import TrainingOrganizers
from openapi_server.models.training_req_create import TrainingReqCreate
from openapi_server.models.training_times import TrainingTimes


pytestmark = pytest.mark.asyncio

async def test_cancel_training(client):
    """Test case for cancel_training

    Delete Training
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}'.format(organizer_key=56, training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_trainings(client):
    """Test case for get_all_trainings

    Get Trainings
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/organizers/{organizer_key}/trainings'.format(organizer_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_manage_training_url(client):
    """Test case for get_manage_training_url

    Get Management URL for Training
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/manageUrl'.format(organizer_key=56, training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisers_for_training(client):
    """Test case for get_organisers_for_training

    Get Training Organizers
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/organizers'.format(organizer_key=56, training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_start_url(client):
    """Test case for get_start_url

    Get Start Url
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/startUrl'.format(organizer_key=56, training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_training(client):
    """Test case for get_training

    Get Training
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}'.format(organizer_key=56, training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_training(client):
    """Test case for schedule_training

    Create Training
    """
    body = {"registrationSettings":{"disableWebRegistration":True,"disableConfirmationEmail":True},"times":[{"endDate":"2000-01-23T04:56:07.000+00:00","startDate":"2000-01-23T04:56:07.000+00:00"},{"endDate":"2000-01-23T04:56:07.000+00:00","startDate":"2000-01-23T04:56:07.000+00:00"}],"name":"name","organizers":[0,0],"description":"description","timeZone":"timeZone"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2T/rest/organizers/{organizer_key}/trainings'.format(organizer_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_training(client):
    """Test case for start_training

    Start Training
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/trainings/{training_key}/start'.format(training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organisers_for_training(client):
    """Test case for update_organisers_for_training

    Update Training Organizers
    """
    body = {"notifyOrganizers":True,"organizers":[0,0]}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/organizers'.format(organizer_key=56, training_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_registration_settings_for_training(client):
    """Test case for update_registration_settings_for_training

    Update Training Registration Settings
    """
    body = {"disableWebRegistration":True,"disableConfirmationEmail":True}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/registrationSettings'.format(organizer_key=56, training_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_training_name_description(client):
    """Test case for update_training_name_description

    Update Training Name and Description
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/nameDescription'.format(organizer_key=56, training_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_training_times(client):
    """Test case for update_training_times

    Update Training Times
    """
    body = {"notifyRegistrants":True,"times":[{"endDate":"2000-01-23T04:56:07.000+00:00","startDate":"2000-01-23T04:56:07.000+00:00"},{"endDate":"2000-01-23T04:56:07.000+00:00","startDate":"2000-01-23T04:56:07.000+00:00"}],"notifyTrainers":True,"timeZone":"timeZone"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/times'.format(organizer_key=56, training_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

