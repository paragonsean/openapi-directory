# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.package import Package
from openapi_server.models.package_file import PackageFile


pytestmark = pytest.mark.asyncio

async def test_delete_package(client):
    """Test case for delete_package

    Delete a package
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/packages/{owner}/{type}/{name}/{version}'.format(owner='owner_example', type='type_example', name='name_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_package(client):
    """Test case for get_package

    Gets a package
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/packages/{owner}/{type}/{name}/{version}'.format(owner='owner_example', type='type_example', name='name_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_package_files(client):
    """Test case for list_package_files

    Gets all files of a package
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/packages/{owner}/{type}/{name}/{version}/files'.format(owner='owner_example', type='type_example', name='name_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_packages(client):
    """Test case for list_packages

    Gets all packages of an owner
    """
    params = [('page', 56),
                    ('limit', 56),
                    ('type', 'type_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/packages/{owner}'.format(owner='owner_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

