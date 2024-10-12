# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.complete_attachment_upload_request import CompleteAttachmentUploadRequest
from openapi_server.models.create_participant_connection_request import CreateParticipantConnectionRequest
from openapi_server.models.create_participant_connection_response import CreateParticipantConnectionResponse
from openapi_server.models.disconnect_participant_request import DisconnectParticipantRequest
from openapi_server.models.get_attachment_request import GetAttachmentRequest
from openapi_server.models.get_attachment_response import GetAttachmentResponse
from openapi_server.models.get_transcript_request import GetTranscriptRequest
from openapi_server.models.get_transcript_response import GetTranscriptResponse
from openapi_server.models.send_event_request import SendEventRequest
from openapi_server.models.send_event_response import SendEventResponse
from openapi_server.models.send_message_request import SendMessageRequest
from openapi_server.models.send_message_response import SendMessageResponse
from openapi_server.models.start_attachment_upload_request import StartAttachmentUploadRequest
from openapi_server.models.start_attachment_upload_response import StartAttachmentUploadResponse


pytestmark = pytest.mark.asyncio

async def test_complete_attachment_upload(client):
    """Test case for complete_attachment_upload

    
    """
    body = {"AttachmentIds":"","ClientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/complete-attachment-upload#X-Amz-Bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_participant_connection(client):
    """Test case for create_participant_connection

    
    """
    body = {"Type":"","ConnectParticipant":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/connection#X-Amz-Bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disconnect_participant(client):
    """Test case for disconnect_participant

    
    """
    body = {"ClientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/disconnect#X-Amz-Bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attachment(client):
    """Test case for get_attachment

    
    """
    body = {"AttachmentId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/attachment#X-Amz-Bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transcript(client):
    """Test case for get_transcript

    
    """
    body = {"NextToken":"","ScanDirection":"","MaxResults":"","SortOrder":"","ContactId":"","StartPosition":{"AbsoluteTime":"","MostRecent":"","Id":""}}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/transcript#X-Amz-Bearer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_event(client):
    """Test case for send_event

    
    """
    body = {"ContentType":"","Content":"","ClientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/event#X-Amz-Bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_message(client):
    """Test case for send_message

    
    """
    body = {"ContentType":"","Content":"","ClientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/message#X-Amz-Bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_attachment_upload(client):
    """Test case for start_attachment_upload

    
    """
    body = {"AttachmentSizeInBytes":"","ContentType":"","AttachmentName":"","ClientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_bearer': 'x_amz_bearer_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/participant/start-attachment-upload#X-Amz-Bearer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

