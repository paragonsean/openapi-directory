# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_patient_request import CreatePatientRequest
from openapi_server.models.create_patient_response import CreatePatientResponse
from openapi_server.models.fetch_coaches_response import FetchCoachesResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse
from openapi_server.models.fetch_patient_response import FetchPatientResponse
from openapi_server.models.fetch_patients_response import FetchPatientsResponse
from openapi_server.models.update_patient_request import UpdatePatientRequest
from openapi_server.models.update_patient_response import UpdatePatientResponse
from openapi_server.models.upsert_patient_request import UpsertPatientRequest


pytestmark = pytest.mark.asyncio

async def test_create_patient(client):
    """Test case for create_patient

    Create a patient
    """
    body = openapi_server.CreatePatientRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/patient',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patient(client):
    """Test case for fetch_patient

    Get a patient
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_coaches(client):
    """Test case for fetch_patient_coaches

    List coaches for a patient
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient/{id}/coaches'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_groups(client):
    """Test case for fetch_patient_groups

    List groups for a patient
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient/{id}/groups'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patients(client):
    """Test case for fetch_patients

    List patients
    """
    params = [('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example'),
                    ('filter[identifier][system]', 'filter_identifier_system_example'),
                    ('filter[identifier][value]', 'filter_identifier_value_example'),
                    ('filter[archived]', True),
                    ('filter[created_at]', 'filter_created_at_example'),
                    ('filter[updated_at]', 'filter_updated_at_example'),
                    ('page[number]', 1),
                    ('page[size]', 10),
                    ('page[limit]', 50),
                    ('page[cursor]', 'page_cursor_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_patient(client):
    """Test case for update_patient

    Update a patient
    """
    body = openapi_server.UpdatePatientRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='PATCH',
        path='/pub/patient/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_patient(client):
    """Test case for upsert_patient

    Upsert patient
    """
    body = openapi_server.UpsertPatientRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='PUT',
        path='/pub/patient',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

