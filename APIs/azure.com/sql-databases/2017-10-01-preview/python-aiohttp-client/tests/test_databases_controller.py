# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database import Database
from openapi_server.models.database_list_result import DatabaseListResult
from openapi_server.models.database_update import DatabaseUpdate
from openapi_server.models.resource_move_definition import ResourceMoveDefinition


pytestmark = pytest.mark.asyncio

async def test_databases_create_or_update(client):
    """Test case for databases_create_or_update

    
    """
    parameters = {"managedBy":"managedBy","kind":"kind","sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":6},"properties":{"maxLogSizeBytes":1,"readReplicaCount":2,"sourceDatabaseDeletionDate":"2000-01-23T04:56:07.000+00:00","failoverGroupId":"failoverGroupId","recoveryServicesRecoveryPointId":"recoveryServicesRecoveryPointId","elasticPoolId":"elasticPoolId","recoverableDatabaseId":"recoverableDatabaseId","restorePointInTime":"2000-01-23T04:56:07.000+00:00","sampleName":"AdventureWorksLT","licenseType":"LicenseIncluded","maxSizeBytes":5,"defaultSecondaryLocation":"defaultSecondaryLocation","minCapacity":5.637376656633329,"collation":"collation","databaseId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","pausedDate":"2000-01-23T04:56:07.000+00:00","earliestRestoreDate":"2000-01-23T04:56:07.000+00:00","requestedServiceObjectiveName":"requestedServiceObjectiveName","resumedDate":"2000-01-23T04:56:07.000+00:00","longTermRetentionBackupResourceId":"longTermRetentionBackupResourceId","readScale":"Enabled","restorableDroppedDatabaseId":"restorableDroppedDatabaseId","createMode":"Default","zoneRedundant":True,"creationDate":"2000-01-23T04:56:07.000+00:00","catalogCollation":"DATABASE_DEFAULT","autoPauseDelay":0,"currentSku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":6},"sourceDatabaseId":"sourceDatabaseId","currentServiceObjectiveName":"currentServiceObjectiveName","status":"Online"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_delete(client):
    """Test case for databases_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_get(client):
    """Test case for databases_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_list_by_elastic_pool(client):
    """Test case for databases_list_by_elastic_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}/databases'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_list_by_server(client):
    """Test case for databases_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_pause(client):
    """Test case for databases_pause

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/pause'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_rename(client):
    """Test case for databases_rename

    
    """
    parameters = {"id":"id"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/move'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_resume(client):
    """Test case for databases_resume

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/resume'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_update(client):
    """Test case for databases_update

    
    """
    parameters = {"sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":6},"properties":{"maxLogSizeBytes":1,"readReplicaCount":2,"sourceDatabaseDeletionDate":"2000-01-23T04:56:07.000+00:00","failoverGroupId":"failoverGroupId","recoveryServicesRecoveryPointId":"recoveryServicesRecoveryPointId","elasticPoolId":"elasticPoolId","recoverableDatabaseId":"recoverableDatabaseId","restorePointInTime":"2000-01-23T04:56:07.000+00:00","sampleName":"AdventureWorksLT","licenseType":"LicenseIncluded","maxSizeBytes":5,"defaultSecondaryLocation":"defaultSecondaryLocation","minCapacity":5.637376656633329,"collation":"collation","databaseId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","pausedDate":"2000-01-23T04:56:07.000+00:00","earliestRestoreDate":"2000-01-23T04:56:07.000+00:00","requestedServiceObjectiveName":"requestedServiceObjectiveName","resumedDate":"2000-01-23T04:56:07.000+00:00","longTermRetentionBackupResourceId":"longTermRetentionBackupResourceId","readScale":"Enabled","restorableDroppedDatabaseId":"restorableDroppedDatabaseId","createMode":"Default","zoneRedundant":True,"creationDate":"2000-01-23T04:56:07.000+00:00","catalogCollation":"DATABASE_DEFAULT","autoPauseDelay":0,"currentSku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":6},"sourceDatabaseId":"sourceDatabaseId","currentServiceObjectiveName":"currentServiceObjectiveName","status":"Online"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_upgrade_data_warehouse(client):
    """Test case for databases_upgrade_data_warehouse

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/upgradeDataWarehouse'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

