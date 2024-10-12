

# ClusterOperationStatus

The status of the operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Output only. A message containing any operation metadata details. |  [optional] [readonly] |
|**innerState** | **String** | Output only. A message containing the detailed operation state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. A message containing the operation state. |  [optional] [readonly] |
|**stateStartTime** | **String** | Output only. The time this state was entered. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |



