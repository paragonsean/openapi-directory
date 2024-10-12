

# HealthErrorSummary

class to define the summary of the health error details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affectedResourceCorrelationIds** | **List&lt;String&gt;** | The list of affected resource correlation Ids. This can be used to uniquely identify the count of items affected by a specific category and severity as well as count of item affected by an specific issue. |  [optional] |
|**affectedResourceSubtype** | **String** | The sub type of any subcomponent within the ARM resource that this might be applicable. Value remains null if not applicable. |  [optional] |
|**affectedResourceType** | **String** | The type of affected ARM resource. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the health error. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of error. |  [optional] |
|**summaryCode** | **String** | The code of the health error. |  [optional] |
|**summaryMessage** | **String** | The summary message of the health error. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| REPLICATION | &quot;Replication&quot; |
| TEST_FAILOVER | &quot;TestFailover&quot; |
| CONFIGURATION | &quot;Configuration&quot; |
| FABRIC_INFRASTRUCTURE | &quot;FabricInfrastructure&quot; |
| VERSION_EXPIRY | &quot;VersionExpiry&quot; |
| AGENT_AUTO_UPDATE | &quot;AgentAutoUpdate&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |
| INFO | &quot;Info&quot; |



