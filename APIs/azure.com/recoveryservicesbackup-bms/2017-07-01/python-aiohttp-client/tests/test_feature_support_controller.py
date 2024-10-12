# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.azure_vm_resource_feature_support_response import AzureVMResourceFeatureSupportResponse
from openapi_server.models.feature_support_request import FeatureSupportRequest


pytestmark = pytest.mark.asyncio

async def test_feature_support_validate(client):
    """Test case for feature_support_validate

    It will validate if given feature with resource properties is supported in service
    """
    parameters = {"featureType":"featureType"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/locations/{azure_region}/backupValidateFeatures'.format(azure_region='azure_region_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

