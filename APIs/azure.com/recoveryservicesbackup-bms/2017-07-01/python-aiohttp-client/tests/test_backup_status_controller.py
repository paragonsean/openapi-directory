# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_status_request import BackupStatusRequest
from openapi_server.models.backup_status_response import BackupStatusResponse


pytestmark = pytest.mark.asyncio

async def test_backup_status_get(client):
    """Test case for backup_status_get

    Get the container backup status
    """
    parameters = {"resourceId":"resourceId","poLogicalName":"poLogicalName","resourceType":"Invalid"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/locations/{azure_region}/backupStatus'.format(azure_region='azure_region_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

