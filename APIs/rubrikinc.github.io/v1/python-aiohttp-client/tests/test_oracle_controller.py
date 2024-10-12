# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.bulk_oracle_db_details import BulkOracleDbDetails
from openapi_server.models.bulk_oracle_host_details import BulkOracleHostDetails
from openapi_server.models.bulk_oracle_rac_details import BulkOracleRacDetails
from openapi_server.models.oracle_aco_parameter_list import OracleAcoParameterList
from openapi_server.models.oracle_aco_validation_result import OracleAcoValidationResult
from openapi_server.models.oracle_bulk_update import OracleBulkUpdate
from openapi_server.models.oracle_data_guard_group_update import OracleDataGuardGroupUpdate
from openapi_server.models.oracle_db_detail import OracleDbDetail
from openapi_server.models.oracle_db_summary_list_response import OracleDbSummaryListResponse
from openapi_server.models.oracle_file_download_link import OracleFileDownloadLink
from openapi_server.models.oracle_restore_estimate_result import OracleRestoreEstimateResult
from openapi_server.models.oracle_update import OracleUpdate
from openapi_server.models.oracle_validate_config import OracleValidateConfig


pytestmark = pytest.mark.asyncio

async def test_bulk_update_oracle_db(client):
    """Test case for bulk_update_oracle_db

    Update Oracle Databases
    """
    body = {"numChannels":5,"hostLogRetentionHours":0,"logBackupFrequencyInMinutes":6,"logRetentionHours":1,"ids":["ids","ids"],"configuredSlaDomainIdDeprecated":"configuredSlaDomainIdDeprecated","nodeOrder":[{"nodeName":"nodeName","order":5},{"nodeName":"nodeName","order":5}],"hostMount":"hostMount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/oracle/db/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_oracle_host(client):
    """Test case for bulk_update_oracle_host

    Update Oracle Hosts
    """
    body = {"numChannels":5,"hostLogRetentionHours":0,"logBackupFrequencyInMinutes":6,"logRetentionHours":1,"ids":["ids","ids"],"configuredSlaDomainIdDeprecated":"configuredSlaDomainIdDeprecated","nodeOrder":[{"nodeName":"nodeName","order":5},{"nodeName":"nodeName","order":5}],"hostMount":"hostMount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/oracle/host/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_oracle_rac(client):
    """Test case for bulk_update_oracle_rac

    Update Oracle RACs
    """
    body = {"numChannels":5,"hostLogRetentionHours":0,"logBackupFrequencyInMinutes":6,"logRetentionHours":1,"ids":["ids","ids"],"configuredSlaDomainIdDeprecated":"configuredSlaDomainIdDeprecated","nodeOrder":[{"nodeName":"nodeName","order":5},{"nodeName":"nodeName","order":5}],"hostMount":"hostMount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/oracle/rac/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_oracle_validate_backup_job(client):
    """Test case for create_oracle_validate_backup_job

    Validate Oracle database backups
    """
    body = {"numChannels":0,"targetMountPath":"targetMountPath","targetOracleHome":"targetOracleHome","sgaMaxSizeInMb":1,"targetOracleHostOrRacId":"targetOracleHostOrRacId","recoveryPoint":{"snapshotId":"snapshotId","timestampMs":6}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/oracle/db/{id}/validate'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_downloaded_snapshots(client):
    """Test case for delete_downloaded_snapshots

    Delete downloaded Oracle database snapshots and log snapshots
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/oracle/db/{id}/downloaded_snapshots'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_aco_parameter_list(client):
    """Test case for get_aco_parameter_list

    List of supported Advanced Cloning Options
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/oracle/aco_parameter_list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_example_aco_download_link(client):
    """Test case for get_example_aco_download_link

    Link to download the Advanced Recovery Options example file
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/oracle/aco_example_download_link',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_oracle_db_v1(client):
    """Test case for get_oracle_db_v1

    Get Oracle database information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/oracle/db/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oracle_restore_estimate(client):
    """Test case for oracle_restore_estimate

    Get a size estimate for a restore or export
    """
    params = [('snapshot_id', 'snapshot_id_example'),
                    ('recovery_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/oracle/db/{id}/restore_estimate'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_oracle_db_v1(client):
    """Test case for query_oracle_db_v1

    Get summary information for Oracle databases
    """
    params = [('name', 'name_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('is_relic', True),
                    ('is_live_mount', True),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('include_backup_task_info', False),
                    ('is_data_guard_group', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/oracle/db',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_oracle_data_guard_group(client):
    """Test case for update_oracle_data_guard_group

    Update an Oracle Data Guard group
    """
    body = {"shouldBackupFromPrimaryOnly":True,"numChannels":5,"hostLogRetentionHours":0,"logBackupFrequencyInMinutes":6,"logRetentionHours":1,"hostMount":"hostMount","preferredDGMemberUniqueNames":["preferredDGMemberUniqueNames","preferredDGMemberUniqueNames"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/oracle/data_guard_group/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_oracle_db_v1(client):
    """Test case for update_oracle_db_v1

    Update an Oracle database
    """
    body = {"numChannels":5,"hostLogRetentionHours":0,"logBackupFrequencyInMinutes":6,"logRetentionHours":1,"configuredSlaDomainIdDeprecated":"configuredSlaDomainIdDeprecated","nodeOrder":[{"nodeName":"nodeName","order":5},{"nodeName":"nodeName","order":5}],"hostMount":"hostMount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/oracle/db/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_oracle_aco_file(client):
    """Test case for validate_oracle_aco_file

    Validate Oracle ACO file
    """
    body = 'body_example'
    params = [('is_live_mount', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/oracle/validate_aco_file',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

