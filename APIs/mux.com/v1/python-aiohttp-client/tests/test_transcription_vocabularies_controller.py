# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_transcription_vocabulary_request import CreateTranscriptionVocabularyRequest
from openapi_server.models.list_transcription_vocabularies_response import ListTranscriptionVocabulariesResponse
from openapi_server.models.transcription_vocabulary_response import TranscriptionVocabularyResponse
from openapi_server.models.update_transcription_vocabulary_request import UpdateTranscriptionVocabularyRequest


pytestmark = pytest.mark.asyncio

async def test_create_transcription_vocabulary(client):
    """Test case for create_transcription_vocabulary

    Create a Transcription Vocabulary
    """
    body = {"name":"name","passthrough":"passthrough","phrases":[null,null,null,null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/transcription-vocabularies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transcription_vocabulary(client):
    """Test case for delete_transcription_vocabulary

    Delete a Transcription Vocabulary
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/transcription-vocabularies/{transcription_vocabulary_id}'.format(transcription_vocabulary_id='transcription_vocabulary_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transcription_vocabulary(client):
    """Test case for get_transcription_vocabulary

    Retrieve a Transcription Vocabulary
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/transcription-vocabularies/{transcription_vocabulary_id}'.format(transcription_vocabulary_id='transcription_vocabulary_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcription_vocabularies(client):
    """Test case for list_transcription_vocabularies

    List Transcription Vocabularies
    """
    params = [('limit', 10),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/transcription-vocabularies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transcription_vocabulary(client):
    """Test case for update_transcription_vocabulary

    Update a Transcription Vocabulary
    """
    body = {"name":"name","passthrough":"passthrough","phrases":[null,null,null,null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/transcription-vocabularies/{transcription_vocabulary_id}'.format(transcription_vocabulary_id='transcription_vocabulary_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

