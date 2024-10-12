# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_timeline import CustomerTimeline
from openapi_server.models.customer_timeline_custom_event import CustomerTimelineCustomEvent
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError


pytestmark = pytest.mark.asyncio

async def test_delete_customer_timeline(client):
    """Test case for delete_customer_timeline

    Delete a Customer Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/customers/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_timeline(client):
    """Test case for get_customer_timeline

    Retrieve a customer Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customers/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_timeline_collection(client):
    """Test case for get_customer_timeline_collection

    Retrieve a list of customer timeline messages
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('sort', ['sort_example']),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customers/{id}/timeline'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_timeline_custom_event_type(client):
    """Test case for get_customer_timeline_custom_event_type

    Retrieve customer timeline custom event type with specified identifier string
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customer-timeline-custom-events/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_timeline_custom_event_type_collection(client):
    """Test case for get_customer_timeline_custom_event_type_collection

    Retrieve a list of customer timeline custom event types
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customer-timeline-custom-events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_timeline_event_collection(client):
    """Test case for get_customer_timeline_event_collection

    Retrieve a list of customer timeline messages for all customers
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customer-timeline-events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_customer_timeline(client):
    """Test case for post_customer_timeline

    Create a customer Timeline comment or custom defined event
    """
    body = {"customEventType":"customEventType","_links":[{"rel":"self"},{"rel":"self"}],"extraData":{"tables":[{"footer":"footer","title":"title","type":"list"},{"footer":"footer","title":"title","type":"list"}],"author":{"userFullName":"userFullName","userId":"userId"},"mentions":{"key":"{\"@test@mail.com\":\"userId-1\"}"},"links":[{"resourceId":"4f6cf35x-2c4y-483z-a0a9-158621f77a21","placeholder":"KYC Document","resourceType":"kyc-document"},{"resourceId":"4f6cf35x-2c4y-483z-a0a9-158621f77a21","placeholder":"KYC Document","resourceType":"kyc-document"}],"actions":[{"action":"resend-email"},{"action":"resend-email"}]},"occurredTime":"","customData":{"customAttribute":"customValue","otherAttribute":"otherValue"},"id":"","message":"message","type":"customer-comment-created","triggeredBy":"rebilly"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/customers/{id}/timeline'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

