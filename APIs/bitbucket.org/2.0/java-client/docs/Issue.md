

# Issue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignee** | [**Account**](Account.md) |  |  [optional] |
|**component** | [**Component**](Component.md) |  |  [optional] |
|**content** | [**BaseCommitSummary**](BaseCommitSummary.md) |  |  [optional] |
|**createdOn** | **OffsetDateTime** |  |  [optional] |
|**editedOn** | **OffsetDateTime** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) |  |  [optional] |
|**links** | [**IssueLinks**](IssueLinks.md) |  |  [optional] |
|**milestone** | [**Milestone**](Milestone.md) |  |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) |  |  [optional] |
|**reporter** | [**Account**](Account.md) |  |  [optional] |
|**repository** | [**Repository**](Repository.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**updatedOn** | **OffsetDateTime** |  |  [optional] |
|**version** | [**Version**](Version.md) |  |  [optional] |
|**votes** | **Integer** |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| BUG | &quot;bug&quot; |
| ENHANCEMENT | &quot;enhancement&quot; |
| PROPOSAL | &quot;proposal&quot; |
| TASK | &quot;task&quot; |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| TRIVIAL | &quot;trivial&quot; |
| MINOR | &quot;minor&quot; |
| MAJOR | &quot;major&quot; |
| CRITICAL | &quot;critical&quot; |
| BLOCKER | &quot;blocker&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| NEW | &quot;new&quot; |
| OPEN | &quot;open&quot; |
| RESOLVED | &quot;resolved&quot; |
| ON_HOLD | &quot;on hold&quot; |
| INVALID | &quot;invalid&quot; |
| DUPLICATE | &quot;duplicate&quot; |
| WONTFIX | &quot;wontfix&quot; |
| CLOSED | &quot;closed&quot; |



