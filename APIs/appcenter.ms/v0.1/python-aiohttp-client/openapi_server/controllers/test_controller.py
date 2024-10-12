from typing import List, Dict
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
from openapi_server import util


async def test_archive_test_run(request: web.Request, test_run_id, owner_name, app_name) -> web.Response:
    """test_archive_test_run

    Logically deletes a test run

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_create_device_selection(request: web.Request, owner_name, app_name, body) -> web.Response:
    """test_create_device_selection

    Creates a short ID for a list of devices

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceList.from_dict(body)
    return web.Response(status=200)


async def test_create_device_set_of_owner(request: web.Request, owner_name, app_name, body) -> web.Response:
    """test_create_device_set_of_owner

    Creates a device set belonging to the owner

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceSetUpdateInformation.from_dict(body)
    return web.Response(status=200)


async def test_create_device_set_of_user(request: web.Request, owner_name, app_name, body) -> web.Response:
    """test_create_device_set_of_user

    Creates a device set belonging to the user

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceSetUpdateInformation.from_dict(body)
    return web.Response(status=200)


async def test_create_subscription(request: web.Request, owner_name, app_name) -> web.Response:
    """test_create_subscription

    Accept a free trial subscription

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_create_test_run(request: web.Request, owner_name, app_name) -> web.Response:
    """test_create_test_run

    Creates a new test run

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_create_test_series(request: web.Request, owner_name, app_name, body) -> web.Response:
    """test_create_test_series

    Creates new test series for an application

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = NameOfTheTestSeries.from_dict(body)
    return web.Response(status=200)


async def test_delete_device_set_of_owner(request: web.Request, id, owner_name, app_name) -> web.Response:
    """test_delete_device_set_of_owner

    Deletes a device set belonging to the owner

    :param id: The UUID of the device set
    :type id: str
    :type id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_delete_device_set_of_user(request: web.Request, id, owner_name, app_name) -> web.Response:
    """test_delete_device_set_of_user

    Deletes a device set belonging to the user

    :param id: The UUID of the device set
    :type id: str
    :type id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_delete_test_series(request: web.Request, test_series_slug, owner_name, app_name) -> web.Response:
    """test_delete_test_series

    Deletes a single test series

    :param test_series_slug: The slug of the test series
    :type test_series_slug: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_gdpr_export_account(request: web.Request, ) -> web.Response:
    """test_gdpr_export_account

    Lists account data


    """
    return web.Response(status=200)


async def test_gdpr_export_accounts(request: web.Request, ) -> web.Response:
    """test_gdpr_export_accounts

    Lists all the endpoints available for Test accounts data


    """
    return web.Response(status=200)


async def test_gdpr_export_app(request: web.Request, owner_name, app_name) -> web.Response:
    """test_gdpr_export_app

    Lists app data

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_gdpr_export_apps(request: web.Request, owner_name, app_name) -> web.Response:
    """test_gdpr_export_apps

    Lists all the endpoints available for Test apps data

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_gdpr_export_feature_flag(request: web.Request, ) -> web.Response:
    """test_gdpr_export_feature_flag

    Lists feature flag data


    """
    return web.Response(status=200)


