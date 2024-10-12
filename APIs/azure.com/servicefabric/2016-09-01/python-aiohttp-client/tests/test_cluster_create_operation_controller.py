# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_clusters_create(client):
    """Test case for clusters_create

    
    """
    parameters = {"properties":{"clusterEndpoint":"clusterEndpoint","availableClusterVersions":[{"supportExpiryUtc":"supportExpiryUtc","environment":"Windows","codeVersion":"codeVersion"},{"supportExpiryUtc":"supportExpiryUtc","environment":"Windows","codeVersion":"codeVersion"}],"certificate":{"x509StoreName":"AddressBook","thumbprint":"thumbprint","thumbprintSecondary":"thumbprintSecondary"},"clusterId":"clusterId","provisioningState":"Updating","reverseProxyCertificate":{"x509StoreName":"AddressBook","thumbprint":"thumbprint","thumbprintSecondary":"thumbprintSecondary"},"upgradeDescription":{"healthCheckRetryTimeout":"healthCheckRetryTimeout","upgradeReplicaSetCheckTimeout":"upgradeReplicaSetCheckTimeout","healthCheckWaitDuration":"healthCheckWaitDuration","forceRestart":True,"deltaHealthPolicy":{"maxPercentUpgradeDomainDeltaUnhealthyNodes":36,"maxPercentDeltaUnhealthyApplications":70,"maxPercentDeltaUnhealthyNodes":93},"healthPolicy":{"maxPercentUnhealthyApplications":20,"maxPercentUnhealthyNodes":41},"overrideUserUpgradePolicy":True,"healthCheckStableDuration":"healthCheckStableDuration","upgradeDomainTimeout":"upgradeDomainTimeout","upgradeTimeout":"upgradeTimeout"},"managementEndpoint":"managementEndpoint","vmImage":"vmImage","upgradeMode":"Automatic","azureActiveDirectory":{"clientApplication":"clientApplication","tenantId":"tenantId","clusterApplication":"clusterApplication"},"clientCertificateCommonNames":[{"isAdmin":True,"certificateIssuerThumbprint":"certificateIssuerThumbprint","certificateCommonName":"certificateCommonName"},{"isAdmin":True,"certificateIssuerThumbprint":"certificateIssuerThumbprint","certificateCommonName":"certificateCommonName"}],"fabricSettings":[{"name":"name","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"name":"name","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"nodeTypes":[{"ephemeralPorts":{"startPort":6,"endPort":0},"reverseProxyEndpointPort":5,"applicationPorts":{"startPort":6,"endPort":0},"durabilityLevel":"Bronze","httpGatewayEndpointPort":5,"isPrimary":True,"name":"name","capacities":{"key":"capacities"},"placementProperties":{"key":"placementProperties"},"clientConnectionEndpointPort":1,"vmInstanceCount":494379917},{"ephemeralPorts":{"startPort":6,"endPort":0},"reverseProxyEndpointPort":5,"applicationPorts":{"startPort":6,"endPort":0},"durabilityLevel":"Bronze","httpGatewayEndpointPort":5,"isPrimary":True,"name":"name","capacities":{"key":"capacities"},"placementProperties":{"key":"placementProperties"},"clientConnectionEndpointPort":1,"vmInstanceCount":494379917}],"reliabilityLevel":"Bronze","clusterState":"WaitingForNodes","diagnosticsStorageAccountConfig":{"protectedAccountKeyName":"protectedAccountKeyName","queueEndpoint":"queueEndpoint","storageAccountName":"storageAccountName","blobEndpoint":"blobEndpoint","tableEndpoint":"tableEndpoint"},"clientCertificateThumbprints":[{"certificateThumbprint":"certificateThumbprint","isAdmin":True},{"certificateThumbprint":"certificateThumbprint","isAdmin":True}],"clusterCodeVersion":"clusterCodeVersion"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

