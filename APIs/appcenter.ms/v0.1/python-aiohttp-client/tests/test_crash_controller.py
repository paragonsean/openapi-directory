# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branch_configurations_delete200_response import BranchConfigurationsDelete200Response
from openapi_server.models.crash import Crash
from openapi_server.models.crash_groups_list200_response import CrashGroupsList200Response
from openapi_server.models.crash_groups_list200_response_crash_groups_inner import CrashGroupsList200ResponseCrashGroupsInner
from openapi_server.models.crash_groups_update_request import CrashGroupsUpdateRequest
from openapi_server.models.crashes_delete200_response import CrashesDelete200Response
from openapi_server.models.crashes_get_app_crashes_info200_response import CrashesGetAppCrashesInfo200Response
from openapi_server.models.crashes_get_app_versions200_response_inner import CrashesGetAppVersions200ResponseInner
from openapi_server.models.crashes_get_crash_attachment_location200_response import CrashesGetCrashAttachmentLocation200Response
from openapi_server.models.crashes_get_raw_crash_location200_response import CrashesGetRawCrashLocation200Response
from openapi_server.models.crashes_list_attachments200_response_inner import CrashesListAttachments200ResponseInner
from openapi_server.models.missing_symbol_groups_info200_response import MissingSymbolGroupsInfo200Response
from openapi_server.models.missing_symbol_groups_list200_response import MissingSymbolGroupsList200Response
from openapi_server.models.missing_symbol_groups_list_default_response import MissingSymbolGroupsListDefaultResponse
from openapi_server.models.stacktrace import Stacktrace
from openapi_server.models.symbol_uploads_complete_request import SymbolUploadsCompleteRequest
from openapi_server.models.symbol_uploads_create200_response import SymbolUploadsCreate200Response
from openapi_server.models.symbol_uploads_create_request import SymbolUploadsCreateRequest
from openapi_server.models.symbol_uploads_get_location200_response import SymbolUploadsGetLocation200Response
from openapi_server.models.symbol_uploads_list200_response_inner import SymbolUploadsList200ResponseInner
from openapi_server.models.symbols_get_location200_response import SymbolsGetLocation200Response
from openapi_server.models.symbols_get_status200_response import SymbolsGetStatus200Response
from openapi_server.models.symbols_list200_response_inner import SymbolsList200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_crash_groups_get(client):
    """Test case for crash_groups_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crash_groups_get_stacktrace(client):
    """Test case for crash_groups_get_stacktrace

    
    """
    params = [('grouping_only', False)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/stacktrace'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crash_groups_list(client):
    """Test case for crash_groups_list

    
    """
    params = [('last_occurrence_from', '2013-10-20T19:20:30+01:00'),
                    ('last_occurrence_to', '2013-10-20T19:20:30+01:00'),
                    ('app_version', 'app_version_example'),
                    ('group_type', 'group_type_example'),
                    ('group_status', 'group_status_example'),
                    ('group_text_search', 'group_text_search_example'),
                    ('$orderby', last_occurrence desc),
                    ('continuation_token', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crash_groups_update(client):
    """Test case for crash_groups_update

    
    """
    body = openapi_server.CrashGroupsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_delete(client):
    """Test case for crashes_delete

    
    """
    params = [('retention_delete', False)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}'.format(crash_group_id='crash_group_id_example', crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get(client):
    """Test case for crashes_get

    
    """
    params = [('include_report', False),
                    ('include_log', False),
                    ('include_details', False),
                    ('include_stacktrace', False),
                    ('grouping_only', False)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}'.format(crash_group_id='crash_group_id_example', crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_app_crashes_info(client):
    """Test case for crashes_get_app_crashes_info

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crashes_info'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_app_versions(client):
    """Test case for crashes_get_app_versions

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/versions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_crash_attachment_location(client):
    """Test case for crashes_get_crash_attachment_location

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/location'.format(crash_id='crash_id_example', attachment_id='attachment_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_crash_text_attachment_content(client):
    """Test case for crashes_get_crash_text_attachment_content

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/text'.format(crash_id='crash_id_example', attachment_id='attachment_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_native_crash(client):
    """Test case for crashes_get_native_crash

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native'.format(crash_group_id='crash_group_id_example', crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_native_crash_download(client):
    """Test case for crashes_get_native_crash_download

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native/download'.format(crash_group_id='crash_group_id_example', crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_raw_crash_location(client):
    """Test case for crashes_get_raw_crash_location

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/raw/location'.format(crash_group_id='crash_group_id_example', crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_get_stacktrace(client):
    """Test case for crashes_get_stacktrace

    
    """
    params = [('grouping_only', False)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/stacktrace'.format(crash_group_id='crash_group_id_example', crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_list(client):
    """Test case for crashes_list

    
    """
    params = [('include_report', False),
                    ('include_log', False),
                    ('date_from', '2013-10-20T19:20:30+01:00'),
                    ('date_to', '2013-10-20T19:20:30+01:00'),
                    ('app_version', 'app_version_example'),
                    ('error_type', 'error_type_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes'.format(crash_group_id='crash_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crashes_list_attachments(client):
    """Test case for crashes_list_attachments

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments'.format(crash_id='crash_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_missing_symbol_groups_get(client):
    """Test case for missing_symbol_groups_get

    Gets missing symbol crash group by its id
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups/{symbol_group_id}'.format(symbol_group_id='symbol_group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_missing_symbol_groups_info(client):
    """Test case for missing_symbol_groups_info

    Gets application level statistics for all missing symbol groups
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups_info'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_missing_symbol_groups_list(client):
    """Test case for missing_symbol_groups_list

    Gets top N (ordered by crash count) of crash groups by missing symbol
    """
    params = [('top', 56)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbol_uploads_complete(client):
    """Test case for symbol_uploads_complete

    
    """
    body = openapi_server.SymbolUploadsCompleteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id}'.format(symbol_upload_id='symbol_upload_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbol_uploads_create(client):
    """Test case for symbol_uploads_create

    
    """
    body = openapi_server.SymbolUploadsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/symbol_uploads'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbol_uploads_delete(client):
    """Test case for symbol_uploads_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id}'.format(symbol_upload_id='symbol_upload_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbol_uploads_get(client):
    """Test case for symbol_uploads_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id}'.format(symbol_upload_id='symbol_upload_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbol_uploads_get_location(client):
    """Test case for symbol_uploads_get_location

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id}/location'.format(symbol_upload_id='symbol_upload_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbol_uploads_list(client):
    """Test case for symbol_uploads_list

    
    """
    params = [('top', 30),
                    ('status', 'status_example'),
                    ('symbol_type', 'symbol_type_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/symbol_uploads'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbols_get(client):
    """Test case for symbols_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}'.format(symbol_id='symbol_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbols_get_location(client):
    """Test case for symbols_get_location

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/location'.format(symbol_id='symbol_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbols_get_status(client):
    """Test case for symbols_get_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/status'.format(symbol_id='symbol_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbols_ignore(client):
    """Test case for symbols_ignore

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/ignore'.format(symbol_id='symbol_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbols_list(client):
    """Test case for symbols_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/symbols'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

