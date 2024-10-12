

# EventSubscriptionStatus

EventSubscription Status denotes the status of the EventSubscription resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Output only. Description of the state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of Event Subscription resource. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| ERROR | &quot;ERROR&quot; |



