# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit_log_item_model import AuditLogItemModel
from openapi_server.models.audit_log_type import AuditLogType
from openapi_server.models.setting_model import SettingModel
from openapi_server.models.setting_model_haljson import SettingModelHaljson


pytestmark = pytest.mark.asyncio

async def test_get_auditlogs(client):
    """Test case for get_auditlogs

    List Audit log items for Product
    """
    params = [('configId', 'config_id_example'),
                    ('environmentId', 'environment_id_example'),
                    ('auditLogType', openapi_server.AuditLogType()),
                    ('fromUtcDateTime', '2013-10-20T19:20:30+01:00'),
                    ('toUtcDateTime', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{product_id}/auditlogs'.format(product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deleted_settings(client):
    """Test case for get_deleted_settings

    List Deleted Settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/configs/{config_id}/deleted-settings'.format(config_id='config_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_auditlogs(client):
    """Test case for get_organization_auditlogs

    List Audit log items for Organization
    """
    params = [('productId', 'product_id_example'),
                    ('configId', 'config_id_example'),
                    ('environmentId', 'environment_id_example'),
                    ('auditLogType', openapi_server.AuditLogType()),
                    ('fromUtcDateTime', '2013-10-20T19:20:30+01:00'),
                    ('toUtcDateTime', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations/{organization_id}/auditlogs'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

