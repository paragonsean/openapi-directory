# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_list import DeviceList
from openapi_server.models.device_selection import DeviceSelection
from openapi_server.models.device_set import DeviceSet
from openapi_server.models.device_set_update_information import DeviceSetUpdateInformation
from openapi_server.models.name_of_the_test_series import NameOfTheTestSeries
from openapi_server.models.subscription1 import Subscription1
from openapi_server.models.test_cloud_error_details import TestCloudErrorDetails
from openapi_server.models.test_cloud_file_hash import TestCloudFileHash
from openapi_server.models.test_cloud_file_hash1 import TestCloudFileHash1
from openapi_server.models.test_cloud_file_hash_response import TestCloudFileHashResponse
from openapi_server.models.test_cloud_start_test_run_options import TestCloudStartTestRunOptions
from openapi_server.models.test_cloud_test_run_start_result import TestCloudTestRunStartResult
from openapi_server.models.test_gdpr_export_account200_response import TestGdprExportAccount200Response
from openapi_server.models.test_gdpr_export_accounts200_response import TestGdprExportAccounts200Response
from openapi_server.models.test_gdpr_export_app200_response import TestGdprExportApp200Response
from openapi_server.models.test_gdpr_export_feature_flag200_response import TestGdprExportFeatureFlag200Response
from openapi_server.models.test_gdpr_export_file_set_file200_response import TestGdprExportFileSetFile200Response
from openapi_server.models.test_gdpr_export_hash_file200_response import TestGdprExportHashFile200Response
from openapi_server.models.test_gdpr_export_pipeline_test200_response import TestGdprExportPipelineTest200Response
from openapi_server.models.test_gdpr_export_test_run200_response import TestGdprExportTestRun200Response
from openapi_server.models.test_get_device_configurations200_response_inner import TestGetDeviceConfigurations200ResponseInner
from openapi_server.models.test_get_test_report200_response import TestGetTestReport200Response
from openapi_server.models.test_run import TestRun
from openapi_server.models.test_run_state import TestRunState
from openapi_server.models.test_series import TestSeries


pytestmark = pytest.mark.asyncio

async def test_test_archive_test_run(client):
    """Test case for test_archive_test_run

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_create_device_selection(client):
    """Test case for test_create_device_selection

    
    """
    body = {"devices":["devices","devices"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/device_selection'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_create_device_set_of_owner(client):
    """Test case for test_create_device_set_of_owner

    
    """
    body = openapi_server.DeviceSetUpdateInformation()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/owner/device_sets'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_create_device_set_of_user(client):
    """Test case for test_create_device_set_of_user

    
    """
    body = openapi_server.DeviceSetUpdateInformation()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/user/device_sets'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_create_subscription(client):
    """Test case for test_create_subscription

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/subscriptions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_create_test_run(client):
    """Test case for test_create_test_run

    
    """
    headers = { 
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_create_test_series(client):
    """Test case for test_create_test_series

    
    """
    body = openapi_server.NameOfTheTestSeries()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/test_series'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_delete_device_set_of_owner(client):
    """Test case for test_delete_device_set_of_owner

    
    """
    headers = { 
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id}'.format(id='id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_delete_device_set_of_user(client):
    """Test case for test_delete_device_set_of_user

    
    """
    headers = { 
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id}'.format(id='id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_delete_test_series(client):
    """Test case for test_delete_test_series

    
    """
    headers = { 
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug}'.format(test_series_slug='test_series_slug_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_account(client):
    """Test case for test_gdpr_export_account

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/account/test/export/accounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_accounts(client):
    """Test case for test_gdpr_export_accounts

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/account/test/export',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_app(client):
    """Test case for test_gdpr_export_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test/export/apps'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_apps(client):
    """Test case for test_gdpr_export_apps

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test/export'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_feature_flag(client):
    """Test case for test_gdpr_export_feature_flag

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/account/test/export/featureFlags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_file_set_file(client):
    """Test case for test_gdpr_export_file_set_file

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test/export/fileSetFiles'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_hash_file(client):
    """Test case for test_gdpr_export_hash_file

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test/export/hashFiles'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_pipeline_test(client):
    """Test case for test_gdpr_export_pipeline_test

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test/export/pipelineTests'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gdpr_export_test_run(client):
    """Test case for test_gdpr_export_test_run

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test/export/testRuns'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_all_test_runs_for_series(client):
    """Test case for test_get_all_test_runs_for_series

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug}/test_runs'.format(test_series_slug='test_series_slug_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_all_test_series(client):
    """Test case for test_get_all_test_series

    
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test_series'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_device_configurations(client):
    """Test case for test_get_device_configurations

    
    """
    params = [('app_upload_id', 'app_upload_id_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/device_configurations'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_device_set_of_owner(client):
    """Test case for test_get_device_set_of_owner

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id}'.format(id='id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_device_set_of_user(client):
    """Test case for test_get_device_set_of_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id}'.format(id='id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_subscriptions(client):
    """Test case for test_get_subscriptions

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/subscriptions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_test_report(client):
    """Test case for test_get_test_report

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/report'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_test_run(client):
    """Test case for test_get_test_run

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_test_run_state(client):
    """Test case for test_get_test_run_state

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/state'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_get_test_runs(client):
    """Test case for test_get_test_runs

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_list_device_sets_of_owner(client):
    """Test case for test_list_device_sets_of_owner

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/owner/device_sets'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_list_device_sets_of_user(client):
    """Test case for test_list_device_sets_of_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/user/device_sets'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_patch_test_series(client):
    """Test case for test_patch_test_series

    
    """
    body = openapi_server.NameOfTheTestSeries()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug}'.format(test_series_slug='test_series_slug_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_start_test_run(client):
    """Test case for test_start_test_run

    
    """
    body = {"test_series":"test_series","device_selection":"device_selection","language":"language","test_parameters":"{}","locale":"locale","test_framework":"test_framework"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/start'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_start_uploading_file(client):
    """Test case for test_start_uploading_file

    
    """
    headers = { 
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/files'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_stop_test_run(client):
    """Test case for test_stop_test_run

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/stop'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_update_device_set_of_owner(client):
    """Test case for test_update_device_set_of_owner

    
    """
    body = openapi_server.DeviceSetUpdateInformation()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id}'.format(id='id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_update_device_set_of_user(client):
    """Test case for test_update_device_set_of_user

    
    """
    body = openapi_server.DeviceSetUpdateInformation()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id}'.format(id='id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_upload_hash(client):
    """Test case for test_upload_hash

    
    """
    body = {"relativePath":"relativePath","checksum":"checksum","fileType":"dsym-file"}
    headers = { 
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/hashes'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_upload_hashes_batch(client):
    """Test case for test_upload_hashes_batch

    
    """
    body = [openapi_server.TestCloudFileHash1()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/hashes/batch'.format(test_run_id='test_run_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

