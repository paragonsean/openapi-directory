# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body_delete_history_items_v1_history_delete_post import BodyDeleteHistoryItemsV1HistoryDeletePost
from openapi_server.models.body_download_history_items_v1_history_download_post import BodyDownloadHistoryItemsV1HistoryDownloadPost
from openapi_server.models.get_history_response_model import GetHistoryResponseModel
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_delete_history_item_v1_history_history_item_id_delete(client):
    """Test case for delete_history_item_v1_history_history_item_id_delete

    Delete History Item
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/history/{history_item_id}'.format(history_item_id='VW7YKqPnjY4h39yTbx2L'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_history_items_v1_history_delete_post(client):
    """Test case for delete_history_items_v1_history_delete_post

    Delete History Items
    """
    body = openapi_server.BodyDeleteHistoryItemsV1HistoryDeletePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/history/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_history_items_v1_history_download_post(client):
    """Test case for download_history_items_v1_history_download_post

    Download History Items
    """
    body = openapi_server.BodyDownloadHistoryItemsV1HistoryDownloadPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/history/download',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audio_from_history_item_v1_history_history_item_id_audio_get(client):
    """Test case for get_audio_from_history_item_v1_history_history_item_id_audio_get

    Get Audio From History Item
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/history/{history_item_id}/audio'.format(history_item_id='VW7YKqPnjY4h39yTbx2L'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_generated_items_v1_history_get(client):
    """Test case for get_generated_items_v1_history_get

    Get Generated Items
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/history',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

