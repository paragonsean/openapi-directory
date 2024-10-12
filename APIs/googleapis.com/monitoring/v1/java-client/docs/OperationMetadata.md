

# OperationMetadata

Contains metadata for longrunning operation for the edit Metrics Scope endpoints.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time when the batch request was received. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Current state of the batch operation. |  [optional] |
|**updateTime** | **String** | The time when the operation result was last updated. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



