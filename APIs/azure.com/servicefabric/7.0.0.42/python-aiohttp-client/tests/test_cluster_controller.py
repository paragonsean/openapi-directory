# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aad_metadata_object import AadMetadataObject
from openapi_server.models.cluster_configuration import ClusterConfiguration
from openapi_server.models.cluster_configuration_upgrade_description import ClusterConfigurationUpgradeDescription
from openapi_server.models.cluster_configuration_upgrade_status_info import ClusterConfigurationUpgradeStatusInfo
from openapi_server.models.cluster_health import ClusterHealth
from openapi_server.models.cluster_health_chunk import ClusterHealthChunk
from openapi_server.models.cluster_health_chunk_query_description import ClusterHealthChunkQueryDescription
from openapi_server.models.cluster_health_policies import ClusterHealthPolicies
from openapi_server.models.cluster_load_info import ClusterLoadInfo
from openapi_server.models.cluster_manifest import ClusterManifest
from openapi_server.models.cluster_upgrade_progress_object import ClusterUpgradeProgressObject
from openapi_server.models.cluster_version import ClusterVersion
from openapi_server.models.fabric_code_version_info import FabricCodeVersionInfo
from openapi_server.models.fabric_config_version_info import FabricConfigVersionInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.provision_fabric_description import ProvisionFabricDescription
from openapi_server.models.resume_cluster_upgrade_description import ResumeClusterUpgradeDescription
from openapi_server.models.start_cluster_upgrade_description import StartClusterUpgradeDescription
from openapi_server.models.unprovision_fabric_description import UnprovisionFabricDescription
from openapi_server.models.update_cluster_upgrade_description import UpdateClusterUpgradeDescription
from openapi_server.models.upgrade_orchestration_service_state import UpgradeOrchestrationServiceState
from openapi_server.models.upgrade_orchestration_service_state_summary import UpgradeOrchestrationServiceStateSummary


pytestmark = pytest.mark.asyncio

