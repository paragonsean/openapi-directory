# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cross_region_restore_request_resource import CrossRegionRestoreRequestResource


pytestmark = pytest.mark.asyncio

async def test_cross_region_restore_trigger(client):
    """Test case for cross_region_restore_trigger

    Restores the specified backed up data in a different region as compared to where the data is backed up.
    """
    parameters = {"properties":{"crossRegionRestoreAccessDetails":{"resourceId":"resourceId","accessTokenString":"accessTokenString","resourceGroupName":"resourceGroupName","coordinatorServiceStampUri":"coordinatorServiceStampUri","datasourceContainerName":"datasourceContainerName","containerType":"containerType","tokenExtendedInformation":"tokenExtendedInformation","resourceName":"resourceName","protectionServiceStampId":"protectionServiceStampId","backupManagementType":"backupManagementType","datasourceType":"datasourceType","containerName":"containerName","datasourceId":"datasourceId","protectionServiceStampUri":"protectionServiceStampUri","recoveryPointTime":"recoveryPointTime","coordinatorServiceStampId":"coordinatorServiceStampId","datasourceName":"datasourceName","subscriptionId":"subscriptionId","recoveryPointId":"recoveryPointId"},"restoreRequest":{"objectType":"objectType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/locations/{azure_region}/backupCrossRegionRestore'.format(azure_region='azure_region_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

