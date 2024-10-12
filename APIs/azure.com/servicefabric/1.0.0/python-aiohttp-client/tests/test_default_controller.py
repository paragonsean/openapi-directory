# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_description import ApplicationDescription
from openapi_server.models.application_health import ApplicationHealth
from openapi_server.models.application_health_report import ApplicationHealthReport
from openapi_server.models.application_list import ApplicationList
from openapi_server.models.application_manifest import ApplicationManifest
from openapi_server.models.application_type import ApplicationType
from openapi_server.models.application_upgrade import ApplicationUpgrade
from openapi_server.models.cluster_health import ClusterHealth
from openapi_server.models.cluster_health_report import ClusterHealthReport
from openapi_server.models.cluster_load_information import ClusterLoadInformation
from openapi_server.models.cluster_upgrade_progress import ClusterUpgradeProgress
from openapi_server.models.create_service_description import CreateServiceDescription
from openapi_server.models.create_service_group_description import CreateServiceGroupDescription
from openapi_server.models.deployed_application import DeployedApplication
from openapi_server.models.deployed_application_health import DeployedApplicationHealth
from openapi_server.models.deployed_application_health_report import DeployedApplicationHealthReport
from openapi_server.models.deployed_code_package import DeployedCodePackage
from openapi_server.models.deployed_replica import DeployedReplica
from openapi_server.models.deployed_replica_detail import DeployedReplicaDetail
from openapi_server.models.deployed_service_health_report import DeployedServiceHealthReport
from openapi_server.models.deployed_service_package import DeployedServicePackage
from openapi_server.models.deployed_service_package_health import DeployedServicePackageHealth
from openapi_server.models.deployed_service_type import DeployedServiceType
from openapi_server.models.disable_node import DisableNode
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.node import Node
from openapi_server.models.node_health import NodeHealth
from openapi_server.models.node_health_report import NodeHealthReport
from openapi_server.models.node_list import NodeList
from openapi_server.models.node_load_information import NodeLoadInformation
from openapi_server.models.partition import Partition
from openapi_server.models.partition_health import PartitionHealth
from openapi_server.models.partition_health_report import PartitionHealthReport
from openapi_server.models.partition_list import PartitionList
from openapi_server.models.partition_load_information import PartitionLoadInformation
from openapi_server.models.register_application_type import RegisterApplicationType
from openapi_server.models.register_cluster_package import RegisterClusterPackage
from openapi_server.models.replica import Replica
from openapi_server.models.replica_health import ReplicaHealth
from openapi_server.models.replica_health_report import ReplicaHealthReport
from openapi_server.models.replica_list import ReplicaList
from openapi_server.models.replica_load_information import ReplicaLoadInformation
from openapi_server.models.resolved_service_partition import ResolvedServicePartition
from openapi_server.models.resume_application_upgrade import ResumeApplicationUpgrade
from openapi_server.models.resume_cluster_upgrade import ResumeClusterUpgrade
from openapi_server.models.service import Service
from openapi_server.models.service_description import ServiceDescription
from openapi_server.models.service_description_template import ServiceDescriptionTemplate
from openapi_server.models.service_group_description import ServiceGroupDescription
from openapi_server.models.service_group_member import ServiceGroupMember
from openapi_server.models.service_health import ServiceHealth
from openapi_server.models.service_health_report import ServiceHealthReport
from openapi_server.models.service_list import ServiceList
from openapi_server.models.service_manifest import ServiceManifest
from openapi_server.models.service_type import ServiceType
from openapi_server.models.start_application_upgrade import StartApplicationUpgrade
from openapi_server.models.start_cluster_upgrade import StartClusterUpgrade
from openapi_server.models.unregister_application_type import UnregisterApplicationType
from openapi_server.models.unregister_cluster_package import UnregisterClusterPackage
from openapi_server.models.update_application_upgrade import UpdateApplicationUpgrade
from openapi_server.models.update_cluster_upgrade import UpdateClusterUpgrade
from openapi_server.models.update_service_description import UpdateServiceDescription
from openapi_server.models.update_service_group_description import UpdateServiceGroupDescription


pytestmark = pytest.mark.asyncio

