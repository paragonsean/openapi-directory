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
from openapi_server.models.telegraf import Telegraf
from openapi_server.models.telegraf_request import TelegrafRequest
from openapi_server.models.telegrafs import Telegrafs


pytestmark = pytest.mark.asyncio

async def test_delete_telegrafs_id(client):
    """Test case for delete_telegrafs_id

    Delete a Telegraf configuration
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/telegrafs/{telegraf_id}'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_telegrafs_id_labels_id(client):
    """Test case for delete_telegrafs_id_labels_id

    Delete a label from a Telegraf config
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/telegrafs/{telegraf_id}/labels/{label_id}'.format(telegraf_id='telegraf_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_telegrafs_id_members_id(client):
    """Test case for delete_telegrafs_id_members_id

    Remove a member from a Telegraf config
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/telegrafs/{telegraf_id}/members/{user_id}'.format(user_id='user_id_example', telegraf_id='telegraf_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_telegrafs_id_owners_id(client):
    """Test case for delete_telegrafs_id_owners_id

    Remove an owner from a Telegraf config
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/telegrafs/{telegraf_id}/owners/{user_id}'.format(user_id='user_id_example', telegraf_id='telegraf_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_telegrafs(client):
    """Test case for get_telegrafs

    List all Telegraf configurations
    """
    params = [('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/telegrafs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_telegrafs_id(client):
    """Test case for get_telegrafs_id

    Retrieve a Telegraf configuration
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
        'accept': application/toml,
    }
    response = await client.request(
        method='GET',
        path='/api/v2/telegrafs/{telegraf_id}'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_telegrafs_id_labels(client):
    """Test case for get_telegrafs_id_labels

    List all labels for a Telegraf config
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/telegrafs/{telegraf_id}/labels'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_telegrafs_id_members(client):
    """Test case for get_telegrafs_id_members

    List all users with member privileges for a Telegraf config
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/telegrafs/{telegraf_id}/members'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_telegrafs_id_owners(client):
    """Test case for get_telegrafs_id_owners

    List all owners of a Telegraf configuration
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/telegrafs/{telegraf_id}/owners'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_telegrafs(client):
    """Test case for post_telegrafs

    Create a Telegraf configuration
    """
    body = {"metadata":{"buckets":["buckets","buckets"]},"name":"name","description":"description","config":"config","orgID":"orgID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/telegrafs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_telegrafs_id_labels(client):
    """Test case for post_telegrafs_id_labels

    Add a label to a Telegraf config
    """
    body = {"labelID":"labelID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/telegrafs/{telegraf_id}/labels'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_telegrafs_id_members(client):
    """Test case for post_telegrafs_id_members

    Add a member to a Telegraf config
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/telegrafs/{telegraf_id}/members'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_telegrafs_id_owners(client):
    """Test case for post_telegrafs_id_owners

    Add an owner to a Telegraf configuration
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/telegrafs/{telegraf_id}/owners'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_telegrafs_id(client):
    """Test case for put_telegrafs_id

    Update a Telegraf configuration
    """
    body = {"metadata":{"buckets":["buckets","buckets"]},"name":"name","description":"description","config":"config","orgID":"orgID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/telegrafs/{telegraf_id}'.format(telegraf_id='telegraf_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

