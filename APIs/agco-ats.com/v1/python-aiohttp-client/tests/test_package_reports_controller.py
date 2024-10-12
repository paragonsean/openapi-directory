# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.update_system_models_package_report import UpdateSystemModelsPackageReport


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_v2_clients_client_id_package_reports_put(client):
    """Test case for api_v2_clients_client_id_package_reports_put

    Submit a package report
    """
    body = openapi_server.UpdateSystemModelsPackageReport()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Clients/{client_id}/PackageReports'.format(client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_package_reports_batch(client):
    """Test case for package_reports_batch

    Submit a batch of package reports
    """
    body = [openapi_server.UpdateSystemModelsPackageReport()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Clients/{client_id}/PackageReports/Batch'.format(client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_reports_default(client):
    """Test case for package_reports_default

    Get the package reports for a client.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Clients/{client_id}/PackageReports'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

