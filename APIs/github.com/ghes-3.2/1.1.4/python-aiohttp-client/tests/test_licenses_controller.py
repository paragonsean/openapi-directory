# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.license import License
from openapi_server.models.license_content import LicenseContent
from openapi_server.models.license_simple import LicenseSimple


pytestmark = pytest.mark.asyncio

async def test_licenses_get(client):
    """Test case for licenses_get

    Get a license
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/licenses/{license}'.format(license='license_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_licenses_get_all_commonly_used(client):
    """Test case for licenses_get_all_commonly_used

    Get all commonly used licenses
    """
    params = [('featured', True),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_licenses_get_for_repo(client):
    """Test case for licenses_get_for_repo

    Get the license for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/license'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

