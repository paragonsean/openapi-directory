# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_import_configuration import AutoImportConfiguration
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.configure_auto_import_interval_request import ConfigureAutoImportIntervalRequest
from openapi_server.models.links_importation_get_importation_monitoring_link import LinksImportationGetImportationMonitoringLink
from openapi_server.models.schedule_auto_import_request import ScheduleAutoImportRequest


pytestmark = pytest.mark.asyncio

async def test_auto_configure_auto_import_interval(client):
    """Test case for auto_configure_auto_import_interval

    Configure Auto Import Interval
    """
    body = openapi_server.ConfigureAutoImportIntervalRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/autoImport/scheduling/interval'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_delete_auto_import(client):
    """Test case for auto_delete_auto_import

    Delete Auto Import
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/catalogs/{store_id}/autoImport'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_get_auto_import_configuration(client):
    """Test case for auto_get_auto_import_configuration

    Get the auto import configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/autoImport'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_pause_auto_import(client):
    """Test case for auto_pause_auto_import

    Pause Auto Import
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/autoImport/pause'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_resume_auto_import(client):
    """Test case for auto_resume_auto_import

    Resume Auto Import
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/autoImport/resume'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_schedule_auto_import(client):
    """Test case for auto_schedule_auto_import

    Configure Auto Import Schedules
    """
    body = openapi_server.ScheduleAutoImportRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/autoImport/scheduling/schedules'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_start_auto_import(client):
    """Test case for auto_start_auto_import

    Start Auto Import Manually
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/autoImport/start'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_activate_auto_import(client):
    """Test case for importation_activate_auto_import

    Activate the auto importation of the last successful manual catalog importation.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/autoImport/activate'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

