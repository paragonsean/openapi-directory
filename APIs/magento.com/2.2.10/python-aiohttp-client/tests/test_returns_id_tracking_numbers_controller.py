# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rma_data_track_search_result_interface import RmaDataTrackSearchResultInterface
from openapi_server.models.rma_track_management_v1_add_track_post_request import RmaTrackManagementV1AddTrackPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rma_track_management_v1_add_track_post(client):
    """Test case for rma_track_management_v1_add_track_post

    returns/{id}/tracking-numbers
    """
    body = openapi_server.RmaTrackManagementV1AddTrackPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/returns/{id}/tracking-numbers'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rma_track_management_v1_get_tracks_get(client):
    """Test case for rma_track_management_v1_get_tracks_get

    returns/{id}/tracking-numbers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/returns/{id}/tracking-numbers'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

