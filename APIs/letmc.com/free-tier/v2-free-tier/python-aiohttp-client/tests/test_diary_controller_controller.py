# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diary_allocation_model import DiaryAllocationModel
from openapi_server.models.diary_allocation_model_results import DiaryAllocationModelResults
from openapi_server.models.diary_appointment_model import DiaryAppointmentModel
from openapi_server.models.diary_appointment_model_results import DiaryAppointmentModelResults
from openapi_server.models.diary_appointment_type_model import DiaryAppointmentTypeModel
from openapi_server.models.diary_appointment_type_model_results import DiaryAppointmentTypeModelResults


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_diary_allocations_diary_allocation_idget(client):
    """Test case for v2_tier1_short_name_diary_allocations_diary_allocation_idget

    Get a specific diary allocation given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/diary/allocations/{diary_allocation_id}'.format(short_name='short_name_example', diary_allocation_id='diary_allocation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_diary_allocations_get(client):
    """Test case for v2_tier1_short_name_diary_allocations_get

    A collection of all diary allocations
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/diary/allocations'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_diary_appointments_diary_appointment_idget(client):
    """Test case for v2_tier1_short_name_diary_appointments_diary_appointment_idget

    Get a specific diary appointment given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/diary/appointments/{diary_appointment_id}'.format(short_name='short_name_example', diary_appointment_id='diary_appointment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_diary_appointments_get(client):
    """Test case for v2_tier1_short_name_diary_appointments_get

    A collection of all diary appointments
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/diary/appointments'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_diary_appointmenttypes_diary_appointment_type_idget(client):
    """Test case for v2_tier1_short_name_diary_appointmenttypes_diary_appointment_type_idget

    Get a specific diary appointment type given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/diary/appointmenttypes/{diary_appointment_type_id}'.format(short_name='short_name_example', diary_appointment_type_id='diary_appointment_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_diary_appointmenttypes_get(client):
    """Test case for v2_tier1_short_name_diary_appointmenttypes_get

    A collection of all diary appointment types
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/diary/appointmenttypes'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

