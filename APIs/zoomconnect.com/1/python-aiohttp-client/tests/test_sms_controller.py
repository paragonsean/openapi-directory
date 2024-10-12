# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_error_dto import RestErrorDTO
from openapi_server.models.web_service_send_sms_request import WebServiceSendSmsRequest
from openapi_server.models.web_service_send_sms_requests import WebServiceSendSmsRequests
from openapi_server.models.web_service_send_sms_response import WebServiceSendSmsResponse
from openapi_server.models.web_service_send_sms_responses import WebServiceSendSmsResponses


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_sms_send_bulk_get(client):
    """Test case for api_rest_v1_sms_send_bulk_get

    send-bulk
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/sms/send-bulk',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_sms_send_bulk_post(client):
    """Test case for api_rest_v1_sms_send_bulk_post

    send-bulk
    """
    body = {"sendSmsRequests":[{"dataField":"dataField","dateToSend":"2000-01-23T04:56:07.000+00:00","campaign":"campaign","message":"message","recipientNumber":"recipientNumber"},{"dataField":"dataField","dateToSend":"2000-01-23T04:56:07.000+00:00","campaign":"campaign","message":"message","recipientNumber":"recipientNumber"}],"defaultDateToSend":"2000-01-23T04:56:07.000+00:00","messagesPerMinute":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/sms/send-bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_sms_send_get(client):
    """Test case for api_rest_v1_sms_send_get

    send
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/sms/send',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_sms_send_post(client):
    """Test case for api_rest_v1_sms_send_post

    send
    """
    body = {"dataField":"dataField","dateToSend":"2000-01-23T04:56:07.000+00:00","campaign":"campaign","message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/sms/send',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_sms_send_url_parameters_get(client):
    """Test case for api_rest_v1_sms_send_url_parameters_get

    send-url-parameters
    """
    params = [('recipientNumber', 'recipient_number_example'),
                    ('message', 'message_example'),
                    ('dateToSend', '2013-10-20T19:20:30+01:00'),
                    ('campaign', 'campaign_example'),
                    ('dataField', 'data_field_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/sms/send-url-parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_sms_send_url_parameters_post(client):
    """Test case for api_rest_v1_sms_send_url_parameters_post

    send-url-parameters
    """
    params = [('recipientNumber', 'recipient_number_example'),
                    ('message', 'message_example'),
                    ('dateToSend', '2013-10-20T19:20:30+01:00'),
                    ('campaign', 'campaign_example'),
                    ('dataField', 'data_field_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/sms/send-url-parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_sms_send_url_token_get(client):
    """Test case for api_rest_v1_sms_send_url_token_get

    send-url
    """
    params = [('recipientNumber', 'recipient_number_example'),
                    ('message', 'message_example'),
                    ('dateToSend', '2013-10-20T19:20:30+01:00'),
                    ('campaign', 'campaign_example'),
                    ('dataField', 'data_field_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/sms/send-url/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_sms_send_url_token_post(client):
    """Test case for api_rest_v1_sms_send_url_token_post

    send-url
    """
    params = [('recipientNumber', 'recipient_number_example'),
                    ('message', 'message_example'),
                    ('dateToSend', '2013-10-20T19:20:30+01:00'),
                    ('campaign', 'campaign_example'),
                    ('dataField', 'data_field_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/sms/send-url/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