async def test_application_healths_get(client):
    """Test case for application_healths_get

    
    """
    params = [('EventsHealthStateFilter', 'events_health_state_filter_example'),
                    ('DeployedApplicationsHealthStateFilter', 'deployed_applications_health_state_filter_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_name}/$/GetHealth'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_application_healths_send(client):
    """Test case for application_healths_send

    
    """
    application_health_report = openapi_server.ApplicationHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/ReportHealth'.format(application_name='application_name_example'),
        headers=headers,
        json=application_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_manifests_get(client):
    """Test case for application_manifests_get

    
    """
    params = [('ApplicationTypeVersion', 'application_type_version_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}/$/GetApplicationManifest'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_types_get(client):
    """Test case for application_types_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_types_list(client):
    """Test case for application_types_list

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_application_types_register(client):
    """Test case for application_types_register

    
    """
    register_application_type = openapi_server.RegisterApplicationType()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ApplicationTypes/$/Provision',
        headers=headers,
        json=register_application_type,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_application_types_unregister(client):
    """Test case for application_types_unregister

    
    """
    unregister_application_type = openapi_server.UnregisterApplicationType()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ApplicationTypes/{application_type_name}/$/Unprovision'.format(application_type_name='application_type_name_example'),
        headers=headers,
        json=unregister_application_type,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_upgrade_rollbacks_start(client):
    """Test case for application_upgrade_rollbacks_start

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/RollbackUpgrade'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_upgrades_get(client):
    """Test case for application_upgrades_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_name}/$/GetUpgradeProgress'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_application_upgrades_resume(client):
    """Test case for application_upgrades_resume

    
    """
    resume_application_upgrade = openapi_server.ResumeApplicationUpgrade()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/MoveNextUpgradeDomain'.format(application_name='application_name_example'),
        headers=headers,
        json=resume_application_upgrade,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_application_upgrades_start(client):
    """Test case for application_upgrades_start

    
    """
    start_application_upgrade = openapi_server.StartApplicationUpgrade()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/Upgrade'.format(application_name='application_name_example'),
        headers=headers,
        json=start_application_upgrade,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_application_upgrades_update(client):
    """Test case for application_upgrades_update

    
    """
    update_application_upgrade = openapi_server.UpdateApplicationUpgrade()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/UpdateUpgrade'.format(application_name='application_name_example'),
        headers=headers,
        json=update_application_upgrade,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_applications_create(client):
    """Test case for applications_create

    
    """
    application_description = openapi_server.ApplicationDescription()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/$/Create',
        headers=headers,
        json=application_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_get(client):
    """Test case for applications_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_name}'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list(client):
    """Test case for applications_list

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example'),
                    ('continuation-token', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_remove(client):
    """Test case for applications_remove

    
    """
    params = [('ForceRemove', True),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/Delete'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_healths_get(client):
    """Test case for cluster_healths_get

    
    """
    params = [('EventsHealthStateFilter', 'events_health_state_filter_example'),
                    ('NodesHealthStateFilter', 'nodes_health_state_filter_example'),
                    ('ApplicationsHealthStateFilter', 'applications_health_state_filter_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
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

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cluster_healths_send(client):
    """Test case for cluster_healths_send

    
    """
    cluster_health_report = openapi_server.ClusterHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/ReportClusterHealth',
        headers=headers,
        json=cluster_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_load_informations_get(client):
    """Test case for cluster_load_informations_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
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

async def test_cluster_manifests_get(client):
    """Test case for cluster_manifests_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
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

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cluster_packages_register(client):
    """Test case for cluster_packages_register

    
    """
    register_cluster_package = openapi_server.RegisterClusterPackage()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/Provision',
        headers=headers,
        json=register_cluster_package,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cluster_packages_unregister(client):
    """Test case for cluster_packages_unregister

    
    """
    unregister_cluster_package = openapi_server.UnregisterClusterPackage()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/Unprovision',
        headers=headers,
        json=unregister_cluster_package,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cluster_upgrades_resume(client):
    """Test case for cluster_upgrades_resume

    
    """
    resume_cluster_upgrade = openapi_server.ResumeClusterUpgrade()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/MoveToNextUpgradeDomain',
        headers=headers,
        json=resume_cluster_upgrade,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_upgrades_rollback(client):
    """Test case for cluster_upgrades_rollback

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
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
async def test_cluster_upgrades_start(client):
    """Test case for cluster_upgrades_start

    
    """
    start_cluster_upgrade = openapi_server.StartClusterUpgrade()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/Upgrade',
        headers=headers,
        json=start_cluster_upgrade,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cluster_upgrades_update(client):
    """Test case for cluster_upgrades_update

    
    """
    update_cluster_upgrade = openapi_server.UpdateClusterUpgrade()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/UpdateUpgrade',
        headers=headers,
        json=update_cluster_upgrade,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_application_healths_get(client):
    """Test case for deployed_application_healths_get

    
    """
    params = [('EventsHealthStateFilter', 'events_health_state_filter_example'),
                    ('DeployedServicePackagesHealthStateFilter', 'deployed_service_packages_health_state_filter_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/GetHealth'.format(node_name='node_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_deployed_application_healths_send(client):
    """Test case for deployed_application_healths_send

    
    """
    deployed_application_health_report = openapi_server.DeployedApplicationHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/ReportHealth'.format(node_name='node_name_example', application_name='application_name_example'),
        headers=headers,
        json=deployed_application_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_applications_get(client):
    """Test case for deployed_applications_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}'.format(node_name='node_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_applications_list(client):
    """Test case for deployed_applications_list

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_code_packages_get(client):
    """Test case for deployed_code_packages_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/GetCodePackages'.format(node_name='node_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_replica_details_get(client):
    """Test case for deployed_replica_details_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetPartitions/{partition_name}/$/GetReplicas/{replica_id}/$/GetDetail'.format(node_name='node_name_example', partition_name='partition_name_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_replicas_get(client):
    """Test case for deployed_replicas_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/GetReplicas'.format(node_name='node_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_service_package_healths_get(client):
    """Test case for deployed_service_package_healths_get

    
    """
    params = [('EventsHealthStateFilter', 'events_health_state_filter_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/GetServicePackages/{service_package_name}/$/GetHealth'.format(node_name='node_name_example', application_name='application_name_example', service_package_name='service_package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_deployed_service_package_healths_send(client):
    """Test case for deployed_service_package_healths_send

    
    """
    deployed_service_package_health_report = openapi_server.DeployedServiceHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/GetServicePackages/{service_manifest_name}/$/ReportHealth'.format(node_name='node_name_example', application_name='application_name_example', service_manifest_name='service_manifest_name_example'),
        headers=headers,
        json=deployed_service_package_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_service_packages_get(client):
    """Test case for deployed_service_packages_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/GetServicePackages'.format(node_name='node_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployed_service_types_get(client):
    """Test case for deployed_service_types_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetApplications/{application_name}/$/GetServiceTypes'.format(node_name='node_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_node_healths_get(client):
    """Test case for node_healths_get

    
    """
    params = [('EventsHealthStateFilter', 'events_health_state_filter_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetHealth'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_node_healths_send(client):
    """Test case for node_healths_send

    
    """
    node_health_report = openapi_server.NodeHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/ReportHealth'.format(node_name='node_name_example'),
        headers=headers,
        json=node_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_node_load_informations_get(client):
    """Test case for node_load_informations_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetLoadInformation'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_node_states_remove(client):
    """Test case for node_states_remove

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/RemoveNodeState'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_nodes_disable(client):
    """Test case for nodes_disable

    
    """
    disable_node = openapi_server.DisableNode()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/Deactivate'.format(node_name='node_name_example'),
        headers=headers,
        json=disable_node,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_enable(client):
    """Test case for nodes_enable

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/Activate'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_get(client):
    """Test case for nodes_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_list(client):
    """Test case for nodes_list

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example'),
                    ('continuation-token', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partition_healths_get(client):
    """Test case for partition_healths_get

    
    """
    params = [('EventsHealthStateFilter', 'events_health_state_filter_example'),
                    ('ReplicasHealthStateFilter', 'replicas_health_state_filter_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetHealth'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_partition_healths_send(client):
    """Test case for partition_healths_send

    
    """
    partition_health_report = openapi_server.PartitionHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/ReportHealth'.format(partition_id='partition_id_example'),
        headers=headers,
        json=partition_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partition_lists_repair(client):
    """Test case for partition_lists_repair

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_name}/$/GetPartitions/$/Recover'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partition_load_informations_get(client):
    """Test case for partition_load_informations_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetLoadInformation'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partition_loads_reset(client):
    """Test case for partition_loads_reset

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/ResetLoad'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partitions_get(client):
    """Test case for partitions_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_name}/$/GetPartitions/{partition_id}'.format(service_name='service_name_example', partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partitions_list(client):
    """Test case for partitions_list

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_name}/$/GetPartitions'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partitions_repair(client):
    """Test case for partitions_repair

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/Recover'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replica_healths_get(client):
    """Test case for replica_healths_get

    
    """
    params = [('EventsHealthStateFilter', 'events_health_state_filter_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}/$/GetHealth'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_replica_healths_send(client):
    """Test case for replica_healths_send

    
    """
    replica_health_report = openapi_server.ReplicaHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}/$/ReportHealth'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        json=replica_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replica_load_informations_get(client):
    """Test case for replica_load_informations_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}/$/GetLoadInformation'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicas_get(client):
    """Test case for replicas_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetReplicas/{replica_id}'.format(partition_id='partition_id_example', replica_id='replica_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replicas_list(client):
    """Test case for replicas_list

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetReplicas'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_descriptions_get(client):
    """Test case for service_descriptions_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_name}/$/GetDescription'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_service_from_templates_create(client):
    """Test case for service_from_templates_create

    
    """
    service_description_template = openapi_server.ServiceDescriptionTemplate()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/GetServices/$/CreateFromTemplate'.format(application_name='application_name_example'),
        headers=headers,
        json=service_description_template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_group_descriptions_get(client):
    """Test case for service_group_descriptions_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_name}/$/GetServices/{service_name}/$/GetServiceGroupDescription'.format(application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_service_group_from_templates_create(client):
    """Test case for service_group_from_templates_create

    
    """
    service_description_template = openapi_server.ServiceDescriptionTemplate()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/GetServiceGroups/$/CreateServiceGroupFromTemplate'.format(application_name='application_name_example'),
        headers=headers,
        json=service_description_template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_group_members_get(client):
    """Test case for service_group_members_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_name}/$/GetServices/{service_name}/$/GetServiceGroupMembers'.format(application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_service_groups_create(client):
    """Test case for service_groups_create

    
    """
    create_service_group_description = openapi_server.CreateServiceGroupDescription()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/GetServices/$/CreateServiceGroup'.format(application_name='application_name_example'),
        headers=headers,
        json=create_service_group_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_groups_remove(client):
    """Test case for service_groups_remove

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/GetServiceGroups/{service_name}/$/Delete'.format(application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_service_groups_update(client):
    """Test case for service_groups_update

    
    """
    update_service_group_description = openapi_server.UpdateServiceGroupDescription()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/GetServices/{service_name}/$/UpdateServiceGroup'.format(application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        json=update_service_group_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_healths_get(client):
    """Test case for service_healths_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_name}/$/GetHealth'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_service_healths_send(client):
    """Test case for service_healths_send

    
    """
    service_health_report = openapi_server.ServiceHealthReport()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_name}/$/ReportHealth'.format(service_name='service_name_example'),
        headers=headers,
        json=service_health_report,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_manifests_get(client):
    """Test case for service_manifests_get

    
    """
    params = [('ApplicationTypeVersion', 'application_type_version_example'),
                    ('ServiceManifestName', 'service_manifest_name_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}/$/GetServiceManifest'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_types_get(client):
    """Test case for service_types_get

    
    """
    params = [('ApplicationTypeVersion', 'application_type_version_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}/$/GetServiceTypes'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_services_create(client):
    """Test case for services_create

    
    """
    create_service_description = openapi_server.CreateServiceDescription()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_name}/$/GetServices/$/Create'.format(application_name='application_name_example'),
        headers=headers,
        json=create_service_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get(client):
    """Test case for services_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_name}/$/GetServices/{service_name}'.format(application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list(client):
    """Test case for services_list

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_name}/$/GetServices'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_remove(client):
    """Test case for services_remove

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_name}/$/Delete'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_resolve(client):
    """Test case for services_resolve

    
    """
    params = [('PartitionKeyType', 56),
                    ('PartitionKeyValue', 'partition_key_value_example'),
                    ('PreviousRspVersion', 'previous_rsp_version_example'),
                    ('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_name}/$/ResolvePartition'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_services_update(client):
    """Test case for services_update

    
    """
    update_service_description = openapi_server.UpdateServiceDescription()
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_name}/$/Update'.format(service_name='service_name_example'),
        headers=headers,
        json=update_service_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upgrade_progresses_get(client):
    """Test case for upgrade_progresses_get

    
    """
    params = [('timeout', 56),
                    ('api-version', 'api_version_example')]
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

