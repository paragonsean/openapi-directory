# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_session_response import GetSessionResponse
from openapi_server.models.post_content_request import PostContentRequest
from openapi_server.models.post_content_response import PostContentResponse
from openapi_server.models.post_text_request import PostTextRequest
from openapi_server.models.post_text_response import PostTextResponse


pytestmark = pytest.mark.asyncio

async def test_get_session(client):
    """Test case for get_session

    
    """
    params = [('checkpointLabelFilter', 'checkpoint_label_filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bot/{bot_name}/alias/{bot_alias}/user/{user_id}/session'.format(bot_name='bot_name_example', bot_alias='bot_alias_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_content(client):
    """Test case for post_content

    
    """
    body = {"inputStream":""}
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
        'x_amz_lex_session_attributes': 'x_amz_lex_session_attributes_example',
        'x_amz_lex_request_attributes': 'x_amz_lex_request_attributes_example',
        'content_type': 'content_type_example',
        'accept': 'accept_example',
        'x_amz_lex_active_contexts': 'x_amz_lex_active_contexts_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bot/{bot_name}/alias/{bot_alias}/user/{user_id}/content#Content-Type'.format(bot_name='bot_name_example', bot_alias='bot_alias_example', user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_text(client):
    """Test case for post_text

    
    """
    body = {"requestAttributes":"","inputText":"","sessionAttributes":"","activeContexts":""}
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bot/{bot_name}/alias/{bot_alias}/user/{user_id}/text'.format(bot_name='bot_name_example', bot_alias='bot_alias_example', user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

