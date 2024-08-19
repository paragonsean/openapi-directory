

# NullableMilestone

A collection of related issues and pull requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedAt** | **OffsetDateTime** |  |  |
|**closedIssues** | **Integer** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**description** | **String** |  |  |
|**dueOn** | **OffsetDateTime** |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** |  |  |
|**labelsUrl** | **URI** |  |  |
|**nodeId** | **String** |  |  |
|**number** | **Integer** | The number of the milestone. |  |
|**openIssues** | **Integer** |  |  |
|**state** | [**StateEnum**](#StateEnum) | The state of the milestone. |  |
|**title** | **String** | The title of the milestone. |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |



