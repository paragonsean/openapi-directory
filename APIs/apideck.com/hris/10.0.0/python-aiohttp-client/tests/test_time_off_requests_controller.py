# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_time_off_request_response import CreateTimeOffRequestResponse
from openapi_server.models.delete_time_off_request_response import DeleteTimeOffRequestResponse
from openapi_server.models.get_time_off_request_response import GetTimeOffRequestResponse
from openapi_server.models.get_time_off_requests_response import GetTimeOffRequestsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.time_off_request import TimeOffRequest
from openapi_server.models.time_off_requests_filter import TimeOffRequestsFilter
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_time_off_request_response import UpdateTimeOffRequestResponse


pytestmark = pytest.mark.asyncio

async def test_time_off_requests_add(client):
    """Test case for time_off_requests_add

    Create Time Off Request
    """
    body = {"end_date":"2022-04-01","amount":3.5,"approval_date":"2022-03-21","notes":{"manager":"Enjoy!","employee":"Relaxing on the beach for a few hours."},"policy_id":"12345","request_type":"vacation","created_at":"2020-09-30T07:43:32Z","description":"Enjoying some sun.","units":"hours","created_by":"12345","custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","employee_id":"12345","request_date":"2022-03-21","updated_by":"12345","id":"12345","start_date":"2022-04-01","status":"approved"}
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
        path='/hris/time-off-requests',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_off_requests_all(client):
    """Test case for time_off_requests_all

    List Time Off Requests
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.TimeOffRequestsFilter()),
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
        path='/hris/time-off-requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_off_requests_delete(client):
    """Test case for time_off_requests_delete

    Delete Time Off Request
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
        path='/hris/time-off-requests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_off_requests_one(client):
    """Test case for time_off_requests_one

    Get Time Off Request
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
        path='/hris/time-off-requests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_off_requests_update(client):
    """Test case for time_off_requests_update

    Update Time Off Request
    """
    body = {"end_date":"2022-04-01","amount":3.5,"approval_date":"2022-03-21","notes":{"manager":"Enjoy!","employee":"Relaxing on the beach for a few hours."},"policy_id":"12345","request_type":"vacation","created_at":"2020-09-30T07:43:32Z","description":"Enjoying some sun.","units":"hours","created_by":"12345","custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","employee_id":"12345","request_date":"2022-03-21","updated_by":"12345","id":"12345","start_date":"2022-04-01","status":"approved"}
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
        path='/hris/time-off-requests/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

