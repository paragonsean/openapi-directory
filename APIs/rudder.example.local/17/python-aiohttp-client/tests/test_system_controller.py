# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_archive200_response import CreateArchive200Response
from openapi_server.models.get_healthcheck_result200_response import GetHealthcheckResult200Response
from openapi_server.models.get_status200_response import GetStatus200Response
from openapi_server.models.get_system_info200_response import GetSystemInfo200Response
from openapi_server.models.list_archives200_response import ListArchives200Response
from openapi_server.models.purge_software200_response import PurgeSoftware200Response
from openapi_server.models.regenerate_policies200_response import RegeneratePolicies200Response
from openapi_server.models.reload_all200_response import ReloadAll200Response
from openapi_server.models.reload_groups200_response import ReloadGroups200Response
from openapi_server.models.reload_techniques200_response import ReloadTechniques200Response
from openapi_server.models.restore_archive200_response import RestoreArchive200Response
from openapi_server.models.update_policies200_response import UpdatePolicies200Response


pytestmark = pytest.mark.asyncio

async def test_create_archive(client):
    """Test case for create_archive

    Create an archive
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/archives/{archive_kind}'.format(archive_kind='full'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_healthcheck_result(client):
    """Test case for get_healthcheck_result

    Get healthcheck
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/system/healthcheck',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    Get server status
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/system/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_system_info(client):
    """Test case for get_system_info

    Get server information
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/system/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_zip_archive(client):
    """Test case for get_zip_archive

    Get an archive as a ZIP
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/system/archives/{archive_kind}/zip/{commit_id}'.format(archive_kind='full', commit_id='commit_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_archives(client):
    """Test case for list_archives

    List archives
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/system/archives/{archive_kind}'.format(archive_kind='full'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purge_software(client):
    """Test case for purge_software

    Trigger batch for cleaning unreferenced software
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/maintenance/purgeSoftware',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regenerate_policies(client):
    """Test case for regenerate_policies

    Trigger a new policy generation
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/regenerate/policies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_all(client):
    """Test case for reload_all

    Reload both techniques and dynamic groups
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/reload',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_groups(client):
    """Test case for reload_groups

    Reload dynamic groups
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/reload/groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_techniques(client):
    """Test case for reload_techniques

    Reload techniques
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/reload/techniques',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_archive(client):
    """Test case for restore_archive

    Restore an archive
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/archives/{archive_kind}/restore/{archive_restore_kind}'.format(archive_kind='full', archive_restore_kind='latestCommit'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_policies(client):
    """Test case for update_policies

    Trigger update of policies
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/system/update/policies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

