# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.snapshot_creation_model import SnapshotCreationModel
from openapi_server.models.snapshot_creation_success_model import SnapshotCreationSuccessModel
from openapi_server.models.snapshot_model import SnapshotModel


pytestmark = pytest.mark.asyncio

async def test_copy_snapshot_to_existing_game_using_post1(client):
    """Test case for copy_snapshot_to_existing_game_using_post1

    copySnapshotToExistingGame
    """
    params = [('includeGameConfig', True),
                    ('includeMetadata', True),
                    ('includeBinaries', True),
                    ('includeCollaborators', True)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/snapshots/{snapshot_id}/copy/to/{target_api_key}'.format(api_key='api_key_example', snapshot_id='snapshot_id_example', target_api_key='target_api_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_snapshot_to_new_game_using_post(client):
    """Test case for copy_snapshot_to_new_game_using_post

    copySnapshotToNewGame
    """
    params = [('includeGameConfig', True),
                    ('includeMetadata', True),
                    ('includeBinaries', True),
                    ('includeCollaborators', True)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/snapshots/{snapshot_id}/copy'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_snapshots_using_post(client):
    """Test case for create_snapshots_using_post

    createSnapshots
    """
    body = {"description":"description"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/snapshots'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_snapshot_using_delete1(client):
    """Test case for delete_snapshot_using_delete1

    deleteSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/restv2/game/{api_key}/admin/snapshots/{snapshot_id}'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_snapshot_id_using_get(client):
    """Test case for get_live_snapshot_id_using_get

    getLiveSnapshotId
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/snapshots/liveSnapshotId'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snapshot_using_get(client):
    """Test case for get_snapshot_using_get

    getSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/snapshots/{snapshot_id}'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snapshots_using_get(client):
    """Test case for get_snapshots_using_get

    getSnapshots
    """
    params = [('pageSize', 20)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/snapshots/page/{page}'.format(api_key='api_key_example', page=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snapshots_using_get1(client):
    """Test case for get_snapshots_using_get1

    getSnapshots
    """
    params = [('pageSize', 20)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/snapshots'.format(api_key='api_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_snapshot_using_post1(client):
    """Test case for publish_snapshot_using_post1

    publishSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/snapshots/{snapshot_id}/publish'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revert_to_snapshot_using_post(client):
    """Test case for revert_to_snapshot_using_post

    revertToSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/snapshots/revert/to/{snapshot_id}'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unpublish_snapshot_using_post(client):
    """Test case for unpublish_snapshot_using_post

    unpublishSnapshot
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/snapshots/{snapshot_id}/unpublish'.format(api_key='api_key_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

