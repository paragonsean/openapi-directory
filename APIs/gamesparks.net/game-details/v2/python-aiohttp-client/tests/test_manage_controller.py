# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.manage_item_summary import ManageItemSummary
from openapi_server.models.manage_query import ManageQuery
from openapi_server.models.manage_result import ManageResult
from openapi_server.models.manage_screen import ManageScreen
from openapi_server.models.manage_snapshot import ManageSnapshot
from openapi_server.models.manage_snippet import ManageSnippet
from openapi_server.models.message_model import MessageModel
from openapi_server.models.snapshot_creation_model import SnapshotCreationModel


pytestmark = pytest.mark.asyncio

async def test_copy_snapshot_to_existing_game_using_post(client):
    """Test case for copy_snapshot_to_existing_game_using_post

    copySnapshotToExistingGame
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/snapshots/{snapshot_id}/copy/to/{target_api_key}'.format(api_key='api_key_example', snapshot_id='snapshot_id_example', target_api_key='target_api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_query_using_post(client):
    """Test case for create_query_using_post

    createQuery
    """
    body = {"qbRules":"qbRules","esRules":"esRules","name":"name","shortCode":"shortCode"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/queries'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_screen_using_post(client):
    """Test case for create_screen_using_post

    createScreen
    """
    body = {"template":"template","name":"name","groups":["groups","groups"],"shortCode":"shortCode"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/screens'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_snapshot_using_post(client):
    """Test case for create_snapshot_using_post

    createSnapshot
    """
    body = {"description":"description"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/snapshots'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_snippet_using_post(client):
    """Test case for create_snippet_using_post

    createSnippet
    """
    body = {"template":"template","name":"name","groups":["groups","groups"],"script":"script","shortCode":"shortCode","scriptData":"scriptData"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/snippets'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_query_using_delete(client):
    """Test case for delete_query_using_delete

    deleteQuery
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/restv2/game/{api_key}/manage/queries/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_screen_using_delete(client):
    """Test case for delete_screen_using_delete

    deleteScreen
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/restv2/game/{api_key}/manage/screens/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_snapshot_using_delete(client):
    """Test case for delete_snapshot_using_delete

    deleteSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/restv2/game/{api_key}/manage/snapshots/{snapshot_id}'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_snippet_using_delete(client):
    """Test case for delete_snippet_using_delete

    deleteSnippet
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/restv2/game/{api_key}/manage/snippets/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_using_get(client):
    """Test case for get_query_using_get

    getQuery
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/queries/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_screen_using_get(client):
    """Test case for get_screen_using_get

    getScreen
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/screens/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snippet_using_get(client):
    """Test case for get_snippet_using_get

    getSnippet
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/snippets/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_executable_screens_using_get(client):
    """Test case for list_executable_screens_using_get

    listExecutableScreens
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/screens/executable'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_queries_using_get(client):
    """Test case for list_queries_using_get

    listQueries
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/queries'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_screens_using_get(client):
    """Test case for list_screens_using_get

    listScreens
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/screens'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_snapshots_using_get(client):
    """Test case for list_snapshots_using_get

    listSnapshots
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/snapshots'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_snippets_using_get(client):
    """Test case for list_snippets_using_get

    listSnippets
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/snippets'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_snapshot_using_post(client):
    """Test case for publish_snapshot_using_post

    publishSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/snapshots/{snapshot_id}/publish'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revert_snapshot_using_post(client):
    """Test case for revert_snapshot_using_post

    revertSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/snapshots/{snapshot_id}/revert'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_query_using_put(client):
    """Test case for update_query_using_put

    updateQuery
    """
    body = {"qbRules":"qbRules","esRules":"esRules","name":"name","shortCode":"shortCode"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/restv2/game/{api_key}/manage/queries/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_screen_using_put(client):
    """Test case for update_screen_using_put

    updateScreen
    """
    body = {"template":"template","name":"name","groups":["groups","groups"],"shortCode":"shortCode"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/restv2/game/{api_key}/manage/screens/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_snippet_using_put(client):
    """Test case for update_snippet_using_put

    updateSnippet
    """
    body = {"template":"template","name":"name","groups":["groups","groups"],"script":"script","shortCode":"shortCode","scriptData":"scriptData"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/restv2/game/{api_key}/manage/snippets/{short_code}'.format(api_key='api_key_example', short_code='short_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

