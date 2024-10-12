

# AssignmentProperties

Detailed properties for Assignment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blueprintId** | **String** | ID of the Blueprint definition resource. |  [optional] |
|**locks** | [**AssignmentLockSettings**](AssignmentLockSettings.md) |  |  [optional] |
|**parameters** | [**Map&lt;String, ParameterValueBase&gt;**](ParameterValueBase.md) | A dictionary for parameters and their corresponding values. |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | State of the assignment. |  [optional] [readonly] |
|**resourceGroups** | [**Map&lt;String, ResourceGroupValue&gt;**](ResourceGroupValue.md) | A dictionary which maps resource group placeholders to the resource groups which will be created. |  |
|**status** | [**AssignmentStatus**](AssignmentStatus.md) |  |  [optional] |
|**description** | **String** | Multi-line explain this resource. |  [optional] |
|**displayName** | **String** | One-liner string explain this resource. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;creating&quot; |
| VALIDATING | &quot;validating&quot; |
| WAITING | &quot;waiting&quot; |
| DEPLOYING | &quot;deploying&quot; |
| CANCELLING | &quot;cancelling&quot; |
| LOCKING | &quot;locking&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| CANCELED | &quot;canceled&quot; |
| DELETING | &quot;deleting&quot; |



