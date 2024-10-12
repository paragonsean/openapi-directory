# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.secret_keys import SecretKeys
from openapi_server.models.secret_keys_response import SecretKeysResponse


pytestmark = pytest.mark.asyncio

async def test_get_orgs_id_secrets(client):
    """Test case for get_orgs_id_secrets

    List all secret keys for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/orgs/{org_id}/secrets'.format(org_id='org_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_orgs_id_secrets(client):
    """Test case for patch_orgs_id_secrets

    Update secrets in an organization
    """
    body = {'key': 'body_example'}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/orgs/{org_id}/secrets'.format(org_id='org_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_orgs_id_secrets(client):
    """Test case for post_orgs_id_secrets

    Delete secrets from an organization
    """
    body = {"secrets":["secrets","secrets"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/orgs/{org_id}/secrets/delete'.format(org_id='org_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

