# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analytics_crash_counts200_response import AnalyticsCrashCounts200Response
from openapi_server.models.analytics_crash_free_device_percentages200_response import AnalyticsCrashFreeDevicePercentages200Response
from openapi_server.models.analytics_crash_group_model_counts200_response import AnalyticsCrashGroupModelCounts200Response
from openapi_server.models.analytics_crash_group_operating_system_counts200_response import AnalyticsCrashGroupOperatingSystemCounts200Response
from openapi_server.models.analytics_crash_groups_totals200_response_inner import AnalyticsCrashGroupsTotals200ResponseInner
from openapi_server.models.analytics_crash_groups_totals200_response_inner_overall import AnalyticsCrashGroupsTotals200ResponseInnerOverall
from openapi_server.models.analytics_crash_groups_totals_request import AnalyticsCrashGroupsTotalsRequest
from openapi_server.models.analytics_device_counts200_response import AnalyticsDeviceCounts200Response
from openapi_server.models.analytics_device_counts200_response_daily_inner import AnalyticsDeviceCounts200ResponseDailyInner
from openapi_server.models.analytics_device_counts_default_response import AnalyticsDeviceCountsDefaultResponse
from openapi_server.models.analytics_distribution_release_counts200_response import AnalyticsDistributionReleaseCounts200Response
from openapi_server.models.analytics_distribution_release_counts_request import AnalyticsDistributionReleaseCountsRequest
from openapi_server.models.analytics_event_count200_response import AnalyticsEventCount200Response
from openapi_server.models.analytics_event_device_count200_response import AnalyticsEventDeviceCount200Response
from openapi_server.models.analytics_event_per_device_count200_response import AnalyticsEventPerDeviceCount200Response
from openapi_server.models.analytics_event_per_session_count200_response import AnalyticsEventPerSessionCount200Response
from openapi_server.models.analytics_event_properties200_response import AnalyticsEventProperties200Response
from openapi_server.models.analytics_event_property_counts200_response import AnalyticsEventPropertyCounts200Response
from openapi_server.models.analytics_events200_response import AnalyticsEvents200Response
from openapi_server.models.analytics_generic_log_flow200_response import AnalyticsGenericLogFlow200Response
from openapi_server.models.analytics_get_audience200_response import AnalyticsGetAudience200Response
from openapi_server.models.analytics_language_counts200_response import AnalyticsLanguageCounts200Response
from openapi_server.models.analytics_list_audiences200_response import AnalyticsListAudiences200Response
from openapi_server.models.analytics_list_custom_properties200_response import AnalyticsListCustomProperties200Response
from openapi_server.models.analytics_list_device_property_values200_response import AnalyticsListDevicePropertyValues200Response
from openapi_server.models.analytics_log_flow200_response import AnalyticsLogFlow200Response
from openapi_server.models.analytics_model_counts200_response import AnalyticsModelCounts200Response
from openapi_server.models.analytics_operating_system_counts200_response import AnalyticsOperatingSystemCounts200Response
from openapi_server.models.analytics_per_device_counts200_response import AnalyticsPerDeviceCounts200Response
from openapi_server.models.analytics_place_counts200_response import AnalyticsPlaceCounts200Response
from openapi_server.models.analytics_session_durations_distribution200_response import AnalyticsSessionDurationsDistribution200Response
from openapi_server.models.analytics_test_audience200_response import AnalyticsTestAudience200Response
from openapi_server.models.analytics_test_audience_request import AnalyticsTestAudienceRequest
from openapi_server.models.analytics_versions200_response import AnalyticsVersions200Response
from openapi_server.models.crashes_list_session_logs200_response import CrashesListSessionLogs200Response
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_analytics_audience_name_exists(client):
    """Test case for analytics_audience_name_exists

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name}'.format(audience_name='audience_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_crash_counts(client):
    """Test case for analytics_crash_counts

    Available for UWP apps only.
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/crash_counts'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_crash_free_device_percentages(client):
    """Test case for analytics_crash_free_device_percentages

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/crashfree_device_percentages'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_crash_group_counts(client):
    """Test case for analytics_crash_group_counts

    Available for UWP apps only.
    """
    params = [('version', 'version_example'),
                    ('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/crash_counts'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_crash_group_model_counts(client):
    """Test case for analytics_crash_group_model_counts

    Available for UWP apps only.
    """
    params = [('version', 'version_example'),
                    ('$top', 30)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/models'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_crash_group_operating_system_counts(client):
    """Test case for analytics_crash_group_operating_system_counts

    Available for UWP apps only.
    """
    params = [('version', 'version_example'),
                    ('$top', 30)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/operating_systems'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_crash_group_totals(client):
    """Test case for analytics_crash_group_totals

    Available for UWP apps only.
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/overall'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_crash_groups_totals(client):
    """Test case for analytics_crash_groups_totals

    
    """
    body = openapi_server.AnalyticsCrashGroupsTotalsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_create_or_update_audience(client):
    """Test case for analytics_create_or_update_audience

    
    """
    body = openapi_server.AnalyticsTestAudienceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name}'.format(audience_name='audience_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_delete_audience(client):
    """Test case for analytics_delete_audience

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name}'.format(audience_name='audience_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_device_counts(client):
    """Test case for analytics_device_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example']),
                    ('app_build', 'app_build_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/active_device_counts'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_distribution_release_counts(client):
    """Test case for analytics_distribution_release_counts

    
    """
    body = openapi_server.AnalyticsDistributionReleaseCountsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/distribution/release_counts'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_event_count(client):
    """Test case for analytics_event_count

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/event_count'.format(event_name='event_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_event_device_count(client):
    """Test case for analytics_event_device_count

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/device_count'.format(event_name='event_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_event_per_device_count(client):
    """Test case for analytics_event_per_device_count

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_device'.format(event_name='event_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_event_per_session_count(client):
    """Test case for analytics_event_per_session_count

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_session'.format(event_name='event_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_event_properties(client):
    """Test case for analytics_event_properties

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties'.format(event_name='event_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_event_property_counts(client):
    """Test case for analytics_event_property_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example']),
                    ('$top', 10)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties/{event_property_name}/counts'.format(event_name='event_name_example', event_property_name='event_property_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_events(client):
    """Test case for analytics_events

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example']),
                    ('event_name', ['event_name_example']),
                    ('$top', 30),
                    ('$skip', 0),
                    ('$inlinecount', none),
                    ('$orderby', 'count desc')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_events_delete(client):
    """Test case for analytics_events_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}'.format(event_name='event_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_events_delete_logs(client):
    """Test case for analytics_events_delete_logs

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/event_logs/{event_name}'.format(event_name='event_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_generic_log_flow(client):
    """Test case for analytics_generic_log_flow

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/generic_log_flow'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_get_audience(client):
    """Test case for analytics_get_audience

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name}'.format(audience_name='audience_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_language_counts(client):
    """Test case for analytics_language_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/languages'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_list_audiences(client):
    """Test case for analytics_list_audiences

    
    """
    params = [('include_disabled', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_list_custom_properties(client):
    """Test case for analytics_list_custom_properties

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/custom_properties'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_list_device_properties(client):
    """Test case for analytics_list_device_properties

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_list_device_property_values(client):
    """Test case for analytics_list_device_property_values

    
    """
    params = [('contains', 'contains_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties/{property_name}/values'.format(property_name='property_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_log_flow(client):
    """Test case for analytics_log_flow

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/log_flow'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_model_counts(client):
    """Test case for analytics_model_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/models'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_operating_system_counts(client):
    """Test case for analytics_operating_system_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/oses'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_per_device_counts(client):
    """Test case for analytics_per_device_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/sessions_per_device'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_place_counts(client):
    """Test case for analytics_place_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/places'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_session_counts(client):
    """Test case for analytics_session_counts

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/session_counts'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_session_durations_distribution(client):
    """Test case for analytics_session_durations_distribution

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/session_durations_distribution'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_test_audience(client):
    """Test case for analytics_test_audience

    
    """
    body = openapi_server.AnalyticsTestAudienceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/audiences/definition/test'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_versions(client):
    """Test case for analytics_versions

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('versions', ['versions_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/analytics/versions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_block_logs(client):
    """Test case for app_block_logs

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/devices/block_logs'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_list_session_logs(client):
    """Test case for crashes_list_session_logs

    
    """
    params = [('date', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/session_logs'.format(crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_block_logs(client):
    """Test case for devices_block_logs

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/devices/block_logs/{install_id}'.format(install_id='install_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

