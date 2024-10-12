# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clip_response_object import ClipResponseObject
from openapi_server.models.clips_response_object import ClipsResponseObject
from openapi_server.models.create_clip_request import CreateClipRequest
from openapi_server.models.create_media_request import CreateMediaRequest
from openapi_server.models.create_webhook_subscription_request import CreateWebhookSubscriptionRequest
from openapi_server.models.direct_upload_response_object import DirectUploadResponseObject
from openapi_server.models.media_response_object import MediaResponseObject
from openapi_server.models.medias_response_object import MediasResponseObject
from openapi_server.models.payment_required_error_response_object import PaymentRequiredErrorResponseObject
from openapi_server.models.too_many_requests_error_response_object import TooManyRequestsErrorResponseObject
from openapi_server.models.unauthorized_error_response_object import UnauthorizedErrorResponseObject
from openapi_server.models.update_clip_by_id_request import UpdateClipByIdRequest
from openapi_server.models.update_media_by_id_request import UpdateMediaByIdRequest
from openapi_server.models.webhook_subscription_response_object import WebhookSubscriptionResponseObject
from openapi_server.models.webhook_subscriptions_response_object import WebhookSubscriptionsResponseObject


pytestmark = pytest.mark.asyncio

async def test_create_clip(client):
    """Test case for create_clip

    create clip
    """
    body = openapi_server.CreateClipRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/clips',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_media(client):
    """Test case for create_media

    create media
    """
    body = openapi_server.CreateMediaRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/medias',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_webhook_subscription(client):
    """Test case for create_webhook_subscription

    create webhook subscription
    """
    body = openapi_server.CreateWebhookSubscriptionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/webhook_subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_clip_by_id(client):
    """Test case for delete_clip_by_id

    delete clip
    """
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/clips/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_media_by_id(client):
    """Test case for delete_media_by_id

    delete media
    """
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/medias/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_webhook_subscription_by_id(client):
    """Test case for delete_webhook_subscription_by_id

    delete webhook subscription
    """
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/webhook_subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_clip_by_id(client):
    """Test case for get_clip_by_id

    show clip
    """
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/clips/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_clips(client):
    """Test case for get_clips

    list clips
    """
    params = [('filter', {'key': {
  "filter[name_eq]": "john h. glenn, kindly air force base hospital",
  "filter[text_start]": "He landed in the sea"
}}),
                    ('page', {'key': {
  "page[number]": 1,
  "page[size]": 5
}}),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/clips',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_by_id(client):
    """Test case for get_media_by_id

    show media
    """
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/medias/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_medias(client):
    """Test case for get_medias

    list medias
    """
    params = [('filter', {'key': {
  "filter[name_eq]": "chimp into space",
  "filter[sourceUrl_start]": "https://archive.org"
}}),
                    ('page', {'key': {
  "page[number]": 1,
  "page[size]": 5
}}),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/medias',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upload_url(client):
    """Test case for get_upload_url

    prepare presigned upload url
    """
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/direct_uploads',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_subscription_by_id(client):
    """Test case for get_webhook_subscription_by_id

    show webhook subscription
    """
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhook_subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_subscriptions(client):
    """Test case for get_webhook_subscriptions

    list webhook subscriptions
    """
    params = [('filter', {'key': {
  "filter[name_eq]": "chimp into space"
}}),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhook_subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_clip_by_id(client):
    """Test case for update_clip_by_id

    update clip
    """
    body = openapi_server.UpdateClipByIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/clips/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_media_by_id(client):
    """Test case for update_media_by_id

    update media
    """
    body = openapi_server.UpdateMediaByIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'BearerHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/medias/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

