# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.delete_characters_character_id_mail_labels_label_id_unprocessable_entity import DeleteCharactersCharacterIdMailLabelsLabelIdUnprocessableEntity
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_mail200_ok import GetCharactersCharacterIdMail200Ok
from openapi_server.models.get_characters_character_id_mail_labels_ok import GetCharactersCharacterIdMailLabelsOk
from openapi_server.models.get_characters_character_id_mail_lists200_ok import GetCharactersCharacterIdMailLists200Ok
from openapi_server.models.get_characters_character_id_mail_mail_id_not_found import GetCharactersCharacterIdMailMailIdNotFound
from openapi_server.models.get_characters_character_id_mail_mail_id_ok import GetCharactersCharacterIdMailMailIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_mail_error520 import PostCharactersCharacterIdMailError520
from openapi_server.models.post_characters_character_id_mail_labels_label import PostCharactersCharacterIdMailLabelsLabel
from openapi_server.models.post_characters_character_id_mail_mail import PostCharactersCharacterIdMailMail
from openapi_server.models.put_characters_character_id_mail_mail_id_contents import PutCharactersCharacterIdMailMailIdContents
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_delete_characters_character_id_mail_labels_label_id(client):
    """Test case for delete_characters_character_id_mail_labels_label_id

    Delete a mail label
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/latest/characters/{character_id}/mail/labels/{label_id}'.format(character_id=56, label_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_characters_character_id_mail_mail_id(client):
    """Test case for delete_characters_character_id_mail_mail_id

    Delete a mail
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/latest/characters/{character_id}/mail/{mail_id}'.format(character_id=56, mail_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_mail(client):
    """Test case for get_characters_character_id_mail

    Return mail headers
    """
    params = [('datasource', tranquility),
                    ('labels', [56]),
                    ('last_mail_id', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/mail'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_mail_labels(client):
    """Test case for get_characters_character_id_mail_labels

    Get mail labels and unread counts
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/mail/labels'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_mail_lists(client):
    """Test case for get_characters_character_id_mail_lists

    Return mailing list subscriptions
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/mail/lists'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_mail_mail_id(client):
    """Test case for get_characters_character_id_mail_mail_id

    Return a mail
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/mail/{mail_id}'.format(character_id=56, mail_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_character_id_mail(client):
    """Test case for post_characters_character_id_mail

    Send a new mail
    """
    mail = openapi_server.PostCharactersCharacterIdMailMail()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/{character_id}/mail'.format(character_id=56),
        headers=headers,
        json=mail,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_character_id_mail_labels(client):
    """Test case for post_characters_character_id_mail_labels

    Create a mail label
    """
    label = openapi_server.PostCharactersCharacterIdMailLabelsLabel()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/{character_id}/mail/labels'.format(character_id=56),
        headers=headers,
        json=label,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_characters_character_id_mail_mail_id(client):
    """Test case for put_characters_character_id_mail_mail_id

    Update metadata about a mail
    """
    contents = openapi_server.PutCharactersCharacterIdMailMailIdContents()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/latest/characters/{character_id}/mail/{mail_id}'.format(character_id=56, mail_id=56),
        headers=headers,
        json=contents,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

