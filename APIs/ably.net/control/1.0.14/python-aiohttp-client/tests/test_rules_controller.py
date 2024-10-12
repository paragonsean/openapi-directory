# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule_patch import RulePatch
from openapi_server.models.rule_post import RulePost
from openapi_server.models.rule_response import RuleResponse


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_rules_get(client):
    """Test case for apps_app_id_rules_get

    Lists Reactor rules
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{app_id}/rules'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_rules_post(client):
    """Test case for apps_app_id_rules_post

    Creates a Reactor rule
    """
    body = openapi_server.RulePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/apps/{app_id}/rules'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_rules_rule_id_delete(client):
    """Test case for apps_app_id_rules_rule_id_delete

    Deletes a Reactor rule
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/apps/{app_id}/rules/{rule_id}'.format(app_id='app_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_rules_rule_id_get(client):
    """Test case for apps_app_id_rules_rule_id_get

    Gets a reactor rule by rule ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{app_id}/rules/{rule_id}'.format(app_id='app_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_rules_rule_id_patch(client):
    """Test case for apps_app_id_rules_rule_id_patch

    Updates a Reactor rule
    """
    body = openapi_server.RulePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/apps/{app_id}/rules/{rule_id}'.format(app_id='app_id_example', rule_id='rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

