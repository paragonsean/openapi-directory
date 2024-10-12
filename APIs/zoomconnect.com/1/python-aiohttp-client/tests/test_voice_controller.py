# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.web_service_send_voice_message_response import WebServiceSendVoiceMessageResponse
from openapi_server.models.web_service_voice_message import WebServiceVoiceMessage
from openapi_server.models.web_service_voice_message_send_single_text_request import WebServiceVoiceMessageSendSingleTextRequest
from openapi_server.models.web_service_voice_messages import WebServiceVoiceMessages


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_voice_all_get(client):
    """Test case for api_rest_v1_voice_all_get

    all
    """
    params = [('pageSize', 100),
                    ('page', 1),
                    ('status', 'status_example'),
                    ('fromDateTimeSent', '2013-10-20T19:20:30+01:00'),
                    ('toDateTimeSent', '2013-10-20T19:20:30+01:00'),
                    ('toNumber', 'to_number_example'),
                    ('message', 'message_example'),
                    ('campaign', 'campaign_example'),
                    ('dataField', 'data_field_example'),
                    ('deleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/voice/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_voice_message_id_delete(client):
    """Test case for api_rest_v1_voice_message_id_delete

    delete
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/app/api/rest/v1/voice/{message_id}'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_voice_message_id_get(client):
    """Test case for api_rest_v1_voice_message_id_get

    get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/voice/{message_id}'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_single_audio(client):
    """Test case for single_audio

    single-audio
    """
    params = [('recipientNumber', 'recipient_number_example'),
                    ('campaign', 'campaign_example'),
                    ('dataField', 'data_field_example'),
                    ('retryCount', 56),
                    ('retryMinimumInterval', 56),
                    ('retryMaximumInterval', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/voice/single-audio',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_single_text(client):
    """Test case for single_text

    single-text
    """
    body = {"dataField":"dataField","retryMinimumInterval":1,"retryMaximumInterval":6,"retryCount":0,"campaign":"campaign","language":"language","message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/voice/single-text',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

