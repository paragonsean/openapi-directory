# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain_topic import DomainTopic
from openapi_server.models.domain_topics_list_result import DomainTopicsListResult


pytestmark = pytest.mark.asyncio

async def test_domain_topics_create_or_update(client):
    """Test case for domain_topics_create_or_update

    Create or update a domain topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}/topics/{domain_topic_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example', domain_topic_name='domain_topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_topics_delete(client):
    """Test case for domain_topics_delete

    Delete a domain topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}/topics/{domain_topic_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example', domain_topic_name='domain_topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_topics_get(client):
    """Test case for domain_topics_get

    Get a domain topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}/topics/{domain_topic_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example', domain_topic_name='domain_topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_topics_list_by_domain(client):
    """Test case for domain_topics_list_by_domain

    List domain topics.
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}/topics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

