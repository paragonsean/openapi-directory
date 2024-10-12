# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_pipeline_response import CreatePipelineResponse
from openapi_server.models.delete_pipeline_response import DeletePipelineResponse
from openapi_server.models.get_pipeline_response import GetPipelineResponse
from openapi_server.models.get_pipelines_response import GetPipelinesResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.pipeline import Pipeline
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_pipeline_response import UpdatePipelineResponse


pytestmark = pytest.mark.asyncio

async def test_pipelines_add(client):
    """Test case for pipelines_add

    Create pipeline
    """
    body = {"archived":False,"win_probability_enabled":True,"updated_at":"2020-09-30T07:43:32Z","display_order":1,"name":"Sales Pipeline","stages":[{"win_probability":50,"display_order":1,"name":"Contract Sent","id":"contractsent","value":"CONTRACT_SENT"},{"win_probability":50,"display_order":1,"name":"Contract Sent","id":"contractsent","value":"CONTRACT_SENT"}],"active":False,"created_at":"2020-09-30T07:43:32Z","currency":"USD","id":"default"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/crm/pipelines',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_all(client):
    """Test case for pipelines_all

    List pipelines
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('pass_through', None),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/pipelines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_delete(client):
    """Test case for pipelines_delete

    Delete pipeline
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/crm/pipelines/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_one(client):
    """Test case for pipelines_one

    Get pipeline
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/pipelines/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_update(client):
    """Test case for pipelines_update

    Update pipeline
    """
    body = {"archived":False,"win_probability_enabled":True,"updated_at":"2020-09-30T07:43:32Z","display_order":1,"name":"Sales Pipeline","stages":[{"win_probability":50,"display_order":1,"name":"Contract Sent","id":"contractsent","value":"CONTRACT_SENT"},{"win_probability":50,"display_order":1,"name":"Contract Sent","id":"contractsent","value":"CONTRACT_SENT"}],"active":False,"created_at":"2020-09-30T07:43:32Z","currency":"USD","id":"default"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/crm/pipelines/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

