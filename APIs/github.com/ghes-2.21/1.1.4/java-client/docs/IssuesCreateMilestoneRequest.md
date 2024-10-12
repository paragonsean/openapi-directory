

# IssuesCreateMilestoneRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the milestone. |  [optional] |
|**dueOn** | **OffsetDateTime** | The milestone due date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the milestone. Either &#x60;open&#x60; or &#x60;closed&#x60;. |  [optional] |
|**title** | **String** | The title of the milestone. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |



