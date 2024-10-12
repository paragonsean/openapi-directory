# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_update_parameters import ClusterUpdateParameters
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_clusters_update(client):
    """Test case for clusters_update

    
    """
    parameters = {"properties":{"upgradeDescription":{"healthCheckRetryTimeout":"healthCheckRetryTimeout","upgradeReplicaSetCheckTimeout":"upgradeReplicaSetCheckTimeout","healthCheckWaitDuration":"healthCheckWaitDuration","forceRestart":True,"deltaHealthPolicy":{"maxPercentUpgradeDomainDeltaUnhealthyNodes":36,"maxPercentDeltaUnhealthyApplications":70,"maxPercentDeltaUnhealthyNodes":93},"healthPolicy":{"maxPercentUnhealthyApplications":20,"maxPercentUnhealthyNodes":41},"overrideUserUpgradePolicy":True,"healthCheckStableDuration":"healthCheckStableDuration","upgradeDomainTimeout":"upgradeDomainTimeout","upgradeTimeout":"upgradeTimeout"},"upgradeMode":"Automatic","clientCertificateCommonNames":[{"isAdmin":True,"certificateIssuerThumbprint":"certificateIssuerThumbprint","certificateCommonName":"certificateCommonName"},{"isAdmin":True,"certificateIssuerThumbprint":"certificateIssuerThumbprint","certificateCommonName":"certificateCommonName"}],"certificate":{"x509StoreName":"AddressBook","thumbprint":"thumbprint","thumbprintSecondary":"thumbprintSecondary"},"fabricSettings":[{"name":"name","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"name":"name","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"reverseProxyCertificate":{"x509StoreName":"AddressBook","thumbprint":"thumbprint","thumbprintSecondary":"thumbprintSecondary"},"nodeTypes":[{"ephemeralPorts":{"startPort":6,"endPort":0},"reverseProxyEndpointPort":5,"applicationPorts":{"startPort":6,"endPort":0},"durabilityLevel":"Bronze","httpGatewayEndpointPort":5,"isPrimary":True,"name":"name","capacities":{"key":"capacities"},"placementProperties":{"key":"placementProperties"},"clientConnectionEndpointPort":1,"vmInstanceCount":494379917},{"ephemeralPorts":{"startPort":6,"endPort":0},"reverseProxyEndpointPort":5,"applicationPorts":{"startPort":6,"endPort":0},"durabilityLevel":"Bronze","httpGatewayEndpointPort":5,"isPrimary":True,"name":"name","capacities":{"key":"capacities"},"placementProperties":{"key":"placementProperties"},"clientConnectionEndpointPort":1,"vmInstanceCount":494379917}],"reliabilityLevel":"Bronze","clientCertificateThumbprints":[{"certificateThumbprint":"certificateThumbprint","isAdmin":True},{"certificateThumbprint":"certificateThumbprint","isAdmin":True}],"clusterCodeVersion":"clusterCodeVersion"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

