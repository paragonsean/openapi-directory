# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.discovered_nas_share import DiscoveredNasShare
from openapi_server.models.host_detail import HostDetail
from openapi_server.models.host_make_primary_request import HostMakePrimaryRequest
from openapi_server.models.host_register import HostRegister
from openapi_server.models.host_summary_list_response import HostSummaryListResponse
from openapi_server.models.host_update import HostUpdate
from openapi_server.models.host_volume_summary_list_response import HostVolumeSummaryListResponse
from openapi_server.models.rbs_host_operation_request import RbsHostOperationRequest
from openapi_server.models.rbs_host_operation_response import RbsHostOperationResponse
from openapi_server.models.rbs_host_summary import RbsHostSummary
from openapi_server.models.search_response_list_response import SearchResponseListResponse


pytestmark = pytest.mark.asyncio

async def test_bulk_register_host_async(client):
    """Test case for bulk_register_host_async

    Register hosts
    """
    body = {"organizationId":"organizationId","hdfsConfig":{"apiToken":"apiToken","hosts":[{"hostname":"hostname","port":0},{"hostname":"hostname","port":0}],"kerberosTicket":"kerberosTicket","nameservices":"nameservices","username":"username"},"oracleQueryUser":"oracleQueryUser","hostname":"hostname","hasAgent":True,"isOracleHost":True,"nasConfig":{"vendorType":"vendorType","apiEndpoint":"apiEndpoint","apiToken":"apiToken","isNetAppSnapDiffEnabled":True,"isIsilonChangelistEnabled":True,"apiHostname":"apiHostname","apiPassword":"apiPassword","zoneName":"zoneName","apiCertificate":"apiCertificate","isShareAutoDiscoveryEnabled":True,"apiUsername":"apiUsername"},"alias":"alias","oracleSysDbaUser":"oracleSysDbaUser"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/bulk_background',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_host(client):
    """Test case for delete_host

    Delete a registered host
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/host/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discover_nas_shares(client):
    """Test case for discover_nas_shares

    Discover and return all shares on a NAS host
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host/{id}/nas_share_discover'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_host(client):
    """Test case for get_host

    Get summary information for a host
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rbs_host_info(client):
    """Test case for get_rbs_host_info

    Get the Rubrik Backup Service details for a host
    """
    params = [('name', 'name_example'),
                    ('username', 'username_example'),
                    ('password', 'password_example'),
                    ('operation_timeout', 600)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host/rbs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_host_make_primary(client):
    """Test case for host_make_primary

    Make this cluster the primary for agents on a set of hosts
    """
    body = {"oldPrimaryClusterUuid":"oldPrimaryClusterUuid","ids":["ids","ids"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/make_primary',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_host(client):
    """Test case for query_host

    Get summary information for hosts
    """
    params = [('operating_system_type', 'operating_system_type_example'),
                    ('operating_system', 'operating_system_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('name', 'name_example'),
                    ('hostname', 'hostname_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_host_volume(client):
    """Test case for query_host_volume

    Get list of Volume Group volumes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host/{id}/volume'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbs_install(client):
    """Test case for rbs_install

    Install Rubrik Backup Service on a host
    """
    body = {"password":"password","operationMode":"Synchronous","operationTimeout":0,"name":"name","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/rbs/install',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbs_uninstall(client):
    """Test case for rbs_uninstall

    Uninstall Rubrik Backup Service from a host
    """
    body = {"password":"password","operationMode":"Synchronous","operationTimeout":0,"name":"name","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/rbs/uninstall',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbs_upgrade(client):
    """Test case for rbs_upgrade

    Upgrade Rubrik Backup Service on a host
    """
    body = {"password":"password","operationMode":"Synchronous","operationTimeout":0,"name":"name","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/rbs/upgrade',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_host(client):
    """Test case for refresh_host

    Refresh a host
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/{id}/refresh'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_host(client):
    """Test case for register_host

    Register a host
    """
    body = {"organizationId":"organizationId","hdfsConfig":{"apiToken":"apiToken","hosts":[{"hostname":"hostname","port":0},{"hostname":"hostname","port":0}],"kerberosTicket":"kerberosTicket","nameservices":"nameservices","username":"username"},"oracleQueryUser":"oracleQueryUser","hostname":"hostname","hasAgent":True,"isOracleHost":True,"nasConfig":{"vendorType":"vendorType","apiEndpoint":"apiEndpoint","apiToken":"apiToken","isNetAppSnapDiffEnabled":True,"isIsilonChangelistEnabled":True,"apiHostname":"apiHostname","apiPassword":"apiPassword","zoneName":"zoneName","apiCertificate":"apiCertificate","isShareAutoDiscoveryEnabled":True,"apiUsername":"apiUsername"},"alias":"alias","oracleSysDbaUser":"oracleSysDbaUser"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_host_async(client):
    """Test case for register_host_async

    Register a host
    """
    body = {"organizationId":"organizationId","hdfsConfig":{"apiToken":"apiToken","hosts":[{"hostname":"hostname","port":0},{"hostname":"hostname","port":0}],"kerberosTicket":"kerberosTicket","nameservices":"nameservices","username":"username"},"oracleQueryUser":"oracleQueryUser","hostname":"hostname","hasAgent":True,"isOracleHost":True,"nasConfig":{"vendorType":"vendorType","apiEndpoint":"apiEndpoint","apiToken":"apiToken","isNetAppSnapDiffEnabled":True,"isIsilonChangelistEnabled":True,"apiHostname":"apiHostname","apiPassword":"apiPassword","zoneName":"zoneName","apiCertificate":"apiCertificate","isShareAutoDiscoveryEnabled":True,"apiUsername":"apiUsername"},"alias":"alias","oracleSysDbaUser":"oracleSysDbaUser"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/background',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_host(client):
    """Test case for search_host

    Search for a file within the host
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host/{id}/search'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_certificate_host(client):
    """Test case for update_certificate_host

    Update certificate
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/host/certificate/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_host(client):
    """Test case for update_host

    Modify information for a registered host
    """
    body = {"hostVfdEnabled":"Enabled","hdfsConfig":{"apiToken":"apiToken","hosts":[{"hostname":"hostname","port":0},{"hostname":"hostname","port":0}],"kerberosTicket":"kerberosTicket","nameservices":"nameservices","username":"username"},"oracleQueryUser":"oracleQueryUser","hostname":"hostname","compressionEnabled":True,"isOracleHost":True,"hostVfdDriverInstalled":True,"nasConfig":{"vendorType":"vendorType","apiEndpoint":"apiEndpoint","apiToken":"apiToken","isNetAppSnapDiffEnabled":True,"isIsilonChangelistEnabled":True,"apiHostname":"apiHostname","apiPassword":"apiPassword","zoneName":"zoneName","apiCertificate":"apiCertificate","isShareAutoDiscoveryEnabled":True,"apiUsername":"apiUsername"},"alias":"alias","oracleSysDbaUser":"oracleSysDbaUser","mssqlCbtDriverInstalled":True,"mssqlCbtEnabled":"Enabled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/host/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

