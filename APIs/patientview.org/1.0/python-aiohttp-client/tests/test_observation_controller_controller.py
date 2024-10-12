# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fhir_observation import FhirObservation
from openapi_server.models.fhir_observation_page import FhirObservationPage


pytestmark = pytest.mark.asyncio

async def test_get_observations_by_code(client):
    """Test case for get_observations_by_code

    Get Observations of a Certain Type For a User
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}/observations/{code}'.format(user_id=56, code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_observations_by_codes(client):
    """Test case for get_observations_by_codes

    Get Observations of Multiple Types For a User
    """
    params = [('code', ['code_example']),
                    ('limit', 56),
                    ('offset', 56),
                    ('orderDirection', 'order_direction_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}/observations'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_patient_entered_observations_by_code(client):
    """Test case for get_patient_entered_observations_by_code

    Get patient entered Observations of a Certain Type For a User
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}/observations/{code}/patiententered'.format(user_id=56, code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

