# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.registrant import Registrant
from openapi_server.models.registrant_created import RegistrantCreated
from openapi_server.models.registrant_detailed import RegistrantDetailed
from openapi_server.models.registrant_fields import RegistrantFields
from openapi_server.models.registration_fields import RegistrationFields


pytestmark = pytest.mark.asyncio

async def test_create_registrant(client):
    """Test case for create_registrant

    Create registrant
    """
    body = {"country":"country","lastName":"lastName","zipCode":"zipCode","address":"address","purchasingRole":"purchasingRole","city":"city","jobTitle":"jobTitle","industry":"industry","questionsAndComments":"questionsAndComments","source":"source","numberOfEmployees":"numberOfEmployees","firstName":"firstName","phone":"phone","organization":"organization","purchasingTimeFrame":"purchasingTimeFrame","responses":[{"questionKey":6,"answerKey":0,"responseText":"responseText"},{"questionKey":6,"answerKey":0,"responseText":"responseText"}],"state":"state","email":"email"}
    params = [('resendConfirmation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'accept': 'accept_example',
    }
    response = await client.request(
        method='POST',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/registrants'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_registrant(client):
    """Test case for delete_registrant

    Delete registrant
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/registrants/{registrant_key}'.format(organizer_key=56, webinar_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_registrants_for_webinar(client):
    """Test case for get_all_registrants_for_webinar

    Get registrants
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/registrants'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registrant(client):
    """Test case for get_registrant

    Get registrant
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/registrants/{registrant_key}'.format(organizer_key=56, webinar_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_fields(client):
    """Test case for get_registration_fields

    Get registration fields
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/registrants/fields'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

