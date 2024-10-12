

# EventRecordFailure

An event update failure resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventId** | **String** | The ID of the event that was not updated. |  [optional] |
|**failureCause** | [**FailureCauseEnum**](#FailureCauseEnum) | The cause for the update failure. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#eventRecordFailure&#x60;. |  [optional] |



## Enum: FailureCauseEnum

| Name | Value |
|---- | -----|
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| INVALID_UPDATE_VALUE | &quot;INVALID_UPDATE_VALUE&quot; |



