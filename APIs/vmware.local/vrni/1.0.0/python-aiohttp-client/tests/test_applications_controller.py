# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.application import Application
from openapi_server.models.application_request import ApplicationRequest
from openapi_server.models.paged_list_response import PagedListResponse
from openapi_server.models.tier import Tier
from openapi_server.models.tier_list_response import TierListResponse
from openapi_server.models.tier_request import TierRequest


pytestmark = pytest.mark.asyncio

async def test_add_application(client):
    """Test case for add_application

    Create an application
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups/applications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_tier(client):
    """Test case for add_tier

    Create tier in application
    """
    body = {"group_membership_criteria":[{"membership_type":"SearchMembershipCriteria","search_membership_criteria":{"entity_type":"VirtualMachine","filter":"security_groups.entity_id = '18230:82:604573173'"}}],"name":"tier-1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups/applications/{id}/tiers'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_application(client):
    """Test case for delete_application

    Delete an application
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/applications/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tier(client):
    """Test case for delete_tier

    Delete tier
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/applications/{id}/tiers/{tier_id}'.format(id='id_example', tier_id='tier_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application(client):
    """Test case for get_application

    Show application details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/applications/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_tier(client):
    """Test case for get_application_tier

    Show tier details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/applications/{id}/tiers/{tier_id}'.format(id='id_example', tier_id='tier_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tier(client):
    """Test case for get_tier

    Show tier details
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/tiers/{tier_id}'.format(tier_id='tier_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_application_tiers(client):
    """Test case for list_application_tiers

    List tiers of an application
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/applications/{id}/tiers'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_applications(client):
    """Test case for list_applications

    List applications
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/applications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

