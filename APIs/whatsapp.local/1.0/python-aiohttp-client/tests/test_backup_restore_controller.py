# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_settings_request_body import BackupSettingsRequestBody
from openapi_server.models.backup_settings_response import BackupSettingsResponse
from openapi_server.models.restore_settings_request_body import RestoreSettingsRequestBody


pytestmark = pytest.mark.asyncio

async def test_backup_settings(client):
    """Test case for backup_settings

    Backup-Settings
    """
    body = {"password":"<Password for Backup>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/settings/backup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_settings(client):
    """Test case for restore_settings

    Restore-Settings
    """
    body = {"data":"<Data to Restore, from Backup API>","password":"<Password for Backup>"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/settings/restore',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

