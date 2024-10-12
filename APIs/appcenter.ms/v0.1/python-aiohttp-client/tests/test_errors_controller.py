# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diagnostics_stack_trace import DiagnosticsStackTrace
from openapi_server.models.errors_app_builds_list200_response import ErrorsAppBuildsList200Response
from openapi_server.models.errors_available_versions200_response import ErrorsAvailableVersions200Response
from openapi_server.models.errors_counts_per_day200_response import ErrorsCountsPerDay200Response
from openapi_server.models.errors_delete_error200_response import ErrorsDeleteError200Response
from openapi_server.models.errors_error_attachment_text200_response import ErrorsErrorAttachmentText200Response
from openapi_server.models.errors_error_attachments200_response_inner import ErrorsErrorAttachments200ResponseInner
from openapi_server.models.errors_error_groups_search200_response import ErrorsErrorGroupsSearch200Response
from openapi_server.models.errors_error_location200_response import ErrorsErrorLocation200Response
from openapi_server.models.errors_error_search200_response import ErrorsErrorSearch200Response
from openapi_server.models.errors_get_retention_settings200_response import ErrorsGetRetentionSettings200Response
from openapi_server.models.errors_group_details200_response import ErrorsGroupDetails200Response
from openapi_server.models.errors_group_error_free_device_percentages200_response import ErrorsGroupErrorFreeDevicePercentages200Response
from openapi_server.models.errors_group_list200_response import ErrorsGroupList200Response
from openapi_server.models.errors_group_model_counts200_response import ErrorsGroupModelCounts200Response
from openapi_server.models.errors_group_operating_system_counts200_response import ErrorsGroupOperatingSystemCounts200Response
from openapi_server.models.errors_latest_error_details200_response import ErrorsLatestErrorDetails200Response
from openapi_server.models.errors_list_for_group200_response import ErrorsListForGroup200Response
from openapi_server.models.errors_list_session_logs200_response import ErrorsListSessionLogs200Response
from openapi_server.models.errors_update_state_request import ErrorsUpdateStateRequest
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_errors_app_builds_list(client):
    """Test case for errors_app_builds_list

    
    """
    params = [('version', 'version_example'),
                    ('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('errorType', 'error_type_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/availableAppBuilds'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_available_versions(client):
    """Test case for errors_available_versions

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('$skip', 0),
                    ('$filter', 'filter_example'),
                    ('$inlinecount', none),
                    ('errorType', 'error_type_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/available_versions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_counts_per_day(client):
    """Test case for errors_counts_per_day

    
    """
    params = [('version', 'version_example'),
                    ('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('app_build', 'app_build_example'),
                    ('errorType', 'error_type_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorCountsPerDay'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_delete_error(client):
    """Test case for errors_delete_error

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errors/{error_id}'.format(error_group_id='error_group_id_example', error_id='error_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_attachment_location(client):
    """Test case for errors_error_attachment_location

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/{error_id}/attachments/{attachment_id}/location'.format(error_id='error_id_example', attachment_id='attachment_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_attachment_text(client):
    """Test case for errors_error_attachment_text

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/{error_id}/attachments/{attachment_id}/text'.format(error_id='error_id_example', attachment_id='attachment_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_attachments(client):
    """Test case for errors_error_attachments

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/{error_id}/attachments'.format(error_id='error_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_download(client):
    """Test case for errors_error_download

    
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errors/{error_id}/download'.format(error_group_id='error_group_id_example', error_id='error_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_free_device_percentages(client):
    """Test case for errors_error_free_device_percentages

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('versions', ['versions_example']),
                    ('app_build', 'app_build_example'),
                    ('errorType', 'error_type_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorfreeDevicePercentages'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_groups_search(client):
    """Test case for errors_error_groups_search

    
    """
    params = [('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('order', desc),
                    ('sort', matchingReportsCount),
                    ('$top', 100),
                    ('$skip', 0)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/search'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_location(client):
    """Test case for errors_error_location

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errors/{error_id}/location'.format(error_group_id='error_group_id_example', error_id='error_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_search(client):
    """Test case for errors_error_search

    
    """
    params = [('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('order', desc),
                    ('sort', timestamp),
                    ('$top', 100),
                    ('$skip', 0)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/search'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_error_stack_trace(client):
    """Test case for errors_error_stack_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errors/{error_id}/stacktrace'.format(error_group_id='error_group_id_example', error_id='error_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_get_error_details(client):
    """Test case for errors_get_error_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errors/{error_id}'.format(error_group_id='error_group_id_example', error_id='error_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_get_retention_settings(client):
    """Test case for errors_get_retention_settings

    gets the retention settings in days
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/retention_settings'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_group_counts_per_day(client):
    """Test case for errors_group_counts_per_day

    
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
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errorCountsPerDay'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_group_details(client):
    """Test case for errors_group_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_group_error_free_device_percentages(client):
    """Test case for errors_group_error_free_device_percentages

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errorfreeDevicePercentages'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_group_error_stack_trace(client):
    """Test case for errors_group_error_stack_trace

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/stacktrace'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_group_list(client):
    """Test case for errors_group_list

    
    """
    params = [('version', 'version_example'),
                    ('app_build', 'app_build_example'),
                    ('groupState', 'group_state_example'),
                    ('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$orderby', 'count desc'),
                    ('$top', 30),
                    ('errorType', 'error_type_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_group_model_counts(client):
    """Test case for errors_group_model_counts

    
    """
    params = [('$top', 30)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/models'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_group_operating_system_counts(client):
    """Test case for errors_group_operating_system_counts

    
    """
    params = [('$top', 30)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/operatingSystems'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_latest_error_details(client):
    """Test case for errors_latest_error_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errors/latest'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_list_for_group(client):
    """Test case for errors_list_for_group

    
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('$top', 30),
                    ('model', 'model_example'),
                    ('os', 'os_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}/errors'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_list_session_logs(client):
    """Test case for errors_list_session_logs

    
    """
    params = [('date', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/{error_id}/sessionLogs'.format(error_id='error_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_update_state(client):
    """Test case for errors_update_state

    
    """
    body = openapi_server.ErrorsUpdateStateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{error_group_id}'.format(error_group_id='error_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

