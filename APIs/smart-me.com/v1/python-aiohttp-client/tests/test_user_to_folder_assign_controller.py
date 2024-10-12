# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_user_to_folder_assign_delete(client):
    """Test case for user_to_folder_assign_delete

    Deletes a user to folder assignement
    """
    params = [('source', 'source_example'),
                    ('target', 'target_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/folder/user/assign',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_to_folder_assign_post(client):
    """Test case for user_to_folder_assign_post

    Assign a user to a folder
    """
    params = [('source', 'source_example'),
                    ('target', 'target_example'),
                    ('oldFolder', 'old_folder_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/folder/user/assign',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

