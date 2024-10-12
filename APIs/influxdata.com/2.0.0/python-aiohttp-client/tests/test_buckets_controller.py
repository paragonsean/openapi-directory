# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets import Buckets
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.patch_bucket_request import PatchBucketRequest
from openapi_server.models.post_bucket_request import PostBucketRequest
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners


pytestmark = pytest.mark.asyncio

async def test_delete_buckets_id(client):
    """Test case for delete_buckets_id

    Delete a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/buckets/{bucket_id}'.format(bucket_id='bucket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_buckets_id_labels_id(client):
    """Test case for delete_buckets_id_labels_id

    Delete a label from a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/buckets/{bucket_id}/labels/{label_id}'.format(bucket_id='bucket_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_buckets_id_members_id(client):
    """Test case for delete_buckets_id_members_id

    Remove a member from a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/buckets/{bucket_id}/members/{user_id}'.format(user_id='user_id_example', bucket_id='bucket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_buckets_id_owners_id(client):
    """Test case for delete_buckets_id_owners_id

    Remove an owner from a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/buckets/{bucket_id}/owners/{user_id}'.format(user_id='user_id_example', bucket_id='bucket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buckets(client):
    """Test case for get_buckets

    List all buckets
    """
    params = [('offset', 56),
                    ('limit', 20),
                    ('after', 'after_example'),
                    ('org', 'org_example'),
                    ('orgID', 'org_id_example'),
                    ('name', 'name_example'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/buckets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buckets_id(client):
    """Test case for get_buckets_id

    Retrieve a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/buckets/{bucket_id}'.format(bucket_id='bucket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buckets_id_labels(client):
    """Test case for get_buckets_id_labels

    List all labels for a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/buckets/{bucket_id}/labels'.format(bucket_id='bucket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buckets_id_members(client):
    """Test case for get_buckets_id_members

    List all users with member privileges for a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/buckets/{bucket_id}/members'.format(bucket_id='bucket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buckets_id_owners(client):
    """Test case for get_buckets_id_owners

    List all owners of a bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/buckets/{bucket_id}/owners'.format(bucket_id='bucket_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sources_id_buckets_0(client):
    """Test case for get_sources_id_buckets_0

    Get buckets in a source
    """
    params = [('org', 'org_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/sources/{source_id}/buckets'.format(source_id='source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_buckets_id(client):
    """Test case for patch_buckets_id

    Update a bucket
    """
    body = {"retentionRules":[{"everySeconds":86400,"type":"expire","shardGroupDurationSeconds":0},{"everySeconds":86400,"type":"expire","shardGroupDurationSeconds":0}],"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/buckets/{bucket_id}'.format(bucket_id='bucket_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_buckets(client):
    """Test case for post_buckets

    Create a bucket
    """
    body = {"retentionRules":[{"everySeconds":86400,"type":"expire","shardGroupDurationSeconds":0},{"everySeconds":86400,"type":"expire","shardGroupDurationSeconds":0}],"name":"name","schemaType":"implicit","description":"description","orgID":"orgID","rp":"rp"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/buckets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_buckets_id_labels(client):
    """Test case for post_buckets_id_labels

    Add a label to a bucket
    """
    body = {"labelID":"labelID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/buckets/{bucket_id}/labels'.format(bucket_id='bucket_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_buckets_id_members(client):
    """Test case for post_buckets_id_members

    Add a member to a bucket
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/buckets/{bucket_id}/members'.format(bucket_id='bucket_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_buckets_id_owners(client):
    """Test case for post_buckets_id_owners

    Add an owner to a bucket
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/buckets/{bucket_id}/owners'.format(bucket_id='bucket_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

