# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_patient_health_metric_request import CreatePatientHealthMetricRequest
from openapi_server.models.create_patient_health_metric_response import CreatePatientHealthMetricResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_patient_health_metric_response import FetchPatientHealthMetricResponse


pytestmark = pytest.mark.asyncio

async def test_create_patient_health_metric(client):
    """Test case for create_patient_health_metric

    Create patient health metrics
    """
    body = openapi_server.CreatePatientHealthMetricRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/patient_health_metric',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_health_metric(client):
    """Test case for fetch_patient_health_metric

    Get a patient health metric
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient_health_metric/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_health_metrics(client):
    """Test case for fetch_patient_health_metrics

    List patient health metrics
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example'),
                    ('page[number]', 1),
                    ('page[size]', 10),
                    ('page[limit]', 50),
                    ('page[cursor]', 'page_cursor_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient_health_metric',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

