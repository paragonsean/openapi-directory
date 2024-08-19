# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_cve200_response import CheckCVE200Response
from openapi_server.models.get_all_cve200_response import GetAllCve200Response
from openapi_server.models.get_cve_check_configuration200_response import GetCVECheckConfiguration200Response
from openapi_server.models.get_cve_list200_response import GetCVEList200Response
from openapi_server.models.get_cve_list_request import GetCVEListRequest
from openapi_server.models.get_cve200_response import GetCve200Response
from openapi_server.models.get_last_cve_check200_response import GetLastCVECheck200Response
from openapi_server.models.read_cv_efrom_fs200_response import ReadCVEfromFS200Response
from openapi_server.models.update_cve200_response import UpdateCVE200Response
from openapi_server.models.update_cve_check_configuration200_response import UpdateCVECheckConfiguration200Response
from openapi_server.models.update_cve_check_configuration_request import UpdateCVECheckConfigurationRequest
from openapi_server.models.update_cve_request import UpdateCVERequest


pytestmark = pytest.mark.asyncio

async def test_check_cve(client):
    """Test case for check_cve

    Trigger a CVE check
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/cve/check',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_cve(client):
    """Test case for get_all_cve

    Get all CVE details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/cve',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cve(client):
    """Test case for get_cve

    Get a CVE details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/cve/{cve_id}'.format(cve_id='cve_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cve_check_configuration(client):
    """Test case for get_cve_check_configuration

    Get CVE check config
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/cve/check/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cve_list(client):
    """Test case for get_cve_list

    Get a list of CVE details
    """
    body = openapi_server.GetCVEListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/cve/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_cve_check(client):
    """Test case for get_last_cve_check

    Get last CVE check result
    """
    params = [('groupId', 'group_id_example'),
                    ('nodeId', 'node_id_example'),
                    ('cveId', 'cve_id_example'),
                    ('package', 'package_example'),
                    ('severity', 'severity_example')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/cve/check/last',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_cv_efrom_fs(client):
    """Test case for read_cv_efrom_fs

    Update CVE database from file system
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/cve/update/fs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cve(client):
    """Test case for update_cve

    Update CVE database from remote source
    """
    body = openapi_server.UpdateCVERequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/cve/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cve_check_configuration(client):
    """Test case for update_cve_check_configuration

    Update cve check config
    """
    body = openapi_server.UpdateCVECheckConfigurationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/cve/check/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

