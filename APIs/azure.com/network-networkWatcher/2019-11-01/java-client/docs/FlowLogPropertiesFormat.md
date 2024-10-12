

# FlowLogPropertiesFormat

Parameters that define the configuration of flow log.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Flag to enable/disable flow logging. |  [optional] |
|**flowAnalyticsConfiguration** | [**TrafficAnalyticsProperties**](TrafficAnalyticsProperties.md) |  |  [optional] |
|**format** | [**FlowLogFormatParameters**](FlowLogFormatParameters.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**retentionPolicy** | [**RetentionPolicyParameters**](RetentionPolicyParameters.md) |  |  [optional] |
|**storageId** | **String** | ID of the storage account which is used to store the flow log. |  |
|**targetResourceGuid** | **String** | Guid of network security group to which flow log will be applied. |  [optional] [readonly] |
|**targetResourceId** | **String** | ID of network security group to which flow log will be applied. |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



