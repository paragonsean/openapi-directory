# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.registrant import Registrant
from openapi_server.models.registrant_created import RegistrantCreated
from openapi_server.models.registrant_req_create import RegistrantReqCreate


pytestmark = pytest.mark.asyncio

async def test_cancel_registration(client):
    """Test case for cancel_registration

    Cancel Registration
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/registrants/{registrant_key}'.format(organizer_key=56, training_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registrant(client):
    """Test case for get_registrant

    Get Registrant
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/registrants/{registrant_key}'.format(organizer_key=56, training_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registrants(client):
    """Test case for get_registrants

    Get Training Registrants
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/registrants'.format(organizer_key=56, training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_for_training(client):
    """Test case for register_for_training

    Register for Training
    """
    body = {"surname":"surname","givenName":"givenName","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2T/rest/organizers/{organizer_key}/trainings/{training_key}/registrants'.format(organizer_key=56, training_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

