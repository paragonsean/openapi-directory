# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_resource import JobResource


pytestmark = pytest.mark.asyncio

async def test_backup_crr_job_details_get(client):
    """Test case for backup_crr_job_details_get

    Get CRR job details from target region.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/locations/{azure_region}/backupCrrJob'.format(azure_region='azure_region_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

