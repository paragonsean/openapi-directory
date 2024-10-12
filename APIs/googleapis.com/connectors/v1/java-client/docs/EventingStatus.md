

# EventingStatus

EventingStatus indicates the state of eventing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Output only. Description of error if State is set to \&quot;ERROR\&quot;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ERROR | &quot;ERROR&quot; |
| INGRESS_ENDPOINT_REQUIRED | &quot;INGRESS_ENDPOINT_REQUIRED&quot; |



