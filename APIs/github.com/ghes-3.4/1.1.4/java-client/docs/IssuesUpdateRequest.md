

# IssuesUpdateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignee** | **String** | Username to assign to this issue. **This field is deprecated.** |  [optional] |
|**assignees** | **List&lt;String&gt;** | Usernames to assign to this issue. Pass one or more user logins to _replace_ the set of assignees on this issue. Send an empty array (&#x60;[]&#x60;) to clear all assignees from the issue. Only users with push access can set assignees for new issues. Without push access to the repository, assignee changes are silently dropped. |  [optional] |
|**body** | **String** | The contents of the issue. |  [optional] |
|**labels** | [**List&lt;IssuesCreateRequestLabelsInner&gt;**](IssuesCreateRequestLabelsInner.md) | Labels to associate with this issue. Pass one or more labels to _replace_ the set of labels on this issue. Send an empty array (&#x60;[]&#x60;) to clear all labels from the issue. Only users with push access can set labels for issues. Without push access to the repository, label changes are silently dropped. |  [optional] |
|**milestone** | [**IssuesUpdateRequestMilestone**](IssuesUpdateRequestMilestone.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The open or closed state of the issue. |  [optional] |
|**stateReason** | [**StateReasonEnum**](#StateReasonEnum) | The reason for the state change. Ignored unless &#x60;state&#x60; is changed. |  [optional] |
|**title** | [**IssuesUpdateRequestTitle**](IssuesUpdateRequestTitle.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |



## Enum: StateReasonEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| NOT_PLANNED | &quot;not_planned&quot; |
| REOPENED | &quot;reopened&quot; |



