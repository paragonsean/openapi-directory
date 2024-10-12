# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_or_update_integration_link_model import AddOrUpdateIntegrationLinkModel
from openapi_server.models.add_or_update_jira_integration_link_model import AddOrUpdateJiraIntegrationLinkModel
from openapi_server.models.connect_request import ConnectRequest
from openapi_server.models.delete_integration_link_model import DeleteIntegrationLinkModel
from openapi_server.models.integration_link_details_model import IntegrationLinkDetailsModel
from openapi_server.models.integration_link_model import IntegrationLinkModel
from openapi_server.models.integration_link_type import IntegrationLinkType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_or_update_integration_link(client):
    """Test case for add_or_update_integration_link

    Add or update Integration link
    """
    body = {"description":"description","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/environments/{environment_id}/settings/{setting_id}/integrationLinks/{integration_link_type}/{key}'.format(environment_id='environment_id_example', setting_id=56, integration_link_type=openapi_server.IntegrationLinkType(), key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_integration_link(client):
    """Test case for delete_integration_link

    Delete Integration link
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/environments/{environment_id}/settings/{setting_id}/integrationLinks/{integration_link_type}/{key}'.format(environment_id='environment_id_example', setting_id=56, integration_link_type=openapi_server.IntegrationLinkType(), key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_integration_link_details(client):
    """Test case for get_integration_link_details

    Get Integration link
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/integrationLink/{integration_link_type}/{key}/details'.format(integration_link_type=openapi_server.IntegrationLinkType(), key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_jira_add_or_update_integration_link(client):
    """Test case for jira_add_or_update_integration_link

    
    """
    body = {"jiraJwtToken":"jiraJwtToken","clientKey":"clientKey","description":"description","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/jira/environments/{environment_id}/settings/{setting_id}/integrationLinks/{key}'.format(environment_id='environment_id_example', setting_id=56, key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_jira_connect_post(client):
    """Test case for v1_jira_connect_post

    
    """
    body = {"jiraJwtToken":"jiraJwtToken","clientKey":"clientKey"}
    headers = { 
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/jira/Connect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

