# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lab_test_details import LabTestDetails
from openapi_server.models.lab_test_public import LabTestPublic


pytestmark = pytest.mark.asyncio

async def test_get_all_lab_tests(client):
    """Test case for get_all_lab_tests

    List all lab tests
    """
    params = [('age.value', 18),
                    ('age.unit', year)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/lab_tests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lab_test(client):
    """Test case for get_lab_test

    Get lab test by id
    """
    params = [('age.value', 18),
                    ('age.unit', year)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/lab_tests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

