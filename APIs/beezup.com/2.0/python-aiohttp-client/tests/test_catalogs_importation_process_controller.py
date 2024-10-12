# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.get_importation_products_report_request import GetImportationProductsReportRequest
from openapi_server.models.get_importation_products_report_response import GetImportationProductsReportResponse
from openapi_server.models.get_importation_report_response import GetImportationReportResponse
from openapi_server.models.import_already_in_progress_response import ImportAlreadyInProgressResponse
from openapi_server.models.importation_monitoring import ImportationMonitoring
from openapi_server.models.importation_technical_progression import ImportationTechnicalProgression
from openapi_server.models.importations_response import ImportationsResponse
from openapi_server.models.links_importation_get_importation_monitoring_link import LinksImportationGetImportationMonitoringLink
from openapi_server.models.start_manual_import_request import StartManualImportRequest


pytestmark = pytest.mark.asyncio

async def test_importation_cancel(client):
    """Test case for importation_cancel

    Cancel importation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/cancel'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_commit(client):
    """Test case for importation_commit

    Commit Importation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/commit'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_commit_columns(client):
    """Test case for importation_commit_columns

    Commit columns
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/commitColumns'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_configure_remaining_catalog_columns(client):
    """Test case for importation_configure_remaining_catalog_columns

    Configure remaining catalog columns
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/configureRemainingCatalogColumns'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_importation_monitoring(client):
    """Test case for importation_get_importation_monitoring

    Get the importation status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_products_report(client):
    """Test case for importation_get_products_report

    Importation Get Products Report
    """
    body = openapi_server.GetImportationProductsReportRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/products/list'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_report(client):
    """Test case for importation_get_report

    Importation Get Report
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/report'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_reportings(client):
    """Test case for importation_get_reportings

    Get the latest catalog importation reporting
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_reportings_all_stores(client):
    """Test case for importation_get_reportings_all_stores

    Get the latest catalog importation reporting for all your stores
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/importations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_start_manual_update(client):
    """Test case for importation_start_manual_update

    Start Manual Import
    """
    body = openapi_server.StartManualImportRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/start'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_technical_progression(client):
    """Test case for importation_technical_progression

    Get technical progression
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/technicalProgression'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