async def test_gdpr_export_file_set_file(request: web.Request, owner_name, app_name) -> web.Response:
    """test_gdpr_export_file_set_file

    Lists file set file data

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_gdpr_export_hash_file(request: web.Request, owner_name, app_name) -> web.Response:
    """test_gdpr_export_hash_file

    Lists hash file data

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_gdpr_export_pipeline_test(request: web.Request, owner_name, app_name) -> web.Response:
    """test_gdpr_export_pipeline_test

    Lists pipeline test data

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_gdpr_export_test_run(request: web.Request, owner_name, app_name) -> web.Response:
    """test_gdpr_export_test_run

    Lists test run data

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_all_test_runs_for_series(request: web.Request, test_series_slug, owner_name, app_name) -> web.Response:
    """test_get_all_test_runs_for_series

    Returns list of all test runs for a given test series

    :param test_series_slug: The slug of the test series
    :type test_series_slug: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_all_test_series(request: web.Request, owner_name, app_name, query=None) -> web.Response:
    """test_get_all_test_series

    Returns list of all test series for an application

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param query: A query string to filter test series
    :type query: str

    """
    return web.Response(status=200)


async def test_get_device_configurations(request: web.Request, owner_name, app_name, app_upload_id=None) -> web.Response:
    """test_get_device_configurations

    Returns a list of available devices

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param app_upload_id: The ID of the test run
    :type app_upload_id: str
    :type app_upload_id: str

    """
    return web.Response(status=200)


async def test_get_device_set_of_owner(request: web.Request, id, owner_name, app_name) -> web.Response:
    """test_get_device_set_of_owner

    Gets a device set belonging to the owner

    :param id: The UUID of the device set
    :type id: str
    :type id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_device_set_of_user(request: web.Request, id, owner_name, app_name) -> web.Response:
    """test_get_device_set_of_user

    Gets a device set belonging to the user

    :param id: The UUID of the device set
    :type id: str
    :type id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_subscriptions(request: web.Request, owner_name, app_name) -> web.Response:
    """test_get_subscriptions

    Get information about the currently active subscriptions, if any

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_test_report(request: web.Request, test_run_id, owner_name, app_name) -> web.Response:
    """test_get_test_report

    Returns a single test report

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_test_run(request: web.Request, test_run_id, owner_name, app_name) -> web.Response:
    """test_get_test_run

    Returns a single test runs

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_test_run_state(request: web.Request, test_run_id, owner_name, app_name) -> web.Response:
    """test_get_test_run_state

    Gets state of the test run

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_get_test_runs(request: web.Request, owner_name, app_name) -> web.Response:
    """test_get_test_runs

    Returns a list of test runs

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_list_device_sets_of_owner(request: web.Request, owner_name, app_name) -> web.Response:
    """test_list_device_sets_of_owner

    Lists device sets belonging to the owner

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_list_device_sets_of_user(request: web.Request, owner_name, app_name) -> web.Response:
    """test_list_device_sets_of_user

    Lists device sets belonging to the user

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_patch_test_series(request: web.Request, test_series_slug, owner_name, app_name, body) -> web.Response:
    """test_patch_test_series

    Updates name and slug of a test series

    :param test_series_slug: The slug of the test series
    :type test_series_slug: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = NameOfTheTestSeries.from_dict(body)
    return web.Response(status=200)


async def test_start_test_run(request: web.Request, test_run_id, owner_name, app_name, body) -> web.Response:
    """test_start_test_run

    Starts test run

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Option required to start the test run
    :type body: dict | bytes

    """
    body = TestCloudStartTestRunOptions.from_dict(body)
    return web.Response(status=200)


async def test_start_uploading_file(request: web.Request, test_run_id, owner_name, app_name) -> web.Response:
    """test_start_uploading_file

    Uploads file for a test run

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_stop_test_run(request: web.Request, test_run_id, owner_name, app_name) -> web.Response:
    """test_stop_test_run

    Stop a test run execution

    :param test_run_id: The ID of the test run to be stopped
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def test_update_device_set_of_owner(request: web.Request, id, owner_name, app_name, body) -> web.Response:
    """test_update_device_set_of_owner

    Updates a device set belonging to the owner

    :param id: The UUID of the device set
    :type id: str
    :type id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceSetUpdateInformation.from_dict(body)
    return web.Response(status=200)


async def test_update_device_set_of_user(request: web.Request, id, owner_name, app_name, body) -> web.Response:
    """test_update_device_set_of_user

    Updates a device set belonging to the user

    :param id: The UUID of the device set
    :type id: str
    :type id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceSetUpdateInformation.from_dict(body)
    return web.Response(status=200)


async def test_upload_hash(request: web.Request, test_run_id, owner_name, app_name, body) -> web.Response:
    """test_upload_hash

    Adds file with the given hash to a test run

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: File hash information
    :type body: dict | bytes

    """
    body = TestCloudFileHash.from_dict(body)
    return web.Response(status=200)


async def test_upload_hashes_batch(request: web.Request, test_run_id, owner_name, app_name, body) -> web.Response:
    """test_upload_hashes_batch

    Adds file with the given hash to a test run

    :param test_run_id: The ID of the test run
    :type test_run_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: File hash information
    :type body: list | bytes

    """
    body = [TestCloudFileHash1.from_dict(d) for d in body]
    return web.Response(status=200)
