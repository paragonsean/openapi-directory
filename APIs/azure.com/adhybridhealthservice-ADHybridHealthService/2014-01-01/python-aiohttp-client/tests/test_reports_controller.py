# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_report_users_entries import ErrorReportUsersEntries
from openapi_server.models.risky_ip_blob_uris import RiskyIPBlobUris


pytestmark = pytest.mark.asyncio

async def test_services_list_all_risky_ip_download_report(client):
    """Test case for services_list_all_risky_ip_download_report

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/reports/riskyIp/blobUris'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_current_risky_ip_download_report(client):
    """Test case for services_list_current_risky_ip_download_report

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/reports/riskyIp/generateBlobUri'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_user_bad_password_report(client):
    """Test case for services_list_user_bad_password_report

    
    """
    params = [('dataSource', 'data_source_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/reports/badpassword/details/user'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

