# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_camera_custom_analytics_artifact_request import CreateOrganizationCameraCustomAnalyticsArtifactRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_camera_custom_analytics_artifact_2(client):
    """Test case for create_organization_camera_custom_analytics_artifact_2

    Create custom analytics artifact
    """
    body = openapi_server.CreateOrganizationCameraCustomAnalyticsArtifactRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_camera_custom_analytics_artifact_2(client):
    """Test case for delete_organization_camera_custom_analytics_artifact_2

    Delete Custom Analytics Artifact
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts/{artifact_id}'.format(organization_id='organization_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_camera_custom_analytics_artifact_2(client):
    """Test case for get_organization_camera_custom_analytics_artifact_2

    Get Custom Analytics Artifact
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts/{artifact_id}'.format(organization_id='organization_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_camera_custom_analytics_artifacts_2(client):
    """Test case for get_organization_camera_custom_analytics_artifacts_2

    List Custom Analytics Artifacts
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

