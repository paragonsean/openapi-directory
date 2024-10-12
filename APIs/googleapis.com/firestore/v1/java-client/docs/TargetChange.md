

# TargetChange

Targets being watched have changed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cause** | [**Status**](Status.md) |  |  [optional] |
|**readTime** | **String** | The consistent &#x60;read_time&#x60; for the given &#x60;target_ids&#x60; (omitted when the target_ids are not at a consistent snapshot). The stream is guaranteed to send a &#x60;read_time&#x60; with &#x60;target_ids&#x60; empty whenever the entire stream reaches a new consistent snapshot. ADD, CURRENT, and RESET messages are guaranteed to (eventually) result in a new consistent snapshot (while NO_CHANGE and REMOVE messages are not). For a given stream, &#x60;read_time&#x60; is guaranteed to be monotonically increasing. |  [optional] |
|**resumeToken** | **byte[]** | A token that can be used to resume the stream for the given &#x60;target_ids&#x60;, or all targets if &#x60;target_ids&#x60; is empty. Not set on every target change. |  [optional] |
|**targetChangeType** | [**TargetChangeTypeEnum**](#TargetChangeTypeEnum) | The type of change that occurred. |  [optional] |
|**targetIds** | **List&lt;Integer&gt;** | The target IDs of targets that have changed. If empty, the change applies to all targets. The order of the target IDs is not defined. |  [optional] |



## Enum: TargetChangeTypeEnum

| Name | Value |
|---- | -----|
| NO_CHANGE | &quot;NO_CHANGE&quot; |
| ADD | &quot;ADD&quot; |
| REMOVE | &quot;REMOVE&quot; |
| CURRENT | &quot;CURRENT&quot; |
| RESET | &quot;RESET&quot; |



