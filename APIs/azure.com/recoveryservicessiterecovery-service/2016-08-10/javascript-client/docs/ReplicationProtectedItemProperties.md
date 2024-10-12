# SiteRecoveryManagementClient.ReplicationProtectedItemProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeLocation** | **String** | The Current active location of the PE. | [optional] 
**allowedOperations** | **[String]** | The allowed operations on the Replication protected item. | [optional] 
**currentScenario** | [**CurrentScenarioDetails**](CurrentScenarioDetails.md) |  | [optional] 
**failoverHealth** | **String** | The consolidated failover health for the VM. | [optional] 
**failoverHealthErrors** | [**[HealthError]**](HealthError.md) | List of failover health errors. | [optional] 
**failoverRecoveryPointId** | **String** | The recovery point ARM Id to which the Vm was failed over. | [optional] 
**friendlyName** | **String** | The name. | [optional] 
**lastSuccessfulFailoverTime** | **Date** | The Last successful failover time. | [optional] 
**lastSuccessfulTestFailoverTime** | **Date** | The Last successful test failover time. | [optional] 
**policyFriendlyName** | **String** | The name of Policy governing this PE. | [optional] 
**policyId** | **String** | The ID of Policy governing this PE. | [optional] 
**primaryFabricFriendlyName** | **String** | The friendly name of the primary fabric. | [optional] 
**primaryProtectionContainerFriendlyName** | **String** | The name of primary protection container friendly name. | [optional] 
**protectableItemId** | **String** | The protected item ARM Id. | [optional] 
**protectedItemType** | **String** | The type of protected item type. | [optional] 
**protectionState** | **String** | The protection status. | [optional] 
**protectionStateDescription** | **String** | The protection state description. | [optional] 
**providerSpecificDetails** | [**ReplicationProviderSpecificSettings**](ReplicationProviderSpecificSettings.md) |  | [optional] 
**recoveryContainerId** | **String** | The recovery container Id. | [optional] 
**recoveryFabricFriendlyName** | **String** | The friendly name of recovery fabric. | [optional] 
**recoveryFabricId** | **String** | The Arm Id of recovery fabric. | [optional] 
**recoveryProtectionContainerFriendlyName** | **String** | The name of recovery container friendly name. | [optional] 
**recoveryServicesProviderId** | **String** | The recovery provider ARM Id. | [optional] 
**replicationHealth** | **String** | The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM&#39;s replication group into account. This is a string representation of the ProtectionHealth enumeration. | [optional] 
**replicationHealthErrors** | [**[HealthError]**](HealthError.md) | List of replication health errors. | [optional] 
**testFailoverState** | **String** | The Test failover state. | [optional] 
**testFailoverStateDescription** | **String** | The Test failover state description. | [optional] 


