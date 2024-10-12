# SiteRecoveryManagementClient.RecoveryPlanProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedOperations** | **[String]** | The list of allowed operations. | [optional] 
**currentScenario** | [**CurrentScenarioDetails**](CurrentScenarioDetails.md) |  | [optional] 
**currentScenarioStatus** | **String** | The recovery plan status. | [optional] 
**currentScenarioStatusDescription** | **String** | The recovery plan status description. | [optional] 
**failoverDeploymentModel** | **String** | The failover deployment model. | [optional] 
**friendlyName** | **String** | The friendly name. | [optional] 
**groups** | [**[RecoveryPlanGroup]**](RecoveryPlanGroup.md) | The recovery plan groups. | [optional] 
**lastPlannedFailoverTime** | **Date** | The start time of the last planned failover. | [optional] 
**lastTestFailoverTime** | **Date** | The start time of the last test failover. | [optional] 
**lastUnplannedFailoverTime** | **Date** | The start time of the last unplanned failover. | [optional] 
**primaryFabricFriendlyName** | **String** | The primary fabric friendly name. | [optional] 
**primaryFabricId** | **String** | The primary fabric Id. | [optional] 
**recoveryFabricFriendlyName** | **String** | The recovery fabric friendly name. | [optional] 
**recoveryFabricId** | **String** | The recovery fabric Id. | [optional] 
**replicationProviders** | **[String]** | The list of replication providers. | [optional] 


