# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_camera_quality_retention_profile_request import CreateNetworkCameraQualityRetentionProfileRequest
from openapi_server.models.update_network_camera_quality_retention_profile_request import UpdateNetworkCameraQualityRetentionProfileRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_camera_quality_retention_profile(client):
    """Test case for create_network_camera_quality_retention_profile

    Creates new quality retention profile for this network.
    """
    body = openapi_server.CreateNetworkCameraQualityRetentionProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/camera/qualityRetentionProfiles'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_camera_quality_retention_profile(client):
    """Test case for delete_network_camera_quality_retention_profile

    Delete an existing quality retention profile for this network.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}'.format(network_id='network_id_example', quality_retention_profile_id='quality_retention_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_quality_retention_profile(client):
    """Test case for get_network_camera_quality_retention_profile

    Retrieve a single quality retention profile
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}'.format(network_id='network_id_example', quality_retention_profile_id='quality_retention_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_quality_retention_profiles(client):
    """Test case for get_network_camera_quality_retention_profiles

    List the quality retention profiles for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/camera/qualityRetentionProfiles'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_camera_quality_retention_profile(client):
    """Test case for update_network_camera_quality_retention_profile

    Update an existing quality retention profile for this network.
    """
    body = openapi_server.UpdateNetworkCameraQualityRetentionProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}'.format(network_id='network_id_example', quality_retention_profile_id='quality_retention_profile_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

