# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_folder_assign_post(client):
    """Test case for folder_assign_post

    Assign a folder (source) or meter to another folder (target). Can be used to create a folder structure.
    """
    params = [('source', 'source_example'),
                    ('target', 'target_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/folder/assign',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

