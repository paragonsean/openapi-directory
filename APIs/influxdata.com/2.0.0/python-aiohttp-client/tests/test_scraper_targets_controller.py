# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server.models.scraper_target_request import ScraperTargetRequest
from openapi_server.models.scraper_target_response import ScraperTargetResponse
from openapi_server.models.scraper_target_responses import ScraperTargetResponses


pytestmark = pytest.mark.asyncio

async def test_delete_scrapers_id(client):
    """Test case for delete_scrapers_id

    Delete a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/scrapers/{scraper_target_id}'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_scrapers_id_labels_id(client):
    """Test case for delete_scrapers_id_labels_id

    Delete a label from a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/scrapers/{scraper_target_id}/labels/{label_id}'.format(scraper_target_id='scraper_target_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_scrapers_id_members_id(client):
    """Test case for delete_scrapers_id_members_id

    Remove a member from a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/scrapers/{scraper_target_id}/members/{user_id}'.format(user_id='user_id_example', scraper_target_id='scraper_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_scrapers_id_owners_id(client):
    """Test case for delete_scrapers_id_owners_id

    Remove an owner from a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/scrapers/{scraper_target_id}/owners/{user_id}'.format(user_id='user_id_example', scraper_target_id='scraper_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scrapers(client):
    """Test case for get_scrapers

    List all scraper targets
    """
    params = [('name', 'name_example'),
                    ('id', ['id_example']),
                    ('orgID', 'org_id_example'),
                    ('org', 'org_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/scrapers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scrapers_id(client):
    """Test case for get_scrapers_id

    Retrieve a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/scrapers/{scraper_target_id}'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scrapers_id_labels(client):
    """Test case for get_scrapers_id_labels

    List all labels for a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/scrapers/{scraper_target_id}/labels'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scrapers_id_members(client):
    """Test case for get_scrapers_id_members

    List all users with member privileges for a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/scrapers/{scraper_target_id}/members'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scrapers_id_owners(client):
    """Test case for get_scrapers_id_owners

    List all owners of a scraper target
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/scrapers/{scraper_target_id}/owners'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_scrapers_id(client):
    """Test case for patch_scrapers_id

    Update a scraper target
    """
    body = {"name":"name","bucketID":"bucketID","type":"prometheus","allowInsecure":False,"orgID":"orgID","url":"http://localhost:9090/metrics"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/scrapers/{scraper_target_id}'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_scrapers(client):
    """Test case for post_scrapers

    Create a scraper target
    """
    body = {"name":"name","bucketID":"bucketID","type":"prometheus","allowInsecure":False,"orgID":"orgID","url":"http://localhost:9090/metrics"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/scrapers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_scrapers_id_labels(client):
    """Test case for post_scrapers_id_labels

    Add a label to a scraper target
    """
    body = {"labelID":"labelID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/scrapers/{scraper_target_id}/labels'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_scrapers_id_members(client):
    """Test case for post_scrapers_id_members

    Add a member to a scraper target
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/scrapers/{scraper_target_id}/members'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_scrapers_id_owners(client):
    """Test case for post_scrapers_id_owners

    Add an owner to a scraper target
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/scrapers/{scraper_target_id}/owners'.format(scraper_target_id='scraper_target_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

