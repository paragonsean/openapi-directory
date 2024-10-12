# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_diff_html_using_get200_response import CreateDiffHTMLUsingGET200Response
from openapi_server.models.get_chat_head_using_get200_response import GetChatHeadUsingGET200Response
from openapi_server.models.get_chat_history_using_get200_response import GetChatHistoryUsingGET200Response
from openapi_server.models.get_html_using_get200_response import GetHTMLUsingGET200Response
from openapi_server.models.get_last_edited_using_get200_response import GetLastEditedUsingGET200Response
from openapi_server.models.get_public_status_using_get200_response import GetPublicStatusUsingGET200Response
from openapi_server.models.get_read_only_id_using_get200_response import GetReadOnlyIDUsingGET200Response
from openapi_server.models.get_revisions_count_using_get200_response import GetRevisionsCountUsingGET200Response
from openapi_server.models.get_text_using_get200_response import GetTextUsingGET200Response
from openapi_server.models.list_all_pads_using_get200_response import ListAllPadsUsingGET200Response
from openapi_server.models.list_authors_of_pad_using_get200_response import ListAuthorsOfPadUsingGET200Response
from openapi_server.models.pad_users_count_using_get200_response import PadUsersCountUsingGET200Response
from openapi_server.models.pad_users_using_get200_response import PadUsersUsingGET200Response


pytestmark = pytest.mark.asyncio

async def test_append_chat_message_using_get(client):
    """Test case for append_chat_message_using_get

    appends a chat message
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example'),
                    ('authorID', 'author_id_example'),
                    ('time', 'time_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/appendChatMessage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_append_chat_message_using_post(client):
    """Test case for append_chat_message_using_post

    appends a chat message
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example'),
                    ('authorID', 'author_id_example'),
                    ('time', 'time_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/appendChatMessage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_token_using_get(client):
    """Test case for check_token_using_get

    returns ok when the current api token is valid
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/checkToken',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_token_using_post(client):
    """Test case for check_token_using_post

    returns ok when the current api token is valid
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/checkToken',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_diff_html_using_get(client):
    """Test case for create_diff_html_using_get

    
    """
    params = [('padID', 'pad_id_example'),
                    ('startRev', 'start_rev_example'),
                    ('endRev', 'end_rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createDiffHTML',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_diff_html_using_post(client):
    """Test case for create_diff_html_using_post

    
    """
    params = [('padID', 'pad_id_example'),
                    ('startRev', 'start_rev_example'),
                    ('endRev', 'end_rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createDiffHTML',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_pad_using_get(client):
    """Test case for create_pad_using_get

    
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_pad_using_post(client):
    """Test case for create_pad_using_post

    
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pad_using_get(client):
    """Test case for delete_pad_using_get

    deletes a pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/deletePad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pad_using_post(client):
    """Test case for delete_pad_using_post

    deletes a pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/deletePad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chat_head_using_get(client):
    """Test case for get_chat_head_using_get

    returns the chatHead (chat-message) of the pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getChatHead',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chat_head_using_post(client):
    """Test case for get_chat_head_using_post

    returns the chatHead (chat-message) of the pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getChatHead',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chat_history_using_get(client):
    """Test case for get_chat_history_using_get

    returns the chat history
    """
    params = [('padID', 'pad_id_example'),
                    ('start', 'start_example'),
                    ('end', 'end_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getChatHistory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chat_history_using_post(client):
    """Test case for get_chat_history_using_post

    returns the chat history
    """
    params = [('padID', 'pad_id_example'),
                    ('start', 'start_example'),
                    ('end', 'end_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getChatHistory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_html_using_get(client):
    """Test case for get_html_using_get

    returns the text of a pad formatted as HTML
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getHTML',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_html_using_post(client):
    """Test case for get_html_using_post

    returns the text of a pad formatted as HTML
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getHTML',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_edited_using_get(client):
    """Test case for get_last_edited_using_get

    returns the timestamp of the last revision of the pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getLastEdited',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_edited_using_post(client):
    """Test case for get_last_edited_using_post

    returns the timestamp of the last revision of the pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getLastEdited',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_status_using_get(client):
    """Test case for get_public_status_using_get

    return true of false
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getPublicStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_status_using_post(client):
    """Test case for get_public_status_using_post

    return true of false
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getPublicStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_read_only_id_using_get(client):
    """Test case for get_read_only_id_using_get

    returns the read only link of a pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getReadOnlyID',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_read_only_id_using_post(client):
    """Test case for get_read_only_id_using_post

    returns the read only link of a pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getReadOnlyID',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_revisions_count_using_get(client):
    """Test case for get_revisions_count_using_get

    returns the number of revisions of this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getRevisionsCount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_revisions_count_using_post(client):
    """Test case for get_revisions_count_using_post

    returns the number of revisions of this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getRevisionsCount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_using_get(client):
    """Test case for get_text_using_get

    returns the text of a pad
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getText',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_using_post(client):
    """Test case for get_text_using_post

    returns the text of a pad
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getText',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_pads_using_get(client):
    """Test case for list_all_pads_using_get

    list all the pads
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listAllPads',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_pads_using_post(client):
    """Test case for list_all_pads_using_post

    list all the pads
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listAllPads',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_authors_of_pad_using_get(client):
    """Test case for list_authors_of_pad_using_get

    returns an array of authors who contributed to this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listAuthorsOfPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_authors_of_pad_using_post(client):
    """Test case for list_authors_of_pad_using_post

    returns an array of authors who contributed to this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listAuthorsOfPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pad_users_count_using_get(client):
    """Test case for pad_users_count_using_get

    returns the number of user that are currently editing this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/padUsersCount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pad_users_count_using_post(client):
    """Test case for pad_users_count_using_post

    returns the number of user that are currently editing this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/padUsersCount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pad_users_using_get(client):
    """Test case for pad_users_using_get

    returns the list of users that are currently editing this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/padUsers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pad_users_using_post(client):
    """Test case for pad_users_using_post

    returns the list of users that are currently editing this pad
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/padUsers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_clients_message_using_get(client):
    """Test case for send_clients_message_using_get

    sends a custom message of type msg to the pad
    """
    params = [('padID', 'pad_id_example'),
                    ('msg', 'msg_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sendClientsMessage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_clients_message_using_post(client):
    """Test case for send_clients_message_using_post

    sends a custom message of type msg to the pad
    """
    params = [('padID', 'pad_id_example'),
                    ('msg', 'msg_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sendClientsMessage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_html_using_get(client):
    """Test case for set_html_using_get

    sets the text of a pad with HTML
    """
    params = [('padID', 'pad_id_example'),
                    ('html', 'html_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setHTML',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_html_using_post(client):
    """Test case for set_html_using_post

    sets the text of a pad with HTML
    """
    params = [('padID', 'pad_id_example'),
                    ('html', 'html_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setHTML',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_public_status_using_get(client):
    """Test case for set_public_status_using_get

    sets a boolean for the public status of a pad
    """
    params = [('padID', 'pad_id_example'),
                    ('publicStatus', 'public_status_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setPublicStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_public_status_using_post(client):
    """Test case for set_public_status_using_post

    sets a boolean for the public status of a pad
    """
    params = [('padID', 'pad_id_example'),
                    ('publicStatus', 'public_status_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setPublicStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_text_using_get(client):
    """Test case for set_text_using_get

    sets the text of a pad
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setText',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_text_using_post(client):
    """Test case for set_text_using_post

    sets the text of a pad
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setText',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

