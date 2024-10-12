# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.android_app import AndroidApp
from openapi_server.models.android_apps_response import AndroidAppsResponse
from openapi_server.models.android_certificates_response import AndroidCertificatesResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.upload_android_app_response import UploadAndroidAppResponse


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_android_apps(client):
    """Test case for get_companies_company_id_android_apps

    Get a list of Android apps
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56),
                    ('packageName', 'package_name_example'),
                    ('versionCode', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/androidApps'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_android_apps_id(client):
    """Test case for get_companies_company_id_android_apps_id

    Get Android app
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/androidApps/{id}'.format(company_id='company_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_android_certificates(client):
    """Test case for get_companies_company_id_android_certificates

    Get a list of Android certificates
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56),
                    ('certificateName', 'certificate_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/androidCertificates'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_companies_company_id_android_apps(client):
    """Test case for post_companies_company_id_android_apps

    Upload Android App
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/companies/{company_id}/androidApps'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

