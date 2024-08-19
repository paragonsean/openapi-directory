from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_transcription_vocabulary_request import CreateTranscriptionVocabularyRequest
from openapi_server.models.list_transcription_vocabularies_response import ListTranscriptionVocabulariesResponse
from openapi_server.models.transcription_vocabulary_response import TranscriptionVocabularyResponse
from openapi_server.models.update_transcription_vocabulary_request import UpdateTranscriptionVocabularyRequest
from openapi_server import util


async def create_transcription_vocabulary(request: web.Request, body) -> web.Response:
    """Create a Transcription Vocabulary

    Create a new Transcription Vocabulary.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateTranscriptionVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_transcription_vocabulary(request: web.Request, transcription_vocabulary_id) -> web.Response:
    """Delete a Transcription Vocabulary

    Deletes a Transcription Vocabulary. The Transcription Vocabulary&#39;s ID will be disassociated from any live streams using it. Transcription Vocabularies can be deleted while associated live streams are active. However, the words and phrases in the deleted Transcription Vocabulary will remain attached to those streams while they are active.

    :param transcription_vocabulary_id: The ID of the Transcription Vocabulary.
    :type transcription_vocabulary_id: str

    """
    return web.Response(status=200)


async def get_transcription_vocabulary(request: web.Request, transcription_vocabulary_id) -> web.Response:
    """Retrieve a Transcription Vocabulary

    Retrieves the details of a Transcription Vocabulary that has previously been created. Supply the unique Transcription Vocabulary ID and Mux will return the corresponding Transcription Vocabulary information. The same information is returned when creating a Transcription Vocabulary.

    :param transcription_vocabulary_id: The ID of the Transcription Vocabulary.
    :type transcription_vocabulary_id: str

    """
    return web.Response(status=200)


async def list_transcription_vocabularies(request: web.Request, limit=None, page=None) -> web.Response:
    """List Transcription Vocabularies

    List all Transcription Vocabularies.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int

    """
    return web.Response(status=200)


async def update_transcription_vocabulary(request: web.Request, transcription_vocabulary_id, body) -> web.Response:
    """Update a Transcription Vocabulary

    Updates the details of a previously-created Transcription Vocabulary. Updates to Transcription Vocabularies are allowed while associated live streams are active. However, updates will not be applied to those streams while they are active.

    :param transcription_vocabulary_id: The ID of the Transcription Vocabulary.
    :type transcription_vocabulary_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTranscriptionVocabularyRequest.from_dict(body)
    return web.Response(status=200)
