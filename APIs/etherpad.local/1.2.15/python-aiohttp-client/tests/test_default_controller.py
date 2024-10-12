# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response


pytestmark = pytest.mark.asyncio

async def test_append_text_using_get(client):
    """Test case for append_text_using_get

    
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/appendText',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_append_text_using_post(client):
    """Test case for append_text_using_post

    
    """
    params = [('padID', 'pad_id_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/appendText',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_pad_using_get(client):
    """Test case for copy_pad_using_get

    
    """
    params = [('sourceID', 'source_id_example'),
                    ('destinationID', 'destination_id_example'),
                    ('force', 'force_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/copyPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_pad_using_post(client):
    """Test case for copy_pad_using_post

    
    """
    params = [('sourceID', 'source_id_example'),
                    ('destinationID', 'destination_id_example'),
                    ('force', 'force_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/copyPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_pad_without_history_using_get(client):
    """Test case for copy_pad_without_history_using_get

    
    """
    params = [('sourceID', 'source_id_example'),
                    ('destinationID', 'destination_id_example'),
                    ('force', 'force_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/copyPadWithoutHistory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_pad_without_history_using_post(client):
    """Test case for copy_pad_without_history_using_post

    
    """
    params = [('sourceID', 'source_id_example'),
                    ('destinationID', 'destination_id_example'),
                    ('force', 'force_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/copyPadWithoutHistory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attribute_pool_using_get(client):
    """Test case for get_attribute_pool_using_get

    
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getAttributePool',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attribute_pool_using_post(client):
    """Test case for get_attribute_pool_using_post

    
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getAttributePool',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pad_id_using_get(client):
    """Test case for get_pad_id_using_get

    
    """
    params = [('roID', 'ro_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getPadID',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pad_id_using_post(client):
    """Test case for get_pad_id_using_post

    
    """
    params = [('roID', 'ro_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getPadID',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_revision_changeset_using_get(client):
    """Test case for get_revision_changeset_using_get

    
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getRevisionChangeset',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_revision_changeset_using_post(client):
    """Test case for get_revision_changeset_using_post

    
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getRevisionChangeset',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_saved_revisions_count_using_get(client):
    """Test case for get_saved_revisions_count_using_get

    
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getSavedRevisionsCount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_saved_revisions_count_using_post(client):
    """Test case for get_saved_revisions_count_using_post

    
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getSavedRevisionsCount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stats_using_get(client):
    """Test case for get_stats_using_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getStats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stats_using_post(client):
    """Test case for get_stats_using_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getStats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_saved_revisions_using_get(client):
    """Test case for list_saved_revisions_using_get

    
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listSavedRevisions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_saved_revisions_using_post(client):
    """Test case for list_saved_revisions_using_post

    
    """
    params = [('padID', 'pad_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listSavedRevisions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_pad_using_get(client):
    """Test case for move_pad_using_get

    
    """
    params = [('sourceID', 'source_id_example'),
                    ('destinationID', 'destination_id_example'),
                    ('force', 'force_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/movePad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_pad_using_post(client):
    """Test case for move_pad_using_post

    
    """
    params = [('sourceID', 'source_id_example'),
                    ('destinationID', 'destination_id_example'),
                    ('force', 'force_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/movePad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_revision_using_get(client):
    """Test case for restore_revision_using_get

    
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/restoreRevision',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_revision_using_post(client):
    """Test case for restore_revision_using_post

    
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/restoreRevision',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_revision_using_get(client):
    """Test case for save_revision_using_get

    
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/saveRevision',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_revision_using_post(client):
    """Test case for save_revision_using_post

    
    """
    params = [('padID', 'pad_id_example'),
                    ('rev', 'rev_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/saveRevision',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

