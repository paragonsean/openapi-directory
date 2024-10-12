

# ManagedClusterProperties

Properties of the managed cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadProfile** | [**ManagedClusterAADProfile**](ManagedClusterAADProfile.md) |  |  [optional] |
|**addonProfiles** | **Object** | Profile of managed cluster add-on. |  [optional] |
|**agentPoolProfiles** | [**List&lt;ManagedClusterAgentPoolProfile&gt;**](ManagedClusterAgentPoolProfile.md) | Properties of the agent pool. Currently only one agent pool can exist. |  [optional] |
|**dnsPrefix** | **String** | DNS prefix specified when creating the managed cluster. |  [optional] |
|**enableRBAC** | **Boolean** | Whether to enable Kubernetes Role-Based Access Control. |  [optional] |
|**fqdn** | **String** | FQDN for the master pool. |  [optional] [readonly] |
|**kubernetesVersion** | **String** | Version of Kubernetes specified when creating the managed cluster. |  [optional] |
|**linuxProfile** | [**ContainerServiceLinuxProfile**](ContainerServiceLinuxProfile.md) |  |  [optional] |
|**networkProfile** | [**ContainerServiceNetworkProfile**](ContainerServiceNetworkProfile.md) |  |  [optional] |
|**nodeResourceGroup** | **String** | Name of the resource group containing agent pool nodes. |  [optional] [readonly] |
|**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response. |  [optional] [readonly] |
|**servicePrincipalProfile** | [**ManagedClusterServicePrincipalProfile**](ManagedClusterServicePrincipalProfile.md) |  |  [optional] |



