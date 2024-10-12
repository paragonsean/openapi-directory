# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_patient_health_result_response import FetchPatientHealthResultResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_health_result(client):
    """Test case for fetch_patient_health_result

    Get a patient health result
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/result/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_health_results(client):
    """Test case for fetch_patient_health_results

    List patient health results
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[actions]', 'filter_actions_example'),
                    ('filter[start_at]', 'filter_start_at_example'),
                    ('filter[end_at]', 'filter_end_at_example'),
                    ('filter[threads]', 'filter_threads_example'),
                    ('filter[created_at]', 'filter_created_at_example'),
                    ('filter[updated_at]', 'filter_updated_at_example'),
                    ('page[number]', 1),
                    ('page[size]', 10),
                    ('page[limit]', 50),
                    ('page[after]', 'page_after_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/result',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

