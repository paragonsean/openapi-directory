

# OpenShiftManagedClusterProperties

Properties of the OpenShift managed cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentPoolProfiles** | [**List&lt;OpenShiftManagedClusterAgentPoolProfile&gt;**](OpenShiftManagedClusterAgentPoolProfile.md) | Configuration of OpenShift cluster VMs. |  [optional] |
|**authProfile** | [**OpenShiftManagedClusterAuthProfile**](OpenShiftManagedClusterAuthProfile.md) |  |  [optional] |
|**clusterVersion** | **String** | Version of OpenShift specified when creating the cluster. |  [optional] [readonly] |
|**fqdn** | **String** | Service generated FQDN for OpenShift API server loadbalancer internal hostname. |  [optional] [readonly] |
|**masterPoolProfile** | [**OpenShiftManagedClusterMasterPoolProfile**](OpenShiftManagedClusterMasterPoolProfile.md) |  |  [optional] |
|**monitorProfile** | [**OpenShiftManagedClusterMonitorProfile**](OpenShiftManagedClusterMonitorProfile.md) |  |  [optional] |
|**networkProfile** | [**NetworkProfile**](NetworkProfile.md) |  |  [optional] |
|**openShiftVersion** | **String** | Version of OpenShift specified when creating the cluster. |  |
|**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response. |  [optional] [readonly] |
|**publicHostname** | **String** | Service generated FQDN for OpenShift API server. |  [optional] [readonly] |
|**routerProfiles** | [**List&lt;OpenShiftRouterProfile&gt;**](OpenShiftRouterProfile.md) | Configuration for OpenShift router(s). |  [optional] |



