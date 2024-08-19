# ContainerServiceClient.OpenShiftManagedClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentPoolProfiles** | [**[OpenShiftManagedClusterAgentPoolProfile]**](OpenShiftManagedClusterAgentPoolProfile.md) | Configuration of OpenShift cluster VMs. | [optional] 
**authProfile** | [**OpenShiftManagedClusterAuthProfile**](OpenShiftManagedClusterAuthProfile.md) |  | [optional] 
**fqdn** | **String** | User-specified FQDN for OpenShift API server loadbalancer internal hostname. | [optional] 
**masterPoolProfile** | [**OpenShiftManagedClusterMasterPoolProfile**](OpenShiftManagedClusterMasterPoolProfile.md) |  | [optional] 
**networkProfile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**openShiftVersion** | **String** | Version of OpenShift specified when creating the cluster. | 
**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response. | [optional] [readonly] 
**publicHostname** | **String** | Optional user-specified FQDN for OpenShift API server. | [optional] 
**routerProfiles** | [**[OpenShiftRouterProfile]**](OpenShiftRouterProfile.md) | Configuration for OpenShift router(s). | [optional] 


