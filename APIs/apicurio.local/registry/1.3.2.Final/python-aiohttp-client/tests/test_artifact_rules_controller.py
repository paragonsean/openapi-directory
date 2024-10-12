# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule import Rule
from openapi_server.models.rule_type import RuleType


pytestmark = pytest.mark.asyncio

async def test_create_artifact_rule(client):
    """Test case for create_artifact_rule

    Create artifact rule
    """
    body = {"config":"FULL","type":"VALIDITY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/artifacts/{artifact_id}/rules'.format(artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_artifact_rule(client):
    """Test case for delete_artifact_rule

    Delete artifact rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/artifacts/{artifact_id}/rules/{rule}'.format(rule='rule_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_artifact_rules(client):
    """Test case for delete_artifact_rules

    Delete artifact rules
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/artifacts/{artifact_id}/rules'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_rule_config(client):
    """Test case for get_artifact_rule_config

    Get artifact rule configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts/{artifact_id}/rules/{rule}'.format(rule='rule_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_artifact_rules(client):
    """Test case for list_artifact_rules

    List artifact rules
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts/{artifact_id}/rules'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_update_artifact(client):
    """Test case for test_update_artifact

    Test update artifact
    """
    headers = { 
        'Accept': 'application/json',
        'x_registry_artifact_type': 'x_registry_artifact_type_example',
    }
    response = await client.request(
        method='PUT',
        path='/artifacts/{artifact_id}/test'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_artifact_rule_config(client):
    """Test case for update_artifact_rule_config

    Update artifact rule configuration
    """
    body = {"config":"FULL","type":"VALIDITY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/artifacts/{artifact_id}/rules/{rule}'.format(rule='rule_example', artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

