# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_rma_track_management_v1_remove_track_by_id_delete(client):
    """Test case for rma_track_management_v1_remove_track_by_id_delete

    returns/{id}/tracking-numbers/{trackId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/returns/{id}/tracking-numbers/{track_id}'.format(id=56, track_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

