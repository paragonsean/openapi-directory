# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_atalk_bot(client):
    """Test case for atalk_bot

    Anonymous Talk
    """
    params = [('input', 'input_example'),
                    ('client_name', 'client_name_example'),
                    ('sessionid', 'sessionid_example'),
                    ('recent', 'recent_example')]
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/atalk/{app_id}/{botname}'.format(app_id='app_id_example', botname='botname_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compile_bot(client):
    """Test case for compile_bot

    Compile a bot
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bot/{app_id}/{botname}/verify'.format(app_id='app_id_example', botname='botname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_bot(client):
    """Test case for create_bot

    Create a bot
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bot/{app_id}/{botname}'.format(app_id='app_id_example', botname='botname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_debug_bot(client):
    """Test case for debug_bot

    Debug a bot conversation
    """
    params = [('input', 'input_example'),
                    ('client_name', 'client_name_example'),
                    ('sessionid', 'sessionid_example'),
                    ('that', 'that_example'),
                    ('topic', 'topic_example'),
                    ('extra', 'extra_example'),
                    ('reset', 'reset_example'),
                    ('trace', 'trace_example'),
                    ('reload', 'reload_example'),
                    ('recent', 'recent_example')]
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/talk/{app_id}/{botname}'.format(app_id='app_id_example', botname='botname_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bot(client):
    """Test case for delete_bot

    Delete a bot
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bot/{app_id}/{botname}'.format(app_id='app_id_example', botname='botname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bot_file1(client):
    """Test case for delete_bot_file1

    Delete a bot file (AIML, set, map, substitution)
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bot/{app_id}/{botname}/{file_kind}/{filename}'.format(app_id='app_id_example', botname='botname_example', file_kind='file_kind_example', filename='filename_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bot_file2(client):
    """Test case for delete_bot_file2

    Delete a bot file (pdefaults, properties)
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bot/{app_id}/{botname}/{file_kind}'.format(app_id='app_id_example', botname='botname_example', file_kind='file_kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bot_file1(client):
    """Test case for get_bot_file1

    Retrieve a bot file (AIML, set, map, substitution)
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bot/{app_id}/{botname}/{file_kind}/{filename}'.format(app_id='app_id_example', botname='botname_example', file_kind='file_kind_example', filename='filename_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bot_file2(client):
    """Test case for get_bot_file2

    Retrieve a bot file (pdefaults, properties)
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bot/{app_id}/{botname}/{file_kind}'.format(app_id='app_id_example', botname='botname_example', file_kind='file_kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bot_files(client):
    """Test case for list_bot_files

    List of bot files
    """
    params = [('return', '_return_example')]
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bot/{app_id}/{botname}'.format(app_id='app_id_example', botname='botname_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bots(client):
    """Test case for list_bots

    List of bots
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bot/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_upload_file1(client):
    """Test case for upload_file1

    Upload a bot file (AIML, set, substitution, map)
    """
    content = 'content_example'
    headers = { 
        'Content-Type': 'application/xml',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bot/{app_id}/{botname}/{file_kind}/{filename}'.format(app_id='app_id_example', botname='botname_example', file_kind='file_kind_example', filename='filename_example'),
        headers=headers,
        json=content,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_upload_file2(client):
    """Test case for upload_file2

    Upload a bot file (pdefaults, properties)
    """
    content = 'content_example'
    headers = { 
        'Content-Type': 'application/xml',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bot/{app_id}/{botname}/{file_kind}'.format(app_id='app_id_example', botname='botname_example', file_kind='file_kind_example'),
        headers=headers,
        json=content,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

