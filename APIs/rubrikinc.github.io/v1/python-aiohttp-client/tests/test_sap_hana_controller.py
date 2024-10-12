# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.sap_hana_add_system_response import SapHanaAddSystemResponse
from openapi_server.models.sap_hana_database_detail import SapHanaDatabaseDetail
from openapi_server.models.sap_hana_database_patch import SapHanaDatabasePatch
from openapi_server.models.sap_hana_database_snapshot_detail import SapHanaDatabaseSnapshotDetail
from openapi_server.models.sap_hana_database_snapshot_summary_list_response import SapHanaDatabaseSnapshotSummaryListResponse
from openapi_server.models.sap_hana_database_summary_list_response import SapHanaDatabaseSummaryListResponse
from openapi_server.models.sap_hana_patch_system_response import SapHanaPatchSystemResponse
from openapi_server.models.sap_hana_recoverable_range_list_response import SapHanaRecoverableRangeListResponse
from openapi_server.models.sap_hana_restore_source_config import SapHanaRestoreSourceConfig
from openapi_server.models.sap_hana_system_config import SapHanaSystemConfig
from openapi_server.models.sap_hana_system_patch import SapHanaSystemPatch
from openapi_server.models.sap_hana_system_summary import SapHanaSystemSummary
from openapi_server.models.sap_hana_system_summary_list_response import SapHanaSystemSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_add_sap_hana_system(client):
    """Test case for add_sap_hana_system

    Add a SAP HANA system
    """
    body = {"password":"password","dataPathSpec":{"dataPathType":"GCP"},"instanceNumber":"instanceNumber","hostIds":["hostIds","hostIds"],"sid":"sid","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sap_hana/system',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_sap_hana_restore(client):
    """Test case for configure_sap_hana_restore

    Configure the target database for system copy restore
    """
    body = {"snappable_id":"snappable_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sap_hana/db/{id}/configure_restore'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_on_demand_sap_hana_backup(client):
    """Test case for create_on_demand_sap_hana_backup

    Create on demand database snapshot
    """
    body = {"slaId":"slaId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sap_hana/db/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_sap_hana_system_refresh(client):
    """Test case for create_sap_hana_system_refresh

    Refresh SAP HANA system metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sap_hana/system/{id}/refresh'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sap_hana_db_snapshot(client):
    """Test case for delete_sap_hana_db_snapshot

    Delete a particular full snapshot of a SAP HANA database
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sap_hana/db/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sap_hana_system(client):
    """Test case for delete_sap_hana_system

    Delete a SAP HANA system
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sap_hana/system/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_missed_sap_hana_db_snapshots(client):
    """Test case for get_missed_sap_hana_db_snapshots

    Retrieve summary information for missed snapshots of a SAP HANA database
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/db/{id}/missed_snapshot'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sap_hana_database(client):
    """Test case for get_sap_hana_database

    Get detailed information for an SAP HANA database
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/db/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sap_hana_db_async_request_status(client):
    """Test case for get_sap_hana_db_async_request_status

    Get the status of a SAP HANA database request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/db/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sap_hana_db_recoverable_ranges(client):
    """Test case for get_sap_hana_db_recoverable_ranges

    Get recoverable ranges of a SAP HANA database
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/db/{id}/recoverable_range'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sap_hana_db_snapshot(client):
    """Test case for get_sap_hana_db_snapshot

    Get SAP HANA database snapshot details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/db/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sap_hana_system(client):
    """Test case for get_sap_hana_system

    Get summary information for a SAP HANA system
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/system/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sap_hana_system_async_request_status(client):
    """Test case for get_sap_hana_system_async_request_status

    Get the status of a SAP HANA system request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/system/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_sap_hana_database(client):
    """Test case for patch_sap_hana_database

    Update the SLA Domain for an SAP HANA database
    """
    body = {"logSnapshotJobIntervalInMinutes":0,"configuredSlaDomainId":"configuredSlaDomainId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/sap_hana/db/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_sap_hana_system(client):
    """Test case for patch_sap_hana_system

    Update the SLA Domain for a SAP HANA system
    """
    body = {"password":"password","configuredSlaDomainId":"configuredSlaDomainId","instanceNumber":"instanceNumber","hostIds":["hostIds","hostIds"],"sid":"sid","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/sap_hana/system/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_sap_hana_databases(client):
    """Test case for query_sap_hana_databases

    Get summary information for discovered SAP HANA databases
    """
    params = [('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('name', 'name_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('is_relic', True),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/db',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_sap_hana_db_snapshot(client):
    """Test case for query_sap_hana_db_snapshot

    Get a summary list of snapshots for a SAP HANA database
    """
    params = [('backup_type', 'backup_type_example'),
                    ('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/db/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_sap_hana_systems(client):
    """Test case for query_sap_hana_systems

    Get summary information for added SAP HANA systems
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('sid', 'sid_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sap_hana/system',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unconfigure_sap_hana_restore(client):
    """Test case for unconfigure_sap_hana_restore

    Reset the configuration for system copy restore on target database
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sap_hana/db/{id}/unconfigure_restore'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

