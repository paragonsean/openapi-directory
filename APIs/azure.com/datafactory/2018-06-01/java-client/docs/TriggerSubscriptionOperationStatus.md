

# TriggerSubscriptionOperationStatus

Defines the response of a trigger subscription operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Event Subscription Status. |  [optional] [readonly] |
|**triggerName** | **String** | Trigger name. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| DEPROVISIONING | &quot;Deprovisioning&quot; |
| DISABLED | &quot;Disabled&quot; |
| UNKNOWN | &quot;Unknown&quot; |



