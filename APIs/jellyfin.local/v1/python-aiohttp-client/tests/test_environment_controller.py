# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_directory_browser_info_dto import DefaultDirectoryBrowserInfoDto
from openapi_server.models.file_system_entry_info import FileSystemEntryInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.validate_path_dto import ValidatePathDto


pytestmark = pytest.mark.asyncio

async def test_get_default_directory_browser(client):
    """Test case for get_default_directory_browser

    Get Default directory browser.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Environment/DefaultDirectoryBrowser',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_directory_contents(client):
    """Test case for get_directory_contents

    Gets the contents of a given directory in the file system.
    """
    params = [('path', 'path_example'),
                    ('includeFiles', False),
                    ('includeDirectories', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Environment/DirectoryContents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_drives(client):
    """Test case for get_drives

    Gets available drives from the server's file system.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Environment/Drives',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_shares(client):
    """Test case for get_network_shares

    Gets network paths.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Environment/NetworkShares',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_parent_path(client):
    """Test case for get_parent_path

    Gets the parent path of a given path.
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Environment/ParentPath',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_validate_path(client):
    """Test case for validate_path

    Validates path.
    """
    body = {"Path":"Path","IsFile":True,"ValidateWritable":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Environment/ValidatePath',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

