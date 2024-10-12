# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cms_data_block_interface import CmsDataBlockInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_cms_block_repository_v1_delete_by_id_delete(client):
    """Test case for cms_block_repository_v1_delete_by_id_delete

    cmsBlock/{blockId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/cmsBlock/{block_id}'.format(block_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cms_block_repository_v1_get_by_id_get(client):
    """Test case for cms_block_repository_v1_get_by_id_get

    cmsBlock/{blockId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/cmsBlock/{block_id}'.format(block_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

