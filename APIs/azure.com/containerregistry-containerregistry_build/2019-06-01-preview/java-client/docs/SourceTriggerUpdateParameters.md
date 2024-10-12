

# SourceTriggerUpdateParameters

The properties for updating a source based trigger.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the trigger. |  |
|**sourceRepository** | [**SourceUpdateParameters**](SourceUpdateParameters.md) |  |  [optional] |
|**sourceTriggerEvents** | [**List&lt;SourceTriggerEventsEnum&gt;**](#List&lt;SourceTriggerEventsEnum&gt;) | The source event corresponding to the trigger. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of trigger. |  [optional] |



## Enum: List&lt;SourceTriggerEventsEnum&gt;

| Name | Value |
|---- | -----|
| COMMIT | &quot;commit&quot; |
| PULLREQUEST | &quot;pullrequest&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