async def test_get_aad_metadata(client):
    """Test case for get_aad_metadata

    Gets the Azure Active Directory metadata used for secured connection to cluster.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetAadMetadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_configuration(client):
    """Test case for get_cluster_configuration

    Get the Service Fabric standalone cluster configuration.
    """
    params = [('api-version', 6.0),
                    ('ConfigurationApiVersion', 'configuration_api_version_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetClusterConfiguration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_configuration_upgrade_status(client):
    """Test case for get_cluster_configuration_upgrade_status

    Get the cluster configuration upgrade status of a Service Fabric standalone cluster.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetClusterConfigurationUpgradeStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_health(client):
    """Test case for get_cluster_health

    Gets the health of a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('NodesHealthStateFilter', 0),
                    ('ApplicationsHealthStateFilter', 0),
                    ('EventsHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('IncludeSystemApplicationHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetClusterHealth',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_health_chunk(client):
    """Test case for get_cluster_health_chunk

    Gets the health of a Service Fabric cluster using health chunks.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetClusterHealthChunk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_cluster_health_chunk_using_policy_and_advanced_filters(client):
    """Test case for get_cluster_health_chunk_using_policy_and_advanced_filters

    Gets the health of a Service Fabric cluster using health chunks.
    """
    cluster_health_chunk_query_description = openapi_server.ClusterHealthChunkQueryDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/GetClusterHealthChunk',
        headers=headers,
        json=cluster_health_chunk_query_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_cluster_health_using_policy(client):
    """Test case for get_cluster_health_using_policy

    Gets the health of a Service Fabric cluster using the specified policy.
    """
    cluster_health_policies = openapi_server.ClusterHealthPolicies()
    params = [('api-version', 6.0),
                    ('NodesHealthStateFilter', 0),
                    ('ApplicationsHealthStateFilter', 0),
                    ('EventsHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('IncludeSystemApplicationHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/GetClusterHealth',
        headers=headers,
        json=cluster_health_policies,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_load(client):
    """Test case for get_cluster_load

    Gets the load of a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetLoadInformation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_manifest(client):
    """Test case for get_cluster_manifest

    Get the Service Fabric cluster manifest.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetClusterManifest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_upgrade_progress(client):
    """Test case for get_cluster_upgrade_progress

    Gets the progress of the current cluster upgrade.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetUpgradeProgress',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_version(client):
    """Test case for get_cluster_version

    Get the current Service Fabric cluster version.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetClusterVersion',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_provisioned_fabric_code_version_info_list(client):
    """Test case for get_provisioned_fabric_code_version_info_list

    Gets a list of fabric code versions that are provisioned in a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('CodeVersion', 'code_version_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetProvisionedCodeVersions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_provisioned_fabric_config_version_info_list(client):
    """Test case for get_provisioned_fabric_config_version_info_list

    Gets a list of fabric config versions that are provisioned in a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('ConfigVersion', 'config_version_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetProvisionedConfigVersions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upgrade_orchestration_service_state(client):
    """Test case for get_upgrade_orchestration_service_state

    Get the service state of Service Fabric Upgrade Orchestration Service.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetUpgradeOrchestrationServiceState',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_provision_cluster(client):
    """Test case for provision_cluster

    Provision the code or configuration packages of a Service Fabric cluster.
    """
    provision_fabric_description = openapi_server.ProvisionFabricDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/Provision',
        headers=headers,
        json=provision_fabric_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_cluster_health(client):
    """Test case for report_cluster_health

    Sends a health report on the Service Fabric cluster.
    """
    health_information = openapi_server.HealthInformation()
    params = [('api-version', 6.0),
                    ('Immediate', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/ReportClusterHealth',
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_resume_cluster_upgrade(client):
    """Test case for resume_cluster_upgrade

    Make the cluster upgrade move on to the next upgrade domain.
    """
    resume_cluster_upgrade_description = openapi_server.ResumeClusterUpgradeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/MoveToNextUpgradeDomain',
        headers=headers,
        json=resume_cluster_upgrade_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rollback_cluster_upgrade(client):
    """Test case for rollback_cluster_upgrade

    Roll back the upgrade of a Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/RollbackUpgrade',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_set_upgrade_orchestration_service_state(client):
    """Test case for set_upgrade_orchestration_service_state

    Update the service state of Service Fabric Upgrade Orchestration Service.
    """
    upgrade_orchestration_service_state = openapi_server.UpgradeOrchestrationServiceState()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/SetUpgradeOrchestrationServiceState',
        headers=headers,
        json=upgrade_orchestration_service_state,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_start_cluster_configuration_upgrade(client):
    """Test case for start_cluster_configuration_upgrade

    Start upgrading the configuration of a Service Fabric standalone cluster.
    """
    cluster_configuration_upgrade_description = openapi_server.ClusterConfigurationUpgradeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/StartClusterConfigurationUpgrade',
        headers=headers,
        json=cluster_configuration_upgrade_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_start_cluster_upgrade(client):
    """Test case for start_cluster_upgrade

    Start upgrading the code or configuration version of a Service Fabric cluster.
    """
    start_cluster_upgrade_description = openapi_server.StartClusterUpgradeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/Upgrade',
        headers=headers,
        json=start_cluster_upgrade_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_verbose_service_placement_health_reporting(client):
    """Test case for toggle_verbose_service_placement_health_reporting

    Changes the verbosity of service placement health reporting.
    """
    params = [('api-version', 6.4),
                    ('Enabled', True),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/ToggleVerboseServicePlacementHealthReporting',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_unprovision_cluster(client):
    """Test case for unprovision_cluster

    Unprovision the code or configuration packages of a Service Fabric cluster.
    """
    unprovision_fabric_description = openapi_server.UnprovisionFabricDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/Unprovision',
        headers=headers,
        json=unprovision_fabric_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_cluster_upgrade(client):
    """Test case for update_cluster_upgrade

    Update the upgrade parameters of a Service Fabric cluster upgrade.
    """
    update_cluster_upgrade_description = openapi_server.UpdateClusterUpgradeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/UpdateUpgrade',
        headers=headers,
        json=update_cluster_upgrade_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

