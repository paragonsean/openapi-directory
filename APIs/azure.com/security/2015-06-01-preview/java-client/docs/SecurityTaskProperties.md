

# SecurityTaskProperties

Describes properties of a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTimeUtc** | **OffsetDateTime** | The time this task was discovered in UTC |  [optional] [readonly] |
|**lastStateChangeTimeUtc** | **OffsetDateTime** | The time this task&#39;s details were last changed in UTC |  [optional] [readonly] |
|**securityTaskParameters** | **SecurityTaskParameters** |  |  [optional] |
|**state** | **String** | State of the task (Active, Resolved etc.) |  [optional] [readonly] |
|**subState** | **String** | Additional data on the state of the task |  [optional] [readonly] |



