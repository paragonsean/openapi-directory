

# SubscriptionState

Subscription State object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**istransitioning** | **Boolean** | Is Transitioning |  [optional] [readonly] |
|**properties** | **Object** | Subscription State properties. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of Azure Subscription |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| REGISTERED | &quot;Registered&quot; |
| UNREGISTERED | &quot;Unregistered&quot; |
| WARNED | &quot;Warned&quot; |
| SUSPENDED | &quot;Suspended&quot; |
| DELETED | &quot;Deleted&quot; |



