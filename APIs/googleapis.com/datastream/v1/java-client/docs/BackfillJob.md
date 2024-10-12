

# BackfillJob

Represents a backfill job on a specific stream object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Output only. Errors which caused the backfill job to fail. |  [optional] [readonly] |
|**lastEndTime** | **String** | Output only. Backfill job&#39;s end time. |  [optional] [readonly] |
|**lastStartTime** | **String** | Output only. Backfill job&#39;s start time. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Backfill job state. |  [optional] [readonly] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | Backfill job&#39;s triggering reason. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| STOPPED | &quot;STOPPED&quot; |
| FAILED | &quot;FAILED&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| UNSUPPORTED | &quot;UNSUPPORTED&quot; |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| TRIGGER_UNSPECIFIED | &quot;TRIGGER_UNSPECIFIED&quot; |
| AUTOMATIC | &quot;AUTOMATIC&quot; |
| MANUAL | &quot;MANUAL&quot; |



