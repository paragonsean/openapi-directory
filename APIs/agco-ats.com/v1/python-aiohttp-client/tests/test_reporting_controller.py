# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_bundle import APIPagedResponseUpdateSystemModelsBundle
from openapi_server.models.api_paged_response_update_system_models_client_status_update_system_models_paged_client_status_metadata import APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata
from openapi_server.models.api_paged_response_update_system_models_package_status_summary import APIPagedResponseUpdateSystemModelsPackageStatusSummary
from openapi_server.models.api_paged_response_update_system_models_update_group import APIPagedResponseUpdateSystemModelsUpdateGroup
from openapi_server.models.api_paged_response_update_system_models_update_group_client_relationship import APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
from openapi_server.models.update_system_models_client import UpdateSystemModelsClient
from openapi_server.models.update_system_models_client_info import UpdateSystemModelsClientInfo
from openapi_server.models.update_system_models_package import UpdateSystemModelsPackage
from openapi_server.models.update_system_models_package_status_summary import UpdateSystemModelsPackageStatusSummary
from openapi_server.models.update_system_models_update_metrics_data import UpdateSystemModelsUpdateMetricsData


pytestmark = pytest.mark.asyncio

async def test_reporting_bundle_status_summary(client):
    """Test case for reporting_bundle_status_summary

    Get a summary of all Packages in a Bundle
    """
    params = [('BundleID', 'bundle_id_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/BundleStatusSummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_bundles_in_update_group(client):
    """Test case for reporting_bundles_in_update_group

    Get a list of bundles for UpdateGroup.
    """
    params = [('ID', 'id_example'),
                    ('IncludeInactive', True),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/BundlesInUpdateGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_client_info(client):
    """Test case for reporting_client_info

    Get Client Information
    """
    params = [('ClientID', 'client_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/ClientInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_current_packages_in_update_group(client):
    """Test case for reporting_current_packages_in_update_group

    Get the current packages for an update group.
    """
    params = [('ID', 'id_example'),
                    ('SubscriptionTypeFilter', 'subscription_type_filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/CurrentPackagesInUpdateGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_get_client(client):
    """Test case for reporting_get_client

    Get a Client in the Update System.
    """
    params = [('ID', 'id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/GetClient',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_get_subscriptions(client):
    """Test case for reporting_get_subscriptions

    Get a list of current Client Subscriptions.
    """
    params = [('ClientID', 'client_id_example'),
                    ('UpdateGroupID', 'update_group_id_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/GetSubscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_package_status_summary(client):
    """Test case for reporting_package_status_summary

    Get a summary report for a Specific Package
    """
    params = [('PackageID', 'package_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/PackageStatusSummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_registered_clients(client):
    """Test case for reporting_registered_clients

    Get a list of subscribed clients
    """
    params = [('UpdateGroupID', 'update_group_id_example'),
                    ('ClientID', 'client_id_example'),
                    ('Tag', 'tag_example'),
                    ('ReportResult', 'report_result_example'),
                    ('ReportResultIsValid', True),
                    ('ReportValue', 'report_value_example'),
                    ('LastCheckInBefore', '2013-10-20T19:20:30+01:00'),
                    ('LastCheckInAfter', '2013-10-20T19:20:30+01:00'),
                    ('OrderBy', 'order_by_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/RegisteredClients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_update_groups(client):
    """Test case for reporting_update_groups

    Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/UpdateGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_update_metrics(client):
    """Test case for reporting_update_metrics

    Get data for pie charts in UpdateMetrics.
    """
    params = [('UpdateGroupID', 'update_group_id_example'),
                    ('bundleNumber', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Reporting/UpdateMetrics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

