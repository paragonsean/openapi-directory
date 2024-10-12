# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deployment_environment_addition import DeploymentEnvironmentAddition
from openapi_server.models.deployment_environment_deployments_results import DeploymentEnvironmentDeploymentsResults
from openapi_server.models.deployment_environment_lookup_model import DeploymentEnvironmentLookupModel
from openapi_server.models.deployment_environment_settings_results import DeploymentEnvironmentSettingsResults
from openapi_server.models.deployment_environment_with_settings import DeploymentEnvironmentWithSettings
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_add_environment(client):
    """Test case for add_environment

    Add environment
    """
    body = {"name":"production","provider":"FTP","settings":{"environmentVariables":[{"name":"my-var","value":{"isEncrypted":False,"value":"123"}}],"providerSettings":[{"name":"server","value":{"isEncrypted":False,"value":"ftp.myserver.com"}},{"name":"username","value":{"isEncrypted":False,"value":"ftp-user"}},{"name":"password","value":{"isEncrypted":True,"value":"password"}}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/environments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_environment(client):
    """Test case for delete_environment

    Delete environment
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/environments/{deployment_environment_id}'.format(deployment_environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_environment_deployments(client):
    """Test case for get_environment_deployments

    Get environment deployments
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/environments/{deployment_environment_id}/deployments'.format(deployment_environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_environment_settings(client):
    """Test case for get_environment_settings

    Get environment settings
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/environments/{deployment_environment_id}/settings'.format(deployment_environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_environments(client):
    """Test case for get_environments

    Get environments
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/environments',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_environment(client):
    """Test case for update_environment

    Update environment
    """
    body = {"settings":{"environmentVariables":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"providerSettings":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"notifications":[{"settings":{"template":"template","authToken":{"isEncrypted":True,"value":"value"},"channel":"channel","onBuildFailure":True,"onBuildStatusChanged":True,"addCustomRequestBody":True,"password":{"isEncrypted":True,"value":"value"},"serverUrl":"https://openapi-generator.tech","from":"from","subjectTemplate":"subjectTemplate","onBuildSuccess":True,"headers":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"method":"GET","customRequestBody":"customRequestBody","room":"room","url":"https://openapi-generator.tech","$type":"Appveyor.Models.CampfireNotificationSettings, Appveyor.Models","customRequestBodyContentType":"customRequestBodyContentType","recipientsValue":"recipientsValue","headersValue":"headersValue","incomingWebhookUrl":"https://openapi-generator.tech","bodyTemplate":"bodyTemplate","recipients":[{"value":"value"},{"value":"value"}],"vsoAccount":"vsoAccount","account":"account","username":"username"},"provider":"Campfire"},{"settings":{"template":"template","authToken":{"isEncrypted":True,"value":"value"},"channel":"channel","onBuildFailure":True,"onBuildStatusChanged":True,"addCustomRequestBody":True,"password":{"isEncrypted":True,"value":"value"},"serverUrl":"https://openapi-generator.tech","from":"from","subjectTemplate":"subjectTemplate","onBuildSuccess":True,"headers":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"method":"GET","customRequestBody":"customRequestBody","room":"room","url":"https://openapi-generator.tech","$type":"Appveyor.Models.CampfireNotificationSettings, Appveyor.Models","customRequestBodyContentType":"customRequestBodyContentType","recipientsValue":"recipientsValue","headersValue":"headersValue","incomingWebhookUrl":"https://openapi-generator.tech","bodyTemplate":"bodyTemplate","recipients":[{"value":"value"},{"value":"value"}],"vsoAccount":"vsoAccount","account":"account","username":"username"},"provider":"Campfire"}]},"deploymentEnvironmentId":0,"securityDescriptor":{"accessRightDefinitions":[{"name":"Delete","description":"description"},{"name":"Delete","description":"description"}],"roleAces":[{"roleId":0,"name":"name","accessRights":[{"allowed":True},{"allowed":True}],"isAdmin":True},{"roleId":0,"name":"name","accessRights":[{"allowed":True},{"allowed":True}],"isAdmin":True}]},"environmentAccessKey":"environmentAccessKey","projects":[{"isSelected":True,"name":"name","projectId":0},{"isSelected":True,"name":"name","projectId":0}],"selectedProjects":[1,1],"created":"2000-01-23T04:56:07.000+00:00","tags":"tags","accountId":6,"provider":"Agent","projectsMode":1,"name":"name","updated":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/environments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

