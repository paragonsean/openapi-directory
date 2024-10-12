# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_staff_model import ApplicationStaffModel
from openapi_server.models.application_staff_model_results import ApplicationStaffModelResults


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_staff_staff_application_staff_idget(client):
    """Test case for v2_tier1_short_name_staff_staff_application_staff_idget

    Get a specific application staff given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/staff/staff/{application_staff_id}'.format(short_name='short_name_example', application_staff_id='application_staff_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_staff_staff_get(client):
    """Test case for v2_tier1_short_name_staff_staff_get

    A collection of all the staff members linked to a specific company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/staff/staff'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

