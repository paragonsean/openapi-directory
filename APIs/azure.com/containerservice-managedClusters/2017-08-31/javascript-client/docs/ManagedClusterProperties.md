# ContainerServiceClient.ManagedClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentPoolProfiles** | [**[ContainerServiceAgentPoolProfile]**](ContainerServiceAgentPoolProfile.md) | Properties of the agent pool. | [optional] 
**dnsPrefix** | **String** | DNS prefix specified when creating the managed cluster. | [optional] 
**fqdn** | **String** | FQDN for the master pool. | [optional] [readonly] 
**kubernetesVersion** | **String** | Version of Kubernetes specified when creating the managed cluster. | [optional] 
**linuxProfile** | [**ContainerServiceLinuxProfile**](ContainerServiceLinuxProfile.md) |  | [optional] 
**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response. | [optional] [readonly] 
**servicePrincipalProfile** | [**ContainerServiceServicePrincipalProfile**](ContainerServiceServicePrincipalProfile.md) |  | [optional] 


