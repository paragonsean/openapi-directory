

# RecoveryPlanProperties

Recovery plan custom details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedOperations** | **List&lt;String&gt;** | The list of allowed operations. |  [optional] |
|**currentScenario** | [**CurrentScenarioDetails**](CurrentScenarioDetails.md) |  |  [optional] |
|**currentScenarioStatus** | **String** | The recovery plan status. |  [optional] |
|**currentScenarioStatusDescription** | **String** | The recovery plan status description. |  [optional] |
|**failoverDeploymentModel** | **String** | The failover deployment model. |  [optional] |
|**friendlyName** | **String** | The friendly name. |  [optional] |
|**groups** | [**List&lt;RecoveryPlanGroup&gt;**](RecoveryPlanGroup.md) | The recovery plan groups. |  [optional] |
|**lastPlannedFailoverTime** | **OffsetDateTime** | The start time of the last planned failover. |  [optional] |
|**lastTestFailoverTime** | **OffsetDateTime** | The start time of the last test failover. |  [optional] |
|**lastUnplannedFailoverTime** | **OffsetDateTime** | The start time of the last unplanned failover. |  [optional] |
|**primaryFabricFriendlyName** | **String** | The primary fabric friendly name. |  [optional] |
|**primaryFabricId** | **String** | The primary fabric Id. |  [optional] |
|**recoveryFabricFriendlyName** | **String** | The recovery fabric friendly name. |  [optional] |
|**recoveryFabricId** | **String** | The recovery fabric Id. |  [optional] |
|**replicationProviders** | **List&lt;String&gt;** | The list of replication providers. |  [optional] |



