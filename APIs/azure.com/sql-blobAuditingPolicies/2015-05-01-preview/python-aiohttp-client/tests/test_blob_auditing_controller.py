# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database_blob_auditing_policy import DatabaseBlobAuditingPolicy


pytestmark = pytest.mark.asyncio

async def test_database_blob_auditing_policies_create_or_update(client):
    """Test case for database_blob_auditing_policies_create_or_update

    
    """
    parameters = {"kind":"kind","properties":{"storageEndpoint":"storageEndpoint","retentionDays":0,"storageAccountAccessKey":"storageAccountAccessKey","isStorageSecondaryKeyInUse":True,"state":"Enabled","auditActionsAndGroups":["auditActionsAndGroups","auditActionsAndGroups"],"storageAccountSubscriptionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/auditingSettings/{blob_auditing_policy_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', blob_auditing_policy_name='blob_auditing_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_blob_auditing_policies_get(client):
    """Test case for database_blob_auditing_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/auditingSettings/{blob_auditing_policy_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', blob_auditing_policy_name='blob_auditing_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

