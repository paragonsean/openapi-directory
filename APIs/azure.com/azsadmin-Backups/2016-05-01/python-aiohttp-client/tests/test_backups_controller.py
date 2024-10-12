# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup import Backup
from openapi_server.models.backup_list import BackupList


pytestmark = pytest.mark.asyncio

async def test_backups_get(client):
    """Test case for backups_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Backup.Admin/backupLocations/{location}/backups/{backup}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', backup='backup_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backups_list(client):
    """Test case for backups_list

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Backup.Admin/backupLocations/{location}/backups'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backups_restore(client):
    """Test case for backups_restore

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Backup.Admin/backupLocations/{location}/backups/{backup}/restore'.format(subscription_id='subscription_id_example', location='location_example', resource_group_name='resource_group_name_example', backup='backup_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

